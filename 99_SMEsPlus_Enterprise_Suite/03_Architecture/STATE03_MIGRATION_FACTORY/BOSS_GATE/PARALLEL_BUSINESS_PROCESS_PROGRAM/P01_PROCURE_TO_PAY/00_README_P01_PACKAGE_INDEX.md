# P01 — PROCURE-TO-PAY — PACKAGE INDEX

| | |
|---|---|
| Session | `SMEPLUS-26-09-04-ACC-P01-P2P-REV2-001` |
| Programme | Parallel Business Process Accounting Deep Research |
| Process | **P01 — Procure-to-Pay** |
| Repository | `TH-PATTARAKRIT/AI-Collaboration-Hub` |
| Working branch | `research/account-p01-procure-to-pay-2026-09-04-001` |
| Canonical branch | `SMEsPlus` — **not merged, not to be merged by this session** |
| Depth | `VERY DEEP / L99999.99999` |
| Governing constitutions | Very Deep Research 8-Criteria Universal Exit Constitution · Canonical Evidence Acquisition Flow Standard · Deep Research Negative Claim Standard · scope-aware correction `SMEPLUS-26-09-04-ACC-REV2-CORR1` |
| Terminal state | **READY FOR CORE ACCOUNTING RECONCILIATION** |
| PMO gate recommendation | **`RECOMMEND HOLD`** — six of eight exit criteria not satisfied |
| Boss | Sole Final Approver |

**This package is not approved, not a pass, not frozen, not merged, and not implementation
authority.**

---

## READ IN THIS ORDER

1. `P01_PMO_REVIEW.md` — the exit test and the recommendation, with the reasons
2. `P01_AAS_PLUS_CONSOLIDATION.md` — consolidated risk, preserved disagreements
3. `P01_DEPLOYED_SCHEMA_EVIDENCE.md` — the strongest evidence in the package
4. `P01_PROCESS_MAP.md` — the process, stage by stage
5. `P01_CONTRADICTION_REGISTER.md` — eleven contradictions, none closed
6. `P01_CORE_RECON_HANDOFF_PACK.md` — what Core Accounting receives and owes back

---

## DELIVERABLES REQUIRED BY THE DIRECTIVE

| File | Content |
|---|---|
| `P01_PROCESS_MAP.md` | The spine, stage by stage, with what each stage does and does not create |
| `P01_FUNCTION_COVERAGE_REGISTER.md` | What was traced, assigned, and not searched. **No coverage percentage** — the denominator is unbounded |
| `P01_MODEL_FIELD_RELATIONSHIP.md` | Object chain, the links that carry accounting meaning, the two that are missing |
| `P01_BUSINESS_EVENT_REGISTER.md` | 22 business facts, their candidate owners, and the double-posting attack results |
| `P01_ACCOUNTING_EVENT_REGISTER.md` | 20 accounting events, each with its condition; and the events that are **not** produced |
| `P01_EVENT_TO_GL_MATRIX.md` | Five ledger patterns behind one document set |
| `P01_SOURCE_TO_AP_TRACE.md` | What business event created the payable, and where the trace breaks |
| `P01_RECEIPT_VALUATION_MATRIX.md` | What a receipt creates, per item shape |
| `P01_THREE_WAY_MATCH_MATRIX.md` | Availability, rules, and why it is a report and not a control |
| `P01_RETURN_REFUND_REVERSAL_MATRIX.md` | Which correction paths preserve history — five of ten do not |
| `P01_CROSS_PROCESS_OWNERSHIP.md` | Ownership matrix, inherited constraints, the tolerance-zero item |
| `P01_EDGE_CASE_TEST_MATRIX.md` | 50 cases; 7 ranked for first execution. **None executed** |
| `P01_CONTRADICTION_REGISTER.md` | 11 contradictions with disposition and lineage |
| `P01_DEPENDENCY_REGISTER.md` | 6 gating dependencies, 7 peer dependencies, and what continued anyway |
| `P01_SOURCE_LINK_REGISTER.md` | Evidence classes ranked; what a reviewer needs to reproduce the package |
| `P01_EVIDENCE_MANIFEST.md` | SHA-256 manifest and the pre-commit scan results |
| `P01_RESEARCH_ERROR_AND_REVISION_LOG.md` | **Six defects found inside this session**, preserved in full |
| `P01_AAS03_EXPERT_CHALLENGE.md` | Four independent experts, disjoint assignments, and what they did to this session's own work |
| `P01_AAS_PLUS_CONSOLIDATION.md` | Agreements, preserved disagreements, consolidated risk |
| `P01_PMO_REVIEW.md` | The 8-criteria exit test |
| `P01_CORE_RECON_HANDOFF_PACK.md` | Handoff |

### Added by this session

| File | Why |
|---|---|
| `P01_SCOPE_OWNERSHIP_MATRIX.md` | Required by the scope-aware constitution correction received mid-session |
| `P01_DEPLOYED_SCHEMA_EVIDENCE.md` | A new evidence class appeared late, from outside the declared evidence base |
| `LAYER2_EVIDENCE_QUARANTINE/E00_P01_PRIMARY_EVIDENCE_BASE.md` | **Layer 2 — Boss / PMO / AI-Audit only.** All reference-system citations |

---

## THE FIVE THINGS A READER SHOULD TAKE AWAY

1. **The receipt-to-bill bridge analysed here has no physical structure to run on in two of the
   three readable deployed databases.** The clearing account and the valuation-layer table are
   absent from both v19 databases.
2. **A soft period lock does not refuse a posting — it rewrites the date and lets it through.**
   Cut-off testing on entry dates is therefore self-confirming.
3. **Correction is by deletion.** Resetting or cancelling a posted bill deletes derived journal
   items rather than reversing them.
4. **A company-scoped financial effect can be created in a company whose ownership of it was
   never proven** — inferred from a tenant-scoped contacts hierarchy, superuser by default,
   optionally auto-posted, with no tenant test found. This is the tolerance-zero item.
5. **Four silent paths lose value or leave a bridge open with no error at all.**

---

## CLEAN-ROOM STATUS

Layer 1 documents were mechanically scanned for reference-system identifiers before commit;
two leaks were found and scrubbed. Reference-system paths, models and line numbers exist **only**
in `LAYER2_EVIDENCE_QUARANTINE/`, which is Boss / PMO / AI-Audit only and must not be
transcribed into any downstream or Team B package. Scan commands and results are in
`P01_EVIDENCE_MANIFEST.md`.

**No statutory claim is made anywhere in this package.** Every Thai tax and withholding
statement is a statement about source behaviour, and every statutory question is held.
