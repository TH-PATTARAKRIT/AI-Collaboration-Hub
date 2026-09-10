# 20 — CANONICAL `17`-BOUNDARY REGISTER

# `BC-01 … BC-17 · DECLARED ON BOSS AUTHORITY · 2 CONDITIONAL ITEMS`

Session: `[SMEPLUS-26-09-10-PHASE-PRETEST-B7R2-REMEDIATION-NEWSESSION-001]`
Authority: **`BOSS-CORR1-01`, option (c), `17_` §2.2** · Boss: **SOLE FINAL APPROVER**

> **Identifier discipline, applied because this package documented its opposite.**
> The classes are named **`BC-01`…`BC-17`**, not *"class `n`"*. `CORR1`'s `CORE-07` was silently re-used
> for a second obligation (`10_` §2); *"class `12`"* would have collided with `XMC-H-12` **and** with the
> new ordinal positions. **`BC-nn` is this session's own family and is declared here.**

---

## 1. THE `17` DECLARED BASE BOUNDARY CLASSES

| `BC` | Declared class | `XMC-H` | Origin | Producer | Consumer | Disposition at primary source |
|---|---|---|---|---|---|---|
| **`BC-01`** | Sales → Inventory | `-01` | `B4′` | Sales | Inventory | `HOLD — EXACT GAP` — route indirect on sell side, direct on buy side; no published contract states which |
| **`BC-02`** | Sales → Manufacturing | `-02` | `B4′` | Sales | Manufacturing | `HOLD — EXACT GAP` — the MO **never raises its own demand**; the Supply Nature rule deciding *make* is undetermined |
| **`BC-03`** | Sales → Purchase (dropship / MTO) | `-03` | `B4′` | Sales | Purchase | `HOLD — EXACT GAP` — **a control breach**: the write bypasses the demand-approval gate every human-raised purchase must pass |
| **`BC-04`** | Manufacturing → Inventory | `-04` | `B4′` | Manufacturing | Inventory | `HOLD — EXACT GAP` — fails on `P6` and on the `BC-05` leg beneath it |
| **`BC-05`** | Inventory → Accounting | `-05` | `B4′` | Inventory | Accounting | `HOLD — EXACT GAP` — element `10` absent · `15` absent · `14` absent by the producer's own record · `12`/`13` partial |
| **`BC-06`** | Sales → AR / Accounting | `-06` | `B4′` | Sales | AR / Accounting | `HOLD — EXACT GAP` — round-trip: Sales derives *already-billed* by reading Accounting's stored result |
| **`BC-07`** | Purchase → AP / Accounting | `-07` | `B4′` | Purchase | AP / Accounting | `HOLD — EXACT GAP` — same round-trip defect |
| **`BC-08`** | Payment → Bank / Accounting | `-08` | `B4′` | Payment | Bank / Accounting | `HOLD — EXACT GAP` — the matching state anchoring the chain is *"freely destructible across a closed period"* |
| **`BC-09`** | Asset → Accounting | `-09` | `B4′` | Asset | Accounting | `HOLD — EXACT GAP` — derecognition `PARTIAL`; **the Equipment consumer has no evidenced route** |
| **`BC-10`** | Expense → Accounting | `-10` | `B4′` | Expense | Accounting | `HOLD — EXACT GAP` — petty cash and employee advance both structurally broken |
| **`BC-11`** | Tax → Accounting / reporting | `-11` | `B4′` | Tax | Accounting / reporting | `HOLD — EXACT GAP` — substitution rule base `EVIDENCE-INSUFFICIENT`; **no statutory claim made** |
| **`BC-12`** | Close → required subledgers / control sources | `-12` | `B4′` | Close | all subledgers | `HOLD — EXACT GAP` — **there is no accounting-period object**; the accounting date is *"silently movable past a lock"* |
| **`BC-13`** | Inventory → Sales and Purchase | `-13` | **`BOSS-CORR1-01` (c)** | Inventory | Sales, Purchase | `HOLD — EXACT GAP` — *"MATCH, with a named hazard"*: two derivations of one fact can disagree and **nothing reconciles them** |
| **`BC-14`** | Quality → Inventory | `-14` | **`BOSS-CORR1-01` (c)** | Quality | Inventory | `HOLD — EXACT GAP` — route Boss-ruled verbatim; **the Quality object itself is absent** — `0` blobs, two shapes, firing positive controls |
| **`BC-15`** | Service / Project performance → Accounting | `-17` | **`BOSS-CORR1-01` (c)** | Service / Project | Accounting | `HOLD — EXACT GAP` — **for a service there is no physical fact, only an assertion**, with no event record; the project derivation writes **three costed rows from one duration** |
| **`BC-16`** | Migration / replay → Inventory and Accounting | `-18` | **`BOSS-CORR1-01` (c)** | Migration | Inventory **and** Accounting | `HOLD — EXACT GAP` — provenance reference does not exist (el. `14`); replay requires a stable identity (el. `15`); **`14` and `15` `NOT SUPPLIABLE`** |
| **`BC-17`** | **Purchase → Inventory** (goods receipt) | **NONE** | **`BOSS-CORR1-01` (c)** | Purchase | Inventory | **`HOLD — EXACT GAP` by construction** — see §3 |

