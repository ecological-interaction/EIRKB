"""Read-only EIRKB preservation/consistency checks; Python 3 standard library.

The immutable Markdown migration snapshot is compared with every collection and
human table. Narrative is reconstructed using the recorded minimal edit/link
crosswalk, not duplicated as JSON prose. Render in a temporary directory only.
"""
from pathlib import Path
import collections
import hashlib
import html
import json
import re
import shutil
import subprocess
import sys
import tempfile
import unicodedata
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]


def digest(data):
    return hashlib.sha256(data).hexdigest()


def sections(text):
    matches = list(re.finditer(r'^## (.+)$', text, re.M))
    return {m[1]: text[m.start():matches[i + 1].start() if i + 1 < len(matches) else len(text)]
            for i, m in enumerate(matches)}


def table(text):
    return ''.join(line for line in text.splitlines(keepends=True) if line.startswith('|'))


def cells(line):
    return [v.strip() for v in re.split(r'(?<!\\)\|', line.rstrip('\n'))[1:-1]]


def slug(value):
    value = html.unescape(re.sub(r'<[^>]+>', '', value)).replace('`', '')
    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode().lower()
    return re.sub(r'[-\s]+', '-', re.sub(r'[^\w\s-]', '', value)).strip('-')


def anchors(text):
    used = set()
    for heading in re.findall(r'^#{1,6} (.+)$', text, re.M):
        base = slug(heading); name = base; n = 0
        while name in used:
            n += 1; name = base + '_' + str(n)
        used.add(name)
    return used | set(re.findall(r'<a id="([^"]+)"', text))


