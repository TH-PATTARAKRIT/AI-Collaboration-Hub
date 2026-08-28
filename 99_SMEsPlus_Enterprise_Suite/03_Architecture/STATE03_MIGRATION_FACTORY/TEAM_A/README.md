# Team A — Source Extraction & Observation

Scope: Multi-source research, source/dump observation, neutral business semantics, migration evidence preparation.

Allowed inputs:
- Customer-authorized ERP source observations
- Customer-authorized database dumps / exports / schemas
- Public official documentation
- Accounting / regulatory / industry standards
- Cross-vendor public references

Required outputs:
- Source Inventory
- Data Dictionary / Field Profile
- Relationship Observation
- Business Meaning Register
- Migration Classification
- Exception / Unknown Register
- Evidence Register
- Source Provenance / Hash Manifest

Forbidden:
- SMEsPlus target architecture design
- SMEsPlus DB/API/DTO/class/folder design
- Copying vendor source code, ORM, table/field structure, internal hooks or workflows into target design
- Production migration or implementation

Handoff: Team A evidence must pass ChatGPT Audit → PMO Verification → Boss Gate before Team B can consume it.