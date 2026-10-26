# Changelog

Meaningful changes to research content, reference registers, database structure,
research classifications, publication interfaces, documentation and releases are
recorded here.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versions identify research-resource releases, separately from document and schema versions.

## [Unreleased]

### Local repository restructuring — 26 October 2026

- Established JSON structured-record authority with a separate immutable original Markdown transcription and all 13 original collections. README and the scientific register are presentations; analytical Markdown retains authority for authored prose. This is a local document/schema transition, not a research release, implemented SQLite database or approved DRM conformance.
- Renamed `registers/` to `_legacy registers/` without opening or modifying workbook bytes. Renamed the active Markdown register to `EIRKB_Scientific_Reference_Register.md`; preserved all scientific tables, category supplements, qualifications and source notes.
- README now contains the new federation diagram, one short introduction, exact copies of References, Concepts and People Index, and a citation/version footer. Preserved the complete earlier README and Guide in `EIRKB_Research_Protocol.md`, explicitly separating superseded historical SQLite/CSV/XLSX and identifier-padding proposals from current JSON authority and exact legacy identifiers.
- Split authored narrative into A01 Historic Arc, A02 Intellectual Lineages and A03 Intellectual Map. Shared introduction is in A01; shared conclusion, local synthesis and checkpoint are in A03. The former Master is now a compatibility index. Original section numbers, explicit and automatic anchors, conceptual chains and uncertainty remain; cross-document links are repaired.
- Minimal conversational edit: removed only “Yes. ” before “The literature is much broader” at A02’s opening. No scientific claim or qualification was rewritten. Other first-person research and provisional framing remain.
- Document editions: README/scientific/machine 1.3; current protocol 1.4 with historical v1.3 retained; serialization schema `eirkb.reference-register/0.1-draft`. No release, DOI, licence or new HA/IL/IM membership is assigned.
- Added a separate reproducible `eirkb_federation` diagram; existing `eirkb_overview` Mermaid, renderer and SVG remain byte-identical and are embedded in all three analytical documents.
- Actual current counts: 156 original References; 142 original Concepts; 180 People Index rows; 95 Categories rows including source supplements and one entirely empty row; 18 Guide rows; 501 Entities; 157 Resources including internal protocol R0157; 175 People; 122 structured Concept Records; zero Classifications; 408 Relationships; 81 Vocabulary rows; 503 Migration mappings. Overlapping presentations intentionally remain separate; these are not additional inferred entities.

#### Unresolved research and historical context

- Original incomplete bibliographic metadata, “et al.” and combined index wording, uncertain dates, source-status terms, unexpanded identities, provisional genealogies and project-interpretation links remain unchanged.
- The empty Classifications collection remains pending approved mappings; narrative scheme descriptions and controlled vocabulary are not memberships. No new HA, IL or IM assignments are inferred.
- Historical statements about accompanying CSV files, planned SQLite operations and former filenames are preserved as source context, not evidence of implemented software or current authority.
- Transcribed evidence/provenance has not been promoted to independent bibliographic verification. All relationship endpoints/evidence and migration entity IDs resolve in the present corpus; semantic review remains separate.


### Added

- Prepared CFF 1.2.0 citation metadata naming Jonathan Minchin and Ecological Interaction.
- Prepared a development changelog and a work-in-progress publication statement.
- Prepared the existing Markdown Reference Register for inclusion in version control.

### Changed

- Removed ChatGPT-specific citation markers and internal conversation metadata from the research Markdown publication copies without adding replacement references.
- Corrected the local Git remote to ecological-interaction/EIRKB following the reported repository transfer.

No database schema, research classification, ontology or structured relationship changes are included in this preparation. No website has been integrated or deployed.

## [0.1.0] — Planned; not released

This is the proposed first public research release. No release date or tag has been assigned. The items below describe its intended contents, not an existing published release.

### Added

- History and Theory of Ecological Information: the existing historical arc, intellectual lineages and conceptual map.
- The existing V0 and v0.1 XLSX reference registers and the Markdown Reference Register.
- The existing project definition, research protocol and proposed SQLite-based knowledge-base methodology.
- Academic attribution, citation metadata and work-in-progress publication documentation.

### Development provenance

