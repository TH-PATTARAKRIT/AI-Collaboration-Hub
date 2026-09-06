# P11 — BLOCKER REGISTER — CORR2

`[SMEPLUS-26-09-06-…-CORR2-PHASES-001]` · `CP-P11C2-06` · **PHASE S**

> **Re-derived, not carried.** CORR1 anchors are anchors, not targets.
> **No blocker closes because its wording improved. No Boss item is decided by P11.**

---

## 1. Movement this round

| id | Blocker | CORR1 | **CORR2** | Basis |
|---|---|---|---|---|
| `B-17` | `X2-F06` — a stated rule that was not the rule applied, compounded by a scope crossing | `CRITICAL` · RE-OPENED | **`CONTRADICTED — CORRECTED AND CLOSED`** | `P11_B17_SCOPE_REPAIR_CORR2.md`. `S3` split into `S3-SRC` / `S3-DEP`; the cross-scope inference **deleted**; `S3-DEP` independently established on **deployed** evidence from `P01` and `P06`. **Verdicts unchanged, warrant replaced** |
| `B-12` | contract establishment vs publication | RE-OPENED | **open — unchanged** | `B-10` still records **0 of 10** peers compliant. Joint artefact; P11 cannot author it alone |
| `B-16` / `T0-13` | the peer tolerance-zero boundary | open | **open — and now corrected at both ends** | `P10` `41_` withdrew its adoption; **`OPT-A` restored**, option set **six**. Still `HOLD — BOSS DECISION REQUIRED`. `UNRESOLVED ≠ ADOPTED` |
| `B-20` | generation the event-to-GL matrix targets | open | **open — narrowed** | `P01` `ERR-P01-23`: a **series-18 deployment exists** (4 companies, 15,522 entries, 47,801 layers, GRNI configured). The generation question is now answerable by Boss declaration, not by more research |
| `B-21` / `T0-14` | `om_data_remove` installed, unauthorised, reachable | `CRITICAL` open | **`CRITICAL` open — strengthened, and its consequence widened** | `P01` `S16-B-05` adds the **schema mechanism**: valuation↔entry FK is **`ON DELETE SET NULL`**. See `B-26` |
| `B-22` | P11 carried a withdrawn figure | HIGH, corrected | **`CONTRADICTED — CORRECTED AND CLOSED` — and P11's correction was itself wrong** | `SPR-01`. P11's CORR1 replacement figure was **generation 2 of a four-generation chain**. Corrected to generation 4. `P11-E-36` |
| `B-23` | no P09 mechanism claim describes a running system | `CRITICAL` open | **`CONTRADICTED — CORRECTED`** | **`X4-C1b`.** Asserted against a **withdrawn** position. `P09` `D26`: *"`B7` is **PARTIALLY WITHDRAWN**. The version-mismatch finding stands for the four databases previously censused; it does **not** stand as a statement about the population. **Every mechanism claim in this programme is version-matched to at least two real deployments**."* P11 quoted generation 4 of a six-generation chain. **`B-23` as worded is withdrawn**; what survives is the narrower `B-23a` — *P09's version-basis caveat holds for the four originally censused databases only* |
| `B-24` | two peer vetoes bind P11's method | HIGH open | **open — honoured by construction in CORR2** | No negative aggregated across processes anywhere in this run |
| `B-01`…`B-11`, `B-13`…`B-15`, `B-18`, `B-19` | — | as recorded | **unchanged** | `B-18` remains the only blocker ever closed by completed work; `B-01` the only one discharged by evidence arriving |

## 2. New this round

