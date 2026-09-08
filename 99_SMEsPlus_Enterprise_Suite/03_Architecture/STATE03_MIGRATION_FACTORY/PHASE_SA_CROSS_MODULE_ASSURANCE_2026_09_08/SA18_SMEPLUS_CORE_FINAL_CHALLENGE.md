# SA18 — SMEs CORE FINAL CHALLENGE

Status: **HOLD — NOT READY FOR BOSS FINAL GATE** (master prompt §25 disposition)
Purpose: attempt to **falsify** the complete Phase SA baseline before Boss sees it.

---

## 1. Challenge result against the §25 list

| # | Challenge class | Result |
|---|---|---|
| 1 | Missing input | **FOUND** — `SA02`: 1 `INPUT-CONTRADICTION`, 1 `INPUT-GAP`, 6 domains cannot state inputs at all |
| 2 | Unusable output | **FOUND** — `SA03-F-01`: three outputs with no consumer; one required input with no producer |
| 3 | Wrong downstream consumer | Not found. Every evidenced route's consumer is named and its compatibility tested |
| 4 | Missing conditional route | **FOUND** — `SA04` §4 created the multi-consumer routes; 6 routes remain `HOLD` |
| 5 | Inventory inconsistency | **FOUND** — `SA06`: 4 of 17 stock-affecting flows unreconciled; `SA06-F-05` neutrality protected only by configuration |
| 6 | Accounting inconsistency | **FOUND** — `SA07`: 7 `UNKNOWN`, 11 `PARTIAL`; `SA11-F-01` a requirement with no mechanism |
| 7 | Timing mismatch | Addressed — ordering-independence is established and is the baseline's strongest principle (`SA09`) |
| 8 | Ownership ambiguity | **FOUND** — joint/co-product costing recorded as owned by no track; `XD-06` ruling without a contract |
| 9 | Exception gap | **FOUND** — 4 of 18 classes not established (`SA09-F-03`), all of them exceptions the world raises against the system |
| 10 | Reversal gap | Partially addressed — BD-ACC-01 rules it; derecognition entry recorded as draft and deletable |
| 11 | Idempotency gap | **FOUND** — handoff element 15 (deterministic idempotency identity) unsuppliable on every measured handoff |
| 12 | Tax gap | **FOUND** — `SA08-F-01`: the determination rule base is a single point of dependence, its own rule set unavailable, statutory currency unverified |
| 13 | Payment gap | **FOUND** — the settlement event's own date is required by Account and unsourced |
| 14 | Tenant leakage | **FOUND** — a company-resolution defect classified Critical, currently unable to fire; `SA10-F-03` |
| 15 | Company leakage | **FOUND** — `SA10-F-05`: two lock-defeat paths in the reference estate, one leaving no record |
| 16 | Approval gap | **FOUND** — `XD-03`: the occurrence half of approval unpopulated on 27,874 rows |
| 17 | Segregation-of-duties gap | **FOUND** — no maker-checker in the reference core ledger; `L7` inventory SoD reference pattern `None evidenced` |
| 18 | Audit evidence gap | **FOUND** — `MTI-50` specified, 0 proven; evidence retention floor specified, unproven |
| 19 | Standard / control gap | **FOUND** — `SA11`: 2 standard gaps, 9 control gaps, and `SA11-F-05` a live compliance overclaim |
| 20 | Source-copying | **Challenged and one instance flagged** — `SA12` §6: ND-02 resembles the reference shape, is adopted on independent rationale, and is flagged rather than hidden |
| 21 | Unsupported assumption | **FOUND in this package's own work** — 8 defects, `SA13` §2 |
| 22 | Unnecessary complexity | Not found. The 22-domain split derives from business natures and Boss boundary decisions, not from module structure |
| 23 | Missing SMEsPlus advantage | **Addressed** — 8 Nature DNA determinations with independent rationale (`SA17` §4) |

**19 of 23 challenge classes returned a finding.** A final challenge that returned few would not
have been a challenge.

---

## 2. The four falsification attempts that failed — and what that means

A challenge is only informative if it could have gone the other way. Four attempts to falsify
this package's central claims did **not** succeed:

| Attempt | Method | Outcome |
|---|---|---|
| *"The Account programme did address the Group A cancellation gate somewhere"* | Content search over all 2,722 blobs, joined to owning programme, with a positive control firing 17/17 | **Not falsified.** `ACCOUNT_REOPEN` = 0. Independently reproduced by a second searcher with different patterns, which additionally found the joint session was constituted and never convened |
| *"Supply routing is evidenced somewhere outside the declared path set"* | Whole-repo corpus, no directory pre-filter, 183 branches | **Not falsified.** 81 blobs, lowest of 22 domains |
| *"Kit / bill-of-material handling exists in the inventory packages"* | Declared pattern over four package populations with a firing positive control | **Not falsified** within those populations. Claim restricted to *not found in these populations* |
| *"The five thin domains are thin because the instrument is narrow"* | Same instrument, same unit, run against known-deep domains | **Not falsified.** Contrast is 4–34 blobs against 154–1,216 |

