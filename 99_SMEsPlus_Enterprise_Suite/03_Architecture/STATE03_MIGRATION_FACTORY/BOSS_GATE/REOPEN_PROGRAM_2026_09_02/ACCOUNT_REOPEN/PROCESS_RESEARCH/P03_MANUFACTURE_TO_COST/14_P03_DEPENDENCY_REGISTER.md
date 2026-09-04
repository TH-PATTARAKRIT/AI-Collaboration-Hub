# 14 — P03 DEPENDENCY REGISTER

**LAYER 2 — AUDIT QUARANTINE.**

Every unknown that P03 could not resolve, with what closes it and who owns it. Per the
Execution Constitution, unaffected work continued in every case; nothing here blocked the
rest of the session.

---

## 1. Register

| ID | Dependency | Blocks | Owner | Status |
|---|---|---|---|---|
| `DEP-01` | `ASSET_DR_CONTINUATION` `BLK-07` — normal capacity vs actual hours as the allocation denominator | `R-05`, `R-14`, `BD-P03-02`, and any SMEsPlus overhead absorption design | **Boss** | **HOLD — quoted unchanged from the Asset register** |
| `DEP-02` | `ASSET_DR_CONTINUATION` `BLK-08` — planned vs unplanned maintenance split | `R-07`, `R-08` — "normal" scrap is undefined without it | **Boss** | **HOLD — quoted unchanged** |
| `DEP-03` | COGS track terminal HOLD; `JT-01/04/05` NOT DECIDABLE | The COGS end of `01` link 14 | COGS track | HOLD, inherited |
| `DEP-04` | The running system's installed-module list — Asset `Q-04`, priority 1 | **Caps every negative claim in `02` §3, `11` §3 and `12` §4** | UAT | **HOLD — UAT REQUIRED** |
| `DEP-05` | Multi-tenant conformance of `DC-11` and the WIP wizard's company handling | Whether these are new invariant breaches or instances of known ones | Inventory MTI conformance track | **EVIDENCE REQUIRED** |
| `DEP-06` | `OWN-03` — treatment of a subcontract bill/receipt price difference for FIFO/average products | Completeness of `CC-05` | **P01 peer** | **EVIDENCE REQUIRED — peer** |
| `DEP-07` | Reconciliation of absorbed labour to posted payroll | `OWN-11`; the labour rate variance in `10` §2 | HR/Payroll + Core Accounting | **NO EVIDENCE FOUND — PATTERN NOT MECHANICAL** (AAS-03 `C-06`) |
| `DEP-08` | Routing of the joint / co-product cost model — `P03-GAP-02` | `CC-18`, `OWN-07` | **Boss** | **FINAL-GATE DECISION REQUIRED** |
| `DEP-09` | Admission of manufacturing to the target process and specification baseline — `P03-GAP-01` | `UNR-P03-03`, and P03's ability to state a performance budget | **Boss / PMO** | **FINAL-GATE DECISION REQUIRED** |
| `DEP-10` | `BD-P03-01` — does SMEsPlus recognise manufacturing variance? | `AE-13`, `10` §6 | **Boss** | **BOSS CONTROLLED DECISION** |
| `DEP-11` | Cross-process reconciliation of the scope determinations in `18` §3 | Whether P03's `TENANT` candidates bind P01–P10 | **P11** | **PEER DEPENDENCY OPEN** |
| `DEP-12` | `SCOPE-Q-01` … `SCOPE-Q-03` — `18` §5 | `R-15`; the tenant/company split of analytic and taxonomy objects | P11 + business semantics | **HOLD — SCOPE EVIDENCE REQUIRED** |
| `DEP-13` | **`SCOPE-02` / P04 `P04-B-35`** — count of work centres with no company | Closes the work-centre scope defect assigned to P03 by P04 | UAT runtime count | **HOLD — UAT REQUIRED**, one query |
| `DEP-14` | Incidence of `DC-14` — do the work-centre and project analytic distributions resolve to a common account in the target configuration? | Magnitude of the analytic double distribution, not its existence | UAT / configuration | **UNRESOLVED** — `UNR-P03-05` |
| `DEP-15` | Reachability of a second labour relief post — `DC-15` | Whether the missing idempotence marker is exploitable | Runtime tracing | **UNRESOLVED** — `UNR-P03-06` |

## 2. Dependencies P03 deliberately did **not** attempt to close

`smeplus-session-execution-pattern` forbids a session adjudicating between two parallel
evidence tracks. The following were within reach of P03's evidence and were left alone:

| Item | Why P03 stopped |
|---|---|
| `BLK-07`, `BLK-08` | Asset-owned, Boss-decision class. P03 added one supporting observation to `BLK-07` (`04` §6) and no recommendation |
| `UNR-C-03` — standard-cost TAS 2 compliance | P03 supplies the mechanism (`10` §4) to the Asset register; the question stays open there |
| `CTR-C-06` — the inert rate snapshot | P03 **confirms** it independently (`04` §3). Confirming is not closing; the Asset register's status is unchanged |
| Inventory valuation behaviour | Owned by the Inventory lineage and its rulings |
| Anything in P01 or P02 | Peers were running concurrently. No peer output was read |

## 3. What would change P03's conclusions

Stated so the package can be falsified rather than merely believed:

| If this were established | These findings change |
|---|---|
| The running system installs modules outside the scope in `02` §3 that inject overhead cost | `CC-07` … `CC-14` and `02` §2 would need re-running. **`DEP-04` closes this** |
| `_get_duration_expected` scales setup and cleanup with quantity | `UNR-P03-02` in `09` §4 dissolves |
| The Project bridge is installed in the target configuration | `DC-10` becomes inert rather than a finding |
| Multi-operator work orders are not used | `DC-01`'s **scale** falls to zero; **the design contradiction remains** |

The last row is deliberate. `DC-01` is a contradiction between two modules' treatment of the
same quantity. Its financial impact is configuration-dependent; its status as a design
defect is not.

## 4. No repeated questions

Per the Execution Constitution, no question in this register repeats one already asked by a
prior session without material delta. `DEP-01` … `DEP-04` are **quotations** of open items
from the Asset, COGS and Inventory registers, carried forward with their status unchanged
and their P03-side consequence stated. They are not re-askings.
