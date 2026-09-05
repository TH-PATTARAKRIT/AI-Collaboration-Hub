# ACCOUNTING — BOSS FINAL GATE PACK

Process `P11 — Central Core Accounting Reconciliation`
Session `SMEPLUS-26-09-04-ACC-P11-CORE-RECON-REV2-001` · Layer 1 clean-room
Repository `TH-PATTARAKRIT/AI-Collaboration-Hub` · Branch `research/account-core-reconciliation-2026-09-04-001`
Jira `ERPPLUS-138` · Date `2026-09-04`
Incorporates constitution correction `SMEPLUS-26-09-04-ACC-REV2-CORR1` (scope-aware), applied in-flight.

> **Recommendation only. Boss is the sole Final Approver. No AI may declare Final Approval.**
> **This pack is written so the Boss can decide without reading every `P01`–`P10` artefact.**

---

## 1. Executive summary

**What was asked:** reconcile ten business processes into one whole-system accounting semantics,
attack it for double counting, challenge it four ways, and hand the Boss a decision pack.

**What happened, in one sentence:**

> ### The reconciliation was scheduled before the things it reconciles existed.

At the moment P11's synthesis was written, **0 of 10** peer processes had published anything. Its
four-expert challenge was commissioned against **0** and reviewed against **2**. By the time the
session closed, **6 had published — and 2 were already at a later commit than P11 had read.**

**What the round nonetheless produced, and it is not nothing:**

| # | Result | Status |
|---|---|---|
| 1 | **Four genuinely new cross-domain findings** — `DC-09` double cost absorption, `DC-07` candidate double tax recognition, `UAE-31` absent absorption variance, `UAE-32` absent prior-period attribution. Each is unfindable from inside one domain; each was confirmed absent from the upstream packages by two reviewers | **stands** |
| 2 | **Four programme-level findings** — no declared output path; the Boss handoff contract binds one producer pair only; four missing statutory handoffs; and **the `P01`–`P11` process taxonomy does not exist in the canonical repository** | **stands** |
| 3 | **The double-counting attack: 17 classes, `0` with a working guard**, 4 of them root-independent design failures | **stands** |
| 4 | **The refusal to fabricate** the 30 withheld debit/credit cells — attacked by all four panels, broken by none | **stands** |
| 5 | The unified registers, the scope-ownership matrix, the ownership test | **`NOT CONVERGED` — 86 findings, 3 critical** |

**The recommendation is `HOLD`.** Not because the work is thin, but because `0 of 8` exit criteria are
met, `13+2` tolerance-zero boundaries stand unresolved — and `T0-13` is **reachable today inside a single company**, independently of any Boss ruling, `4+3` vetoes are undischarged, and the round's
own instruments failed under independent test.

## 1b. The joint position across three processes — stated as three halves, never as one figure

`P07` @ `1928410` put the cross-process ledger plainly and it belongs in front of the Boss as plainly
as the improvements do. **P11 publishes it under its own `P11-G-02`: three declared positions, each
executed or attributed by its owner, and no joint total** — because a cross-party tally cannot be
executed by any party to it.

| Process | Position | Evidence class |
|---|---|---|
| **`P11`** | **17 blockers, `0` closed. 13 tolerance-zero, `0` resolved. `0 of 8` exit criteria.** 27 own errors logged | **owner-executed** @ this commit |
| **`P04`** | `READY FOR CORE ACCOUNTING RECONCILIATION`; **`0 of 4` inherited blockers closed**; blocker rows risen 26 → 45 | `PEER-PUBLISHED` @ `6953856`, **not re-derived** |
| **`P07`** | **`RECOMMEND HOLD`, `0 of 8`**, tolerance-zero open, **no blocker closed** | `PEER-PUBLISHED` @ `1928410`, **not re-derived** |

> ### Three sessions. Materially stronger evidence bases. **Not one gate item closed between them.**
>
> The exchange **did** convert inference into fact in three packages — a peer recovered 685 asset
> records and two findings from evidence it had declared away; another closed a runtime unknown from a
> dump inside its own declared path set; P11 corrected a Boss-facing cost column and found ten
> accepted review findings that had never been applied.
>
> **None of that closed a gate item.** It made the packages more honest about how far they are from
> closing one. **Both halves belong in the record, and the second half is the one that bears on this
> decision.**

## 2. Whole business process map

