# 37 — P05 AAS+ TARGETED CONSOLIDATION

`LAYER 2 — AUDIT QUARANTINE`
AAS+ reconciles without forcing consensus. Dissent is recorded, not suppressed.
AAS+ may issue `HOLD` or `VETO` on individual findings. **AAS+ output is a recommendation and is not
Boss approval.**

## 1. What the Closure Actually Achieved

| Objective | Outcome |
|---|---|
| `U-01` deployed module list | **Materially resolved** for six named registries at class **A**; class **B** for any wider population; class **D** for the v18 target |
| `U-02` runtime trace | **Split**: database half closed at production scale; execution half `HOLD — RUNTIME EVIDENCE REQUIRED` |
| Exit criteria dispositioned | **8 of 8 dispositioned**; 2 satisfied, 6 not |
| Handoff elements | **10 of 10 dispositioned**: 2 complete, 3 partial, 4 blocked, 1 not-applicable |
| Tolerance-zero boundaries | **13 reconciled on two axes; 0 closed** |
| `EC-07` | measured against its quoted definition: **0 of 2**, structurally |
| Cross-process handoff | **6 peers routed** with evidence, no peer architecture decided |
| `CORR1` revalidation | confirmed, **one call overturned and reinstated** |
| Four-expert challenge | **4 of 4 completed** (1 first attempt, 3 on retry) |

## 2. Positions Held Jointly After Challenge

| ID | Position | Survived |
|---|---|---|
| `AP+01` | **`TX-01` is the best-evidenced finding in the package.** Predicted from source, proven *structurally overdetermined* by the ORM field definition (`tax_line_id` is a stored related field of `tax_repartition_line_id`, never set on a write-off line), and measured in production: **5,426 of 5,863 lines — 92.55% — of withholding posted to the withholding account carry no `tax_line_id`** and would be dropped by the enterprise PND export's inner join. | Expert 3, and the author's own measurement |
| `AP+02` | **The most consequential live findings in this package are not P05's.** The vendor down payment that is never deducted, and the `sudo()` wizard letting any internal user create a vendor bill, are **live in all four distinct databases evidenced** and both belong to **P01**. | Expert 1 (with the count corrected downward) |
| `AP+03` | **Petty cash and employee advance are confirmed defects in code that no evidenced deployment runs.** Reach `LATENT`; defect status `CONFIRMED`. | Experts 1, 2 |
| `AP+04` | **No tolerance-zero boundary is closed**, and none was closed on deployment evidence. | Expert 1 (mechanically verified) |
| `AP+05` | **The claim↔entry foreign key is not a stable reconciliation key** — confirmed verbatim against every cited line — **bounded** by a forensic chatter/attachment path that survives three of four severing mechanisms. | Expert 4 |
| `AP+06` | **The withholding certificate table has no UNIQUE constraint and no index beyond its primary key**, at v16 and all three v19 registries. One exact duplicate exists in 5,201. | Expert 2, author-verified |
| `AP+07` | **`R-02`, `R-03`, `R-04`, `R-05` scope determinations stand**; `R-01` is reinstated and narrowed. | Expert 4 |

## 3. Non-Consensus — Recorded, Not Resolved

