# [SMEPLUS-26-09-04-INV-R4-AAS-PMO-REVIEW-001]
# 06 — Accounting COGS Dependency Review

Control Level: `/L9999.9999`
Status: `HOLD - ACCOUNTING COGS GAP EVIDENCE REQUIRED — DEPENDENCY CONFIRMED NOT LIFTED — R4's TREATMENT VERIFIED CORRECT`

---

## 1. The Question

The authorization asks whether the Accounting COGS dependency remains a `HOLD`, and requires the review to confirm what the commit `a959327938cc1168c93e1e4a89bd1dcf846871c5` evidence actually establishes.

This is the one area where a reviewer can be misled in **both** directions. Declaring the dependency lifted because a research package now exists would be wrong. Declaring the research un-executed would also be wrong, and was the standing position until R4 corrected it.

---

## 2. Independent Verification Of The Evidence Chain

Every branch and commit R4 cites was resolved in this session's own clone. Nothing below is taken from R4's description.

| Package | Commit Cited | Resolves? | Deliverables Claimed | Deliverables Found | Terminal State Per R4 |
|---|---|---|---|---:|---:|---|
| COGS Deep Research (`ERPPLUS-142`) | `a959327938cc1168c93e1e4a89bd1dcf846871c5` | **Yes** | 37 | **37** in `.../COGS_DEEP_RESEARCH/RESEARCH_V1/` | `HOLD / EVIDENCE REQUIRED — COGS MATERIAL UNKNOWN NOT EXHAUSTED` |
| COGS Fact Verification | `178cd06f7e9923bb3f876e17664f4833e534833c` | **Yes** | 20 | Confirmed present | `PARTIAL FACT BASELINE — TARGETED EVIDENCE REQUIRED` |
| COGS Targeted Resolution | `8a90f60b629eea2c1d34b39eb08123f0c16acd97` | **Yes** | 25 | Confirmed present | `PARTIAL RESOLUTION — CONTROLLED DECISIONS REQUIRED` |
| COGS Joint Closure | `13219268caa67a8e9bd32a062a346edc958e78ab` | **Yes** | 4 — governance container only | **Exactly 4**: session control, baseline pointers, resume-blocker register, Boss execution authorization | `HOLD — DEPENDENCY EVIDENCE PACKAGE BEING RESTORED` |

**Both of R4's load-bearing factual claims about the chain verify exactly.**

### 2.1 The Joint Closure branch is confirmed content-empty for closure

This review independently listed the tree at `13219268` and found precisely the four governance-container files R4 names, and **no joint decision closure document, no joint cross-proof, and no closure verdict**.

This matters more than its size suggests. A downstream reader encountering a branch named `audit/cogs-joint-closure-...` would reasonably assume closure occurred. It did not.

**Any claim, present or future, that the Joint track has closed anything is unsupported by the evidence on that branch.** This review restates that in the same terms as R4.

### 2.2 `R4-D-01` is a correct and material correction

The Inventory v2.0 package recorded `RISK-COGS-01`, severity `BLOCKING`, asserting that the COGS Deep Research had **not been executed** and that *"no commit, branch or archived record exists for any of its 37 mandatory deliverables."*

That assertion is **factually false as of today**, verified directly: the commit resolves and carries exactly 37 deliverables.

R4's handling of the correction is exactly right and this review endorses it without reservation:

- The correction is recorded, not buried.
- **The dependency is not lifted by it.** The executed package closes none of the twelve Joint decisions, and its own terminal state is a `HOLD`.
- What changes is the **reason** Inventory is blocked, and therefore the **remedy**. It is no longer "the research has not been done". It is "the research was done and concluded the decisions still cannot be closed."

**Consequence for Boss, restated because it is the practical point:** commissioning the COGS Deep Research again would achieve nothing. Its own named missing inputs are business-SME input, Thai statutory confirmation, and live reference-instance access — **none of which another research pass supplies**. PMO recommends against re-commissioning it and this review concurs.

---

## 3. The Ten Dependency Areas

R4 reports 10 of 10 locked. This review checked each against its governing decision and finds the lock correctly applied in every case.

