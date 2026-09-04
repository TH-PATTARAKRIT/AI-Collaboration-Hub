# [SMEPLUS-26-09-04-INV-R4-AAS-PMO-REVIEW-001]
# 05 — 92 Open Items — Lane Split Register

Control Level: `/L9999.9999`
Status: `LANE SPLIT COMPLETE — 32 NEW ITEMS FULLY ENUMERATED — 60 PRIOR ITEMS CLASSIFIED BY FAMILY — ROLL-UP NOT INDEPENDENTLY RECONSTRUCTABLE`

---

## 1. Method And Field Set

Every item below carries the nine fields the authorization requires: item ID, source file, evidence citation, lane, severity, owner, next action, whether it blocks Inventory Final Solution v2.0, and whether it blocks the Development Final Gate.

**Nothing in this register is closed by this review.** Assigning a lane is not closure, and naming an owner is not authorization.

---

## 2. Lane Vocabulary Collision — Read This Before The Tables

This is the single largest misreading risk in the R4 handover and it must be stated before any table.

**R4's registers use a different lane vocabulary from the one this authorization mandates, and the two use the same letters for different meanings.**

| Letter | R4's meaning (v2.0 decision matrix, `20` §1) | This authorization's meaning |
|---|---|---|
| **A** | Proceeds now, unaffected | Inventory-owned architecture / control / data identity |
| **B** | Proceeds now, valuation-adjacent but not gated | **Accounting COGS / valuation / period-close dependency** |
| **C** | **Waits for Accounting COGS Gap evidence** | Business SME / Thai user / statutory validation |
| **D** | Waits for a Boss-only ruling independent of COGS | Clean-room / governance / audit veto / Boss ruling |
| **E** | — | Cross-module joint decision |
| **F** | — | Duplicate / superseded / no-action |

The collision is severe on **B** and **C**, which are almost inverted: R4's Lane C is this authorization's Lane B.

**Worked example.** `R4-F-05` (landed cost allocation distorts silently) is recorded by R4 as **Lane C**. A reader applying this authorization's vocabulary would read that as "Business SME / Thai validation". It is in fact a **COGS / valuation dependency** — this authorization's **Lane B**.

**Every lane value in the tables below is this authorization's vocabulary.** Where R4 assigned a lane, its original letter is shown in parentheses so the translation is auditable rather than silent.

Recorded as `REV-F-03`, severity `MATERIAL`, Lane D. **Recommended action: Boss ratifies one lane vocabulary for the programme.** Until then, every cross-document lane reference is ambiguous, and this review's translation is the only published mapping.

---

## 3. The 92 Figure — Reconstructability Test

The authorization asks whether the 92 open items are complete, duplicated, under-specified or misclassified. This review tested the figure arithmetically.

**The 32 new items reconstruct exactly:** 25 `R4-F-*` + 3 `R4-D-*` (disclosures `03`, `04`, `05`; `R4-D-01` and `R4-D-02` are corrections to existing items, not new items) + 3 `R4-Q-*` + 1 `R4-N-6` = **32**. Independently verified: 25 distinct `R4-F-*` IDs counted in the register.

**The 60 prior items do not reconstruct.** Summing the categories `20` §2 itself lists gives: 5 clean-room + 10 carried conflicts and unknowns + 12 Joint + 23 `GAP-FS` + 9 `TH-HOLD` + 1 `RISK-COGS-01` + 31 `GAP-MD` = **91**, before the row that reads only "as above". The register states the total as **60** on a "v2.0 roll-up basis", which necessarily involves substantial de-duplication — `GAP-MD-*` items map onto `GAP-FS-*` items, `U-01`..`U-07` map onto `RISK-U01`..`RISK-U07`, `C-01`..`C-05` map onto `RISK-C01`..`RISK-C05`.

**No de-duplication map is published.** The crosswalk R4 does publish (`02` §1A) is a **menu** identifier crosswalk (`INV-M*` ↔ `MENU-*`), not an open-item crosswalk. This review counted **151 distinct prior item identifiers** actually cited across the R4 package.

| Question | Answer |
|---|---|
| Is the 92 total wrong? | **Not demonstrably.** It is a carried roll-up and may well be correct |
| Is it independently reconstructable? | **No** |
| Is the *new* portion reconstructable? | **Yes — 32 of 32, exactly** |
| Is anything duplicated? | **Almost certainly yes, by design** — `GAP-MD`/`GAP-FS` and `U-*`/`RISK-U*` are overlapping identifier families and the register says so |
| Is anything under-specified? | **Yes — the roll-up basis itself.** A count cited in the Boss package and the closure record should be reproducible from published evidence |