| ID | Disagreement | Positions | AAS+ disposition |
|---|---|---|---|
| `NC+06` | **Is deployment reach the right axis at all?** | *Package*: reach separates what is at risk in a running system from what is not. *Expert 1*: for a build-decision programme it is close to the wrong axis — a defect in code nobody runs is a mistake SMEsPlus can still decline to inherit, so it may matter **more**, not less. | **Both stand. Neither is averaged.** `26 §2` carries Expert 1's challenge verbatim and `26 §5` is retitled and qualified. AAS+ rules that reach governs **remediation** sequencing and must **not** govern **build scope**. A reader using `26 §5` for build scope is using the wrong axis. |
| `NC+07` | **Is `iTEST02` a production tenant?** | *Author*: counted it among "real business databases". *Expert 1*: the name signals test/UAT; class **C**, unconfirmed. | **Expert 1 governs.** Counted as a distinct database, flagged as likely non-production, not upgraded. The `TZ-11`/`TZ-12` reach claim is restated on four databases with that caveat attached. |
| `NC+08` | **Severity of `TX-13` after correction** | *Author (original)*: mass duplication. *Expert 2*: one instance in 5,201; the structural gap is the real finding. | **Expert 2 governs.** `TX-13` is a control defect with one production instance, not a mass-duplication finding. Expert 2's view that `DB-01`..`DB-06` are *more* actionable than the findings it was sent to challenge is **recorded and not argued with**. |
| `NC+09` | **Does `SR-07a` weaken `SR-07`?** | *Expert 4*: chatter and attachments survive three of four paths. *Package*: no relational path survives. | **Both stand.** AAS+ rules the bound does **not** weaken the design requirement (`17 §6 DI-05`): parsing chatter HTML is not a reconciliation key. Severity bounded, conclusion unchanged. |
| `NC+10` | **Coverage of the challenge round** | Three of four experts ran on a smaller model after rate-limit termination. | **Disclosed, not absorbed** (`36 §1`). Mitigation: every retry finding was author-verified against source or data before adoption, and every one that could be checked reproduced exactly. |

## 4. AAS+ Rulings on Individual Findings

| Finding | Ruling |
|---|---|
| `TX-01` | **UPHELD — strengthened.** Best-evidenced finding in the package. |
| `TX-13` | **HOLD on the original figure (withdrawn); UPHELD on the corrected control defect.** |
| `TX-20` | **VETO on the original claim** — mechanism inverted, published wrong. **UPHELD on the corrected finding**: a `NOT NULL` column named `payment_date` carries no payment information in 100% of rows. |
| `TZ-11` / `TZ-12` (P01) | **UPHELD**, reach restated as four distinct databases. |
| `R-01` withdrawal | **VETO.** Reinstated, narrowed to late-failure. |
| "the deployed estate" | **VETO.** Population never established. |
| `TX-12` "potentially already-filed" | **VETO.** Unsourced statutory assumption. |
| `H-P07-2` "(legitimate)" | **VETO.** P05 pre-answered P07's question. |
| `SR-07` | **UPHELD, bounded** by `SR-07a`. |
| `AASV-01` (implementation veto, original round) | **UPHELD AND EXTENDED** — see §5. |

## 5. The Veto

> **`AASV-01` remains in force. AAS+ vetoes any implementation start on P05.**

The original grounds stand. The closure adds a sharper one:

**Across two challenge rounds, every single material correction to this package came from independent
review. None came from the author.** Round 1: 12 of 32 author findings corrected, 60 new findings.
Round 2: of three findings published from new evidence, **two were overturned by the first reviewer to
look at them**, and four more author claims fell to the remaining three experts. The author's
pre-publication self-check caught none of them while holding the same data.

That is not a reason to distrust the *evidence* — the evidence is stronger than it has ever been, and
`TX-01` is now proven three independent ways. It is a reason to distrust **any author-produced
conclusion in this package that has not been through independent review**, which is most of
`TX-02`..`TX-24` and the non-P07 rows of `30` (Expert 3 declared those explicitly unchecked, class **D**).

> **`AASV-02` NEW.** AAS+ additionally vetoes citing any *uncorrected* section of this package as
> settled input to design without a further independent pass over it. The corrected sections
> (`24`, `25`, `26`, `07 TX-01`, `22 R-01`) may be relied on at their stated classes.

## 6. What AAS+ Recommends Boss Decide First

Not the eight `BD-` items — those need P07 and P11 input first. AAS+ recommends **three unblocking
decisions**, in this order:

1. **Release the deployed module list for the v18 target**, or authorise a runtime enumeration
   (`U-01` residue). Cheapest; unblocks `EC-01` and most of `EC-03`.
2. **Authorise restoring an existing dump into a disposable database for read-only ORM queries**
   (`U-02b`). This is the only thing that can close `U-03` and settle `TX-14`, and it needs no new
   infrastructure — the dumps already exist and have already been read as files.
3. **Route the P01 findings now, ahead of the rest of P05.** `TZ-11` and `TZ-12` are live in every
   evidenced deployment and are not P05's to fix. Waiting for P05's gate delays a live exposure in
   another process.