**`17` classes, each named once. `BC-13`…`BC-17` are the `5` added by the ruling.**

> **Note on ordinals:** `BC-15` is `XMC-H-17` and `BC-16` is `XMC-H-18`. **The two numbering systems
> diverge from `BC-13` onward.** Every citation in this package uses `BC-nn` for a declared class and
> `XMC-H-nn` for a register row, never interchangeably.

---

## 2. MEMBERSHIP PROOF

```
POPULATION : the declared canonical boundary classes
UNIT       : boundary class
PATTERN    : enumerated from the Boss ruling text at 17_ SS2.2, member by member
PATH SET   : 17_ (this package) for the ruling; SA_CORR3_08 L213-230 for XMC-H dispositions;
             SA_CORR4_02 SS5 for contract rows
AUTHORITY  : BOSS-CORR1-01 option (c) -- a Boss declaration, not an inherited or derived set

BASE CLASSES DECLARED                 17
  carried forward from B4' (12)       12   BC-01..BC-12
  added by BOSS-CORR1-01 (c)           5   BC-13..BC-17
  CHECK  12 + 5                       17   OK

MAPPED TO AN XMC-H ROW                16   BC-01..BC-16
NOT MAPPED TO ANY XMC-H ROW            1   BC-17
  CHECK  16 + 1                       17   OK

XMC-H ROWS (18) DISPOSITION
  inside the declared base set        16   -01..-14, -17, -18
  CONDITIONAL APPLICABILITY ITEMS      2   -15, -16
  CHECK  16 + 2                       18   OK
```

**Positive control on the enumeration instrument:** `grep -oE 'XMC-H-[0-9]{2}' SA_CORR3_08 | sort -u |
wc -l` → **`18`**, and `Sales → Inventory` matches while `Purchase → Inventory` returns **`0`** in three
command shapes. **The instrument discriminates.**

---

## 3. `BC-17` — THE DECLARED CLASS WITH NO TESTED ROW

| Attribute | Value |
|---|---|
| Declared by | **`BOSS-CORR1-01` (c)**, verbatim: *"the goods-receipt handoff from an approved purchasing document into physical inventory"* |
| `XMC-H` row | **NONE** — the cross-module contract proof never carried this boundary |
| Register that carries it | **`HX-04`** — *"Purchase → Inventory · Expected receipt: product, quantity, expected date, supplier, price reference · Purchase order confirmed · Create the receipt · `OP-03` · `INV-OWNED`"* |
| Whose register | **Inventory's**, header *"SMEsPlus-OWNED HANDOFF DESIGN"*. **It is the receiving party's record of what it expects**, not the emitter's commitment |
| Contract row | **row `4`, `CONTRACT-GAP`** — *"none authored by the emitter"* |
| Emitting party | **Purchase** |
| Producing-side design package for Purchase | **NONE** — `SA_CORR4_00` §5: `FINAL_SOLUTION` holds `30` paths, **`0` outside `INVENTORY`** |
| Related row | `HX-05` *"Inventory → Purchase · Received quantity, date, lot, over- or under-receipt · Three-way match, backorder decision · **over-receipt tolerance policy still open**"* |
| Scenario | **`X-01`** stockable purchase receipt → handoff · `HOLD` · *"goods-received bridge is a **swept suspense account, not item-matched**"* · **`X-05`** partial receipt · `HOLD` · over-receipt tolerance undefined |
| Status | **`HOLD — EXACT GAP`** |

> **`BC-17` is the most fundamental inventory inflow in an ERP and it enters the canonical denominator
> with no emitter-authored artefact, no `XMC-H` row, an unmatched suspense bridge and an undefined
> over-receipt tolerance.** Carried to `21_`, `28_` and `29_`.

---

## 4. `XMC-H-15` / `XMC-H-16` — CONDITIONAL APPLICABILITY, DETERMINED

**Ruled at `17_` §2.3: not silently `N/A`; `8` attributes required from authoritative configuration
semantics; unsupported `N/A` not allowed.**

### 4.1 The single governing invariant

`SA06-F-05`, verbatim: *"internal-transfer financial neutrality **is protected only by configuration;
no independent check exists**."*

The rule: *"A movement between two internal company locations changes where stock is and creates no
accounting consequence."*

`SA_CORR3_08` §2.6 and `SA_CORR2_05` §3.1 establish that **one unprotected invariant governs three
things**: transfer neutrality (`-16`), quality-hold cost-neutrality (`-15`), **and the `N/A` status of
both**. `SA_CORR3_06` classifies it **`Live`, not latent**: *"neutrality is configuration-protected and
**one change breaks both**."*

