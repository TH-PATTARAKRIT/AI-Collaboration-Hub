# SA_CORR3_06 — JOINT CROSS-PROOF VERIFICATION 22×22
## CP-SA-C3-30 — JOINT CROSS-PROOF VERIFIED OR EXACTLY BOUNDED

Session: `[SMEPLUS-26-09-09-PHASE-SA-CORR3-PROOF-001]`
Branch: `architecture/phase-sa-corr3-proof-verification-2026-09-09-001` @ `5953ce26`
Governing law: CORR3 master prompt §9, read verbatim. Frame: **`CORR3-FRAME`**, adopted by pointer.
Finding prefix: `JCP3-`.

> **Orchestrator intake note.** Same-model executor; labelled `INTERNAL ADVERSARIAL SELF-CHALLENGE`;
> **not adopted on its word.** The load-bearing new finding `JCP3-F-02` was re-executed against the
> primary contract text (`b4c39831…` lines 33–48) and **CONFIRMED**: of the sixteen elements, **six**
> carry an applicability qualifier (4, 7, 8, 9, 13, 14) and **ten** carry none (1, 2, 3, 5, 6, **10**,
> 11, 12, **15**, 16). Element 10 is the only element whose definition contains the word `mandatory`;
> **element 15 carries no qualifier of any kind**; element 14 is qualified *"where the handoff is
> created/replayed through migration or recovery"*. `JCP3-F-07` was independently reproduced by a
> second executor working on a different subject (`SA_CORR3_04` `MNT-F-12`) — two instruments,
> different populations, same defect.

**Result, stated first: `0 VERIFIED · 0 NOT APPLICABLE — EVIDENCE-BACKED · 22 HOLD — EXACT PROOF
GAP`. And the figure Boss should read from this register is not that one — it is that discharging
handoff element 10 alone moves the result from `0 of 22` to `0 of 22`.**

---

## 1. Authority, and verification of the two governing controls against primary text

Master prompt §9 orders a re-run *"for verification, not coverage"*. Verification requires that the
controls themselves be read, not cited. Both were located **by pattern, not by assumed path** — the
brief's path fragment was incomplete; the true path sits under `BOSS_GATE/REOPEN_PROGRAM_2026_09_02/`.

| Control | Blob | Status field, verbatim |
|---|---|---|
| 22-Scenario Cross-Proof Baseline | `a1fc7cd6497061f9a6e1fd2d0f755589412830df` | `BOSS APPROVED / EFFECTIVE AS MINIMUM JOINT CROSS-PROOF BASELINE` |
| Minimum Handoff Data Contract | `b4c3983185a6122a832649779834e48ca437bdbc` | `BOSS APPROVED / EFFECTIVE` |

Each resolves to **exactly one unique text blob** across the whole frame — no version ambiguity, no
supersession to resolve. Each is carried on **66 branch heads**.

### 1.1 `JCP3-F-01` — element 10 is unconditional. Re-verified in **both** controls, two shapes.

**Handoff Contract §3**, verbatim:

> `10.` `` `WHICH Company / Tenant` `` — **mandatory company and tenant context.**

Mechanical extraction of all 16 elements (`UNIT` = numbered element; `PATTERN` = `^[0-9]+\. \``;
`PATH SET` = the §3 block):

| Qualifier present | Elements | n |
|---|---|---|
| Carries an applicability qualifier | 4 *("or explicit pending/hold condition")*, 7 *("where not applicable or not yet approved")*, 8 *("where applicable")*, 9 *("as applicable")*, 13 *("where applicable")*, **14** *("where the handoff is created/replayed through migration or recovery")* | **6** |
| **No qualifier of any kind** | 1, 2, 3, 5, 6, **10**, 11, 12, **15**, 16 | **10** |

**Element 10 is the only one of the sixteen carrying `mandatory` in its own definition.**

**Independent confirmation in the second control.** The Baseline §3 lists **19 required proof items,
5 qualified `where applicable`, 14 unqualified** — with `tenant / company context` **unqualified** and
`migration / replay batch identity where applicable` **qualified**.

**Both Boss controls agree, independently.** CORR2's reading is confirmed on primary text.

### 1.2 `JCP3-F-02` — the same test, applied to element 15, is the finding CORR2 did not draw

The instrument that proved element 10 unconditional proves **element 15 equally unconditional, in both
controls.** Contract §3 element 15 — *"deterministic identity used to prevent duplicate
processing/effect"* — carries no qualifier. Baseline §3 — *"idempotency / duplicate-protection
identity"* — carries no qualifier.

