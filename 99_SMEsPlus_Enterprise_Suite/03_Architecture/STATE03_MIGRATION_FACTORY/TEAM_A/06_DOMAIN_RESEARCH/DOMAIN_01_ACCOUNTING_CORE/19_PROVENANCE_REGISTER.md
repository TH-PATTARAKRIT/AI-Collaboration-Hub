> DOMAIN_01 — Accounting Core | Team A (Maker) | READ ONLY | No target design | Boss sole Final Approver

# 19 — PROVENANCE REGISTER

| Code | Meaning | Used in this domain |
|---|---|---|
| P1 | Direct source-code observation (readable licence) | Yes — `account` LGPL-3, 40 model files |
| P2 | Database structural observation | Yes — via approved Evidence_CSV structural inventory |
| P3 | Database row/data observation | **NO — unavailable** (no restore; UAT snapshot) |
| P4 | Manifest / metadata observation | Yes — 1,504-module register |
| P5 | Approved prior evidence carried forward | Yes — A0/A1, STEP040301/0403xx chain, V2.0 Evidence_CSV |
| P6 | External/public authoritative source | **NO — EXTERNAL_RESEARCH_ACCESS = UNAVAILABLE** |
| P7 | Vendor documentation | No |
| P8 | Inference / analyst judgment | Yes — explicitly marked where used |

## Provenance by finding class
| Finding group | Provenance |
|---|---|
| Lifecycle, invariants, constraints, functions (SE-01…SE-27) | **P1** |
| Table/column/constraint/index counts, monetary types, FK shape | **P2** (via P5 artefacts) |
| Module counts, licences, areas | **P4 + P5** |
| Snapshot is configuration/UAT, ~6 entries | **P5** |
| Cross-vendor classification | **P8** with confidence stated; P6 unavailable |
| Advancement candidates | **P8**, derived from P1/P2 observations |

**No finding in this pack rests on P3 or P6.** Where those would be needed, a gap is recorded
rather than an assertion made.