### 4.2 The `8` required attributes

| # | Attribute | **`XMC-H-15`** Quality hold → Accounting | **`XMC-H-16`** Internal transfer → Accounting |
|---:|---|---|---|
| `1` | **Enable condition** (row EMITS a valuation fact → enters the denominator) | any configuration in which a **quality hold changes carried cost** — a hold location valued differently from the source, or a hold state mapped to a distinct valuation account | any configuration in which an **internal location change produces a value event** — locations mapped to different valuation accounts, or a transfer crossing a valuation boundary |
| `2` | **Disabling condition** (`N/A` holds) | hold is cost-neutral: the held stock retains its carried cost and its valuation account | internal→internal is value-neutral: location is a **place**, not a valuation dimension |
| `3` | **Applicable business scenario** | **`X-13`** scrap / damage / write-off (adjacent), and the quality-hold path of **`X-14`** | **`X-14`** internal warehouse transfer — *"no inappropriate financial effect"* |
| `4` | **Tenant / company applicability** | **COMPANY** — valuation-account mapping is company-scoped under `BD-ACC-02`'s boundary | **COMPANY**. **Cross-company movement is NOT this row** — it is `X-15`, and `BD-ACC-02` forbids cross-company statutory posting |
| `5` | **Configuration path** | valuation-account mapping by location / stock state, under **Product Category** measurement policy (`BD-ACC-03A/B`) | **identical path** — this is why one change breaks both |
| `6` | **Ownership** | **Inventory** emits or does not emit; **Accounting** consumes if emitted | **Inventory** |
| `7` | **Evidence** | `SA_CORR3_08` §2.6 · `SA06-F-05` · `SA_CORR2_05` §3.1 · `SA_CORR3_06` L434 · scenario `X-14` at `PT01` | same |
| `8` | **Boundary consequence** | **if enabled, an ungoverned posting**: the row has no contract, so a valuation fact would cross with no published payload, guarantee or consumer obligation | **identical** |

### 4.3 Determination

| | |
|---|---|
| Is the `N/A` **supported today**? | **YES** — evidence-backed, reason stated, primary source sound |
| Is the `N/A` **durable**? | **NO** — defeasible by a configuration change, on a path shared with `-15` |
| Is there an **independent check** that would detect the flip? | **NO** — `R4-F-18`: *"no independent check exists"* |
| `§24` / `17_` §2.3 disposition | **`CONDITIONAL APPLICABILITY — UNRESOLVED`.** Not `N/A`; not in the base `17`; **enters the applicable denominator of any scenario in which the enable condition holds** |
| Which scenario | **`X-14`**, which is itself `HOLD`: its Boss-stated obligation is to demonstrate *"no inappropriate financial effect"* — **a negative recorded as unproven** |

> **`CORR2-CND-01` — MATERIAL.** The `N/A` is correct today, undurable by construction, **and its flip is
> undetectable**. Under the five-status rule this is **not** `N/A — AUTHORITY SUPPORTED ONLY`: an
> authority-supported `N/A` requires the exclusion to be **stable**, and this one is protected by a
> setting no control observes. **It is `HOLD AT CURRENT PHASE`, and its closure is an independent-check
> obligation** carried at `27_` (`ZT-04`) and `29_`.

---

## 5. COVERAGE OF THE `17`

| Measure | Denominator | Numerator | Coverage | Floor | Verdict |
|---|---:|---:|---:|---:|---|
| Declared classes with a named `XMC-H` row | `17` | `16` | **`94.1 %`** | `96 %` | **HOLD** — `BC-17` |
| Declared classes reached by a contract row | `17` | `12` | **`70.6 %`** | `96 %` | **HOLD** |
| Declared classes that are **contract-sufficient** | `17` | `2` | **`11.8 %`** | `96 %` | **HOLD** |
| Declared classes **contract-compliant** | `17` | **`0`** | **`0 %`** | `96 %` | **HOLD** |
| Gap-carrying flows **outside** the declared set | — | `0` base · **`2` conditional** | — | — | improved by the ruling |
| Conditional items carrying all `8` attributes | `2` | `2` | **`100 %`** | `100 %` | **MEETS** — §4.2 |

---

## 6. CHECKPOINT

> **`BC-01`…`BC-17` declared and enumerated · `12` carried + `5` added = `17` ✔ ·
> `16` mapped to an `XMC-H` row, **`1` (`BC-17`) mapped to none** · `18` rows = `16` inside + `2`
> conditional ✔ · `XMC-H-15`/`-16` determined against all `8` required attributes and classified
> **`CONDITIONAL APPLICABILITY — UNRESOLVED`**, not `N/A` · **`0` unsupported `N/A`** ·
> `4` of `5` coverage measures **below floor**, and `3` moved **worse** than the pre-ruling `12`.**

No Evidence = No Progress. Never Skip Gate. Truth over Pass.
**Boss is the SOLE FINAL APPROVER.**
