# 21 — BOUNDARY `17 ↔ 18 ↔ 10` CROSSWALK

# `10 of 10 ROWS MAP · 12 of 17 CLASSES REACHED · CORE-08 DISCHARGED`

Session: `[SMEPLUS-26-09-10-PHASE-PRETEST-B7R2-REMEDIATION-NEWSESSION-001]`
Authority: `BOSS-CORR1-01` (c) via `17_` §2.2 · **Supersedes `06_`'s `12 ↔ 18 ↔ 10`** · Boss: **SOLE FINAL APPROVER**

> **Rebuilt from zero on the `17`. `06_`'s figures are not carried forward** — they were measured on a
> denominator the ruling replaced.

---

## 1. THE FULL CROSSWALK — `15` ATTRIBUTES PER CLASS

**Legend.** `CS` = `CONTRACT-SUFFICIENT` · `CG` = `CONTRACT-GAP` · `HEG` = `HOLD — EXACT GAP`.
Applicability: **`A`** always · **`C`** conditional. Accounting / Inventory consequence: **`Y`** / **`N`**.

| `BC` | Class | Producer | Source event | Output | Consumer | `XMC-H` | Contract row | Appl. | Exception | Reversal | Migration behaviour | Acct. | Inv. | Evidence | **Status** |
|---|---|---|---|---|---|---|---|:-:|---|---|---|:-:|:-:|---|---|
| `BC-01` | Sales → Inventory | Sales | SO confirmed | demand: product, qty, date, customer, destination, priority | Inventory | `-01` | **`1` `CG`** | `A` | route indirect sell-side / direct buy-side | via `-13` cancellation | `HX-01` is Inventory's receiving row | `N` | `Y` | `SA_CORR3_08` L213 | **`HEG`** |
| `BC-02` | Sales → Manufacturing | Sales | make-route resolved | component demand + FG expectation | Manufacturing | `-02` | **`2` `CG`** | `A` | **MO never raises its own demand** | undetermined | **no emitting artefact at all** | `N` | `Y` | L214 | **`HEG`** |
| `BC-03` | Sales → Purchase (dropship/MTO) | Sales | buy-route resolved | purchase demand | Purchase | `-03` | **`3` `CG`** | `A` | **bypasses the demand-approval gate** | undetermined | control-floor gap | `N` | `Y` | L215 | **`HEG`** |
| `BC-04` | Manufacturing → Inventory | Manufacturing | MO confirmed / output | component issue; FG receipt | Inventory | `-04` | **`6` `CG`** (first leg) | `A` | fails on `P6` | `X-17`, **no variance mechanism** | `HX-18` is Inventory's receiving row | `N` | `Y` | L216 | **`HEG`** |
| `BC-05` | Inventory → Accounting | Inventory | movement validated | valuation fact | Accounting | `-05` | **`5` `CS`** | `A` | el. `10` absent · `12`/`13` partial | `X-11` correction-by-return only | el. `14`/`15` absent | `Y` | `Y` | L217 | **`HEG`** |
| `BC-06` | Sales → AR / Accounting | Sales | invoice raised | receivable fact | AR / Accounting | `-06` | **`7` `CG`** | `A` | **round-trip** — Sales reads Accounting's stored result | credit note | — | `Y` | `N` | L218 | **`HEG`** |
| `BC-07` | Purchase → AP / Accounting | Purchase | bill posted | payable fact | AP / Accounting | `-07` | **`7` `CG`** | `A` | same round-trip | debit note | — | `Y` | `N` | L219 | **`HEG`** |
| `BC-08` | Payment → Bank / Accounting | Payment | payment / receipt | settlement fact | Bank / Accounting | `-08` | **`7` `CG`** | `A` | matching state **freely destructible across a closed period** | unmatch | — | `Y` | `N` | L220 | **`HEG`** |
| `BC-09` | Asset → Accounting | Asset | capitalisation / depreciation | asset value fact | Accounting | `-09` | **`8` `CG`** | `A` | derecognition **`PARTIAL`** | derecognition unposted | — | `Y` | `N` | L221 | **`HEG`** |
| `BC-10` | Expense → Accounting | Expense | expense recognised | expense fact | Accounting | `-10` | **`9` `CG`** | `A` | petty cash & employee advance **structurally broken** | — | — | `Y` | `N` | L222 | **`HEG`** |
| `BC-11` | Tax → Accounting / reporting | Tax | taxable event | tax fact | Accounting / reporting | `-11` | **`10` `CS` (context)** | `A` | substitution rule base **`EVIDENCE-INSUFFICIENT`** | — | **company-scoped** `BD-ACC-02` | `Y` | `N` | L223 | **`HEG`** |
| **`BC-12`** | **Close → subledgers** | Close | period close | lock / control signal | all subledgers | `-12` | **NONE** | `A` | **no accounting-period object exists** | — | accounting date *"silently movable past a lock"* | `Y` | `Y` | L224 | **`HEG` · §5** |
| `BC-13` | Inventory → Sales and Purchase | Inventory | delivery / receipt validated | progress, availability, transfer status | Sales, Purchase | `-13` | **NONE** | `A` | **two derivations of one fact can disagree; nothing reconciles them** | after partial cancel / return | — | `N` | `Y` | L225 | **`HEG`** |
| `BC-14` | Quality → Inventory | Quality | inspection result | hold / release | Inventory | `-14` | **NONE** | `A` | **the Quality object itself is absent** — `0` blobs | release | — | `N` | `Y` | L226 | **`HEG`** |
| `BC-15` | Service / Project → Accounting | Service / Project | performance asserted | revenue / cost fact | Accounting | `-17` | **NONE** | `A` | **no physical fact, only an assertion; no event record** | — | — | `Y` | `N` | L229 | **`HEG`** |
| `BC-16` | Migration / replay → Inventory **and** Accounting | Migration | cutover / replay | opening balances; history | Inventory **and** Accounting | `-18` | **NONE** | `A` | **el. `14` and `15` `NOT SUPPLIABLE`** | replay non-idempotent (`CORR1-F-03`) | **this class *is* migration** | `Y` | `Y` | L230 | **`HEG`** |
| **`BC-17`** | **Purchase → Inventory** (goods receipt) | **Purchase** | PO confirmed → receipt | expected receipt: product, qty, date, supplier, price reference | Inventory | **NONE** | **`4` `CG`** | `A` | **over-receipt tolerance undefined**; bridge is a **swept suspense account, not item-matched** | `X-08` purchase return, basis `PENDING` | `HX-04` is Inventory's receiving row | `Y` | `Y` | `HX-04`; `SA_CORR4_02` §5 r4; `X-01`, `X-05` | **`HEG` · §4** |
| — | *`XMC-H-15` Quality hold → Accounting* | Quality | hold applied | **none, if neutral** | Accounting | `-15` | none | **`C`** | see `20_` §4 | — | — | `C` | `N` | `20_` §4 | **CONDITIONAL** |
| — | *`XMC-H-16` Internal transfer → Accounting* | Inventory | internal move | **none, if neutral** | Accounting | `-16` | none | **`C`** | see `20_` §4 | — | — | `C` | `N` | `20_` §4 | **CONDITIONAL** |

