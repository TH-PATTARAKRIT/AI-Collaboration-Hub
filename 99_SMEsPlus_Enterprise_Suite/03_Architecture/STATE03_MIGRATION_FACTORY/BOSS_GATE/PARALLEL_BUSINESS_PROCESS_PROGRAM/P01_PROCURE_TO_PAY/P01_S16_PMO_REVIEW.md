# P01 — SERIES-16 PMO REVIEW

Session: `SMEPLUS-26-09-05-ACC-P01-P2P-S16-SOURCE-DEPLOYMENT-DIRECT-VERIFY-001`
Checkpoint: `CP-P01S16-13`

PMO verifies process, not accounting. Each check returns YES, NO or PARTIAL with its evidence.

| # | Check | Result | Evidence |
|---|---|---|---|
| 1 | All claimed evidence exists | **YES** | 41 `T_*.sql` extracts + `schema_full.sql`; every figure traceable to a named table |
| 2 | Source locator is reproducible | **YES** | E-ENT tree named with `release.py` `version_info = (16,0,0,FINAL,0,'')`; custom root named by Expert 4 |
| 3 | Database identity declared | **YES** | `database.uuid = 45a8e08e-…`, `swr.smeplus.asia`, archive 2026-07-11 |
| 4 | Denominator explicit | **PARTIAL — and this is the round's process failure** | Row-level denominators were declared. **The state basis was not** (`ERR-P01-45`), the ratio unit was not (bills-to-POs), and the **extraction denominator was never declared** — 41 of 651 tables, 6.3% (`GAP-P01-07`) |
| 5 | Changed findings have revision lineage | **YES** | `ERR-P01-42`…`47`, `REV-P01-06`, `NEAR-MISS-P01-07/08/09`, `METHOD-P01-03`, `GAP-P01-07` |
| 6 | No old wrong finding deleted | **YES** | Every superseded statement struck in place with its correction beside it |
| 7 | No external Series-16 acquisition | **YES** | All source from the local estate; the whole-host index is local and pre-existing. No web, no external repo, no download |
| 8 | Peer dependencies named | **YES** | P03 (routing withdrawn), P05 (preserved), P06 (corroborated), P07 (statutory), P08, P11, P04 |
| 9 | Gate movement evidence-based only | **YES** | No exit criterion claimed as improved; `EC` position unchanged |
| 10 | Package frozen before review | **NO** | 15 files entered the "frozen" directory during the challenge (`NEAR-MISS-P01-09`) |
| 11 | Statutory discipline held | **YES** | Six items routed to P07; no statement about Thai law anywhere, including from experts |
| 12 | Decision-authority integrity | **YES** | P05 disagreement preserved; expert disagreements preserved unreconciled; Boss items stated as options |
| 13 | Prohibited verdict wording absent | **YES** | Swept; the single grep hit was "pass through" in ordinary prose |
| 14 | Implementation prohibition observed | **YES** | Read-only throughout; no database written, no source modified, no module installed |

---

## THE TWO CHECKS THAT DO NOT PASS, STATED PLAINLY

**Check 4 — PARTIAL.** The round declared row denominators diligently and then published seven monetary
totals whose **state basis** was undeclared, one of which inverted in sign under the correct basis. It also
never declared that **93.7% of the archive's tables were never opened**. Declaring a denominator is not the
same as declaring the *right* denominator, and this round proves the difference.

**Check 10 — NO.** The freeze was declared and not enforced.

---

## PMO POSITION

**The round is process-sound in its lineage and unsound in its boundary declarations.**

Every correction is recorded, nothing was deleted, no peer was overruled, no statutory claim was made, and no
gate was moved. That is the part the process is for, and it worked: **six of seven corrections came from the
challenge layer, which is the control functioning as designed.**

But the authoring half published a sign-inverted headline, a mechanism conclusion from one account's count,
and a ledger claim tested from the subledger side — **three boundary failures of a kind this programme has
now recorded more than twenty times.**

> **PMO records: RECOMMEND HOLD**, concurring with AAS+, and notes that `S16-B-05` reaches two previously
> published rounds and should be tested before any reliance on their zero-link findings.