- The sole existing EIRKB commit, `3462f2571a8343287084e5deab0913b1acc74f43` (12 October 2026), established the independent repository and preserved the README, Master narrative and both XLSX registers, with Jonathan Minchin as author and committer.
- The project protocol records v1.2 on 1 October 2026 and v1.3 on 3 October 2026. These are document-history entries, not EIRKB Git release tags.
- The existing Markdown Reference Register identifies its edition as 1.2, dated 13 October 2026, derived from the v0.1 workbook. It was untracked before this release preparation.

SQLite implementation, later data migration, publication integration and licensing decisions remain future work.


## Preservation crosswalk

| Original material | Preserved destination | Treatment |
|---|---|---|
| Reference Register — References (156 rows) | `EIRKB_Machine_Reference.json#/collections/original_reference_records`; `EIRKB_Scientific_Reference_Register.md#references`; `README.md#references` | Original headers, cells and ordering preserved; see JSON crosswalk for hashes and source lines. |
| Reference Register — Concepts (142 rows) | `EIRKB_Machine_Reference.json#/collections/original_concept_records`; `EIRKB_Scientific_Reference_Register.md#concepts`; `README.md#concepts` | Original headers, cells and ordering preserved; see JSON crosswalk for hashes and source lines. |
| Reference Register — People Index (180 rows) | `EIRKB_Machine_Reference.json#/collections/people_index`; `EIRKB_Scientific_Reference_Register.md#people-index`; `README.md#people-index` | Original headers, cells and ordering preserved; see JSON crosswalk for hashes and source lines. |
| Reference Register — Categories (95 rows) | `EIRKB_Machine_Reference.json#/collections/categories_and_research_notes`; `EIRKB_Scientific_Reference_Register.md#categories` | Original headers, cells and ordering preserved; see JSON crosswalk for hashes and source lines. |
| Reference Register — Guide (18 rows) | `EIRKB_Machine_Reference.json#/collections/historical_administrative_guide`; `EIRKB_Research_Protocol.md#guide`; `EIRKB_Scientific_Reference_Register.md#guide-research-qualifications` | Original headers, cells and ordering preserved; see JSON crosswalk for hashes and source lines. |
| Reference Register — Entities (501 rows) | `EIRKB_Machine_Reference.json#/collections/entities`; `EIRKB_Scientific_Reference_Register.md#entities` | Original headers, cells and ordering preserved; see JSON crosswalk for hashes and source lines. |
| Reference Register — Resources (157 rows) | `EIRKB_Machine_Reference.json#/collections/resources`; `EIRKB_Scientific_Reference_Register.md#resources` | Original headers, cells and ordering preserved; see JSON crosswalk for hashes and source lines. |
| Reference Register — People (175 rows) | `EIRKB_Machine_Reference.json#/collections/people`; `EIRKB_Scientific_Reference_Register.md#people` | Original headers, cells and ordering preserved; see JSON crosswalk for hashes and source lines. |
| Reference Register — Concept Records (122 rows) | `EIRKB_Machine_Reference.json#/collections/structured_concept_records`; `EIRKB_Scientific_Reference_Register.md#concept-records` | Original headers, cells and ordering preserved; see JSON crosswalk for hashes and source lines. |
| Reference Register — Classifications (0 rows) | `EIRKB_Machine_Reference.json#/collections/classifications`; `EIRKB_Scientific_Reference_Register.md#classifications` | Original headers, cells and ordering preserved; see JSON crosswalk for hashes and source lines. |
| Reference Register — Relationships (408 rows) | `EIRKB_Machine_Reference.json#/collections/relationships`; `EIRKB_Scientific_Reference_Register.md#relationships` | Original headers, cells and ordering preserved; see JSON crosswalk for hashes and source lines. |
| Reference Register — Vocabulary (81 rows) | `EIRKB_Machine_Reference.json#/collections/controlled_vocabulary`; `EIRKB_Scientific_Reference_Register.md#vocabulary` | Original headers, cells and ordering preserved; see JSON crosswalk for hashes and source lines. |
| Reference Register — Migration (503 rows) | `EIRKB_Machine_Reference.json#/collections/migration_source_mappings`; `CHANGELOG.md#migration` | Original headers, cells and ordering preserved; see JSON crosswalk for hashes and source lines. |
| README — complete protocol and front matter | `EIRKB_Research_Protocol.md` | Current rules precede labelled historical text; working links repaired only. |
| Master — opening and section I | `A01_Historic_Arc.md` | Authored prose/numbering preserved. |
| Master — section II | `A02_Intellectual_Lineages.md` | Only initial “Yes. ” removed. |
| Master — section III and shared conclusion | `A03_Intellectual_Map.md` | Synthesis, warnings and historical checkpoint preserved. |
| Master — status/edit history | Appendix below; research warning also in A03 | Complete historical text retained. |