Recorded as `REV-F-04`, severity `MATERIAL`, Lane D. **Recommended action: publish an open-item crosswalk and de-duplication map before the 92 figure is relied on for scope or resourcing.** This is a register-hygiene defect, not an evidence defect — no finding is affected.

---

## 4. Lane Split — The 32 New R4 Items

Blocks v2.0 = blocks Inventory Final Solution v2.0 finalization. Blocks DFG = blocks the Development Final Gate.

### 4.1 Lane A — Inventory-owned architecture / control / data identity

| ID | Source | Evidence | Severity | Owner | Next Action | v2.0 | DFG |
|---|---|---|---|---|---|---|---|
| `R4-F-01` | `20` §4 | `INV-M01`, `INV-M27` shortfall uses greater of min/max; inverted entry silently accepted | MATERIAL | Inventory | Design validation rejecting inverted min/max | No | Yes |
| `R4-F-02` | `20` §4 | `INV-M02`; count is an attribute of the balance, no lifecycle or approval state | MATERIAL | Inventory | Originate count document identity + approval state | **Yes** | Yes |
| `R4-F-04` | `20` §4 | `INV-M04`; scrap has two states, no approval or rejection path | MATERIAL | Inventory | Originate scrap approval control | **Yes** | Yes |
| `R4-F-06` | `20` §4, `10` §2 | Traceable identity unique on (identifier, product, company); company-less identities possible; reactive duplicate check only | **BLOCKING** | Inventory + SaaS Foundation | Make company assignment mandatory below the application layer | **Yes** | **Yes** |
| `R4-F-07` | `20` §4 | `INV-M10`; available quantity display-clamped at zero while true on-hand can be negative | MATERIAL | Inventory | Decide and state the display contract | No | Yes |
| `R4-F-08` | `20` §4 | `INV-M12`; running balance differs by entry-sequence vs effective-date ordering | MATERIAL | Inventory | State and apply one ordering rule — **non-blocked, actionable now** | No | Yes |
| `R4-F-09` | `20` §4, `10` §2 | `INV-M18`; location company assignment is optional | **BLOCKING** | Inventory + SaaS Foundation | Make company mandatory on locations | **Yes** | **Yes** |
| `R4-F-11` | `20` §4 | `INV-M27`; rule uniqueness per (product, location, company); overlapping nested-location rules each raise supply | MATERIAL | Inventory | Hierarchy-aware uniqueness / conflict detection | No | Yes |
| `R4-F-12` | `20` §4 | `INV-M28`; misparsed structured barcode yields plausible wrong quantity silently | MATERIAL | Inventory | Parse-failure surfacing; depends on `R4-Q-03` | No | Yes |
| `R4-F-13` | `20` §4 | `INV-M29`; default conversion rounding upward, monotonic silent inflation | MATERIAL | Inventory | Decide rounding policy and residual handling | No | Yes |
| `R4-F-14` | `20` §4 | `INV-M01`; planning reads forecast including in-progress supply; run not reproducible | MATERIAL | Inventory | Record per-run input snapshot | No | Yes |
| `R4-F-15` | `20` §4 | `L7`; reference ERP supplies almost no approval infrastructure | MATERIAL, trending BLOCKING for build | Inventory + Boss scope | Boss scope ruling on internal-control origination | **Yes** | **Yes** |
| `R4-F-16` | `20` §4, `12` §2, `16` §3 | Three of sixteen contract elements unsuppliable; re-derived at `04` | **BLOCKING** | **Boss** | Commission the three capabilities in the `04` §4 ranked order | **Yes** | **Yes** |
| `R4-F-17` | `20` §4 | On-hand, reserved and incoming all depend on the one missing movement identity | **BLOCKING** | **Boss** | Follows rank 2 of `04` §4; severity gated on `C-02` | **Yes** | **Yes** |
| `R4-F-21` | `20` §4 | `L7-09`; two-staff SME will bypass a segregation model that cannot degrade | MATERIAL | Inventory + Thai validation | Compensating-control path; needs Lane C input | No | Yes |
| `R4-F-22` | `20` §4, `10` | Isolation must be proven on derived surfaces, not only stored records | MATERIAL | SaaS Foundation | Fold into the invariant set (rank 1) | **Yes** | **Yes** |
| `R4-F-23` | `20` §4 | `L10`; migrating legacy batch identities without company scope imports collisions in bulk | MATERIAL | Migration | Migration identity rules; depends on `R4-F-06` | No | Yes |
| `R4-F-24` | `20` §4 | `L10`; assigning location kinds by name-matching mis-states historical financial meaning | MATERIAL | Migration | Explicit location-kind mapping with human certification | No | Yes |
| `R4-F-25` | `20` §4, `12` §5 | Quantity-side cutover reconciliation achievable independently of value — **opportunity** | MATERIAL | Inventory | Certify the quantity half now — **non-blocked, actionable now** | No | No |
| `R4-D-05` | `20` §5 | Two reachable leads not followed: `C-04`, `N-A13-01` | MATERIAL | Inventory / Track 07 | One bounded verification pass — see `REV-F-01` at `02` §5 | No | Yes |

