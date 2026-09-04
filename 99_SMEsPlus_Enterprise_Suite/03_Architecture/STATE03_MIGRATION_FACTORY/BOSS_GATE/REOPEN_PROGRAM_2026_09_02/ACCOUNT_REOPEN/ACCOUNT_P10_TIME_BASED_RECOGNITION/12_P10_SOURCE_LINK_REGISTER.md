# P10 — SOURCE LINK REGISTER

Session: `SMEPLUS-26-09-04-ACC-P10-TBR-REV2-001` · Layer 1

**Clean-room boundary.** This register resolves Layer 1 evidence identifiers to their Layer 2 location. It deliberately does **not** carry vendor file paths, model names, method names or line numbers — those exist only in the Layer 2 quarantine file, which is Boss / PMO / AI-Audit only and must not be transcribed into any reference package or Team B artefact.

---

## 1. Resolution

| Layer 1 identifier range | Resolves to | Access |
|--------------------------|-------------|--------|
| `E-P10-001` .. `E-P10-045` | `LAYER2_P10_EVIDENCE/L2_P10_RAW_SOURCE_CITATIONS.md` §1 | Layer 2 |
| `E-P10-046` .. `E-P10-068` | `LAYER2_P10_EVIDENCE/L2_P10_RAW_SOURCE_CITATIONS.md` §3 | Layer 2 |
| Enumeration outputs | `LAYER2_P10_EVIDENCE/raw/` | Layer 2 |
| Enumeration scripts | `LAYER2_P10_EVIDENCE/p10_scripts/` | Layer 2 — re-runnable unmodified |
| Independent challenge reports | `CHALLENGE/` | Layer 2 |

## 2. Evidence Provenance Summary

| Provenance | Count | Carried as |
|------------|-------|-----------|
| Read directly from primary source by the primary author | 45 | `VERIFIED FACT` |
| Produced by independent challenge, **re-read line-by-line by the author** | 14 | `VERIFIED FACT` |
| Produced by independent challenge, **not independently re-read** | 9 | Reviewer-supplied, class `B`; never the sole support for a gate-changing finding |
| Prior-session evidence carried forward without re-derivation | 3 | Cited to the originating session |
| Statutory / standard evidence | **0** | No statutory claim is made anywhere in this package |

## 3. Prior-Session Evidence Carried Forward

| Item | Origin | Used for |
|------|--------|----------|
| Two day conventions in the asset engine; 8% February divergence; 0.05% annual agreement | `SMEPLUS-26-09-04-ASSET-DEEP-L1-L6-001` | `08` §4 — the detection-blindness transfer to deferrals |
| The legacy Thai daily method and the standard calendar mode are numerically equivalent within `0.03 THB` per period | same | `08` §4 |
| Evidence for a claimed control must include proof that its executor exists | same session's dead-code finding | `04` §4 methodology |

Cited as prior evidence. **Not re-derived by this session** — per the reopen rule, existing approved evidence remains audit lineage.

## 4. Repository Lineage

| Item | Value |
|------|-------|
| Repository | `TH-PATTARAKRIT/AI-Collaboration-Hub` |
| Canonical branch | `SMEsPlus` |
| Working branch | `research/account-p10-time-based-recognition-2026-09-04-001` |
| Branch base | `origin/SMEsPlus` at the head carrying the canonical evidence-acquisition flow standard |
| Merge status | **Not merged, and no merge proposed.** Boss decides. |
| Jira lineage | `ERPPLUS-138` — the Accounting Core reopen issue. A session comment records branch, commit and file list. Not transitioned. |

## 5. Reference Root Declaration

All source evidence in this package is bounded to reference root `RR-1`, declared in Layer 2 §0 with its module count and the command that produced it. A second directory carrying the same build string holds a materially different module population; this is recorded as `P10-C-07`.

**Any negative claim from this package re-used elsewhere must carry the root declaration with it.**

## 6. Clean-Room Scan

A mechanical scan for vendor tokens was run over every Layer 1 document before commit. The result is recorded in `18_P10_CORE_RECON_HANDOFF_PACK.md` §6.