| # | Area | Governing Decision | Lock Correct? |
|---:|---|---|---|
| 1 | COGS at delivery | `JT-04` **NOT DECIDABLE** | Yes |
| 2 | Stock input interim | Pre-version-19 pattern only; periodic equivalent is a blocking open item | Yes |
| 3 | Stock output interim | Same open question, sale side | Yes |
| 4 | Periodic vs perpetual | `JT-03`; **no stable reference pattern exists to imitate** | Yes |
| 5 | Standard / average / FIFO | `JT-02`; FIFO return behaviour **community-corroborated only** | Yes — and the evidence grading is correctly preserved rather than levelled up |
| 6 | Return cost basis | `JT-05` **NOT DECIDABLE** | Yes |
| 7 | Scrap and salvage | No safe default documented; **salvage has no reference concept at all** | Yes |
| 8 | Landed cost allocation and posting | `JT-08`, **Audit VETO retained** | Yes |
| 9 | Period close and late movement | `JT-06`, `JT-07`; guard mechanism fixed in v1.0, late-cost consequence locked | Yes — the split between fixed mechanism and locked consequence is precise and correct |
| 10 | Inventory report to GL reconciliation | Holds at the closing boundary, not continuously | Yes — **with a non-blocked disclosure obligation**, see §5 |

**10 of 10 remain locked. No area is upgraded by R4 and none is upgraded by this review.**

---

## 4. Did R4 Trespass On Accounting's Territory?

This is the test AAS+ Track 06 applied and the one most worth re-running, because a Deep Research session that quietly decides valuation questions would be a serious control failure.

| Test | Result |
|---|---|
| Did R4 decide any of the twelve Joint decisions? | **No.** All twelve remain open; three are formally NOT DECIDABLE |
| Did R4 state Accounting facts as settled positions? | **No.** Facts are cited as *recorded in the COGS evidence*, and every conclusion drawn from them carries `DEPENDENCY: ACCOUNTING COGS GAP` |
| Did R4 build on evidence whose owner does not consider it complete? | **Yes — and it discloses this.** Track 06 raised it; the qualification is carried throughout. The distinction must survive into any downstream summary, which this review restates |
| Did R4 answer `SME-Q-03`? | **No.** Explicitly not attempted. The prohibition on any AI answering it is preserved |
| Did R4 make any Thai statutory claim? | **No.** All nine `TH-HOLD-*` items routed to the Accounting-Tax track and held. Independently scanned — no statutory assertion found |
| Did R4 contribute anything valuation-adjacent it should not have? | **No.** Its seven contributions at `17` §6 are each a *fact* or a *consequence*, never a decision |

**Verdict: no trespass.** The dependency lock is applied with discipline, and in the one place where R4 comes closest to arguing toward a Boss decision (`C-02`), it states the evidence and explicitly declines the decision — which AAS+ Track 09 tested and accepted.

---

## 5. What The Dependency Does *Not* Block

Recorded because the largest practical risk in this register is that a reader treats `HOLD` as a general stop on Inventory.

The seven Inventory-owned obligations at `17` §7 and `12` §5 require **no** Joint decision and **no** COGS evidence:

1. Classification on every non-sale stock reduction — **the single highest-value item here**, because it is what stops a periodic cost-of-sales computation from silently mislabelling scrap, shrinkage, write-down and adjustment as cost of sales. Inventory is the only domain that can supply it.
2. Reversal-to-original linkage on every correction.
3. Physical event date and entry date carried as two distinct values.
4. Landed cost allocation statement inspectable **before** validation.
5. Quantity-side cutover reconciliation, certifiable independently of the value side (`R4-F-25`).
6. An independent check that internal-to-internal movements net to zero value effect (`R4-F-18`).
7. Movement history with an explicitly stated ordering rule (`R4-F-08`).

Plus the disclosure obligation from dependency area 10: any SMEsPlus reconciliation output must **state which posture it measures against**. R4's point stands and is worth repeating — an unqualified claim that the two balances always match is not supported by any evidence in this programme.

**These are Lane A. They are the work that is available now.**

---

## 6. Verdict

| Question From The Authorization | Answer |
|---|---|
| Does the Accounting COGS dependency remain a `HOLD`? | **Yes. Confirmed, and not lifted by any evidence reviewed** |
| Does the COGS evidence exist? | **Yes — verified. 37 deliverables at `a959327`** |
| Does its existence resolve the dependency? | **No.** It closes none of the twelve Joint decisions and its own terminal state is a `HOLD` |
| Is the Joint Closure branch a source of closure? | **No — independently confirmed content-empty for closure deliverables** |
| Is `R4-D-01` correct? | **Yes**, and it is material because it changes the remedy |
| Should the COGS research be re-commissioned? | **No.** Its missing inputs are business-SME, Thai statutory and live-instance — not research |
| Are all ten dependency areas still locked? | **Yes — 10 of 10** |

**`HOLD - ACCOUNTING COGS GAP EVIDENCE REQUIRED` — CONFIRMED AND CARRIED. Nothing closed by this review.**

---

`No Evidence = No Progress.`
`Never Skip Gate.`
`Boss = Sole Final Approver.`