```
 P01 Procure-to-Pay ─┐                                    ┌─> P07 Tax-to-Compliance
 P02 Order-to-Cash  ─┤                                    │
 P03 Manufacture-   ─┼─> Layer 2 VALUATION ─> Layer 3 ─> Layer 4 ─┼─> P08 Record-to-Report
     to-Cost         │   JT-01..05, JT-08,     ACCOUNTING  LEDGER │
 P04 Acquire-to-    ─┤   BLK-07 — ALL OPEN     EVENT              ├─> P09 Plan-to-Analyze
     Retire          │                       (DOES NOT EXIST)     │   (read-only; substrate
 P05 Expense-to-Pay ─┤                                            │    destructible)
 P10 Time-Based     ─┘                                            │
     Recognition                                                  │
 P06 Bank-to-Reconcile ──> emits UAE-01/02/03 ────────────────────┘
     (a consumer that is also a producer, owning none of what it emits)
```

**Missing from this map and from the canonical repository:** payroll; service and non-stockable
revenue; statutory document issuance; statutory filing. And the canonical
`END_TO_END_BUSINESS_PROCESS_MATRIX.md` contains **no cash, bank, payment, settlement or
reconciliation process** and **no manufacturing** — its chain terminates at *invoice* on both sides.

## 3. Whole accounting architecture

Four layers. The reference model has 1, 2 and 4. **It has no layer 3**, and seven independently
recorded symptoms across four domain programmes reduce to that one absence
(`P11_WHOLE_ACCOUNTING_SEMANTIC_MODEL.md` §4).

## 4–7. Canonical events, ownership, event-to-GL

| Register | Content | Position |
|---|---|---|
| Business events | **44 registered**; business denominator `UNBOUNDED` by declaration | **Under-extracted four ways** against its own bounded published sources (`X1-F08`, `X1-F14`) |
| Accounting events | **32** — 9 ledger-emitted, 16 producer-requested, **7 required and absent** | **27 of 32 have no verified posting pattern** (20 of 25 over extant events) |
| Ownership | `C1` **fails 44 of 44** — there is no accounting-event object. `C2` 9, `C3` 9, `C4` 1 of 44 | The `C1` universal failure **is** the finding; the rest are its consequences |
| Event-to-GL | 5 rows verified; **30 of 30 producer debit/credit cells withheld** | **Deliberately empty. Not one cell filled from convention** |

## 8–17. Domain integration

| # | Area | Position |
|---|---|---|
| 8 | Inventory / cost / COGS | **10 of 10 dependency areas `LOCKED`**; 12 Joint decisions open; `JT-01`/`JT-04`/`JT-05` **`NOT DECIDABLE`**; the Joint Closure branch is a **governance container only — 4 files, no closure deliverable** |
| 9 | AR | Subledger of record; recognition verified; **posting pattern withheld** |
| 10 | AP | As AR; `P05` producer contract **not established** |
| 11 | Asset | **The asset subledger is not reconciled to the ledger; six break mechanisms; none detected.** *"A reconciliation must be **originated** by SMEsPlus. There is nothing to adapt"* |
| 12 | Manufacturing cost | Conversion cost **excludes all fixed production overhead by construction** — inventory understated; **and machine time is charged twice where two people work one machine** — inventory overstated. **Five unreconciled monetisations of one machine hour** |
| 13 | Banking / settlement | **7 confirmed defects from 8 attacks.** *"The identity system fails open at every layer, in the same direction."* Duplicate bank transactions reachable by *"import a file twice — the lowest bar in the set"* |
| 14 | Tax / Thailand | 3 closed positions — **two accounting-standard, one regulatory; no `THAI STATUTORY REQUIREMENT` is closed by P11.** 7 statutory items held |
| 15 | Analytic / management | **Analytic is not a subledger of record.** No `P09` figure reconciles across any correction |
| 16 | Deferred recognition | **Producer contract not established at all** |
| 17 | GL / core ledger | Wave A `HOLD`; 12 tolerance-zero unresolved; `unbalanced-and-posted` **reachable** |

## 18–22. Reporting, close, multi-company, SaaS, correction