The only conditionality attaching to element 15 anywhere is Contract **§4** disqualifier bullet 7:
*"unable to prevent duplicate/replayed effects **when idempotency is required**."* The governing
Inventory-side review has already adjudicated exactly that clause. `REV-F-02`, primary text, status
field `R4-F-16 CONCLUSION CONFIRMED — SUPPORTING REASONING REFINED ON ONE ELEMENT — THE THREE BLOCKERS
ARE NOT EQUALLY LOAD-BEARING`:

> | **15** — Idempotency identity | … no qualifier at §3 | … **no qualifier** | **Effectively no.** Only
> the §4 enforcement bullet adds *"when idempotency is required"* | `RISK-C02` — no stable identity
> exists | **Every handoff where a retry is possible; squarely and unavoidably scenario 22** |

and §3.4:

> | All three elements block all ten material handoffs | **REFINED.** Element 10 does. **Element 15 does
> wherever a retry is possible, which in practice is everywhere.** **Element 14 does not** |

> **Element 10 is *sufficient* to produce `0 of 22`. It is not *necessary*.** `REV-F-02` §3.4 says
> *"Element 10 alone is **sufficient**"* — a sufficiency claim, correctly stated. `SA_CORR2_04` §7.1
> converts it into *"the reason is now exact. **It is** element 10, unconditionally, on every
> scenario"* — which reads as **identification**, and identification is a different claim than
> sufficiency.

**This is the reciprocal of `JCP-04`, and it holds in the direction CORR3 was ordered to test.**
`JCP-04` observed that *"resolving the entire COGS Gap tomorrow would move the result from 0 of 22 to
0 of 22."* **The identical arithmetic applies one level up: resolving element 10 tomorrow would move
the joint cross-proof result from `0 of 22` to `0 of 22`.**

### 1.3 The §4 gate, which makes element 10 doubly load-bearing

Contract §4 attaches the contract to *"every scenario **with an Inventory → Accounting handoff**"* and
lists **8 disqualifiers**. Two are decisive and neither is conditional: bullet 3 `unsupported by
evidence` (which catches *specified-but-not-built*), and bullet 8 `missing company/tenant isolation
context` (element 10 again, **as a free-standing disqualifier independent of §3**). §3's recording
discipline is a **recording** rule, not a rescue: §4 disqualifies regardless of how the blank is
annotated.

### 1.4 `JCP3-F-12` — the scope-aware correction does not rescue element 10

`SA10` §8.2 records the standing correction **`SCOPE-AWARE EVERYWHERE`** — `PLATFORM` requires neither
context, `TENANT` requires tenant, `COMPANY` requires both — which *"**withdraws** any blanket reading
that tenant + company are mandatory on every operation."*

This register **applies** that correction rather than ignoring it, and it does not move element 10. A
material Inventory → Accounting handoff emits a valuation fact posting to a company ledger; under
`BD-ACC-02` statutory tax is company-scoped, so the handoff population is **`COMPANY`-scoped by
nature**, and `COMPANY` requires **both** contexts. The correction bites on platform-scoped objects;
the contract population contains none. **Recorded pre-emptively so this register is not read as
re-introducing the over-constraint the correction removed.**

---

## 2. Method, and what `VERIFIED` means at Phase SA

Contract §3: an element must be **`known, traceable, and evidence-backed`** — three conjuncts; a
specification satisfies none of the three alone. `SA10`'s reliance rule governs what may be cited:
*"**a specification is not a control.** The isolation guarantees may be cited as *design intent* and
may not be cited as *assurance*."*

The isolation proof matrix defines proof as three parts, two of which are absent **by
authorization**: a proposition (supplied), an implementation (Team B, not authorized), and an executed
test (a later pass, not authorized) — with `PROVEN` *"never used in this file. **No proof is achieved
by a design session**."*

> **Therefore `VERIFIED` at Phase SA is unreachable by any amount of reading.** Not a limitation of
> effort — the definition of the word in the controlling documents. A register returning `VERIFIED`
> rows from a corpus search would commit the exact defect the standard exists to prevent. Master
> prompt §9's checkpoint name concedes this: `JOINT CROSS-PROOF VERIFIED **OR EXACTLY BOUNDED**`.
> This register delivers the second, and §4 is the bounding.

### 2.1 An explicit veto governs the wording of element 10

`AAS-V-01`, status `CHALLENGE COMPLETE — CONTROLLING VERDICT: HOLD / DESIGN SPECIFIED, NOT PROVEN —
3 VETOES ISSUED — NO PASS DECLARED`:

