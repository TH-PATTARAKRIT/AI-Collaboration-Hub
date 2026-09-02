# 07 — RISK IF DECISION DELAYED

This file states program-level consequences of the Boss decision queue remaining unresolved, at a broader grain than the per-component "Risk if deferred" already recorded in `05_BOSS_DECISION_FORM_SC01_SC10.md`. It does not recommend a ruling; it states what continues to be true, or grows worse, for every cycle this package sits unresolved.

## Program-level risks (apply across most or all of the 13 components)

| # | Risk | Mechanism | Evidence |
|---|---|---|---|
| PR-1 | Downstream research packs stay idle even though Batch A already authorized "controlled research and routing" | Boss's own Batch A approval (`16_BOSS_APPROVAL_BATCH_A_OPERATING_DIRECTIVE.md`) explicitly listed `ACC-DEC-004`–`013` as `RESEARCH REQUIRED / BOSS FINAL DECISION PENDING` — three sessions deep (Batch A → Boss decision/legal-tax routing → this package) and zero of the ten source scope items have moved | `06_BATCH_A_EVIDENCE_GATE_SUMMARY.md`: "Gate register snapshot... Unchanged" across every row |
| PR-2 | `COA-Gxx` gate cascade stays fully blocked | `COA-G01` blocks `G02`–`G05`; `COA-G04S` (`DC-10`), `COA-G06` (`DC-06A`/`DC-06B`/`DC-08B`), `COA-G07` (`DC-08A`) are each independently `HOLD`; none of the eight `COA-Gxx` gates has moved since Batch A | `20_GAP_OWNER_GATE_IMPACT_REGISTER.md` §E "Gate impact summary" — every row "No" under "Moved?" |
| PR-3 | Migration subledger tie-out (`MG-C11`) cannot be signed off | `DC-01`/`DC-02` (asset/deferral roll-forward) and `DC-04` (Treasury) all feed `MG-C11`; none has a research pass started | `10` §A "unblocks `MG-C11` subledger tie-out"; `17` `VC-04`: "Subledger tie-out... remains a `GAP`" |
| PR-4 | Legal-Tax review backlog compounds across four components simultaneously | `DC-06A`, `DC-06B`, `DC-08B` (and, for template mechanics, `DC-10`'s recommended-not-required Legal-Tax input) all queue behind one not-yet-commissioned reviewer engagement | `06_LEGAL_TAX_REVIEW_BRIEF.md` §E: "Owner field is `UNASSIGNED` until named" |
| PR-5 | Owner-gap components (`DC-04`, `DC-08A`, `DC-09`) stay ownerless regardless of any scope ruling | These three need no scope decision at all — only a name — yet remain blocked purely on an administrative step | `20` §B: three of ten rows are `GAP OWNER ROUTING REQUIRED`, not `BOSS DECISION REQUIRED` |
| PR-6 | Joint Session 3 (`ACC-DEC-019`) stays unconvened while both sides' packages already state readiness | Inventory reopen has "handed over its side"; Account side has produced its agenda brief — the only missing step is Boss convening | `07_ACCOUNT_INVENTORY_JOINT_SESSION_3_ROUTING_BRIEF.md` §Why now |
| PR-7 | Re-derivation cost grows with every additional routing session | Each of the four prior sessions in this chain (menu-process deep-study → boss-decision/legal-tax routing → batch-A → scope-evidence cross-check) re-read and re-cited the same ten items without resolving any — this package is now the fourth layer of routing on top of the same unresolved facts | `14_NEXT_DEEP_RESEARCH_PROMPT_RECOMMENDATION.md`: "this cross-check adds no new pack" |

## Per-component delay-risk rating

| Component | Delay risk if unresolved another cycle | Why |
|---|---|---|
| `DC-01` | Medium | Well-evidenced, Mandatory-classified area stays unscoped; migration roll-forward `GAP` persists |
| `DC-02` | Medium | Same mechanism as `DC-01`, one step further sequenced |
| `DC-03` | Low | Weak evidentiary basis means little is lost by continued HOLD, beyond opportunity cost |
| `DC-04` | **High** | Pure administrative gap (owner name only) with zero scope dispute — the single lowest-cost, highest-leverage unblock in this entire package |
| `DC-05A` | Low–Medium | HR-expense sub-item well-evidenced and low-risk to rule; other three sub-items weaker |
| `DC-05B` | Medium | Compounds the pre-existing `OB-11` gate-scope mismatch the longer it stays unconvened |
| `DC-06A` | **High** | Blocks `COA-G06` and every VAT/CIT design decision; benchmark's self-contradictory template is a standing inheritance risk if any design work proceeds without the review |
| `DC-06B` | Medium | Narrower than `DC-06A` but shares the same commissioning blocker |
| `DC-07` | Low | No downstream pack is currently waiting on this ruling |
| `DC-08A` | Medium | `COA-G07` cannot even state its own acceptance criteria (`UK-08`) while this stays unassigned |
| `DC-08B` | Medium | Blocks both a statutory conclusion and the dimension-model design (`DIM-02`) |
| `DC-09` | **High** | Critical-path owner gap — when `COA-G01`/Legal-Tax clear, an absent owner becomes the new bottleneck at the worst possible time |
| `DC-10` | **High** | Gates `COA-G04S` and, by extension, most of the `COA-Gxx` sequence; carried forward unresolved across multiple rounds already |

## Explicit non-claim

This file states risk. It does not rule, approve, or reject any component, and it does not itself recommend acceleration over the evidence-quality concerns already recorded in `03_AAS_PLUS_CHALLENGE_RECOMMENDATION.md` and `05_BOSS_DECISION_FORM_SC01_SC10.md` — those concerns stand even where this file rates delay-risk as High.