---

## 3. SA18-F-01 — the convergence claimed in `SA07` §4 is weaker than it looks

`SA07` §4 states that three instruments — a routing matrix, an inventory matrix and an
accounting matrix — independently converge on the same seven-item set, and adds that the
convergence is only meaningful if the instruments are genuinely independent.

**Tested. They are not fully independent.** All three inherit the domain classification made
once in `SA01` and the business-nature list made once in `SA05`. A domain wrongly classified
`THIN` in `SA01` would propagate into all three matrices and produce exactly the agreement
observed.

**What survives the test.** The `SA01` classification is itself measured against a contrast set
(§2 above, attempt 4), and the Group A finding was reproduced by a genuinely separate searcher
with different patterns and a different unit. So the *domain thinness* is independently
supported; the *seven-item set* is one classification seen three times.

**Correction applied:** `SA07` §4's convergence must be read as **one classification expressed
in three registers**, not three independent confirmations. This is recorded here rather than
silently left, because three instruments sharing one blind spot agree exactly as loudly as three
that are correct.

## 4. SA18-F-02 — the package's own instrument failures outnumber its reasoning failures

Of the defects found in this session's work, the count by class:

| Class | Count |
|---|---|
| Instrument / measurement defect (wrong pattern, wrong key, broken extraction, miscount) | 6 |
| Evidence-location defect (did not consume an artefact that was present) | 1 |
| Overclaim narrowed on new evidence | 1 |
| Reasoning defect | **0** |

Every defect found was a defect of *how the package looked*, not of *what it concluded from
what it saw*. That is consistent with the programme's own recorded history and is the reason
`SA00` §3 publishes the instrument failures rather than only the results.

**It is also a warning:** a package whose reasoning has never been falsified has probably not
been challenged by anyone whose reasoning differs. This session's challenge layers are the same
model as the author (`SA13` §1), so this row is expected and should not be read as strength.

## 5. SA18-F-03 — one class of defect this challenge could not test

Master prompt §25 asks for *missing SMEsPlus advantage*. Eight Nature DNA determinations are
recorded, each with independent rationale. **None has been tested against a differently-biased
party**, and a written method is not a controlled method until someone with a different bias
runs it.

Specifically untestable in this session: whether the eight determinations are the *right* eight,
and whether a genuinely independent architect would have reached different ones. That is not a
gap in the determinations; it is a gap in the assurance around them, and it is bounded by
`SA13` §1.

---

## 6. Material unresolved defects — the §25 disposition

| # | Defect | Why it blocks the gate |
|---|---|---|
| 1 | `XD-01` sell-side cancellation gate | A verified programme has been blocked on it for eight days; only Boss can resolve it |
| 2 | `XD-03` approval occurrence never recorded | An approval control with no evidence half is not a control |
| 3 | 7 of 18 business natures unroutable | The Business-Nature Routing Law is the constitutional core of Phase SA |
| 4 | 7 of 18 end-to-end scenarios not traversable, incl. the ordinary forward sale carrying two breaks | SMEsPlus cannot yet prove end to end that it can sell something |
| 5 | `SA11-F-01` overhead absorption required with no mechanism | A standards requirement with no route, gated behind a Boss decision |
| 6 | `SA11-F-05` live compliance overclaim on every branch | Prohibited by two Boss decisions; propagating |
| 7 | `SA13-F-01` prohibited verdict wording in the authorizing gate | The authority this session runs under carries a verdict the constitution forbids |
| 8 | `SA13` §1 the challenge is not independent | The programme's own independence standard is unmet |

Per master prompt §25: **any material unresolved defect ⇒ `HOLD — NOT READY FOR BOSS FINAL GATE`.**

There are eight.

---

## 7. What this means for the Boss Final Gate

`SA19` is produced and is **ready to be read**, because master prompt §26 requires Boss to see a
gate pack after challenge, and because two of the eight defects above are decisions **only Boss
can make** — leaving them unpresented would itself breach the first-detector rule.

But `SA18`'s own disposition on the *substance* is `HOLD`, and `SA19` states it that way. Boss is
being asked to decide, not to approve a completed phase.

---

`SA18 — HOLD — NOT READY FOR BOSS FINAL GATE` on substance; gate pack presented for the
decisions that are Boss's alone.

Boss remains the sole Final Approver.