> **VETO on recording handoff element 10 as supplied, satisfied or suppliable on the basis of this
> package.** Its status is `specified, not built, not verified` and no other wording may be
> substituted … Any downstream document recording element 10 as supplied would make ten handoffs
> appear compliant when zero are.

**This register uses `specified, not built, not verified` and no substitute.**

### 2.2 The 16-element status baseline carried

Re-extracted mechanically and re-verified against the contract's own text (two shapes agree;
8 + 2 + 3 + 3 = 16):

| Status | Elements | n | Cause |
|---|---|---:|---|
| `SUPPLIABLE` | 1, 2, 3, 5, 6, 8, 9, 11 | **8** | — |
| `HELD` | 4, 7 | **2** | `ACCOUNTING COGS GAP` |
| `PARTIAL — depends on element 15` | 12, 13, 16 | **3** | downstream of element 15 |
| `NOT SUPPLIABLE` | **10**, 14, **15** | **3** | `RISK-U03`, `GAP-FS-08`, `RISK-C02` |

> **`JCP3-F-05` — an element-level fact that inverts the leverage ranking.** Element 15 governs
> **three** dependent elements (12, 13, and 16's evidence half all carry `depends on element 15`).
> Element 10 governs **one**. **Measured by contractual reach, element 15 is the higher-leverage object
> of the two, and every register in the lineage ranks element 10 first.**

### 2.3 Falsification searches run before publishing the negatives

| Negative claim | Tool / patterns | Authority for what was not searched |
|---|---|---|
| No document records element 10 as supplied/proven/verified | `grep -rlE` over 3,900 blobs, **8 distinct pattern shapes** | Complement stated in the frame. **Five near-miss hits were opened**, each resolving to a different scope |
| No document records element 15 / a deterministic accounting-event identity as supplied or built | 5 pattern shapes → **0 hits** | as above |
| The Boss 22 are enumerated by name in only three documents | 3 independent distinctive-phrase patterns; all three return the same document set | as above |

### 2.4 `JCP3-I-01` — internal self-challenge: one false negative, caught and corrected before publication

Mid-execution this register concluded the Inventory-side proof register covered only **17 of 22** Boss
scenarios. **That was false.** The instrument was an `awk` script carrying a variable across records:
three `L11-` sections genuinely lack a "Boss scenarios" row, and the script **silently reprinted the
previous section's value**, so a partial sub-population read as the whole. Corrected by re-running
with a second shape and reading §4 directly.

> **The generalisable control: a stateful extraction instrument produces false positives that look
> like data.** Every count below was validated with a second command of a different shape, and where
> the two disagreed the disagreement is published rather than resolved silently.

---

## 3. The 22-scenario register

### 3.0 Fields carried identically on all 22, stated once

Repeating an identical cell 22 times manufactures the appearance of 22 independent determinations.

| Required field | Value common to all 22 |
|---|---|
| **Upstream authoritative source** | `BD-ACC-01`: *"Source Module owns the Business Fact. Accounting Core owns the canonical Accounting Event Identity. Posting Engine owns Ledger Posting."* `CLOSED / BOSS APPROVED` |
| **Process baseline** | The Boss-approved minimum 22, `BOSS APPROVED / EFFECTIVE` |
| **Tenant/Company boundary** | `specified, not built, not verified`. **58 invariants specified — 0 proven**; `0 of 8` isolation proofs; `0 of 13` enforcement surfaces; `0 of 52` negative access tests executable *"because no implementation exists"*; `0 of 3` cross-context register entries; `0 of 10` handoffs contract-compliant |
| **Tax effect** | Accounting determines tax for both commercial sides — `R-19` `HARD`, *"neither computes tax itself"*. **No statutory Thai claim is made anywhere in this register** — `HOLD / EVIDENCE REQUIRED`. `BD-ACC-02`: company-scoped, no cross-company posting, offsetting or filing |
| **Payment / settlement durability** | `H-07` `NOT DURABLE` — matching is *"not an entry"* and matching rows are **freely destructible across a closed period**; cash-basis tax keys off it |
| **Period integrity** | `H-06` `UNSAFE` — the accounting date is *"silently movable past a lock"*, and **there is no accounting-period object**. Re-dating past a lock is **the default behaviour, not an edge case** |
| **Proof result** | `HOLD — EXACT PROOF GAP` on all 22 |

**Element accounting common to all 22 non-migration scenarios:** 8 `SUPPLIABLE`; element 14 `N/A with
reason`, therefore **contract-compliant**; elements **10** and **15** `NOT SUPPLIABLE`; elements 12,
13, 16 `PARTIAL`, downstream of 15. Elements 4 and 7 `HELD` on the COGS-gated subset only.

### 3.1 The register

`(c)` = **the named blocker that is NOT element 10 and NOT element 15** — the column that determines
whether the root cause is one object or many.

| # | Scenario | Inv | Acc | Route | L11 | **(c) — blocker independent of el.10 and el.15** | Result |
|---:|---|---|---|---|---|---|---|
| 1 | Stockable purchase receipt → handoff | `IR-02` `RECONCILED` | `AR-04` `RECONCILED` | `R-08`/`R-13`/`R-10` | `DEPENDENCY` | el.4/7 COGS; goods-received bridge is **a swept suspense account, not item-matched**, weakening el.12 | `HOLD` |
| 2 | Vendor bill with receipt timing variation | `IR-02` `RECONCILED` | `AR-05` `RECONCILED` | `R-10`/`R-11` | `DEPENDENCY` | el.4/7; **no prior-period attribution mechanism exists at all** | `HOLD` |
| 3 | Stockable sales delivery → cost handoff | `IR-01` `RECONCILED` | `AR-01` `RECONCILED` | `R-13`/`R-05` | `DEPENDENCY` | el.4/7; recognition-point split — `BP-02` (COGS at delivery) **not selectable** | `HOLD` |
| 4 | Customer invoice with delivery timing variation | `IR-01` `RECONCILED` | `AR-02` `RECONCILED` | `R-05`/`R-06` | `DEPENDENCY` | el.4/7. **`JT-04`'s `CONFLICTING` flag is discharged** — the only scenario whose named non-element blocker CORR2 closed | `HOLD` |
| 5 | Partial receipt | `IR-02` | `AR-04` | `R-08`/`R-13` | `DEPENDENCY` | el.4/7; over-receipt tolerance undefined | `HOLD` |
| 6 | Partial delivery | `IR-01` | `AR-01`/`AR-02` | `R-05`/`R-13` | `DEPENDENCY` | el.4/7; **`H-05`** — a draft invoice consumes billable quantity while posting nothing and is freely deletable | `HOLD` |
| 7 | Backorder | `IR-11` `RECONCILED — no consumer` | `AR-01` | **`R-17` `NO CONSUMER`** | `STRUCTURAL` | remainder-supply record **has no consumer at all**; never-mode remainder cancellation leaves **no document trail** | `HOLD` |
| 8 | Purchase return | `IR-04` | `AR-14` `RECONCILED — AND EVIDENCED` | `R-18` `ADVISORY` | `DEPENDENCY` | el.4/7; return basis conflict `PENDING — INVENTORY INTERNAL RESOLUTION FIRST` | `HOLD` |
| 9 | Sales return | `IR-03` | `AR-13` `RECONCILED — AND EVIDENCED` | `R-18` | `DEPENDENCY` | el.4/7; **`JT-05` NOT DECIDABLE** — original-cost vs current-cost reversal basis | `HOLD` |
| 10 | Cancellation before physical execution | `IR-09`-adj. | `AR-23` `PARTIAL` | **`R-20` `XD-01`** | `STRUCTURAL` | **`C-01` cancellation symmetry unarbitrated**; **`C2-F-01` durability precondition**. *(Now resolved — see `SA_CORR3_01`)* | `HOLD` |
| 11 | Correction after physical execution | `IR-03`/`IR-04` | `AR-13`/`AR-14` | `R-03` blocked → return route | `STRUCTURAL` | the **only** correction route after a completed movement is a return; corrected-entry link **does not exist** | `HOLD` |
| 12 | Inventory count / adjustment | `IR-10` | `AR-10`-adj. | `R-13` | `STRUCTURAL` — *"closest to specifiable"* | **approval mechanism absent**; an adjustment can **silently reduce a reservation** | `HOLD` |
| 13 | Scrap / damage / write-off | `IR-07` `RECONCILED — no cost causality` | `AR-12` `PARTIAL` | boundary rule | `DEPENDENCY` | **salvage is not merely unproven, it is undefined**; scrap has **no cost causality** | `HOLD` |
| 14 | Internal warehouse transfer — no inappropriate financial effect | `IR-09` `RECONCILED — RULE NOW STATED` | `AR-10` `RECONCILED — NO POSTING BY DESIGN` | boundary rule `DETERMINED` | `STRUCTURAL` | **`R4-F-18` — no independent check exists**; neutrality is **configuration-protected only**, and one change breaks two flows | `HOLD` |
| 15 | Multi-company / tenant boundary | `IR-16` `PARTIAL` | `BD-ACC-02`, `GB-08` | register **empty** | `STRUCTURAL` | **this scenario *is* element 10**; `0 of 8` isolation proofs; `SA10-F-05` **two** lock-defeat paths, the second leaving no record | `HOLD` |
| 16 | Manufacturing RM → WIP → FG | `IR-05`/`IR-06` | `AR-11` `PARTIAL` | `R-21`; **`R-22` `GAP`** | `DEPENDENCY` | el.4/7; **fixed-overhead elements have no injection path** | `HOLD` |
| 17 | Manufacturing reversal / scrap / variance | `IR-08` | `AR-12` `PARTIAL` | `R-22` `GAP` | `DEPENDENCY` | el.4/7; **no variance mechanism exists** — one variance of nine recognised | `HOLD` |
| 18 | Stockable vs consumable vs service routing | `IR-17` `PARTIAL` | `AR-26` `PARTIAL` | `R-27` `HOLD` | `STRUCTURAL` | **two-axis classification tie-break undefined**; `BD-ACC-01` presumes a physical fact and is **silent for services** | `HOLD` |
| 19 | Period-end / cut-off | `IR-10` | `AR-20` `PARTIAL` | `R-13` | `DEPENDENCY` | el.4/7; **no accounting-period object exists**; reconciliation holds **at the closing boundary, not continuously** | `HOLD` |
| 20 | Historical migration across fiscal years | `IR-15`/`IR-16` | — | — | `STRUCTURAL` | **element 14 genuinely attaches here** — the provenance reference **does not exist and must be originated** | `HOLD` |
| 21 | AI migration mapping + deterministic reconciliation | — | — | — | `STRUCTURAL` | **element 14**; `MTI-42` prohibits inferring context at migration | `HOLD` |
| 22 | Retry / idempotency / replay | `IR-*` | `AR-*` | — | `STRUCTURAL` | **this scenario *is* element 15**; `RISK-C02` `CARRIED / BLOCKING`; `UAE-29` `HOLD — BOSS DECISION REQUIRED — the root` | `HOLD` |

**Every one of the 22 rows carries a named `(c)` blocker. Not one scenario is blocked by element 10
alone.**

### 3.2 Conditional routing — one output creating several downstream obligations

| Output | All routes created | Scenarios |
|---|---|---|
| Completed movement | → Sales *delivered* · → Purchase *received* · → on-hand and forecast · → Accounting (cost, via valuation policy) | 1, 3, 5, 6, 7, 11, 12, 16 |
| Commitment cancelled | → Inventory transfer cancellation · → Accounting reversal event under `BD-ACC-01` · → the sell-side gate question `XD-01` | 10 |
| Billing posted | → already-billed derivation · → AR/AP ageing · → payment matching · → tax register | 2, 4, 6, 8, 9 |
| Production completed | → FG into Inventory · → cost into Accounting · → variance into Accounting · → Equipment usage/meter (`HOLD`) | 16, 17 |

**Exception / reversal behaviour** (population 20 classes; `16 ESTABLISHED / 4 NOT ESTABLISHED`): the
four not established are **wrong item · supplier-SLA lateness · approval rejection (Boss-owned) ·
idempotency (regraded downward)**. Reversal itself is `ESTABLISHED`: a credit note posts and reverses
**revenue, receivable, tax and cost**, `FACT VERIFIED`.

**The durability inversion governing every reversal field** — `FACT VERIFIED`:

> the **physical event is immutable, the accounting event is reversible, and the settlement history is
> freely destructible.**

### 3.3 `JCP3-F-10` — element 10 also fails at the field level, in CORR2's own data

`SA_CORR2_01` §6, seven changed handoffs, `UNIT` = matrix row, column 7 read mechanically:
**`H-01` records `Tenant + Company`; `H-02`…`H-07` record `Company` only — 1 of 7 vs 6 of 7.**
Element 10 requires *"mandatory company **and** tenant context."* And the single compliant row is
compliant **by citation to a ruling, not by evidence of a carried value** — `H-01`'s own status is
`CONTRACT REQUIRED — content now known, interface still unpublished`.

**A second, independent measurement of element 10's failure**, in a different unit (matrix rows rather
than invariants) and a different path set (the Accounting-side register rather than the Inventory
isolation programme), reaching the same result.