### 4.2 Lane B — Accounting COGS / valuation / period-close dependency

| ID | Source | Evidence | Severity | Owner | Next Action | v2.0 | DFG |
|---|---|---|---|---|---|---|---|
| `R4-F-05` (R4: C) | `20` §4 | `INV-M05`; weight/volume landed-cost allocation distorts when attributes unmaintained | MATERIAL | Inventory + Joint | Allocation-basis integrity check; posting gated on `JT-08` | **Yes** | Yes |
| `R4-F-18` (R4: A mechanism / C value) | `20` §4 | `L5-08`; internal-movement financial neutrality protected only by configuration | MATERIAL | Inventory | **Mechanism is Lane A and actionable now** — build the independent zero-value check. Value semantics gated | No | Yes |
| `R4-F-20` (R4: C) | `20` §4, `19` `L13-01` | Retroactive cost compensation sequenced by record creation order, not effective date | MATERIAL | Joint | Escalated to `L13-01`; requires `JT-03`, `JT-06` | **Yes** | Yes |

### 4.3 Lane C — Business SME / Thai user / statutory validation

| ID | Source | Evidence | Severity | Owner | Next Action | v2.0 | DFG |
|---|---|---|---|---|---|---|---|
| `R4-F-19` | `20` §4, `18` | Every semantic reaches the user as an unvalidated Thai label | **BLOCKING** for user-facing design | **Boss to commission** | Commission Thai validation; fill the review panel | **Yes** | **Yes** |
| `R4-Q-01` | `20` §6, `18` §6 | Reason taxonomy for adjustments and scrap — keeps non-sale reductions distinguishable | MATERIAL | Thai business panel | Route to panel; **no AI may answer** | **Yes** | Yes |
| `R4-Q-02` | `20` §6, `18` §6 | Are `INV-M12` / `INV-M13` comprehensible as two menus | MATERIAL | Thai business panel | Route to panel | No | Yes |
| `R4-Q-03` | `20` §6, `18` §6 | Which structured barcode formats Thai suppliers actually use | MATERIAL | Thai field validation | Route to panel; gates `R4-F-12` | No | Yes |
| `R4-N-6` | `20` §6, `18` §3.1 | Thai candidate strings diverge across three registers for five menus | MATERIAL | Thai naming panel | Panel settles; **executor may not** | No | Yes |

### 4.4 Lane D — Clean-room / governance / audit veto / Boss ruling

| ID | Source | Evidence | Severity | Owner | Next Action | v2.0 | DFG |
|---|---|---|---|---|---|---|---|
| `R4-D-03` | `20` §5 | Branch-base disclosure; two canonical-branch controls read by commit citation | WATCH | Boss / Audit VETO | Acknowledge. **This review verified both commits resolve** — see `01` §3 | No | No |
| `R4-D-04` | `20` §5, `13` §1.1 | Charter conditionality; two competing 9 Veto Council definitions (`U-07`) | **BLOCKING** for challenge finality | **Boss only** | Rule which charter governs. If the other governs, L12 must be re-run | **Yes** | **Yes** |

### 4.5 Lane E — Cross-module joint decision

| ID | Source | Evidence | Severity | Owner | Next Action | v2.0 | DFG |
|---|---|---|---|---|---|---|---|
| `R4-F-03` (R4: A scope / C value) | `20` §4, `19` `L13-02` | Scrap carries no salvage concept; salvage is original design work | MATERIAL | Inventory + Joint | **Boss scope ruling first** (Lane D), then Joint value treatment | **Yes** | Yes |
| `R4-F-10` (R4: C) | `20` §4 | `INV-M24`; product category owns reporting, put-away **and** costing — root of `GAP-FS-02` / `JT-01` | MATERIAL | Joint | Blocked on `JT-01`, which is **NOT DECIDABLE** | **Yes** | Yes |

### 4.6 Lane F — Duplicate / superseded / no-action

