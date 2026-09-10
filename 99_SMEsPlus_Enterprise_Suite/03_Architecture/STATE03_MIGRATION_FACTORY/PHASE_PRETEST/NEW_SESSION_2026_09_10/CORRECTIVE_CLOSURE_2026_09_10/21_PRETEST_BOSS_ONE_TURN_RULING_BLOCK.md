# 21 — BOSS ONE-TURN RULING BLOCK

## `CHECKPOINT F — 9 ITEMS · ONE RESPONSE`

Session: `[SMEPLUS-26-09-10-PHASE-PRETEST-BOSS-RESOLUTION-001]` · **Boss: SOLE FINAL APPROVER**

> **Approve, modify or reject in one response. NO automatic approval. `0` items are pre-approved.**
> **Nothing below creates a `PASS`, discharges a veto by itself, or authorizes Functional Design.**

---

```
================================================================
SMEsPlus PHASE PRE-TEST — BOSS CONSOLIDATED RULING BLOCK
Session  [SMEPLUS-26-09-10-PHASE-PRETEST-NEWSESSION-001]
Branch   architecture/account-phase-pretest-new-session-2026-09-10-001
Head     c9ed125a
================================================================

B4'  TWELVE-BOUNDARY SET — DECLARE MEMBERSHIP
     No authority enumerates a set. I DECLARE the canonical boundary
     set as the following, as a Boss-declared closed denominator:

        1  Sales -> Inventory
        2  Sales -> Manufacturing (where make is required)
        3  Sales -> Purchase (where dropship/buy/MTO requires procurement)
        4  Manufacturing -> Inventory
        5  Inventory -> Accounting
        6  Sales -> AR/Accounting
        7  Purchase -> AP/Accounting
        8  Payment -> Bank/Accounting
        9  Asset -> Accounting
       10  Expense -> Accounting
       11  Tax -> Accounting/reporting
       12  Close -> required subledgers/control sources

     RULING:  [ ] DECLARE AS ABOVE (12)
              [ ] DECLARE 18 (XMC-H-01..18)
              [ ] DECLARE 10 (SA_CORR4_02 §5)
              [ ] DECLARE OTHER: ______________________

B3'  VETO CANONICAL COUNT
     RULING:  [ ] RATIFY CLASS C — canonical count = 7
              [ ] KEEP 6 and publish a declared exclusion, reason: ______
     NOTE: AAS+ is the issuer; this ratifies membership, not discharge.

CC-D-01  PRODUCT CLASSIFICATION + SERVICE UNDER ND-09
     (a) PRECEDENCE
         [ ] Opt 3 (rec) KIND governs admissibility, CATEGORY governs
                         measurement, with an explicit refusal rule
         [ ] Opt 1 KIND governs   [ ] Opt 2 CATEGORY governs
         [ ] Opt 4 other: ______________________
     (b) SERVICE UNDER ND-09
         [ ] Opt B (rec) recorded determination that no cost recognition arises
         [ ] Opt A bound cost recognition from IR-17 consumption
         [ ] Opt C split by whether IR-17 consumption occurred

B1   SIX OPEN DECISIONS (all recommendation-complete)
     RC-D-03 Private Company escalation criteria
         [ ] APPROVE Model (a) objective-threshold, NEVER list binding,
             four externally-attributable trigger classes, closed for v1
         [ ] MODIFY: ______________________
     RC-D-04 Mapping-layer ownership (CF-XCR-GAP-01)
         [ ] APPROVE Model (a) split ownership, pre-assigned, dormant in v1
         [ ] MODIFY: ______________________
     POH-D-01  [ ] APPROVE as recommended  [ ] MODIFY: __________
               (NOTE: POH-D-01 also gates scenarios X-16 and X-17)
     POH-D-03  [ ] APPROVE  [ ] MODIFY: __________
     POH-D-04  [ ] APPROVE  [ ] MODIFY: __________
     POH-D-05  [ ] APPROVE  [ ] MODIFY: __________
     EXCLUDED: POH-D-02 — Thai statutory evidence absent; no Boss act
               can move it. NOT presented.

B6   PTX EXIT-CONTROL SET
     RULING:  [ ] ADOPT PTX-01..PTX-11 as canonical, denominator = 11
              [ ] REJECT   [ ] AMEND: ______________________
     NOTE: 9+11=20 would double-count RT-E15. 0 of 11 are satisfied.

B2   AAS-V-02 RATIFICATION
     RULING:  [ ] RATIFY the discharge act   [ ] WITHHOLD again
     NOTE: implementation start stays barred by RC-V-01 either way.

B7'  B-7 APPOINTEE
     RULING:  APPOINTEE = ______________________________
              [ ] different model/vendor, new session (strongest)
              [ ] same model family, new session, no context inheritance
     Eligibility criteria: 20_ §2. SMEs Core named 0 candidates.

B8'  E2E-04 RE-GRADE OWNER
     RULING:  [ ] STRUCTURE A (rec) SMT re-grades; B-7 verifies independently
              [ ] STRUCTURE B  B-7 owns the re-grade
              [ ] OTHER: ______________________

B9'  MIGRATION CLASS ADMISSION
     RULING:  [ ] ADMIT MF-01 (certified opening balance) to IR and AR
              [ ] ADMIT MF-02 (historical movement history) to IR
              [ ] EXCLUDE MF-03 (replay) as a dimension, not a flow
              [ ] OTHER: ______________________
     EFFECT IF AS RECOMMENDED: IR 18 -> 20, AR 29 -> 30.

----------------------------------------------------------------
NOT ASKED, AND WHY
  B5'  19/2/1 readiness split — carried PROVISIONAL; it is B-7
       attack target #1 and adopting it now could be reversed in
       one round. Boss may still direct adoption.
  B10' Commercial-terms freeze flag — resolved as an Architecture
       determination (TERMINAL BY DESIGN at the cross-module
       boundary; it freezes 8 named line fields within its own
       module, so it is wired, not unwired). Boss may overturn.
----------------------------------------------------------------

THIS RULING BLOCK DOES NOT:
  - declare Pre-Test PASS
  - authorize Functional Design
  - discharge any veto
  - create runtime proof (0 of 48 unchanged)
  - substitute for Thai statutory authority
================================================================
```

