# ACCOUNT WAVE A — MCC MASTER RECONCILIATION

Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-MCC-001` · Layer 1 clean-room
Parent `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-MC-001` · commit `33cdc6fa009c4eafcca543c253ccad19e97fd0dc`
Programme `SMEPLUS-26-09-04-ACCOUNT-FULL-DEEP-001` · Standard `SMEPLUS-DR-MC-001`
Depth `VERY DEEP / L99999.99999` · Mode `AUTONOMOUS / TARGETED / EVIDENCE-FIRST / FIXED-POINT`

> **Recommendation only. Boss is the sole Final Approver. Nothing here is a gate movement.**

---

## 1. What was asked, and what happened

**Asked:** do not reopen broad research. Close, in order, `GB-03` → `FX-08` / `MCU-13` → gating
unknowns → denominator reconciliation → negative claims → balanced-but-wrong → fixed point →
`MC-01`…`MC-10` → expert challenge → reusable method.

**Happened:** the chain was executed in order and to its end. **One of the four blockers reported
"closed with evidence" was closed on a mechanism that does not exist on this build.** The rate-table
population became the first population in the programme's history to reach a **proven path set at
100% evidence coverage**. Nine gating unknowns closed against a prior record of zero. And then two
fresh independent passes returned **fifteen material deltas**, invalidated **three of this round's own
claims**, added **three tolerance-zero boundaries**, and found **962 manifested modules outside the
tree that five rounds had been searching**.

---

## 2. The targeted chain — result per link

| Link | Result |
|---|---|
| `GB-03` root closure | **`PARTIAL`.** Split into two axes with different owners: the **branch** axis is research-complete with one residual; the **null-company** axis is an unclosed verified defect that reduces into `GB-01`, the Boss company/tenant decision |
| `FX-08` / `MCU-13` forensic re-verification | **`PARTIALLY VERIFIED`.** Resolver half re-confirmed **and extended**; **writer half `CONTRADICTED` at three independent layers**; composite defect **`NOT REPRODUCIBLE`** on this build; `BW-16` withdrawn; one residual, class `D` |
| Gating unknown exhaustion | **9 of 17 closed** — the first non-zero closure count in the programme. **Standing total 17**, membership almost entirely different |
| Denominator reconciliation | **`41` vs `59` RESOLVED**: they count two differently-keyed populations with **no crosswalk in any file**. 15 of 15 recounted denominators reproduce; **6 of 6 definitions tested fail** |
| Negative-claim exhaustion | **`PARTIALLY VERIFIED`.** First round whose own output was fully scanned; 3 of its own negatives withdrawn; 9 unbounded negatives found in the parent; 2 class-`B` claims wearing class-`A` clothing reclassified |
| Balanced-but-wrong fixed-point proof | **19 of 19 classes now searched.** Floor **36**. **Both** previously-empty classes produced a verified defect on first search |
| Fixed-point convergence | **`FIXED POINT NOT REACHED`.** Six of seven criteria fail on **both** consecutive passes |
| `MC-01` … `MC-10` re-run | **8 not met · 2 partially met · 0 met.** One up, one down, no criterion weakened |
| Expert and audit challenge | §7 |
| Reusable method harvest | `ER-CORE-1` … `ER-CORE-7` + 7 boundary-specific rules + 8 proposed standard deltas |

---

## 3. The single most consequential finding

> ### `FX-08` — a blocker the programme has carried as a `VERIFIED DEFECT` through two gate reports — describes a state that cannot be constructed on this build.

Its recorded mechanism is *"the writer stores a branch company; the resolver looks for root-or-null;
the two do not intersect."* Three independent layers each foreclose the writer half:

1. a **model constraint** rejects any rate row naming a company that has a parent;
2. the company model **refuses any write containing the parent field** — the hierarchy is immutable
   after creation, closing the only route to a rate row becoming branch-scoped later;
3. **the company currency is root-delegated** — a branch cannot hold a currency different from its
   root's, so a branch has no currency for which it could need its own rate. The scenario is not
   merely blocked; it is **semantically empty**.

And the parent round's stated reason for not acting on this — *"a constraint can be bypassed by paths
that do not go through it (raw SQL: 62 sites)"* — **does not survive**: across 1,752 module
directories there is **no raw-SQL write to the rate table at all**, and none of the 62 accounting
raw-SQL sites touches it.

**What this does not mean.** It does not exonerate the rate table. The **other** half of `GB-03` — the
company-less rate row — is untouched and is worse than `FX-08` ever was: admitted by an explicit
disjunct in the record rule, creatable by a routine accounting role, resolved by six paths and refused
by six others, **and widened again on the version SMEsPlus is targeting.**

---

## 4. Blocker position after this round

| # | Blocker | Position |
|---|---|---|
| `GB-01` | Cross-company / cross-tenant measurement crossing | **UNCHANGED — Boss decision.** `GB-03`'s open half now reduces into it, so it carries more weight, not less |
| `GB-02` | Cross-company rewrite of a posted fact bypassing the hard lock | **WIDENED TWICE.** A new path admits **cross-branch reconciliation, exchange-difference posting and a raw-SQL settlement write**; and the lock-exception object — the control over the lock — has **no record rule**, honours a caller-supplied company on create, and authorises revocation on **group membership alone** before writing under elevated privilege |
| `GB-03` | Inconsistent company scoping over one rate table | **`PARTIAL`** — §2. Bounded for the first time: **20 files, 14 sites / 12 expressions, 6 including the shared row and 6 refusing it** |
| `GB-04` | Cross-boundary exposure not characterised | **UNCHANGED IN SUBSTANCE, WORSE IN SCOPE.** 192 sites bounded, 9 assessed — and the bound was computed over a path set now known to exclude 962 modules |
| `GB-05` | Affirmative safety claims unaudited | **UNCHANGED.** 7 contradicted claims still live in the canonical registers |
| `GB-06` | No correction-propagation channel | **CHANNEL NOW EXISTS AND WAS DEMONSTRATED**, including on this round's own errors. **Backlog uncleared** |
| `GB-07` | The Wave A source surface is under-bounded | **CONFIRMED AND WIDENED ON A NEW AXIS.** Not only the file list: the **module tree** itself. 791 searched, 962 manifested modules unsearched, holding **904 of 906 localisations** |
| **`GB-08`** | **NEW — the reference implementation is not stable across the versions SMEsPlus spans** | A branch-preference behaviour exists in a later v18 point release and in **neither** v19 tree; a rate reader exists in v18-e-20250608 and in no other tree; and **v19 adds an eleventh rate resolver in the ORM core**, bypassing every record rule, converting at *today*, with a **fourth** fallback semantic. **A v18 → v19 migration widens the control surface rather than converging it.** Second independent confirmation of this property in this programme, in a second domain |

---

## 5. Tolerance-zero position

| id | Boundary | Status |
|---|---|---|
| `T0-01` … `T0-06` | inherited | **UNRESOLVED** |
| `T0-07` | Cross-company rate resolution in raw SQL with an undeclared par fallback | **CHARACTERISED — worse than registered.** 8 raw-SQL reads, three addons, **four** distinct fallback semantics. **UNRESOLVED** |
| **`T0-08`** | **Entry identity** | **NEW.** Declared uniqueness constraint with an **empty definition string**; real control a raw-DDL index scoped by **journal, not company**; conditional lock; missing index degrades to a **log line**; a wizard that **blanks the number to escape the index**; a database-wide key disabling number/date alignment. **UNRESOLVED** |
| **`T0-09`** | **Declared-but-inert control** | **NEW.** 16 company-consistency guards on the company model — on the destination accounts of automatically generated ledger facts — that **can never execute**. **UNRESOLVED** |
| **`T0-10`** | Cross-company creation and revocation of the lock exception | **NEW. UNRESOLVED** |

**Ten boundaries. Zero resolved. `CONDITIONAL PASS` is unavailable by rule, not by judgement.**

---

## 6. What this round proved about the method

Three facts, and they point one way.

**1. The discovery asymmetry survived a round designed to break it.** Five rounds; every material
correction from an independent reviewer, none from the author — *including this round, convened to
close the round convened to diagnose that pattern.* Pass 1 caught **one** of its own four errors.

**2. The author mis-calibrated the instrument.** The reviewer brief written by this session named the
ORM core one directory too deep. A reviewer following it literally would have scored a class-`B`
result as class `A`. One reviewer found the real path and **reported the brief as defective**.
**A control designed by the author is not independent of the author.**

**3. Every remaining defect is one defect in six costumes.** The rate surface, the module tree, the
localisation surface, the demo data, the version comparison, the unit of count — **a proxy was
substituted for the source, and the proxy was chosen by the person whose claim it bounded.**

> ### A denominator is `POPULATION` + `PATTERN` + `PATH SET` + `UNIT`, and none of the four may be chosen by the author of the claim it bounds.
>
> `GB-04` learned *population*. `GB-07` learned *pattern*. This round learned *path set* — twice, once
> against itself — and *unit*. **The fifth clause, independence, is the one never implemented, and it
> is why the other four keep failing.**

---

## 7. Expert and audit challenge

See `MCC_J_FRESH_EXPERT_AND_AUDIT_CHALLENGE.md`. Consolidated position and any veto are recorded
there and carried into the gate report.

---

## 8. Progress — reported only where a verified denominator exists

| Metric | Value | Denominator basis |
|---|---|---|
| `% MCC phase completion` | **11 of 11 (100%)** | Phases A–K, fixed by the round instruction |
| `% Targeted closure chain executed` | **10 of 10 (100%)** | §2 |
| `% Rate-table surface evidence coverage` | **20 of 20 files (100%)** | proven path set, declared pattern, 3 false-negative modes tested |
| `% Rate-table scoping-rule assessment` | **100%** | 14 sites / 12 expressions, all read |
| `% Config-key assessment` | **6 of 6 (100%)** | call-site enumeration, each site read |
| `% Balanced-but-wrong classes searched` | **19 of 19 (100%)** | the taxonomy's own class list |
| `% Gating unknown closure` | **9 of 17 (52.9%)** | the inherited gating set |
| `% Denominators reproducing under recount` | **15 of 15 (100%)** this round; **20 of 24** on the adversarial recount | the selected sets, listed |
| `% Denominator DEFINITIONS surviving challenge` | **0 of 6 (0%)** | the six tested |
| `% Elevation-site assessment` | **0 of 93 (0%)** | — |
| `% Raw-SQL-site assessment` | **0 of 62 (0%)** | — |
| `% Board`, `% STATE`, `% STEP` | `PERCENTAGE NOT REPORTABLE — DENOMINATOR NOT VERIFIED` | no verified programme-level denominator exists |
| `% Evidence coverage (whole package)` | `PERCENTAGE NOT REPORTABLE — DENOMINATOR NOT VERIFIED` | the published 95.5% is invalidated by an unapplied correction notice |
| `% Contradiction resolution` | `PERCENTAGE NOT REPORTABLE — DENOMINATOR NOT VERIFIED` | the metric was widened at the parent gate |
| `% Unknown closure (whole package)` | `PERCENTAGE NOT REPORTABLE — DENOMINATOR NOT VERIFIED` | two incompatible id schemes, no crosswalk |

---

## 9. What is NOT declared

**Converged · Final approved · Final freeze · Wave A closed · Gate movement · Implementation
authorisation · Team B or Team C hand-off.**
**Wave B has not started. No SMEsPlus or reference source code was modified. Nothing was merged or
deployed.**