| ID | Source | Evidence | Severity | Owner | Next Action | v2.0 | DFG |
|---|---|---|---|---|---|---|---|
| `R4-D-01` | `20` §5, `17` §3 | Correction: `RISK-COGS-01` factually superseded — COGS package exists at `a959327` with 37 deliverables | CARRIED | Boss | **Acknowledge the correction and retire `RISK-COGS-01` as stated.** Verified independently at `06` §2. The dependency itself is **not** lifted | No | No |
| `R4-D-02` | `20` §5, `14` §5 | Correction: a packaging structure with a contained base quantity **does** exist | CARRIED | Boss | Acknowledge; `GAP-MD-18` stays open on its corrected premise | No | No |

**New-item lane distribution: A 20 · B 3 · C 5 · D 2 · E 2 · F 2 = 32.**

---

## 5. Lane Split — The 60 Prior Items, By Identifier Family

Classified by family because the roll-up is not item-reconstructable (§3). Every family is carried; **none is closed by this review**.

| Family | Count | Lane | Severity | Owner | Next Action | v2.0 | DFG |
|---|---:|---|---|---|---|---|---|
| `JT-01` .. `JT-12` Joint decisions | 12 | **E** | **BLOCKING** — `JT-01`, `JT-04`, `JT-05` formally NOT DECIDABLE | Joint Accounting × Inventory | See `09`. `SME-Q-03` to a Business SME is the fastest single unblock | **Yes** | **Yes** |
| `TH-HOLD-01` .. `TH-HOLD-09` Thai statutory | 9 | **C** (statutory sub-track) | `HOLD / EVIDENCE REQUIRED` | **Accounting-Tax track — not the user panel** | Route and hold. **No AI statutory claim permitted** | **Yes** | **Yes** |
| `GAP-FS-01` .. `GAP-FS-23` design gaps | 23 | Mixed — predominantly **A**, with `GAP-FS-08`/`-10` **A**, `GAP-FS-11`/`-13`/`-15`/`-16`/`-17`/`-18`/`-21`/`-22` **C**, `GAP-FS-19` **D** (scope ruling), `GAP-FS-02` **E** | Mixed to **BLOCKING** | Inventory / Boss / panel | Six have a materially improved evidence basis from R4 (`20` §3) — **improved, not closed** | Mixed | Mixed |
| `GAP-MD-01` .. `GAP-MD-31` Menu Deep Challenge gaps | 31 | Mixed, mapping onto `GAP-FS-*` | Mixed | As above | Six upgraded from *no evidence* to *first-hand structural evidence* | Mixed | Mixed |
| `RISK-U03` / `GAP-FS-10` multi-tenant invariant set | 1 | **A** | **BLOCKING** | Boss / SaaS Foundation | **Rank 1 of `04` §4.** Blocks all 8 L9 proofs and all 22 scenarios | **Yes** | **Yes** |
| `RISK-C02` / `IV-06` idempotency | 1 | **A** build / **D** severity ruling | **BLOCKING** | **Boss** | Rank 2 of `04` §4. Severity ruling is `C-02` | **Yes** | **Yes** |
| `GAP-FS-08` / `CN-36` provenance reference | 1 | **A** | **BLOCKING** for migration/replay | Migration + Inventory | Rank 3 of `04` §4 | **Yes** | **Yes** |
| `RISK-U01` / `U-01` authorization scope | 1 | **D** then **A** | **BLOCKING** for `L9-03` | **Boss** | Scope ruling on warehouse- and operation-level rights | **Yes** | Yes |
| `RISK-U02` / `U-02` damaged-goods state | 1 | **C** | MATERIAL | Thai panel | Recorded in prior evidence as *"simply never asked"* | No | Yes |
| `C-01` / `RISK-C01` cancellation-cascade symmetry | 1 | **A** | CONFLICTING | Team A / Track 01 | Arbitrate; blocks scenario 10 | No | Yes |
| `C-03` / `RISK-C03` / `JT-05` return cost basis | 1 | **E** | CONFLICTING, NOT DECIDABLE | Joint | Needs `SME-Q-02`, `TH-NEW-02`, live FIFO-return test | **Yes** | Yes |
| `C-04` / `N-CONC-01` reservation locking | 1 | **A** | CONFLICTING | Team A / Track 07 | **One bounded verification pass — reachable now.** See `REV-F-01` | No | Yes |
| `N-A13-01` override path | 1 | **A** | CONFLICTING | Team A / Track 07 | Same bounded pass | No | Yes |
| `C-05` / `RISK-C05`, `RISK-C05B` clean-room exposure | 2 | **D** | **BLOCKING** for downstream reliance | **Boss only** | Written containment ruling. **Independently confirmed still live** — see `08` §3 | **Yes** | **Yes** |
| `U-07` / `RISK-U07` charter conflict | 1 | **D** | **BLOCKING** for challenge finality | **Boss only** | Rule which charter governs | **Yes** | **Yes** |
| `RISK-CR-01`, `RISK-CR-02` verification risks | 2 | **D** | MATERIAL | Boss | Commission independent verification. **Partially addressed by this review — see `08` §5** | **Yes** | Yes |
| `RISK-COGS-01` | 1 | **F** | Superseded in fact | Boss | Retire per `R4-D-01` | No | No |
| `RISK-G1G2G3`, `RISK-G5`, `RISK-G7` | 3 | **E** | Mixed | Joint | Carried; `G-5` ties to `JT-11` | **Yes** | Yes |
| `RISK-N-A12-01` | 1 | **E** | MATERIAL | Joint | Blocks Joint Backbone publication | **Yes** | Yes |
| `GAP-FS-19` Manufacturing scope | 1 | **D** | **BLOCKING** for `JT-09` | **Boss** | Programme scope ruling | **Yes** | Yes |
| `U-05` multi-lane dispatch independence | 1 | **D** | WATCH | Boss | Governance unknown; raised again by Track 09 | No | No |
| `U-06` Material Unknown Exhaustion status | 1 | **D** | WATCH | Boss | Never formally re-declared or superseded | No | Yes |