The machine-readable [preservation crosswalk](EIRKB_Preservation_Crosswalk.json) lists every original Master heading/anchor, line ranges, baseline hashes and exact link/narrative changes. It is migration evidence, not a second source of authored prose.

<a id="master-document-administrative-history"></a>

## Master document administrative history

Historical source text follows unchanged. Its “not modified” statements describe that original checkpoint, not a new independent audit.

## Document status and edit history

### Baseline Master Document — Bioregional Course

**Status:** Preserved baseline for subsequent development.  
**Prepared:** 30 September 2026.  

- This is preservation of the historical discussion, not a fresh fact-check or endorsement of every historical claim or proposed connection. The map remains provisional.
- Subsequent development should retain this baseline and explicitly record additions or changed terminology. The Ecological Reference Register V2 workbook has not been modified.

### Status update — 2026-09-30 21:09:25 CEST (UTC+0200)

**Edit: merge the expanded three-structure conceptual framework.** Integrated the expanded conceptual framework into the existing master: 20 historical/conceptual stages, 14 overlapping lineages and eight knowledge territories. Retained all original section titles and substantive passages, reconciled changed titles as nested headings with original section numbers, and kept the original provisional map. Consolidated repeated explanations and replaced repeated closing contents lists with cross-references. No Reference Register changes were made.


<a id="migration"></a>

## Migration — provenance appendix

Complete original Migration table from Markdown register edition 1.2. Mappings are also preserved in the machine reference; source-sheet names, row locators and legacy labels retain their historical meaning.

