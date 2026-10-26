# EIRKB project instructions

Read README.md, EIRKB_Research_Protocol.md and CHANGELOG.md before research or architecture changes. This independent repository is an EIRKB architecture pilot; do not impose its structure on neighbours.

## Authorities and preservation

- EIRKB_Machine_Reference.json is the current structured-record authority. Its collections retain original transcription and existing structured representations separately. EIRKB_Machine_Reference.schema.json is a small serialization schema, not an ontology or approved DRM specification.
- EIRKB_Scientific_Reference_Register.md and the three README tables are human presentations of the JSON collections. Preserve original headers, cells, empty values, IDs, dates, qualifiers, links, evidence and ordering. Keep presentations consistent with deliberate structured-record changes.
- The machine file's source_transcription is immutable migration evidence, not a second editable authority. EIRKB_Preservation_Crosswalk.json records baseline fingerprints, source lines and destinations; preserve it as migration history.
- A01_Historic_Arc.md, A02_Intellectual_Lineages.md and A03_Intellectual_Map.md remain authoritative for authored prose, including provisional analysis and local synthesis. A01–A03 identify documents, not HA/IL/IM classification codes. The old Master is a compatibility index, not another prose source.
- `_legacy registers/` contains legacy workbooks. Preserve bytes and filenames. Do not import or audit workbook contents unless explicitly asked. Historical source paths and spreadsheet locators are provenance, not current working links.
- Keep R001–R156, R0157 and every issued identifier exactly as assigned. Do not pad, renumber, infer aliases or allocate identities from examples. R0157 is the historical internal protocol, not a new external scholarly citation.
- Keep entity identities, classification definitions, memberships and assertions separate. Classifications remains empty pending explicitly approved mappings. Do not infer HA, IL, IM, SC, SD or EP memberships from narrative headings or terms.
- Preserve source-status wording, uncertain dates, confidence, provenance tokens, evidence IDs and locators. Transcription evidence is not independent bibliographic verification. Do not resolve et al., unnamed partners, overlaps or provisional genealogies by inference.
- Current JSON authority supersedes the labelled historical SQLite/CSV/XLSX authority proposals. SQLite or another store requires an explicitly approved and validated authority transition. DRM remains developing Database Reference Methodology; conformance is not established.
- Keep citation metadata in CITATION.cff, administrative history in CHANGELOG.md and the protocol, and source supplements/qualifications with the scientific records. Do not invent releases, DOIs, licences or verification status.
- Run `python3 scripts/validate_eirkb.py` after edits. Validate tables, identifiers, evidence, migration mappings, local links, preservation fingerprints and deterministic SVG output. The validator requires Python 3; use the optional JSON Schema and CFF schema checks during review when the corresponding validation dependencies are available.

## Diagram maintenance

- New corpus/federation overview: assets/diagrams/eirkb_federation.mmd is authoritative for labels, layout and typography; regenerate assets/diagrams/eirkb_federation.svg with `python3 assets/diagrams/render_eirkb_federation.py`.
- Existing analytical organisation diagram: preserve assets/diagrams/eirkb_overview.mmd, its SVG and renderer. All three A01–A03 files embed that existing SVG with alternative text/full-size links. Its older architecture wording is retained as historical analytical context, not a new implementation claim.
- Generate twice and compare bytes. Preserve SVG title, description, viewBox, source checksum and repository-relative asset paths. Do not edit derived SVG independently.
- Shared palette/layout conventions express conceptual or proposed relationships, not operational integrations, a new taxonomy or inferred memberships.

## Publication boundaries

- Source repositories remain authoritative; websites publish approved pinned views. Publication-manifest and website changes are a separately authorised stage.
- Do not stage, commit, push, configure remotes, edit the website or deploy unless explicitly authorised. Preserve unrelated uncommitted work.