### 3.4 `JCP3-F-05b` — the joint finding: element 15's only mechanism is disqualified by element 10

**This result exists only because both elements were read together, which is what a joint cross-proof
is for.**

The blanket claim *"element 15 does not exist today"* has been **narrowed on the record and the
narrowing accepted**. `X2-F11`, severity `HIGH`, disposition **`ACCEPTED`**:

> **The `F7` absence is stated at a strength the governing correction denies.** … **`PARTIALLY
> VERIFIED`** — *"a real database constraint exists, but only with an optional module installed, and
> it is **table-global rather than tenant-scoped**."*

Corroborated from the other direction — `P08-AEI-01`, `FACT VERIFIED`:

> **Durable accounting-event identity exists where the event originates OUTSIDE the system, and is
> absent where it originates INSIDE it.**
> **Every one of the 13,814 bank transactions in the production-scale database was created by a path
> that sets no deduplication key at all.** Because a database `UNIQUE` constraint permits unlimited
> empty values, the constraint admits all 13,814 rows without objection.

> **The joint consequence. The one idempotency carrier that exists anywhere in the estate is
> `table-global with no tenant scoping` — so the sole mechanism that could satisfy element 15 is, by
> its own scoping, incapable of satisfying element 10.** Element 10 and element 15 are not two
> independent gaps that happen to co-occur. **At the mechanism level they are one missing object with
> two contractual names, and a remedy that supplies either one without the other supplies neither.**
> Neither domain's register states this, because each holds only one half.