| id | Blocker | Class | Basis |
|---|---|---|---|
| **`B-25`** | **A whole class of prior peer negatives is unreliable, and P11 relied on them.** `P05` `RE-20`: *"P11 should treat any prior P05 statement of the form 'not found in the deployed population' as **class B at best** unless it post-dates `41`."* `P05`'s prior handoff **excluded the target platform** — 6 registries were really **9 identities**, and `idemo18_uat` (Odoo 18, 44 MB) was *"on the host throughout"*. Three modules recorded absent are **INSTALLED** | **HIGH** | P11 accepts and **widens it against its own package**: every P11 row whose evidence is a peer negative of that form, predating that peer's own evidence-base correction, is **downgraded to class B pending re-derivation** |
| **`B-26`** | ~~**Every** zero-shaped negative~~ → **BOUNDED BY MECHANISM (`X2-C11`, `X4-C3`).** The universal is **withdrawn**. `ON DELETE SET NULL` NULLs **foreign keys**; tested against the six zeros P11 named, the mechanism is **coherent for 2** (the valuation-layer link zeros — P01's own example), **unestablished for 1** (identity rows, not shown to be an FK) and **incoherent for 3**: a journal seal flag and a company lock date are not FKs to a deleted parent, and an **unfiltered** table delete leaves **0 lines, not 447,384 lines with zero COGS**. P02's zero-COGS instrument is separately **positively controlled**. **P11 converted the owner's bounded statement — *"a competing explanation exists and was never excluded"*, about two valuation-layer findings — into a package-wide downgrade P01 never made.** Restated: **the two valuation-layer zeros are downgraded; the rest are not.** `stock_valuation_layer_account_move_id_fkey … ON DELETE SET NULL` (schema-verified, controls: 584 `CASCADE` / 1,741 `SET NULL` in the same schema) means deleting entries **silently NULLs** the link — *"reproducing exactly the '0 of N valuation layers linked' signature"* (**0 of 47,801**; **0 of 14,441**). *"'Never posted' and 'posted and later deleted' are **observationally identical**."* | **`CRITICAL`** | Affects `0 of 13,814` identity rows · `0 of 109` sealed journals · `0 of 89` companies with a lock · `P02`'s **zero COGS across 447,384** · P11's own **0 subledgers of record**. **Downgraded, not withdrawn.** ~~no evidence says the module fired~~ — **FALSE (`X1-C5`), and P11 carried the contrary sentence at CORR1**: `P06` `70_` states *"a remediation module written inside this programme states the destructive path **has already been run and produced user-visible breakage**"*. P11 generalised P01's **series-16-specific** *"no evidence the module ran in the series-16 deployment"* into an unqualified programme-wide negative. **And *user-visible breakage* is a TRACE**, which undercuts both premises `OC-10` rests on (*"leaves no trace by design"*, *"observationally identical"*). Exclusion = the query `P06` named — **scoped by P06 to the `iEVING` v19 dump, so it cannot exclude deletion in the series-16 or series-18 deployments** |

| **`B-27`** | **The instrument that selected CORR2's evidence is defective, and the population it produced is not the declared one.** The `S8` pattern is a conjunction whose blind spot P11 declared as an intersection; **804 files carry a peer id and no token**; the positive control could only exercise the working half. Enumerated **53**, published **47**; addressed **18**, published **12**; **≥15 actually read**. Six addressed artefacts were enumerated and never consumed, and **P02 — recorded *"none addressed to P11"* — carries a section headed *"What P11 Receives"*** | **`CRITICAL`** | Every CORR2 conclusion inherits an evidence base selected by this instrument. Re-run with the disjunction, publish `returned` vs `processed` per `P09` `NC-12`, then **re-challenge** |
| **`B-28`** | **`฿29,029,467.66` received-not-invoiced is absent from the package.** `P01` heads the section *"THE NUMBER P11 AND P08 BOTH NEED"*: 1,580 PO lines, *"recognised nowhere in the ledger — no receipt entry, no clearing balance, no accrual"*, accrual control **0 of 15,522**. Also absent: **10 of 1,904** mis-typed payables (฿12,969.27) that `P01` explicitly routes as *"a subledger-to-ledger reconciliation difference — **P11's and P08's scope**"*, and **฿39.2m misallocated / 8 posted items > ฿1bn** | **HIGH** | A pure **completeness / cut-off** item — P11's own core subject — missed while the round wrote about completeness. Intake required |
| **`B-29`** | **P08's `AAS+-VETO-01` over the handoff supplying 8 of P11's 17 single-owner facts is absent from the package.** `58_` §4: *"**`AAS+-VETO-01` applies to this handoff.** No item here may be relied upon for design until its two conditions are met."* Condition C-1 is **undischarged** — the owner records *"three of eleven predicates were wrong in a prior round and **all three passed a positive control**"* | **HIGH** | P11 records `P06` and `P09` vetoes and omitted the one over its **largest** evidence source. Every P08-sourced disposition must carry it |

## 3. Position

> **Re-executed after the CORR2 challenge**, unit = distinct `P11-B-nn` id:
> `grep -rho 'P11-B-[0-9][0-9]' | sort -u | wc -l` → **30** (`B-01` … `B-30`, contiguous).

| | CORR1 | **CORR2** |
|---|---|---|
| Registered | 24 | **30** |
| Closed by completed work | 1 (`B-18`) | **1** |
| `CONTRADICTED — CORRECTED AND CLOSED` | 0 | **2** (`B-22`; `B-23` **as worded**) — **`B-17`'s closure was withdrawn by the challenge** |
| Discharged by evidence arriving | 1 (`B-01`) | **1** |
| **Open** | 22 | **26** |
| **`CRITICAL` open** | ~~2~~ **3** | **3** (`B-21`, `B-26`, `B-27`) — **unchanged** |

> ~~**Two blockers closed, two opened, and the `CRITICAL` count went up.**~~ **CORRECTED (`X2-C10`).**
> **CORR1 had THREE `CRITICAL` open** — `B-17`, `B-21`, `B-23` — not two. Executed:
> `grep -cE 'CRITICAL.*(OPEN|RE-OPENED)'` returns **3**. The movement is **3 → 3, unchanged**, and the
> round's headline sentence rested on a figure two P11 artefacts already contradicted in opposite
> directions.
>
> **`B-26` is no longer the most consequential item in the package.** Bounded by mechanism it covers
> **two** valuation-layer zeros, not the class. The claim that it attached a competing explanation to
> *"the entire class of negatives the package is built from"* is **withdrawn** — that was rhetoric the
> mechanism does not support, and it is the `P11-E-01` class again: a headline outrunning its table.

**`CP-P11C2-06` (blockers) — COMPLETE — EVIDENCE VERIFIED.**