---

## 2. THE THREE LEGS, MEASURED

```
LEG A  17 <-> 18
  classes with an XMC-H row          16 / 17   94.1 %   (BC-17 has none)
  XMC-H rows inside the base set     16 / 18   88.9 %   (-15, -16 conditional)

LEG B  17 <-> 10
  contract rows reaching a class     10 / 10  100.0 %   (row 4 now reaches BC-17)
  classes reached by a contract row  12 / 17   70.6 %
    reached   : BC-01..BC-11, BC-17
    NOT reached: BC-12, BC-13, BC-14, BC-15, BC-16
  rows spanning >1 class              2        (row 6 -> BC-04+BC-05; row 7 -> BC-06+BC-07+BC-08)

LEG C  18 <-> 10  (unchanged by the ruling)
  XMC-H rows with a contract row     11 / 18   61.1 %
  CONTRACT-SUFFICIENT rows            2 / 10   20.0 %   (rows 5, 10)
  CONTRACT-COMPLIANT rows             0 / 10    0.0 %   -- stated by SA_CORR4_02 SS5 itself

CHECK  12 reached + 5 not reached = 17   OK
CHECK  16 mapped + 1 unmapped     = 17   OK
CHECK  16 inside + 2 conditional  = 18   OK
```

### 2.1 Direction of movement — recorded, because the expansion makes coverage worse