---

## 4. The (a) / (b) / (c) decomposition — and the figure master prompt §9 asked for

### 4.1 (a) — what is verifiable NOW

Large, and the half the `0 of 22` headline conceals. Counted by reading each source register's
**status column**, not its headline, and validated with a second command shape:

| Measure | Enumerated |
|---|---|
| Handoff elements `SUPPLIABLE` on every scenario | **8 of 16** |
| Stock-affecting flows `RECONCILED` | **14 of 18** |
| Material business flows with an explicitly determined accounting semantic | **29 of 29**; `15 RECONCILED / 14 PARTIAL / 0 UNKNOWN` |
| Cross-module routes evidenced | **20 of 28** |
| Exception classes `ESTABLISHED` | **16 of 20** |

**(a) is not a scenario-level result.** No scenario reaches `VERIFIED`, because `VERIFIED` requires an
implementation and an executed test and Phase SA may produce neither. **What (a) establishes is that
the specification and semantic work is substantially complete and the gate is a build-and-prove gate.**

### 4.2 (b) — blocked ONLY by element 10

> ### **`0 of 22`.**

Two independent reasons, either sufficient:

1. **Element 15 blocks every scenario too.** Unconditional in both Boss controls; reach adjudicated by
   `REV-F-02` as *"every handoff where a retry is possible, **which in practice is everywhere**"*; and
   listed among the failing elements on **10 of 10** scenarios in the Inventory register's own
   per-scenario tables. The Inventory process handoff map states it directly: *"Elements 10, 14 and 15
   fail on **every single one**"* of the ten material handoffs.
