# 05 — MATERIAL-FLOW CANONICAL REGISTER

## `DENOMINATOR NOT CLOSABLE — THE GAP IS NOW SPECIFIC`

Session: `[SMEPLUS-26-09-10-PHASE-PRETEST-CORRECTIVE-CLOSURE-001]` · Boss: **SOLE FINAL APPROVER**

> **§8: *"Do not assume migration is outside the flow model."* — TESTED, and it is NOT outside it.**

---

## 1. The two convergence registers, and what they enumerate

| Register | Unit | Members | Status |
|---|---|---:|---|
| `IR-01`…`IR-18` (`SA_CORR2_05`) | stock-affecting flow | **`18`** | `14 RECONCILED / 3 PARTIAL / 1 NOT RECONCILED` |
| `AR-01`…`AR-29` (`SA_CORR2_06`) | material business flow | **`29`** | `15 RECONCILED / 14 PARTIAL / 0 UNKNOWN` |

**All `18` `IR` members are operational movements:** sales delivery · purchase receipt · customer return ·
vendor return · RM consumption · FG receipt · scrap · by-product · internal transfer · adjustment ·
partial fulfilment · kit component · dropship · quality hold · **asset capitalization from stock** ·
cross-company transfer · service/project consumption · equipment/maintenance consumption.

**`0` of them is a migration, opening-balance or cutover flow. Same for `AR-01`…`AR-29`.**

---

## 2. The measurement — §8 executed

**INSTRUMENT:** case-insensitive `migration` and `opening balance` over each register.
**POSITIVE CONTROL:** `reconcil` in `SA_CORR2_05` → **`41`** (the instrument reaches the file).

| Register | `migration` | `opening balance` |
|---|---:|---:|
| `SA_CORR2_05` (`IR`) | **`0`** | **`0`** |
| `SA_CORR2_06` (`AR`) | **`0`** | **`0`** |

**`XMC-F-14`'s original instrument agrees:** `migration\|opening balance\|cutover` over `SA06`, `SA07`,
`SA_CORR2_05`, `SA_CORR2_06` → **`0`, `0`, `0`, `0`**, positive control **`11`** files corpus-wide.

---

## 3. `CC-F-05` — migration is INSIDE the model, and absent from exactly two registers

**§8 asked whether migration sits outside the flow model. It does not:**

| Where migration IS represented | Members |
|---|---|
| **Scenario population** | **`X-20`** historical migration across fiscal years · **`X-21`** AI migration mapping + deterministic reconciliation |
| **Handoff register** (`HX`) | **`HX-23`** master data with a provenance reference · **`HX-24`** **certified opening balances, quantity and value** · **`HX-25`** movement history, or opening plus history from the cutover date |
| **Handoff contract** | **element `14`** — migration / replay batch identity |
| **Runtime obligations** | `RT-E15-05` — replay reproduces identical identities and **adds zero events** |
| **Where it is ABSENT** | **`IR-01`…`IR-18` and `AR-01`…`AR-29` — the two registers that establish flow convergence** |

> **The defect is not that migration was forgotten. It is that migration is carried in the scenario,
> handoff, contract and runtime models and was **never admitted to the flow-convergence population** —
> so its Stock-Truth and Financial-Truth reconciliation was never asked.**

**Consequence:** `X-20` and `X-21` are graded `SA-SPEC COMPLETE / RUNTIME PROOF REQUIRED` against a
convergence analysis whose population **excludes their own flow class**.

---

## 4. Why the denominator still cannot be closed

**Evidence-derived candidate members for the missing class:**

| Candidate | Source | Would it be `1` flow or several? |
|---|---|---|
| Certified opening balance (qty + value) | `HX-24` | plausibly its own flow — it creates value with no movement |
| Movement history / opening-plus-history from cutover | `HX-25` | plausibly its own — it creates history |
| Master data with provenance reference | `HX-23` | arguably **not** a material flow — no quantity or value |
| Replay of a migration batch | element `14`, `RT-E15-05` | a **dimension** of the above, or its own flow |

> **`3` candidates and `1` dimension. Whether they resolve to `1`, `2` or `3` flow rows is a
> determination by the flow register's owner — it is NOT derivable from the evidence, and §8 requires the
> denominator be *"explicit and evidence-derived."***

**This round therefore does NOT publish a closed denominator.** Assigning a number would be inventing
membership — the same act §5 forbids for the gate set.

| | |
|---|---|
| Status | **`HOLD — DENOMINATOR NOT CLOSABLE`** |
| Progress made | `PT05-F-03` said *"short by at least one."* It is now **specific**: short by **the migration/opening-balance class**, whose candidate members are **enumerated** (`HX-23`/`-24`/`-25` + element `14`) and whose absence is confined to **exactly two registers** |
| Owner | **SMEs Core** to propose the flow rows · **PMO/Boss** to admit them to the convergence population |
| Corrected denominators once admitted | `IR` `18 → 18 + n`; `AR` `29 → 29 + n` |

---

## 5. Checkpoint

> **§8 executed: migration is **not** outside the flow model — it is in the scenario, handoff, contract
> and runtime models and **absent from both convergence registers** (`0`/`0`, positive control `41`) ·
> `X-20`/`X-21` were graded against a population that excludes their own flow class ·
> **`3` candidate members enumerated; the denominator is NOT closed, because deriving `n` from this
> evidence is not possible and inventing it is forbidden** · `HOLD`.**