| # | Area | Position |
|---|---|---|
| 18 | Financial reporting | 15 trace lanes; **3 complete on the ✘ test; 0 free of an unresolved break.** The report-definition object is scope-mismatched (`MCU-04`, `CLOSED — VERIFIED DEFECT`) |
| 19 | Period close | **There is no period close. There is a moved date.** No close artefact, no stated basis, no period object, no reopening authority distinct from the closing one. **2 of 11 processes can assert close today** |
| 20 | Multi-company | A depreciation charge into a locked period is **re-dated seven months into the following year carrying full value**, while the same lock **hard-refuses** a disposal — one control, two opposite behaviours |
| 21 | SaaS / tenant | Scope-aware model adopted per `REV2-CORR1`; **9 scope mismatches** registered; highest is a control store with **no dimension at all — one write disables it for every tenant in the database**. `P03` adds a `Tolerance = 0` company-scope violation: **conversion-cost accounts resolve against the acting user's company** |
| 22 | Reversal / correction | Reverse-and-re-enter only; the destructive path is `REJECT`. **The architecture is ledger-side only** — without a producer-document correction path, operators will delete and re-key the source document, reproducing `DC-01` one layer up |

## 23. Double-counting findings

> ### **17 attack classes. `0` with a working guard. 1 partial.**
> **4 of the 17 do not depend on the undeclared reference root at all** — they are failures of the
> **design contract** (`DC-01` element 15, `DC-05` elements 12/15, `DC-12` element 14 and `F7`,
> `DC-16`) and cannot be argued away by declaring the root.
>
> **Confirmed reachable by a published peer:** duplicate bank transaction (*import a file twice*);
> duplicate payment against one invoice; silent destruction of a bank reconciliation by an ordinary
> document reset; an unowned bank account admitted into **every** company.
>
> **Confirmed and measured:** machine cost charged twice on a head-count base (`Tolerance = 0`).

## 24. Contradictions

7 found between packages (4 closed, 3 held); 14 carried unresolved; **`0` resolved by P11**.

## 25. Unresolved evidence

Four UAT queries would close four blockers between them, in minutes each — `Q-04` alone *"caps every
negative finding in two research packages"*. Business-SME and Thai statutory inputs gate `JT-04` and
`JT-05`, and **no AI may answer them**.

## 26. Remaining blockers

**16 P11 blockers, `0` closed.** (`P11-B-14`/`P11-B-15` from Delta 02; `P11-B-16` carries the new tolerance-zero boundary `T0-13` from Delta 03.) (`P11-B-14`/`P11-B-15` added by `P11_PEER_INTAKE_DELTA_02.md`.) Inherited: `GB-01`…`GB-08`; `MCU-21` and 17 gating unknowns;
`T0-01`…`T0-12`; `JT-01`…`JT-12`; `BLK-01`, `BLK-02`, `BLK-07`, `BLK-08`; `P06`'s 42.
**Correction backlog: 86 accepted findings, corrected in this session at source for the Boss-control
and evidence-integrity classes; the register-level count and membership corrections are scoped to
P11 CORR1 and are named, not deferred silently.**

## 27. AAS-03 four-expert challenge

**86 findings · 3 CRITICAL · 38 HIGH · `0` disputed · 31 claims attacked and not broken.**
**Six defects were found independently by two or more panels; three were found three times.**

The two critical ones are the ones that matter:
1. **P11's own evidence script could not measure what it declared** — inert by construction, found only by executing it.
2. **The subledger test's stated rule was not the rule applied**, collapsing three *"of record"* verdicts.

## 28. AAS+ verdict

> ## `NOT CONVERGED — P11 CORR1 REQUIRED`
> `AASP-P11-VETO-01` **UPHELD** — no part may be relied on as a cross-process reconciliation.
> `AASP-P11-VETO-02` **UPHELD** — no design position may seed implementation; 11 of 49 are not
> enforceable as written.

## 29. PMO recommendation

> ## `RECOMMEND HOLD`
> `0 of 8` exit criteria met. `CONDITIONAL PASS` is unavailable **by rule** — twelve inherited
> tolerance-zero boundaries stand unresolved and `P03` hands forward two more.

## 30. Controlled design freeze readiness

> ## `NOT READY.`
> Freeze requires a converged evidence base. Six of ten peers published during this session, four
> have not, two moved SHA mid-intake, and the Boss-approved convergence rule is explicit:
> **Accounting and Inventory must not be independently frozen and only reconciled afterward.**

## 31. Explicit decisions required from Boss

