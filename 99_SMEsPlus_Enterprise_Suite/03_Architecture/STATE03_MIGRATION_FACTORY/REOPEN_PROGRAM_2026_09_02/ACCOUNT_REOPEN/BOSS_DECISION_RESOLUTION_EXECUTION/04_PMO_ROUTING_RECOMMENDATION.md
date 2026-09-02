# 04 — PMO ROUTING RECOMMENDATION (CP-04)

`Never Skip Gate.` For each decision component, PMO defines: Owner status · Evidence status · Gate impact · Routing option · Next prompt pack · Blocker if any · What Boss must decide.

| Component | Owner status | Evidence status | Gate impact | Routing option | Next prompt pack | Blocker if any | What Boss must decide |
|---|---|---|---|---|---|---|---|
| `DC-01` | Boss (asset sub-domain owner inside Accounting Core: `UNASSIGNED`) | Verified | No gate defined (COA-G04/G05/G06 side effects) | `RECOMMEND IN — BOSS RULING REQUIRED` | `PP-06` if ruled IN | None to the ruling itself; owner assignment blocks the *research pass* once ruled IN | IN / OUT / DEFERRED, and (if IN) name the asset sub-domain owner |
| `DC-02` | Boss (same owner gap as `DC-01`) | Verified | No gate defined (COA-G04/G05/G06 side effects) | `RECOMMEND IN — BOSS RULING REQUIRED` | `PP-06` if ruled IN, sequenced behind `DC-01` | Deferral-schedule research should not start before this ruling (`10` §A sequencing note) | IN / OUT / DEFERRED |
| `DC-03` | Boss (research owner `UNASSIGNED` regardless of ruling) | Verified (pointer); weak (subject-matter business-need signal) | No gate defined | `RECOMMEND HOLD — EVIDENCE REQUIRED` | None until Boss ruling | Zero benchmark module installed; `Conditional` (not `Mandatory`) classification; no owner candidate | Confirm the Thai-SME business need before ruling, or accept the weaker basis and rule anyway |
| `DC-04` | `UNASSIGNED` | Partial | No gate defined; unblocks `HO-11`/`HO-12` | `OWNER ASSIGNMENT REQUIRED` | `PP-07` once owner named | Owner gap only — scope itself is not disputed | Name a Treasury owner (Team B / Treasury-specific role) |
| `DC-05A` | Boss | Verified | No gate defined | `RECOMMEND IN — BOSS RULING REQUIRED` (conditional on Accounting owning these controls) | None named in `12_NEXT_CONTROLLED_PROMPT_PACKS.md`; PMO recommends Boss authorize a new pack if ruled IN | Evidence quality is uneven across the four sub-items (HR-expense concretely mapped; WT Certificates/Cash Roundings/Tax Returns menu-label-only) | IN / OUT / DEFERRED per sub-item |
| `DC-05B` | Joint (Account + Inventory) | Verified | Account + Inventory Backbone baseline HOLD | `JOINT_SESSION_REQUIRED` | `PP-04` | Cannot close from the Account side alone (`07` explicit) | Convene Joint Session 3 (`ACC-DEC-019`) |
| `DC-06A` | Boss / Legal-Tax | Partial | `COA-G06` | `LEGAL_TAX_REVIEW_REQUIRED` | `PP-03` (prerequisite), then the ownership ruling itself returns to `PP-01`'s successor pack | Zero VAT/CIT research; benchmark's own exempt-input-VAT template self-contradicts | Commission the Legal-Tax reviewer; ownership ruling (Accounting Core vs. separate Tax domain vs. split-by-form) follows the review |
| `DC-06B` | Legal-Tax | Partial | `COA-G06` | `LEGAL_TAX_REVIEW_REQUIRED` | `PP-03` | Same commissioning gap as `DC-06A` | Commission the Legal-Tax reviewer; scope ruling on `PND1`/`PND54`/`PP36` follows |
| `DC-07` | Boss | Verified | `CO-02` | `RECOMMEND HOLD — EVIDENCE REQUIRED` | None named in `12`; Team B designs at `CO-02` once unblocked | Workflow "assumed in the close checklist but scoped by nobody" (`OBJN-07`) — ruling issued without a `CO-02` tie-in risks re-design | IN / OUT, explicitly tied to the `CO-02` segregation-of-duties boundary |
| `DC-08A` | `UNASSIGNED` | Verified | `COA-G07` | `OWNER ASSIGNMENT REQUIRED` | None named in `12`; PMO recommends a new dedicated pack once owner is named | "Currently owned by nobody in the design chain" (`13` §8 finding 4) | Name an Accounting Core (Team B DOMAIN_01) owner for the analytic/dimension model |
| `DC-08B` | Legal-Tax | Verified | `COA-G06` / `COA-G07` | `LEGAL_TAX_REVIEW_REQUIRED` | `PP-03` | Branch (สาขา) VAT-filing-unit question unanswered (`13` `UK-01`; `06` `DBD-6`) | Commission Legal-Tax review of branch statutory status |
| `DC-09` | `UNASSIGNED` (Team B, sequenced) | Verified | `COA-G05` | `OWNER ASSIGNMENT REQUIRED` | `PP-08`, sequenced behind `PP-02` (`COA-G01` unblock) + `PP-03` (legal-tax) | Design *work* cannot start before `COA-G01` clears and DBD statement-format evidence returns (`10` §C) — but owner naming is not blocked by this | Name the Financial Reporting design owner now; the *start date* is separately gated |
| `DC-10` | Boss | Verified | `COA-G04S` | `RECOMMEND HOLD — EVIDENCE REQUIRED` | None until Boss ruling — carries forward | "Explicitly unapproved... unchanged" from a prior round (`17` `VC-05`); every underlying template row is individually `COA-G06 LEGAL_TAX_REVIEW_REQUIRED` | APPROVE / REJECT / MODIFY `B13 DT-03`, ideally after (or alongside) the depreciation-rate/TFRS-NPAEs Legal-Tax findings |

## PMO cross-track sequencing note

Independent of the per-row detail above, PMO highlights three sequencing dependencies that affect *when* a Boss ruling can be acted on even after it is given, carried forward unchanged from `10_RESEARCH_ROUTING_AR_AP_ASSET_TREASURY_REPORTING.md`:

```
COA-G01 unblock (PP-02)  ──┐
                            ├──>  DC-09 design start (PP-08)  ──> COA-G05
Legal-tax review (PP-03)  ──┘

DC-01 / DC-02 rulings  ──>  PP-06 (AR/AP + Asset research)  (independent of the above)

DC-04 owner naming  ──>  PP-07 (Treasury research)  (independent of the above)

DC-06A / DC-06B / DC-08B  ──>  PP-03 must complete before any ownership/scope ruling closes
```

## Explicit non-claim

This file routes. It does not commission any session, does not name any owner, and does not rule on any component. Every routing option above requires Boss action before it can be executed.