2. **Every scenario carries a named `(c)` blocker** — 22 of 22 populated.

### 4.3 (c) — blocked by something else, named and classified

| `(c)` class | Scenarios | n | Closable by research? |
|---|---|---:|---|
| Element 15 / accounting-event identity | all 22 | **22** | **No — a design act.** Owner SMEs Core |
| COGS gap, elements 4 and 7 | 1–6, 8, 9, 13, 16, 17, 19 | **12** | No — Joint decision |
| A named **design mechanism that does not exist** | 2, 7, 12, 13, 14, 16, 17, 19 | **8** | No — origination |
| A **Boss decision** | 8, 9, 10, 18, 22 | **5** | No — normative |
| **Element 14**, contractually attaching | 20, 21 | **2** | No — origination |
| Closed by CORR2 | 4 | **1** | Already closed |

### 4.4 The counterfactual, run explicitly

| If discharged tomorrow | Elements resolved | Scenarios moving to `VERIFIED` |
|---|---:|---:|
| The entire COGS gap (4 + 7) | 2 | **0** — `JCP-04`, confirmed here |
| **Element 10 alone** | **1** | **0** |
| Element 15 alone | 3 (15, and 12/13 depending on it) | **0** |
| **Elements 10 and 15 together** | 4 | **0** — §4.3's design/decision/origination classes remain, and scenarios 15 and 22 **are** the two elements, still requiring `0 of 8` isolation proofs and `0 of 52` negative tests to be **executed** |

> **`JCP3-F-02`, as the figure master prompt §9 asked for: discharging element 10 moves the joint
> cross-proof result from `0 of 22` to `0 of 22`. The reciprocal test CORR3 ordered returns the same
> answer for element 10 that CORR2 returned for COGS.**
>
> **The honest characterisation is neither "one root cause" nor "22 independent HOLDs".** It is:
> **two unconditional contractual blockers of equal reach that reduce to one missing object (§3.4),
> sitting above a floor of scenario-specific gaps that no single discharge clears.** A register
> attributing all 22 to element 10 would tell Boss to commission one thing and expect twenty-two
> results.