def validate():
    data = json.loads((ROOT / 'EIRKB_Machine_Reference.json').read_text())
    crosswalk = json.loads((ROOT / 'EIRKB_Preservation_Crosswalk.json').read_text())
    json.loads((ROOT / 'EIRKB_Machine_Reference.schema.json').read_text())
    snapshot = data['source_transcription']['markdown']
    assert digest(snapshot.encode()) == data['source_transcription']['sha256']
    original = sections(snapshot)
    scientific = sections((ROOT / 'EIRKB_Scientific_Reference_Register.md').read_text())
    readme = sections((ROOT / 'README.md').read_text())
    protocol = (ROOT / 'EIRKB_Research_Protocol.md').read_text()
    changelog = (ROOT / 'CHANGELOG.md').read_text()
    counts = {}
    for name, item in data['collections'].items():
        source = item['source_section']
        expected = table(original[source])
        assert item['raw_markdown'] == expected, source
        lines = expected.splitlines(keepends=True)
        assert item['headers'] == cells(lines[0]), source
        assert len(item['rows']) == len(lines) - 2, source
        for ordinal, (row, raw) in enumerate(zip(item['rows'], lines[2:]), 1):
            assert row['cells'] == cells(raw) and row['raw_markdown'] == raw, (source, ordinal)
            assert len(row['cells']) == len(item['headers']), (source, ordinal)
            assert all(isinstance(v, str) for v in row['cells']), (source, ordinal)
            assert row['source_row_ordinal'] == ordinal
            assert row['original_empty_cells'] == [i for i, v in enumerate(row['cells']) if v == '']
        counts[source] = len(item['rows'])
        if source not in {'Guide', 'Migration'}:
            assert table(scientific[source]) == expected, source
        if source in {'References', 'Concepts', 'People Index'}:
            assert table(readme[source]) == expected, source
        if source == 'Guide':
            assert expected in protocol
        if source == 'Migration':
            assert expected in changelog
        cross = next(c for c in crosswalk['register_sections'] if c['section'] == source)
        assert digest(expected.encode()) == cross['raw_table_sha256']
        if source == 'Categories':
            assert original[source] == scientific[source], 'Category supplements or notes changed'
    collection = data['collections']
    rows = lambda name: [r['cells'] for r in collection[name]['rows']]
    entity_rows = rows('entities'); ids = [r[0] for r in entity_rows]
    assert len(ids) == len(set(ids))
    assert all(re.match(r'^(R|P|C|O|F|M|IND|PL|T|PH|I|DS|PR)[0-9]+$', r[0]) and r[0].startswith(r[1]) for r in entity_rows)
    reference_ids = [r[0] for r in rows('original_reference_records')]
    assert reference_ids == [f'R{i:03}' for i in range(1, 157)]
    resource_ids = {r[0] for r in rows('resources')}
    assert resource_ids == set(reference_ids) | {'R0157'}
    assert 'R0157' in ids and 'R0157' not in reference_ids
    assert rows('classifications') == [], 'No inferred classification memberships permitted'
    values = collections.defaultdict(set)
    for register, code, *_ in rows('controlled_vocabulary'):
        values[register].add(code)
    for r in entity_rows:
        assert not r[4] or r[4] in ids
        assert r[3] in values['lifecycle']
    unresolved = []
    for n, r in enumerate(rows('relationships'), 1):
        assert r[0] in ids and r[2] in ids, n
        assert r[1] in values['predicate'] and r[5] in values['provenance'], n
        assert not r[6] or r[6] in values['confidence'], n
        for evidence in html.unescape(r[3]).split('|'):
            assert not evidence or evidence in resource_ids, (n, evidence)
    for n, r in enumerate(rows('migration_source_mappings'), 1):
        if r[3] and r[3] not in ids:
            unresolved.append({'row': n, 'entity_id': r[3]})
    assert unresolved == data['source_context']['referentially_unresolved_mappings']
    assert not unresolved, 'Unresolved IDs must be reported, never inferred'
    for item in data['source_context']['workbooks']:
        assert digest((ROOT / item['current_path']).read_bytes()) == item['sha256']
        assert Path(item['current_path']).name == Path(item['historical_path']).name
    assert not (ROOT / 'registers').exists()
    assert sorted(p.name for p in (ROOT / '_legacy registers').iterdir()) == sorted(Path(x['current_path']).name for x in data['source_context']['workbooks'])
    # Existing analytical asset bytes must remain preserved.
    for name, info in crosswalk['baseline_files'].items():
        if name.startswith('assets/diagrams/'):
            assert digest((ROOT / name).read_bytes()) == info['sha256'], name
    # Reconstruct the original manuscript exactly, reversing only recorded edits.
    parts = []
    for doc in data['analytical_documents']:
        name = doc['file']; text = (ROOT / name).read_text()
        marker = '[View full-size research organisation diagram](assets/diagrams/eirkb_overview.svg).\n\n'
        assert text.count(marker) == 1
        body = text.split(marker, 1)[1]
        if name.startswith('A01'):
            body = '# History and Theory of Ecological Information\n\n' + body
        if name.startswith('A03'):
            body = body.split('\n### Preserved baseline qualification\n\n', 1)[0]
        original_explicit = {a['anchor'] for a in crosswalk['master_explicit_anchors'] if a['destination'] == name}
        for added in set(re.findall(r'<a id="([^"]+)"', body)) - original_explicit:
            body = body.replace(f'<a id="{added}"></a>\n\n', '')
        for edit in crosswalk['narrative_edits']:
            if edit['file'] == name:
                assert edit['after'] in body
                body = body.replace(edit['after'], edit['before'], 1)
        for edit in crosswalk['link_repairs']:
            if edit['file'] == name:
                body = body.replace(edit['after'], edit['before'])
        assert digest(body.encode()) == doc['source_sha256'], 'Narrative preservation failed: ' + name
        parts.append(body)
        for h in crosswalk['master_headings_and_anchors']:
            if h['destination'] == name:
                assert h['anchor'] in anchors(text), (name, h['anchor'])
    history = changelog[changelog.index('## Document status and edit history'):].split('\n<a id="migration">', 1)[0]
    original_master = ''.join(parts) + history
    assert digest(original_master.encode()) == crosswalk['baseline_files']['MASTER_history_theory_ecological_information.md']['sha256']
    original_readme = protocol[protocol.index('# Ecological Information Research Knowledge Base'):].split('\n\n## Historical register front matter and navigation', 1)[0]
    original_readme = original_readme.replace('](EIRKB_Scientific_Reference_Register.md)', '](EIRKB%20Reference%20Register.md)').replace('](_legacy%20registers/', '](registers/')
    assert digest(original_readme.encode()) == crosswalk['baseline_files']['README.md']['sha256'], 'Historical protocol preservation'
    # Check repository-local Markdown links and fragments, including renamed workbook paths.
    links = 0
    for path in ROOT.rglob('*.md'):
        if '.git' in path.parts:
            continue
        for target in re.findall(r'!?\[[^\]\n]*\]\(([^\s)]+)\)', path.read_text()):
            url = urlsplit(target)
            if url.scheme or url.netloc:
                continue
            dest = path.parent / unquote(url.path) if url.path else path
            assert dest.exists(), (str(path.relative_to(ROOT)), target)
            if url.fragment and dest.suffix == '.md':
                assert unquote(url.fragment) in anchors(dest.read_text()), (str(path.relative_to(ROOT)), target)
            links += 1
    # Reproduce SVG bytes without writing into this repository.
    with tempfile.TemporaryDirectory(prefix='eirkb-diagram-validation-') as directory:
        tmp = Path(directory)
        for filename in ['eirkb_federation.mmd', 'render_eirkb_federation.py']:
            shutil.copyfile(ROOT / 'assets/diagrams' / filename, tmp / filename)
        subprocess.run([sys.executable, '-B', str(tmp / 'render_eirkb_federation.py')], check=True)
        first = (tmp / 'eirkb_federation.svg').read_bytes()
        subprocess.run([sys.executable, '-B', str(tmp / 'render_eirkb_federation.py')], check=True)
        assert first == (tmp / 'eirkb_federation.svg').read_bytes() == (ROOT / 'assets/diagrams/eirkb_federation.svg').read_bytes()
    import xml.etree.ElementTree as ET
    svg = ET.fromstring(first)
    assert svg.attrib['role'] == 'img' and svg.attrib['aria-labelledby'] == 'title description'
    assert svg.find('{http://www.w3.org/2000/svg}title').text
    assert svg.find('{http://www.w3.org/2000/svg}desc').text
    citation = (ROOT / 'CITATION.cff').read_text()
    assert citation.startswith('cff-version: 1.2.0\n')
    for required in ['family-names: Minchin', 'given-names: Jonathan', 'affiliation: Ecological Interaction', 'https://orcid.org/0000-0001-8152-1796']:
        assert required in citation
    assert not re.search(r'^(doi|license|date-released|version):', citation, re.M)
    print(json.dumps({'status': 'PASS', 'counts': counts, 'unique_entity_ids': len(ids), 'resolved_relationships': counts['Relationships'], 'migration_mappings': counts['Migration'], 'classification_assignments': 0, 'workbook_hashes_preserved': len(data['source_context']['workbooks']), 'narrative': 'Exact source hash reconstructed after reversing the single recorded conversational edit and cross-document links', 'local_links_and_anchors': links, 'diagram': 'Reproduced twice byte-for-byte in a temporary directory; accessible SVG metadata present'}, indent=2))


if __name__ == '__main__':
    validate()