| # | Decision | Why only Boss | Cost to decide |
|---|---|---|---|
| `D-1` | **Declare the reference core root** (`MCU-21`) — 22 exist, none declared | A programme declaration, not a research result | **hours.** Re-scopes `MCU-18`, `MCU-19b`, `GB-07`, `GB-08` and every class `A` absence at once |
| `D-2` | **Declare the programme output path and the process taxonomy** (`P11-F-01`, `P11-F-04`) — six sessions wrote to six locations; the canonical matrix has no bank, payment, settlement, reconciliation or manufacturing process | Governance | **hours** |
| `D-3` | **Authorise the four UAT queries** — `Q-04`, `Q-01`, `Q-02`, `P06-B-27` | Access | **minutes each, read-only** |
| `D-3b` | **Authorise reading the PostgreSQL dumps already on the host.** `P11-F-09`: readable dumps exist, the client reads at least one (19,957 TOC entries), and `MCU-19` is a **database** question P11 had mis-filed as needing a running instance. **P11 verified the dumps exist; extraction was refused by its own session boundary and P11 does not assert what they contain** | Access | **unknown, plausibly cheap — and it is the programme's recorded failure mode.** **AMENDED per `P11-F-10` and `P11-F-11`: the authorisation must (1) specify the client version, (2) require EVERY generation to be opened, and (3) require THE POPULATION TO BE RANKED BEFORE SELECTION, WITH THE UNIT RANKED BY DECLARED.** Condition (3) binds hardest: a peer satisfying (1) and (2) still built its entire runtime section on a **23-line** database because it was the first one located, and a finding was withdrawn as a result. **The unit clause matters: one database here is largest by rows, a different one by populated tables — the deepest data set and the broadest install are not the same file, and the right one depends on the kind of claim.** A peer has shown that tool capability correlates with database generation, so default tooling can open only the deployments in which a defect is **absent** — producing a *named wrong conclusion*, not a completeness gap |
| `D-4` | **`GB-08`** — FX rate ownership and missing-rate policy | Packaged, not decided; four options stated, none selected | Boss |
| `D-5` | **The accounting-event identity** (`P11-B-02`) — introduce a layer-3 event object, or not | No research closes it; seven recorded symptoms across four programmes reduce to it | Boss |
| `D-6` | **`BLK-07`** — absorption denominator: normal capacity, actual hours, or `P04`'s **third option** (usage-based depreciation absorbed at normal capacity) | AAS+ veto on costing implementation stands until decided | Boss |
| `D-7` | **`JT-03`** — perpetual or periodic | **No stable reference pattern exists to imitate** | Boss |
| `D-8` | **Generalise the handoff contract** (`P11-F-02`) to all producers, with elements 17 (owning process) and 18 (declared scope) | `BC-02` binds Inventory→Accounting only; nine producers hand facts to the ledger under no contract | Boss |
| `D-9` | **Commission `SME-Q-02` / `SME-Q-03` and the Thai statutory questions** | **No AI may answer on the business's behalf** | Boss |
| `D-10` | **Authorise P11 CORR1** against the terminal peer packages | The round's own premise expired | Boss |
| `D-11` | **Declare the exception to "unrelated independent companies = separate tenants by default", and who may grant it** | The correction states a default and names **no** exception and **no** authority. Raised by `P04-SC-03`; the same gap `X3-F11` found independently. Until declared, P11 rules the default operates as **absolute** | Boss |
| `D-12` | **Rule whether a company hierarchy may span a tenant boundary.** P11 recommends **NO**. **Restated after source corroboration (`P11_PEER_INTAKE_DELTA_03.md`): the Boss is deciding not whether a parent may close a child's period, but whether an act in one tenant may SILENTLY MIS-PERIODISE another tenant's books — no error, no refusal, no trace — through a traversal the source documents as deliberately reaching companies the caller cannot access, producing a lock that cannot be undone** | Raised by `P04-SC-04`; corroborated from primary source by `P04-F-66` (`FACT VERIFIED`) and compounded with `P04-B-31`. **The ruling alone does not discharge the HOLD** — an enforced tenant-assignment invariant of the `MTI-04` class is additionally required | Boss |

---

# TERMINAL STATE

> ## `HOLD — P11 CORR1 REQUIRED`
>
> **This is deliberately NOT `READY FOR BOSS ACCOUNTING FINAL GATE`.**
>
> That terminal state presupposes a reconciliation. **No reconciliation of `P01`–`P10` has occurred**,
> because at synthesis time none of them had published, and six published during the session — two
> already moving past the SHA this session read. Declaring readiness over that would be `PARTIAL`
> wearing `PASS`'s label, which the constitution forbids in terms.
>
> **What IS ready for the Boss** is a decision pack: ten named decisions, four of which cost hours or
> minutes and none of which is blocked on any peer process.

**Not declared:** `PASS` · `APPROVED` · converged · frozen · merged · build authorised ·
implementation authorised · any gate movement · any Team hand-off.

**No SMEsPlus or reference source code was read for modification, and none was modified. Nothing was
merged. Nothing was deployed.**