---

## 6. Roll-Up

| Lane | Meaning | New Items | Character Of The Prior Set |
|---|---|---:|---|
| **A** | Inventory-owned architecture / control / data identity | **20** | The three structural capabilities, both reachable leads, `C-01` |
| **B** | Accounting COGS / valuation / period-close | 3 | Ten dependency areas, all locked (`06`) |
| **C** | Business SME / Thai / statutory | 5 | 78 unvalidated items, 9 statutory holds |
| **D** | Clean-room / governance / Boss ruling | 2 | `C-05`, `U-07`, `U-01`, `GAP-FS-19`, `C-02` severity, `RISK-CR-*` |
| **E** | Cross-module joint | 2 | All 12 `JT-*`, `RISK-N-A12-01`, `G-*` |
| **F** | Duplicate / superseded / no-action | 2 | `RISK-COGS-01` |

**The distribution is the finding.** Twenty of the thirty-two new items are Lane A — Inventory-owned and dependent on nothing upstream. R4 states this and this review confirms it under the authorization's own vocabulary, which is a stricter test than R4's, because this vocabulary does not let "not COGS-gated" absorb governance and Thai items into Lane A.

**Items closed by this review: 0.**

---

## 7. This Review's Own New Items

| ID | Item | Lane | Severity | Owner | Next Action |
|---|---|---|---|---|---|
| `REV-F-01` | Two reachable leads unfollowed is a **material shortfall under the corrected Full Depth standard**, not merely a scope choice | **A** | MATERIAL | Inventory / Track 07 | One bounded targeted pass on `C-04` and `N-A13-01` |
| `REV-F-02` | Handoff element 14 is contractually **conditional**; the three blockers are not equally load-bearing | **A** | MATERIAL | Boss / PMO | Commission in the ranked order at `04` §4 |
| `REV-F-03` | Lane vocabulary collision between R4's registers and this authorization | **D** | MATERIAL | Boss / PMO | Ratify one lane vocabulary programme-wide |
| `REV-F-04` | The 92 / 60 roll-up is not independently reconstructable; no open-item crosswalk exists | **D** | MATERIAL | PMO | Publish an open-item crosswalk and de-duplication map |
| `REV-OBS-01` | Manifest §4 names `bdef581` as fixing it, but `cefa39c` did | **D** | WATCH | PMO | Note; integrity unaffected — all 24 digests match |
| `REV-OBS-02` | File-count figures (24 / 25 / 26) inconsistent across `21`, `23`, `24` | **D** | WATCH | PMO | Note; no reliance consequence |
| `REV-OBS-03` | `L15-02` is a relocated carried conflict rather than a true escalation | **A** | WATCH | PMO | Note; read L13+ as 5 escalations + 1 relocation |
| `REV-OBS-04` | `20` §7 names five new BLOCKING IDs while stating "4 new" | **D** | WATCH | PMO | Reconcile the BLOCKING count — see `10` §4 |

---

`No Evidence = No Progress.`
`Never Skip Gate.`
`Boss = Sole Final Approver.`