---

## 5. Result tally, cross-checked against this register's own rows

| Allowed result | Scenarios | Count |
|---|---|---:|
| `VERIFIED` | — | **0** |
| `NOT APPLICABLE — EVIDENCE-BACKED` | — | **0** |
| `HOLD — EXACT PROOF GAP` | 1…22 | **22** |
| **Total** | | **22** |

**Check, executed mechanically:** the §3.1 table yields **22 rows**, scenario numbers **1…22 each
exactly once** (two shapes agree), every Result cell reads `HOLD`. `0 + 0 + 22 = 22`. ✓

**Why `NOT APPLICABLE — EVIDENCE-BACKED` is 0, stated rather than assumed.** Contract §4 scopes the
elements to *"every scenario with an Inventory → Accounting handoff"*, so a scenario without one would
be outside the contract. **Scenario 14 is the only genuine candidate** — internal→internal *"emits no
valuation fact"*. It is nonetheless `HOLD`, because the scenario's Boss-stated proof obligation is to
demonstrate **no inappropriate financial effect** — a negative that `R4-F-18` records as unproven,
with *"no independent check"* existing. **An absent handoff is not an evidence-backed absence until
something can demonstrate the absence.**

---

## 6. Findings raised

| id | Sev | Finding |
|---|---|---|
| `JCP3-F-01` | `MATERIAL` | Element 10 unconditional, **re-verified in both Boss controls**, two shapes; the only one of 16 carrying `mandatory`. Confirms CORR2 |
| **`JCP3-F-02`** | **`HIGH`** | **Element 15 equally unconditional with equal reach. Element 10 is sufficient but not necessary. `(b)` = 0; discharging element 10 alone moves `0 of 22` → `0 of 22`** |
| `JCP3-F-03` | `MATERIAL` | `SA_CORR2_04` §7.1 — *"It is element 10, unconditionally, on every scenario"* — is contradicted by its own §4.1 table, which names element 10 on **21 of 22** rows |
| `JCP3-F-04` | `MATERIAL` | The same table names element 15 on **1 of 22** rows while its own `JCP-04` states elements 10 and 15 *"fail on every scenario regardless"*. **Understates the second blocker by 21 rows** |
| **`JCP3-F-05`** | **`HIGH`** | Element 15 governs **3** dependent elements; element 10 governs **1**. The leverage ranking in every register in the lineage is inverted |
| **`JCP3-F-05b`** | **`HIGH`** | **The sole existing idempotency carrier is `table-global with no tenant scoping`** — element 15's only mechanism is disqualified by element 10's own requirement. One missing object, two names. Held by neither domain alone |
| `JCP3-F-06` | `MATERIAL` | *"No stable identity exists"* is carried without the narrowing `X2-F11` (`ACCEPTED`) and `P08-AEI-01` (`FACT VERIFIED`) put on the record: identity **exists** on one inbound channel, optional-module, table-global, **populated on 0 of 13,814 rows** |
| `JCP3-F-07` | `MATERIAL` | `SA_CORR2_05`'s closing status line reads **`13 of 18 reconciled, 4 partial, 1 not reconciled`** — the **exact figures its own correction note retires**. §2.1 reads `14 / 3 / 1`. *(Independently reproduced by a second executor — `SA_CORR3_04` `MNT-F-12`)* |
| `JCP3-F-08` | `MATERIAL` | `SA_CORR2_06`'s closing status line and §2 prose read **`13`**; its §2.1 table reads `PARTIAL = 14`. **Same defect, same round, two files** — a correction applied to the table and left standing in the sentence Boss reads last |
| `JCP3-F-09` | `MATERIAL` | The Inventory L11 register's §6 tally (`8` / `14`) contradicts its own §4 status column (**`10` / `12`**). Both sum to 22, so an identifier check passes. **The non-COGS-gated population is understated by 2** — which strengthens the finding that COGS is not binding |
| `JCP3-F-10` | `MATERIAL` | Element 10 fails at field level in CORR2's own handoff matrix: **1 of 7** rows records tenant context |
| `JCP3-F-11` | `MINOR` | `SA15` §4's self-check — *"4 + 7 + 7 = 18, and every identifier appears exactly once"* — is **false as written**: the table enumerates **13 of 18** and prints counts `4 / 7 / 2` |
| `JCP3-F-12` | `MATERIAL` | `SCOPE-AWARE EVERYWHERE` does not rescue element 10; recorded pre-emptively as the strongest available counter-argument |
| `JCP3-F-13` | `MATERIAL` | `SA_CORR2_04` row 22 asserts duplicate posting **`REACHABLE`** as fact; `SA_CORR2_09` §2.8 — same package, same session — quotes *"**Exploitability is UNRESOLVED — EVIDENCE REQUIRED** and the two halves must not be collapsed."* **CORR2 committed, in `04`, the collapse it documents in `09`** |
| `JCP3-F-14` | `MINOR` | `SA04` §1.1's *"seven of those eight trace to…"* should read **six**, leaving `R-17` and `R-22` unattributed |
| `JCP3-I-01` | — | Internal self-challenge: one false negative produced and corrected (a stateful instrument reprinting a prior record's value). **Published rather than suppressed** |

---

## 7. Residual uncertainty, exact proof gaps, and what to attack first

### (a) Residual uncertainty

1. **Element 15's universal reach rests on an adjudication, not a measurement.** `REV-F-02` reasons
   retry is possible *"in practice everywhere"* — a judgement about the target architecture, not a
   count. Corroborated by the Inventory register listing element 15 on 10 of 10 scenarios, but **no
   party has enumerated, scenario by scenario, which handoffs admit a retry.**
2. **Contract §3 and §4 are in tension on element 15** and no Boss ruling resolves it. §3 requires the
   identity unconditionally; §4 disqualifies only *"when idempotency is required"*. This register
   reads §3 as governing. **A Boss reading that lets §4 bullet 7 scope §3 element 15 would change
   `(b)` from 0 to a positive number. This is the single most consequential open item here.**
3. **`FE-01`'s reachability is contested inside CORR2 itself.** Nothing in the result depends on it,
   but any severity ranking using `REACHABLE` stands on a collapsed tag.
4. **The `(c)` classification in §4.3 is this register's construction** and no other party has reviewed
   the classes.

### (b) What could not be proven, and the exact gap

| Could not prove | Exact gap |
|---|---|
| That any scenario reaches `VERIFIED` | **Structural and by authorization.** `0 of 8` isolation proofs, `0 of 13` enforcement surfaces, `0 of 52` negative access tests, `0 of 60` proof requirements — all stated cause: *"because no implementation exists"* |
| That element 10 is unsatisfiable **as a fact about a running system** | No SMEsPlus system exists |
| That element 15 admits no retry-free subset | Not attempted by any party |
| That the corpus contains no document supplying element 10 or 15 | Bounded, not absolute. Eight pattern shapes over 3,900 blobs; **complement declared** |
| That scenario 14's neutrality holds | **Live**, not latent: neutrality is configuration-protected and one change breaks both transfer neutrality and quality-hold cost-neutrality |

### (c) The claim a challenger should attack first

> **Attack `JCP3-F-02` at its weakest joint: not the unconditionality of element 15 — verified in both
> control texts by two command shapes — but the *reach* claim that element 15 blocks every scenario.**

That is the load-bearing half, and it is supported by an adjudication rather than an enumeration. The
attack is cheap and well-defined: **enumerate the 22 and identify any for which no retry, replay or
duplicate-submission path exists.** Candidates worth testing: **scenario 14** (emits no valuation fact,
so may have nothing to duplicate) and the **service branch of scenario 18** (no physical event at all,
only an assertion — which may or may not be replayable).

**If even one scenario survives, element 10 becomes the sole blocker there, `(b)` becomes non-zero,
and §4.2's headline must be restated. This could not be closed here, and it is named rather than left
to the adjudication silently.**

Second priority: attack §3.4 by looking for a **tenant-scoped** idempotency carrier anywhere in the
estate. Five pattern shapes found only the table-global constraint. **A single counter-example would
break the "one missing object" claim** and restore elements 10 and 15 to genuinely independent status
— changing the remediation sequence, though not the `0 of 22` result.

---

`CP-SA-C3-30 — JOINT CROSS-PROOF EXACTLY BOUNDED (execution status).` **22 of 22 re-run against both
Boss controls read as primary text. 0 verified. 0 not applicable. 22 `HOLD — EXACT PROOF GAP`, each
with a named blocker that is not element 10.** The proof activity is executed; its result is that the
gate is a build-and-prove gate, and the `0 of 22` figure has **two** unconditional causes reducing to
**one** missing object, not one cause.

Checkpoint completion is **not** Boss approval. Boss remains the sole Final Approver.
