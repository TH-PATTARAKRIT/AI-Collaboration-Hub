# 47 — P03 UNRESOLVED EVIDENCE REGISTER

**LAYER 2 — AUDIT QUARANTINE.** Everything P03 does not know, with what would close it.

---

## 1. Unresolved

| ID | Item | Class | What closes it | Owner |
|---|---|---|---|---|
| `UNR-P03-01` | Whether the target configuration uses multi-operator work orders — governs `DC-01`'s magnitude, not its existence | `UNRESOLVED` | A deployment with work orders | UAT |
| `UNR-P03-02` | Whether setup/cleanup is charged once per backorder split | `UNRESOLVED` | Runtime trace | UAT |
| `UNR-P03-03` | Performance budget for P03 flows | `UNRESOLVED` | `DEP-09` — manufacturing admitted to the target baseline | Boss/PMO |
| `UNR-P03-04` | Whether `AE-06`'s subtraction-derived component cost survives a bill correction | `UNRESOLVED` | P01 | **P01** |
| `UNR-P03-05` | Incidence of `DC-14` — do both distributions resolve to a common account? | `UNRESOLVED` | A deployment with the project bridge installed | UAT |
| `UNR-P03-06` | Reachability of a second labour post | **HOLD — RUNTIME EVIDENCE REQUIRED** | Runtime tracing; forbidden to this session | UAT |
| **`UNR-P03-07`** | **`iTEST02` dump unreadable** — `pg_restore: unsupported version (1.16)` | **HOLD — TOOLING** | Upgrade local PostgreSQL client tools. **Cheapest open item in the package** | Environment |
| `UNR-P03-10` | Whether any of the three readable databases is the system SMEsPlus must migrate | `UNRESOLVED` | Boss / programme statement | Boss |
| `SCOPE-Q-01` | Analytic plan — `TENANT` or `COMPANY`? | **HOLD — SCOPE EVIDENCE REQUIRED** | P09 + P11 | **P09** |
| `SCOPE-Q-02` | Productivity-loss taxonomy — `PLATFORM` with tenant extension, or `TENANT`? | **HOLD — SCOPE EVIDENCE REQUIRED** | Business semantics | P11 |
| `SCOPE-Q-03` | May one tenant's BOM reference another tenant's product? | **HOLD — SCOPE EVIDENCE REQUIRED** | Design decision | P11 |

## 2. Closed this round

| ID | Was | Now |
|---|---|---|
| `UNR-P03-08` | Custom addon sets unswept | **CLOSED** — swept with a positive control; no manufacturing cost override exists — `27` §7 |
| `UNR-P03-09` | Landed-cost interaction with manufacturing unmeasured | **CLOSED — EXECUTED.** `stock_landed_cost` = **0** rows in both databases; `stock_valuation_adjustment_lines` = 0. Positive control in the same run: `mrp_production` = 10,764. `mrp_landed_costs` is installed and **has never been used** |
| `DEP-04` | Installed-module list unknown; capped every negative claim | **PARTIALLY CLOSED** — obtained for 2 of 4 databases — `26` §6 |
| `DEP-13` | `HOLD — UAT REQUIRED`, one query | **EXECUTED — VACUOUS**, 0 of 0 — `31` |

### Round 4 — changes

| ID | Status |
|---|---|
| **`UNR-P03-07`** iTEST02 unreadable | **CLOSED** — `62` |
| **`UNR-P03-14`** `DC-04` cost method unknown | **CLOSED** — measured: `iSMEs` 18 FIFO + 8 average, 0 standard; `iTEST02` standard but periodic. `DC-04` **UNREACHABLE** |
| `UNR-P03-01` multi-operator work orders | **PARTLY CLOSED** — 7 of 13 work orders carry >1 log; 1 genuinely overlaps; that log has **zero duration**, so the effect is zero |
| `UNR-P03-05` `DC-14` incidence | **MEASURED — zero.** Modules installed in `iTEST02`; **0 of 60** work centres carry a distribution |
| `UNR-P03-11` **new** | `iSMEs` and `iTEST02` are **different schema generations** — company-dependent properties as rows vs `jsonb` columns; `iTEST02` has no valuation-layer table. No finding crosses them without saying so |
| `UNR-P03-15` **new** | Whether the 49 unvalued finished moves are a manufacturing or an inventory-valuation defect — routed to Inventory |
| `UNR-P03-16` **new** | Whether the material-only carrying value and the never-posted COGS compound — joint P02/P03/Inventory, routed to P11 |
| `UNR-P03-17` **new** | The production-account balance in `iTEST02` was **not** decomposed — the one measurement that would test `DC-03`/`DC-04` directly |
| `UNR-P03-18` **new** | The company-dependent valuation **fallback** was inferred from an absent valuation table and a 32-line ledger, **not read from `ir_default`** — `E4`'s preserved dissent |

## 3. Explicitly *not* P03's to resolve

| Item | Owner | Status quoted unchanged |
|---|---|---|
| `BLK-07` allocation denominator | **Boss** | HOLD — DESIGN DECISION REQUIRED |
| `BLK-08` maintenance split | **Boss** | HOLD — DESIGN DECISION REQUIRED |
| `BLK-01`, `BLK-02` | UAT | HOLD — UAT REQUIRED |
| `UNR-C-03` standard-cost TAS 2 compliance | **Asset** | Medium-High, open |
| COGS `JT-01/04/05` | COGS track | NOT DECIDABLE |
| `BD-P03-01/02` variance recognition | **Boss** | BOSS CONTROLLED DECISION |
| `DEP-08` joint/co-product routing | **Boss** | FINAL-GATE DECISION REQUIRED |
| `P03-GAP-08` indirect labour / overhead pool unowned | **Boss** | routing required — `39` §3 |
| `P11-D-1/2/3` | **P11** | PEER DEPENDENCY OPEN |

## 4. The honest total

**11 unresolved, 4 closed or advanced this round, 9 items owned elsewhere.**

Counted by hand from §1 (12 rows), §2 (3 rows) and §3 (9 rows) rather than asserted —
`smeplus-totals-are-unverified-claims`.