| source_sheet | source_row | source_label | entity_id | migration_note |
| --- | --- | --- | --- | --- |
| References | 2 | R001 | R001 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 3 | R002 | R002 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 4 | R003 | R003 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 5 | R004 | R004 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 6 | R005 | R005 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 7 | R006 | R006 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 8 | R007 | R007 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 9 | R008 | R008 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 10 | R009 | R009 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 11 | R010 | R010 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 12 | R011 | R011 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 13 | R012 | R012 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 14 | R013 | R013 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 15 | R014 | R014 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 16 | R015 | R015 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 17 | R016 | R016 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 18 | R017 | R017 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 19 | R018 | R018 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 20 | R019 | R019 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 21 | R020 | R020 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 22 | R021 | R021 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 23 | R022 | R022 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 24 | R023 | R023 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 25 | R024 | R024 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 26 | R025 | R025 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 27 | R026 | R026 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 28 | R027 | R027 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 29 | R028 | R028 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 30 | R029 | R029 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 31 | R030 | R030 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 32 | R031 | R031 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 33 | R032 | R032 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 34 | R033 | R033 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 35 | R034 | R034 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 36 | R035 | R035 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 37 | R036 | R036 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 38 | R037 | R037 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 39 | R038 | R038 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 40 | R039 | R039 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 41 | R040 | R040 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 42 | R041 | R041 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 43 | R042 | R042 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 44 | R043 | R043 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 45 | R044 | R044 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 46 | R045 | R045 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 47 | R046 | R046 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 48 | R047 | R047 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 49 | R048 | R048 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 50 | R049 | R049 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 51 | R050 | R050 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 52 | R051 | R051 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 53 | R052 | R052 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 54 | R053 | R053 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 55 | R054 | R054 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 56 | R055 | R055 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 57 | R056 | R056 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 58 | R057 | R057 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 59 | R058 | R058 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 60 | R059 | R059 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 61 | R060 | R060 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 62 | R061 | R061 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 63 | R062 | R062 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 64 | R063 | R063 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 65 | R064 | R064 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 66 | R065 | R065 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 67 | R066 | R066 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 68 | R067 | R067 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 69 | R068 | R068 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 70 | R069 | R069 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 71 | R070 | R070 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 72 | R071 | R071 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 73 | R072 | R072 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 74 | R073 | R073 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 75 | R074 | R074 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 76 | R075 | R075 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 77 | R076 | R076 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 78 | R077 | R077 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 79 | R078 | R078 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 80 | R079 | R079 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 81 | R080 | R080 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 82 | R081 | R081 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 83 | R082 | R082 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 84 | R083 | R083 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 85 | R084 | R084 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 86 | R085 | R085 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 87 | R086 | R086 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 88 | R087 | R087 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 89 | R088 | R088 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 90 | R089 | R089 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 91 | R090 | R090 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 92 | R091 | R091 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 93 | R092 | R092 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 94 | R093 | R093 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 95 | R094 | R094 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 96 | R095 | R095 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 97 | R096 | R096 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 98 | R097 | R097 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 99 | R098 | R098 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 100 | R099 | R099 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 101 | R100 | R100 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 102 | R101 | R101 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 103 | R102 | R102 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 104 | R103 | R103 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 105 | R104 | R104 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 106 | R105 | R105 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 107 | R106 | R106 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 108 | R107 | R107 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 109 | R108 | R108 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 110 | R109 | R109 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 111 | R110 | R110 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 112 | R111 | R111 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 113 | R112 | R112 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 114 | R113 | R113 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 115 | R114 | R114 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 116 | R115 | R115 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 117 | R116 | R116 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 118 | R117 | R117 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 119 | R118 | R118 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 120 | R119 | R119 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 121 | R120 | R120 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 122 | R121 | R121 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 123 | R122 | R122 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 124 | R123 | R123 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 125 | R124 | R124 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 126 | R125 | R125 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 127 | R126 | R126 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 128 | R127 | R127 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 129 | R128 | R128 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 130 | R129 | R129 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 131 | R130 | R130 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 132 | R131 | R131 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 133 | R132 | R132 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 134 | R133 | R133 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 135 | R134 | R134 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 136 | R135 | R135 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 137 | R136 | R136 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 138 | R137 | R137 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 139 | R138 | R138 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 140 | R139 | R139 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 141 | R140 | R140 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 142 | R141 | R141 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 143 | R142 | R142 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 144 | R143 | R143 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 145 | R144 | R144 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 146 | R145 | R145 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 147 | R146 | R146 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 148 | R147 | R147 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 149 | R148 | R148 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 150 | R149 | R149 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 151 | R150 | R150 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 152 | R151 | R151 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 153 | R152 | R152 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 154 | R153 | R153 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 155 | R154 | R154 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 156 | R155 | R155 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| References | 157 | R156 | R156 | All original fields remain unchanged in References. Date copied as text; unknown metadata left blank. |
| People Index | 2 | Alexander von Humboldt | P0028 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 3 | Anna Lowenhaupt Tsing | P0044 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 4 | Aristotle | P0001 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 5 | Benjamin H. Bratton | P0058 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 6 | Bruno Latour | P0062 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 7 | Bruno Latour &amp; Peter Weibel (eds.) | P0062 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 7 | Bruno Latour &amp; Peter Weibel (eds.) | P0063 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 8 | C. S. Holling | P0026 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 9 | Charles Darwin | P0033 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 10 | Charles Sanders Peirce | P0003 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 11 | Christopher Frayling | P0098 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 12 | Claude E. Shannon | P0005 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 13 | Claude E. Shannon &amp; Warren Weaver | P0005 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 13 | Claude E. Shannon &amp; Warren Weaver | P0006 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 14 | David B. Lindenmayer &amp; Gene E. Likens | P0077 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 14 | David B. Lindenmayer &amp; Gene E. Likens | P0078 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 15 | David J. Rapport | P0074 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 16 | Denis Noble | P0040 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 17 | Donna Haraway | P0042 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 18 | E. F. Schumacher | P0083 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 19 | Eben Kirksey | P0045 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 20 | Eduardo Kohn | P0041 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 21 | Elinor Ostrom | P0096 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 22 | Emanuele Coccia | P0046 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 23 | Eugene P. Odum | P0020 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 24 | Eva Meijer | P0050 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 25 | Francisco Varela, Evan Thompson &amp; Eleanor Rosch | P0013 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 25 | Francisco Varela, Evan Thompson &amp; Eleanor Rosch | P0014 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 25 | Francisco Varela, Evan Thompson &amp; Eleanor Rosch | P0015 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 26 | Frans de Waal | P0049 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 27 | Frederic E. Clements | P0068 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 28 | GEO BON | O0005 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 29 | George Church | P0039 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 30 | Gilbert Simondon | P0060 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 31 | Gregor Mendel | P0034 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 32 | Gregory Bateson | P0010 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 33 | Heinz von Foerster | P0009 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 34 | Henrique M. Pereira et al. | P0076 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 35 | Henry Lin | P0067 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 36 | Herman E. Daly | P0097 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 37 | Howard T. Odum | P0021 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 38 | Humberto Maturana &amp; Francisco Varela | P0012 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 38 | Humberto Maturana &amp; Francisco Varela | P0013 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 39 | Ian L. McHarg | P0084 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 40 | Ilya Prigogine | P0024 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 41 | Isabelle Stengers | P0064 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 42 | Jakob von Uexküll | P0004 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 43 | James Bridle | P0051 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 44 | James E. Lyons, Michael C. Runge, Harold P. Laskowski &amp; William L. Kendall | P0079 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 44 | James E. Lyons, Michael C. Runge, Harold P. Laskowski &amp; William L. Kendall | P0080 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 44 | James E. Lyons, Michael C. Runge, Harold P. Laskowski &amp; William L. Kendall | P0081 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 44 | James E. Lyons, Michael C. Runge, Harold P. Laskowski &amp; William L. Kendall | P0082 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 45 | James J. Gibson | P0011 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 46 | James Lovelock &amp; Lynn Margulis | P0030 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 46 | James Lovelock &amp; Lynn Margulis | P0031 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 47 | James Watson &amp; Francis Crick | P0035 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 47 | James Watson &amp; Francis Crick | P0036 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 48 | Jennifer Gabrys | P0052 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 49 | Jesper Hoffmeyer | P0017 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 50 | Jianguo Liu et al. | P0093 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 51 | John Tillman Lyle | P0088 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 52 | John Zimmerman, Jodi Forlizzi &amp; Shelley Evenson | P0099 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 52 | John Zimmerman, Jodi Forlizzi &amp; Shelley Evenson | P0100 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 52 | John Zimmerman, Jodi Forlizzi &amp; Shelley Evenson | P0101 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 53 | Jussi Parikka | P0054 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 54 | Lisa Parks | P0057 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 55 | Ludwig Boltzmann | P0002 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 56 | Marten Scheffer et al. | P0027 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 57 | Monica Gagliano | P0047 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 58 | N. Katherine Hayles | P0053 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 59 | NASA | O0002 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 60 | NASA / University of Cape Town and partners | O0002 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 60 | NASA / University of Cape Town and partners | O0004 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 61 | NASA / University of Maryland | O0002 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 61 | NASA / University of Maryland | O0003 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 62 | National Research Council | O0001 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 63 | Norbert Wiener | P0007 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 64 | Paul N. Edwards | P0056 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 65 | Peter B. Landres, Jared Verner &amp; James W. Thomas | P0069 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 65 | Peter B. Landres, Jared Verner &amp; James W. Thomas | P0070 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 65 | Peter B. Landres, Jared Verner &amp; James W. Thomas | P0071 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 66 | Peter Berg &amp; Raymond Dasmann | P0089 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 66 | Peter Berg &amp; Raymond Dasmann | P0090 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 67 | Peter Godfrey-Smith | P0048 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 68 | Piers Blaikie &amp; Harold Brookfield | P0091 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 68 | Piers Blaikie &amp; Harold Brookfield | P0092 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 69 | Rick Bonney et al. | P0094 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 70 | Robert Costanza et al. | P0075 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 71 | Robert E. Ulanowicz | P0023 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 72 | Robert Frosch &amp; Nicholas Gallopoulos | P0085 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 72 | Robert Frosch &amp; Nicholas Gallopoulos | P0086 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 73 | Robert H. MacArthur | P0022 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 74 | Robert U. Ayres | P0087 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 75 | Rosalind Franklin &amp; Raymond Gosling | P0037 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 75 | Rosalind Franklin &amp; Raymond Gosling | P0038 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 76 | Shannon Mattern | P0055 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 77 | Stuart A. Kauffman | P0025 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 78 | Susan L. Brantley et al. | P0065 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 79 | Suzanne P. Anderson | P0066 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 80 | Thomas A. Sebeok | P0016 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 81 | Timo Maran &amp; Kalevi Kull | P0018 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 81 | Timo Maran &amp; Kalevi Kull | P0019 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 82 | Timothy M. Lenton | P0032 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 83 | Timothy Morton | P0061 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 84 | Vinciane Despret | P0043 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 85 | Virginia H. Dale &amp; Suzanne C. Beyeler | P0072 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 85 | Virginia H. Dale &amp; Suzanne C. Beyeler | P0073 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 86 | Vladimir I. Vernadsky | P0029 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 87 | W. Ross Ashby | P0008 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 88 | Yochai Benkler | P0095 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 89 | Yuk Hui | P0059 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 90 | Stafford Beer | P0102 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 91 | Alfred J. Lotka | P0103 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 92 | Raymond L. Lindeman | P0104 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 93 | Gilles Deleuze | P0105 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 94 | Félix Guattari | P0106 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 95 | EuropaBON consortium / European Commission | O0006 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 95 | EuropaBON consortium / European Commission | O0007 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 96 | Robert U. Ayres | P0087 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 97 | Allen V. Kneese | P0107 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 98 | Thomas E. Graedel | P0108 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 99 | Braden R. Allenby | P0109 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 100 | Marina Fischer-Kowalski | P0110 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 101 | Stefan Pauliuk | P0111 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 102 | Edgar G. Hertwich | P0112 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 103 | John Ehrenfeld | P0113 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 104 | Nicholas Gertler | P0114 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 105 | Marian R. Chertow | P0115 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 106 | Kalundborg Symbiosis | O0008 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 107 | Eurostat | O0009 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 108 | Paul H. Brunner | P0116 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 109 | Helmut Rechberger | P0117 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 110 | International Organization for Standardization | O0010 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 111 | Ronald E. Miller | P0118 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 112 | Peter D. Blair | P0119 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 113 | Abel Wolman | P0120 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 114 | Fridolin Krausmann | P0121 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 115 | E. M. Harper | P0122 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 116 | N. T. Nassar | P0123 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 117 | Philip Nuss | P0124 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 118 | Barbara K. Reck | P0125 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 119 | OECD | O0011 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 120 | Ellen MacArthur Foundation | O0012 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 121 | Thomas Robert Malthus | P0126 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 122 | Irmi Seidl | P0127 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 123 | Clem A. Tisdell | P0128 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 124 | William E. Rees | P0129 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 125 | Mathis Wackernagel | P0130 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 126 | Global Footprint Network | O0013 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 127 | Jeroen C. J. M. van den Bergh | P0131 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 128 | Harmen Verbruggen | P0132 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 129 | Fabio Grazi | P0133 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 130 | Nicholas Georgescu-Roegen | P0134 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 131 | Kate Raworth | P0135 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 132 | Donella H. Meadows | P0136 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 133 | Dennis L. Meadows | P0137 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 134 | Jørgen Randers | P0138 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 135 | William W. Behrens III | P0139 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 136 | Johan Rockström | P0140 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 137 | Will Steffen | P0141 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 138 | Katherine Richardson | P0142 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 139 | Joyeeta Gupta | P0143 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 140 | Dahe Qin | P0144 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 141 | David A. Keith | P0145 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 142 | IUCN | O0014 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 143 | Helmut Haberl | P0146 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 144 | Thomas O. Wiedmann | P0147 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 145 | IPCC | O0015 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 146 | N. LeRoy Poff | P0148 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 147 | Arjen Y. Hoekstra | P0149 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 148 | Ashok K. Chapagain | P0150 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 149 | Maite M. Aldaya | P0151 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 150 | Mesfin M. Mekonnen | P0152 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 151 | Benjamin D. Stocker | P0153 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 152 | Yue Li | P0154 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 153 | Stephen P. Good | P0155 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 154 | Lixin Wang | P0156 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 155 | US National Science Foundation | O0016 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 156 | Melissa M. Rohde | P0157 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 157 | Haozhi Ma | P0158 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 158 | Dario Grana | P0159 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 159 | Brady A. Flinchum | P0160 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 160 | Denys Grombacher | P0161 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 161 | Andrew D. Parsekian | P0162 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 162 | Clifford S. Riebe | P0163 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 163 | W. Steven Holbrook | P0164 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 164 | Critical Zone Collaborative Network (CZNet) | O0017 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 165 | Compton J. Tucker | P0165 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 166 | Takeshi Motohka | P0166 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 167 | D. M. Woebbecke | P0167 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 168 | G. E. Meyer | P0168 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 169 | K. Von Bargen | P0169 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 170 | D. A. Mortensen | P0170 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 171 | John Maynard Smith | P0171 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 172 | David Harper | P0172 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 173 | Philip Francis Thomsen | P0173 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 174 | Eske Willerslev | P0174 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 175 | Giorgos Kallis | P0175 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 176 | Timothy M. Lenton | P0032 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 177 | NASA | O0002 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 178 | Yale Center for Industrial Ecology | O0018 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 179 | Yale University / International Society for Industrial Ecology | O0019 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 179 | Yale University / International Society for Industrial Ecology | O0020 | Named creators split into individual records; original row and reference links retained in People Index. |
| People Index | 180 | Journal of Industrial Ecology |  | Journal label retained unchanged; not misclassified as a person or organization. |
| People Index | 181 | International Society for Industrial Ecology | O0020 | Named creators split into individual records; original row and reference links retained in People Index. |
| Concepts | 2 | Difference | C0001 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 3 | Information | C0002 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 4 | Signal | C0003 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 5 | Cue | C0004 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 6 | Noise | C0005 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 7 | Semiosis | C0006 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 8 | Umwelt | C0007 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 9 | Affordance | C0008 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 10 | Enaction | C0009 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 11 | Feedback | C0010 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 12 | Requisite variety | C0011 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 13 | Observability | C0012 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 14 | Ecological observability | C0013 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 15 | Indicator | C0014 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 16 | Proxy | C0015 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 17 | Detection probability | C0016 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 18 | Sensitivity / specificity | C0017 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 19 | Early-warning signal | C0018 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 20 | Essential Biodiversity Variable | IND0001 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 21 | Adaptive monitoring | C0019 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 22 | Critical Zone | C0020 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 23 | Critical Zones | C0021 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 24 | Bioregion | C0022 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 25 | Social–ecological system | C0023 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 26 | Resilience | C0024 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 27 | Regime shift | C0025 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 28 | Telecoupling | C0026 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 29 | Industrial metabolism | C0027 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 30 | Industrial symbiosis | C0028 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 31 | Appropriate technology | C0029 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 32 | Regenerative design | C0030 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 33 | Situated knowledge | C0031 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 34 | More-than-human | C0032 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 35 | Environmental sensing | C0033 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 36 | Knowledge infrastructure | C0034 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 37 | Planetary computation | C0035 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 38 | Productive affordance | C0036 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 39 | Ecological inference | C0037 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 40 | Productive inference | C0038 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 41 | Situated Ecological Technology | C0039 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 42 | Generative infrastructure | C0040 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 43 | Viable System Model | IND0002 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 44 | Trophic dynamics | C0041 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 45 | Rhizome | C0042 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 46 | Assemblage | C0043 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 47 | Industrial ecology | F0001 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 48 | Material balance | C0044 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 49 | Societal / socioeconomic metabolism | C0045 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 50 | Material Flow Analysis (MFA) | M0001 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 51 | Substance Flow Analysis (SFA) | M0002 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 52 | Life-Cycle Assessment (LCA) | M0003 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 53 | Life-cycle inventory | C0046 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 54 | Input–output analysis | M0004 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 55 | Energy-flow analysis | M0005 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 56 | Material stocks | C0047 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 57 | Urban metabolism | C0048 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 58 | Eco-industrial parks | C0049 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 59 | Design for environment | C0050 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 60 | Extended producer responsibility | C0051 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 61 | Circular economy | C0052 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 62 | Critical materials | C0053 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 63 | Resource efficiency | C0054 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 64 | Decarbonisation / energy systems | C0055 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 65 | Prospective industrial systems modelling | C0056 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 66 | Carrying capacity | C0057 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 67 | Logistic growth / K | C0058 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 68 | Ecological footprint | IND0003 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 69 | Biocapacity | C0059 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 70 | Global hectare | C0060 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 71 | Ecological deficit / reserve | C0061 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 72 | Ecological overshoot | C0062 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 73 | Earth Overshoot Day | C0063 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 74 | Planetary Boundaries | IND0004 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 75 | Safe operating space | C0064 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 76 | Safe and Just Earth System Boundaries | IND0005 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 77 | Doughnut Economics | IND0006 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 78 | Steady-state economics | C0065 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 79 | Degrowth | C0066 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 80 | Natural capital | C0067 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 81 | Ecosystem services | C0068 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 82 | Limits to Growth / World3 | C0069 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 83 | Ecological capacity | C0070 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 84 | Productive demand | C0071 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 85 | Regenerative contribution | C0072 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 86 | Pressure | C0073 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 87 | State | C0074 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 88 | Ecological threshold | C0075 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 89 | Boundary | C0076 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 90 | Boundary transgression | C0077 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 91 | Tipping point | C0078 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 92 | Critical slowing down | C0079 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 93 | Resistance and recovery | C0080 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 94 | IUCN Red List of Ecosystems | IND0007 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 95 | Human Appropriation of Net Primary Production (HANPP) | IND0008 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 96 | Net primary production (NPP) | C0081 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 97 | Material footprint | IND0009 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 98 | Carbon footprint | IND0010 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 99 | Land footprint | IND0011 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 100 | Water footprint | IND0012 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 101 | Remaining carbon budget | C0082 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 102 | Environmental flows / ELOHA | IND0013 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 103 | Groundwater recharge and abstraction | C0083 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 104 | Nutrient boundaries | C0084 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 105 | Biosphere integrity | C0085 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 106 | Ecosystem functional integrity | C0086 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 107 | Atmosphere-to-aquifer transect | C0087 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 108 | Gradient of observability | C0088 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 109 | Direct observation | C0089 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 110 | Indirect subsurface measurement | C0090 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 111 | Inverse modelling | M0006 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 112 | Model-derived state | C0091 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 113 | Epistemic distance | C0092 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 114 | Measurement-to-inference chain | C0093 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 115 | Rooting-zone water storage | C0094 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 116 | Surface versus root-zone soil moisture | C0095 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 117 | Plant water-source inference | C0096 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 118 | Electrical resistivity / electromagnetic sensing | M0007 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 119 | Seismic imaging | M0008 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 120 | NDVI | IND0014 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 121 | GRVI | IND0015 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 122 | Excess Green (ExG) | IND0016 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 123 | Rhizosphere and below-ground biology | C0097 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 124 | Above-ground / below-ground biomass | C0098 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 125 | Organism information worlds | C0099 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 126 | Organisms as information | C0100 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 127 | Signal versus incidental cue | C0101 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 128 | Environmental DNA (eDNA) | C0102 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 129 | Metabarcoding / metagenomics / eRNA | C0103 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 130 | Situated productive inference | C0104 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 131 | Critical Zone–socioeconomic metabolism intersection | C0105 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 132 | EuropaBON | PR0001 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 133 | Industrial ecosystem | C0106 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 134 | Emergent industrial symbiosis | C0107 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 135 | Sap flow and leaf water potential | C0108 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 136 | Canopy temperature and spectral response | C0109 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 137 | Soil water content and water potential | C0110 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 138 | Groundwater level and pore-water chemistry | C0111 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 139 | Stable water isotopes | C0112 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 140 | Hydrometeorological measurements | C0113 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 141 | Soil electrical conductivity | C0114 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 142 | Spatial support, temporal resolution and uncertainty | C0115 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
| Concepts | 143 | Epistemic confidence and productive implications | C0116 | Definition and anchors retained verbatim in Concepts. Entity class allocated under EIRKB; no original reference changed. |
