# 08 — SC-07 APPROVAL-BEFORE-POSTING WORKFLOW EVIDENCE POINTER CHECK

| Field | Required Value |
|---|---|
| SC ID | `SC-07` |
| Decision ID | `ACC-DEC-010` |
| Topic | Approval-before-posting workflow (`ACC-004` draft) — IN or OUT |
| Source files checked | `05_ACCOUNT_SCOPE_RESEARCH_REGISTER_SC01_SC10.md` (Batch A); `05_SCOPE_DECISION_ROUTING_REGISTER_SC01_SC10.md` (source pack); `14_CONTROL_LOCK_RECONCILIATION_AUDIT_TRAIL_MAP.md` row `OBJN-07` (deep-study, line 141) |
| Evidence pointer result | Verified |
| Owner status | Boss |
| Gate impact | `CO-02` |
| GL impact known? | No — this is a posting-workflow control, not an account; it gates *when* an entry may post, not what it posts to |
| TB impact known? | No |
| BS / PL / Cash Flow / Tax Report impact known? | N/A |
| Subledger or interface impact | N/A (Control layer, per `14_CONTROL_LOCK_RECONCILIATION_AUDIT_TRAIL_MAP.md` file scope — `M-CTL-*`) |
| Thai menu/report communication issue | No |
| AI Audit SMEsPlus objection | `OBJN-07` itself already raises the sharpest available objection: "a Veto seat may object that the checklist... assumes an approval step that no authority has scoped" — i.e., other parts of this same evidence chain (`M-CTL-08`) may be *presuming* this workflow is IN before Boss has ruled, which is exactly the scope-creep risk `SC-07` exists to prevent. This session did not find that presumption acted upon anywhere in the required inputs, but flags it as worth Boss's attention when ruling |
| Readiness classification | `READY AFTER BOSS SCOPE DECISION` |
| Next action | Boss rules IN / OUT; if IN, "Team B designs at `CO-02` once unblocked," per both required registers |

## Detail

Both required registers cite "source `05` row `ACC-DEC-010`; source `14` OBJN-07." "Source `14` OBJN-07" resolves outside the required perimeter to `14_CONTROL_LOCK_RECONCILIATION_AUDIT_TRAIL_MAP.md` line 141:

> `OBJN-07` | Approval requirement (`CTL-08`) exists only as a STATE04 draft (`ACC-004`, HOLD); no gate owns it; the benchmark has none; a Veto seat may object that the checklist (§2) assumes an approval step that no authority has scoped | Scope creep vs missing control — both possible | `ACC-004`; `F02 M-CTL-08` | Boss — scope decision | UNVERIFIED | No gate defined — BOSS SCOPE DECISION; `ACC-004` HOLD | GAP

This is a precise, on-point match: the exact `ACC-004` draft cited in this row's own topic description ("Approval-before-posting workflow (`ACC-004` draft)") is the subject of `OBJN-07`, and both sources agree the item carries no gate and awaits a Boss scope decision. **Verified**, no discrepancy between the required registers and the underlying anchor.

`02_BOSS_DECISION_QUEUE.md` (required input) independently corroborates the same citation at row `ACC-DEC-010`: "`20 SC-07; 14 OBJN-07`... `BOSS DECISION REQUIRED`... Gate Impact `CO-02`." Consistent across all three documents checked.