---

## 1. What each ruling unblocks — and what stays blocked regardless

| Item | Unblocks | Still blocked after |
|---|---|---|
| `B4′` | FD blocker 1 · the applicability declaration | contract **content** per boundary |
| `B3′` | the veto denominator · `CC-F-06` | limb-2 re-wording (**AAS+**) |
| `CC-D-01` | FD blocker 5 · `X-18` · `E2E-08` | `IR-17` service consumption `PARTIAL` |
| `B1` | `X-16`/`X-17` gating (via `POH-D-01`) · `F5`/`F6` residue | `POH-D-02` — statutory |
| `B6` | exit criteria defined | **`0 of 11` satisfied** — element 15 unbuilt |
| `B2` | one veto's residual act | `5` other vetoes |
| `B7′` | `EC-07` route · `CP-PT-14` route | `EC-07` `0/2` until **2 clean passes** |
| `B8′` | exit condition 11 route | the re-grade itself |
| `B9′` | exit condition 5 | `MF-01`'s counterpart account |

> **`0` of the nine produces runtime proof. `EC-04` stays `0/3` and the 48-point register stays
> `0 PASS / 48 HOLD` no matter how Boss rules.** Rulings unblock **writability and scope**, never proof.

---

## 2. Checkpoint

> ## `CHECKPOINT F — ONE-TURN PACK PUBLISHED`
>
> **`9` items in one block · `2` withheld with reasons · `1` (`POH-D-02`) excluded on statutory grounds ·
> `0` pre-approved · `0` rulings create a `PASS`, discharge a veto, or authorize Functional Design.**