| Measure | On `12` (`06_`) | **On `17`** | |
|---|---:|---:|---|
| classes reached by a contract row | `91.7 %` | **`70.6 %`** | **`−21.1` pts** |
| classes with an `XMC-H` row | `100 %` | **`94.1 %`** | **`−5.9` pts** |
| classes contract-sufficient | `16.7 %` | **`11.8 %`** | **`−4.9` pts** |
| contract rows reaching a class | `90.0 %` | `100 %` | `+10.0` pts |
| gap-carrying flows outside the set | `5` floor → `7` | `0` base · `2` conditional | resolved |

> **Boss: *"a deliberate scope declaration, not an arithmetic repair."*** The declaration brought `5`
> flows **inside** a denominator they were previously outside of. **Nothing was fixed by declaring
> them; they are now counted.** That is the correct direction for a scope act and the wrong direction
> for a coverage percentage, and both are published.

---

## 3. `CORE-08` — DISCHARGED AS A MAPPING ACT

`22_` §1.1 created the obligation: *"`12 ↔ 18 ↔ 10` is now derivable and has not been derived. Until it
is, the per-boundary applicability declaration (`SC-11` §6 #5) can name its targets but **cannot say
which handoff rows each target covers**."*

| | |
|---|---|
| Obligation | map the declared classes onto the `18` and the `10` |
| **Discharged** | **YES — §1 states, for every one of the `17`, which `XMC-H` row and which contract row covers it, or that none does** |
| `SC-11` §6 #5 | **UNBLOCKED as a mapping.** The per-boundary applicability declaration can now name its targets **and** their covering rows |
| What remains | **not a mapping act** — `5` classes have no contract row (§5) and `1` has no `XMC-H` row (§4). Those are **coverage gaps**, carried at `29_` |
| Identifier | **`CORE-08`** — renamed from the recovery's re-used `CORE-07` per `17_` §3. **`CORE-07` reverts to `CORR1`'s `FIFO` layer obligation** (`24_`) |

---

## 4. `BC-17` — THE MANDATORY PROOF `§11` REQUIRES

**Ruled: prove `Purchase → Goods Receipt → Inventory State → Valuation / Financial Handoff.`**

| Leg | Evidence | Status |
|---|---|---|
| **Purchase → Goods Receipt** | `HX-04`: *"Expected receipt: product, quantity, expected date, supplier, **price reference** · Purchase order confirmed · **Create the receipt**"* — **Inventory's receiving-side row**; `SA_CORR4_02` §5 r4: *"**none authored by the emitter**"* | **`CONTRACT-GAP`** — no emitter-authored artefact |
| **Goods Receipt → Inventory State** | `HX-05`: *"Received quantity, date, lot, **over- or under-receipt** · Three-way match, backorder decision"*; **`INV-OWNED` — over-receipt tolerance policy still open** | **PARTIAL** — the state transition is specified; **its tolerance boundary is not** |
| **Inventory State → Valuation** | routed through **`BC-05`** (`XMC-H-05`), which is `HOLD — EXACT GAP` on elements `10`, `12`, `13`, `14`, `15` | **`HEG`** — inherits `BC-05`'s gap |
| **→ Financial Handoff** | **`X-01`: the goods-received bridge is a *"swept suspense account, not item-matched"*** | **STRUCTURAL GAP** — the receipt cannot be matched to its bill at item level |

**Governing configuration:** over-receipt tolerance is *"a **company-scoped configuration**; its default
(refuse vs accept-and-event) is a control-default election"* — Boss election **`B4`**, ruled **refuse
(`0`)**. Carried at `22_` as **`CFG-04`**.

> **`CORR2-XW2-01` — MATERIAL.** The mandatory `BC-17` chain is **specified at three legs and broken at
> all four**: no emitter artefact, an open tolerance boundary, an inherited valuation gap, and a
> **swept suspense bridge that is not item-matched**. **The last is the one a Functional Designer cannot
> work around**, because it makes purchase-receipt-to-bill matching non-derivable at line level.

---

## 5. `BC-12` — THE GAP THE RULING REFUSED TO ABSORB

**Ruled at `17_` §2.4: *"This remains an OPEN CONTRACT SUFFICIENCY GAP. The expansion to `17` does NOT
hide or discharge it."***

| | |
|---|---|
| Contract rows reaching `BC-12` | **`0` of `10`** — verified row by row at §1 |
| `XMC-H-12` disposition | `HOLD — EXACT GAP` |
| Root cause at primary source | *"**There is no accounting-period object**, and the accounting date is *'silently movable past a lock'*. The producing side designed a native period guard with **no global bypass** and is **waiting for a lock source with no object behind it**."* |
| Scenario | **`X-19`** period-end / cut-off · `HOLD` · *"no accounting-period object exists; reconciliation holds at the boundary, not continuously"* |
| Why no contract row exists | the `10` rows are **flow-shaped**. Close is not a flow between two modules; it is **a control event addressed to all of them**. The contract register has no shape for it |
| Owner | **Architecture / Contract Semantics**, as ruled |
| Closure requirement | an **accounting-period object** with identity, state and a lock the accounting date cannot pass; then a contract row addressed to all subledgers |
| Status | **OPEN CONTRACT SUFFICIENCY GAP** — `29_` blocker |

**The other `4` classes reached by no contract row** — `BC-13`, `BC-14`, `BC-15`, `BC-16` — have the same
structural cause on the `10`-row register: it enumerates **emitting flows into Accounting or Inventory**,
and these four are, respectively, a reverse-direction fact, an optional-module fact, an assertion without
a physical event, and a cutover. **`0` of the `5` is an oversight; all `5` are shape mismatches**, and
that is itself the finding: **the `10`-row contract register cannot express `5` of the `17` declared
classes.**

> **`CORR2-XW2-02` — MATERIAL.** `SA_CORR4_02` §5's `10` rows are not a partial sample of the `17`;
> they are a **different unit** — emitting flows, not boundary classes. **`70.6 %` is therefore not a
> shortfall to be closed by writing `5` more rows**; it measures a register whose shape covers `12` of
> the `17` and cannot, as constituted, cover the rest.

---

## 6. COVERAGE SUMMARY

| Dimension | Denominator | Named | Numerator | Coverage | Floor | Verdict |
|---|---:|:-:|---:|---:|---:|---|
| `F` Cross-module — classes with an `XMC-H` row | `17` | ✔ | `16` | **`94.1 %`** | `96 %` | **HOLD** |
| `F` Cross-module — classes reached by a contract row | `17` | ✔ | `12` | **`70.6 %`** | `96 %` | **HOLD** |
| `F` Cross-module — contract rows reaching a class | `10` | ✔ | `10` | **`100 %`** | `96 %` | **MEETS** |
| `F` Cross-module — classes contract-sufficient | `17` | ✔ | `2` | **`11.8 %`** | `96 %` | **HOLD** |
| `F` Cross-module — classes contract-compliant | `17` | ✔ | **`0`** | **`0 %`** | `96 %` | **HOLD** |
| `F` Conditional items fully attributed | `2` | ✔ | `2` | **`100 %`** | `100 %` | **MEETS** |
| `K` `BC-17` mandatory chain legs proven | `4` | ✔ | **`0`** | **`0 %`** | `96 %` | **HOLD** |

---

## 7. CHECKPOINT

> **Crosswalk rebuilt on the `17` · `15` attributes per class · **`10 / 10` rows map · `12 / 17` classes
> reached · `16 / 17` have an `XMC-H` row** · `CORE-08` **DISCHARGED as a mapping act** ·
> `BC-17`'s mandatory chain proven at **`0 of 4` legs**, broken at the suspense bridge ·
> `BC-12` carried as an **OPEN CONTRACT SUFFICIENCY GAP**, expressly not absorbed ·
> **`5` unreached classes are a register-shape mismatch, not `5` missing rows** ·
> `3` coverage measures moved **worse** than on the `12`, and all `3` are published ·
> **`0` declared class left unmapped without an explicit blocker.**

No Evidence = No Progress. Never Skip Gate. Truth over Pass.
**Boss is the SOLE FINAL APPROVER.**
