# 31 — COGS-to-Inventory Handoff Contract Candidates

Session: `SMEPLUS-26-09-02-COGS-DR-001` | Jira: `ERPPLUS-142` | Control Level: `/L9999.9999`
Status: `CANDIDATE CONTRACTS ONLY — NOT REVIEWED, NOT RECONCILED WITH INVENTORY, NOT APPROVED — PREPARATION FOR JOINT CROSS-PROOF`

---

## 1. Purpose and Standing

Governing prompt §19 requires this research to end with candidate contracts sufficient for a later Joint Cross-Proof session — not a final interface. Every clause below is built to map cleanly onto the Inventory Final Solution v1.0 handoff register (`10_INVENTORY_CROSS_MODULE_HANDOFF_V1.md`, rows `HX-01`–`HX-31`) rather than inventing a second, conflicting vocabulary, per the instruction in file `01` §3.4. Every clause is explicitly conditioned on one or more still-open Joint decisions (`JT-01`–`JT-12`) and is not itself a resolution of any of them.

These contracts are candidates for the **Boss-approved 22-Scenario Accounting × Inventory Cross-Proof baseline** (commit `296b495`) and the **16-field Inventory → Accounting Minimum Handoff Data Contract** (commit `d9e845e`) to test against — they do not amend either of those Boss-approved artifacts, and neither is re-opened here.

---

## 2. Foundational Rule Restated

**Inventory emits facts; Accounting decides postings.** Every clause below describes what Accounting requires *of* a fact Inventory emits, never a posting Inventory itself performs. Where a clause says "Inventory must emit X," it is stating an input requirement on the existing `HX-*` handoff rows, not proposing a new Inventory-side design.

---

## 3. Contract A — Inventory Cost Contract

**Governs:** what costs may enter Inventory Value, when, under which policy/version, and with which evidence.

| Clause | Statement | Evidence Base | Conditioned On |
|---|---|---|---|
| `A-01` | A cost may enter Inventory Value only via a named, evidenced event class: purchase receipt (`HX-07`), landed-cost allocation (`HX-14`), inventory adjustment gain (`HX-11`), manufacturing output (`HX-19`/`HX-20`), or a certified opening-balance fact (`HX-24`). No other event class may silently increase Inventory Value. | File `16` Scenarios 1, 2, 9, 21, 27–29; file `27` Identity 2 | `JT-01`, `JT-08`, `JT-09`, `JT-11` |
| `A-02` | The cost basis applied at receipt is the policy-defined basis in force at that moment (Standard/AVCO/FIFO/Specific Identification per `JT-02`) — never a value invented after the fact to make a later reconciliation balance. | File `15` (all four methods); file `28` V-9 (no fabricated cost) | `JT-02` |
| `A-03` | Landed cost may capitalize into Inventory Value only for the portion of quantity still on hand at allocation time; the portion attributable to already-released quantity must route to a cost-release event (Contract B), never remain a phantom addition to Inventory Value with no stock behind it. | File `21` §3.3 (`LC-03`); file `16` Scenario 10 | `JT-08` |
| `A-04` | Where the receiving policy uses a fixed planned cost (Standard Cost), a vendor-bill price variance is a variance question, never a silent cost-basis edit — `LC-04`'s principle, independently corroborated by the reference ERP's own Price Difference Account mechanism. | File `21` §4.2; `LC-04` (Inventory Final Solution v1.0, file 08) | `JT-02` |
| `A-05` | Recoverable input VAT must not be capitalized into Inventory Value if Thai rules so require — `AUTHORITATIVE`, per TAS 2's cost-of-purchase clause (net of amounts subsequently recoverable from the tax authority). Import duty, being non-recoverable, is includible. | File `24` §2.1, §2.6 (`AUTHORITATIVE`) | `TH-HOLD-03` (materially advanced, not fully closed) |
| `A-06` | A cost-method change (Standard/AVCO/FIFO) does not retroactively rebase existing on-hand Inventory Value — confirmed only in the direction of moving away from Standard Cost; the reverse and lateral directions remain `HOLD`. | File `15` §7 | `JT-02`, `CGS-U29` |
| `A-07` | Manufacturing raw-material consumption and WIP completion are cost *transfers within* Inventory Value (raw material → WIP → finished goods), never a Cost Release event — only the eventual sale of the finished good releases cost. | File `22` §5.1–§5.2; file `27` §4.2 | `JT-09`, `GAP-FS-19` (Manufacturing scope, Boss-owned) |
| `A-08` | A migrated/certified opening Inventory Value is subject to the same evidentiary bar as an ordinary period-1 opening count (Contract with `HX-24`); it is a balance-sheet carrying amount, never a source from which pre-cutover COGS can be recomputed. | File `26` §4; file `01` §3.2 | `JT-11`/`G-5` |

---

## 4. Contract B — COGS Recognition Contract

**Governs:** when and how Inventory Value is released into COGS or another approved financial classification, including revenue/physical/invoice timing differences.

| Clause | Statement | Evidence Base | Conditioned On |
|---|---|---|---|
| `B-01` | Every Inventory Value release must resolve to exactly one of a closed set of approved classifications: COGS (sale), Inventory Loss/Adjustment (scrap, shrinkage, count loss), a WIP/production transfer (Contract A `A-07`), or a Joint-approved valuation adjustment (write-down/NRV) — never an undifferentiated "inventory decrease." This is the direct operational form of Reconciliation Identity 3 (`VERIFIED` as a governing constraint, file `27` §4). | File `16` (all 32 scenarios); file `20` §2 master decision table; file `27` §4 | `JT-01` (classification-rule-set ownership, still `HOLD`) |
| `B-02` | The triggering event for COGS recognition — physical dispatch, or customer invoice posting — is **not** settled by reference-ERP evidence and must be decided independently by SMEsPlus. Reference evidence itself is internally unstable on this point across its own version history (pre-19 `PROVISIONAL`, tied to invoicing but with unresolved exact timing; 19.0+ unambiguously invoice-triggered; Periodic/Continental has no per-transaction trigger at all). | Files `12`, `13`, `14`, `18` (the package's single most cross-corroborated finding, `CGS-U01`) | `JT-04` — **not resolvable by this contract; decision required** |
| `B-03` | Under a Periodic-style policy, if adopted, COGS must never be computed as an undifferentiated residual (`Opening + Purchases − Closing`) without first separately identifying and removing non-COGS releases (scrap, loss, write-down, adjustment) — the naive formula silently mislabels every non-sale reduction as COGS. | File `27` §5.2 (the single most material correction this research produced); file `16` Scenarios 21–24 | `JT-01`; requires SMEsPlus to actually provenance non-COGS releases at `HX-11`/`HX-12` granularity |
| `B-04` | A manufactured finished good's COGS release follows the identical recognition-timing rule as a purchased product — manufacturing introduces no separate, parallel COGS-timing rule of its own. | File `22` §5.3 | `JT-04`, `JT-09` |
| `B-05` | Revenue recognition (Income Account) and cost recognition (Expense/COGS) are evidenced as independently-timed axes in the reference ERP, not a single coupled event, under at least one configuration (Periodic) — SMEsPlus must decide explicitly whether it wants them coupled or independently timed, not inherit either answer by default. | File `12` §4.4; file `04` field `B-03` vs. `B-04` | `JT-04` |
| `B-06` | Recognition of the inventory carrying amount as an expense when related revenue is recognized is `AUTHORITATIVE` under Thai TAS 2 — this is the statutory floor `JT-04` must satisfy, whatever event SMEsPlus ultimately selects as the trigger. | File `24` §2.4 (`AUTHORITATIVE`) | `JT-04` — this is a constraint on the decision, not the decision itself |

---

## 5. Contract C — Cost Reversal / Adjustment Contract

**Governs:** how returns, cancellations, correction, late cost, landed cost, write-down, scrap, manufacturing variance, and period-close adjustments preserve original-event linkage and avoid duplicate financial effects.

| Clause | Statement | Evidence Base | Conditioned On |
|---|---|---|---|
| `C-01` | Every reversal, correction, or adjustment fact must carry a mandatory reference to the original cost-release or receipt fact it reverses. A claimed "return" with no resolvable original-fact reference must be rejected as a return at the Inventory-fact layer and, if justified, re-entered as an adjustment instead — never silently accepted with an assumed or fabricated original cost. | File `19` §9; `HX-10` | `JT-05`/`C-03` |
| `C-02` | Post-movement corrections are modeled as new, dated, referenced reversal/adjustment facts — never as an in-place mutation of a posted valuation layer or journal entry. This is the reference ERP's own consistently-observed pattern across every correction path examined (no in-place-edit path was found anywhere in the evidence reviewed), and it is adopted here as a process-shape candidate independent of how any cost-basis question is eventually resolved. | File `19` §8 | Audit VETO alignment (file `28` V-1) |
| `C-03` | The cost basis assigned to a customer return (original issue cost vs. current cost vs. a policy-defined blend) is the single most material open item this entire research package carries forward — the reference ERP's own evidence is internally split (AVCO uses current cost, never recalculated; FIFO's layer behavior is only community-corroborated; a documented, unreconciled discrepancy exists between credit-note amount and inventory-value reversal). Accounting, not Inventory, must decide the basis; Inventory supplies the linked reference (`HX-10`) and nothing more. | File `19` §2, §6, §11; `CGS-U32` | `JT-05`/`C-03` — **not resolvable by this contract; decision required** |
| `C-04` | A cancellation before any physical movement is a no-financial-effect event by definition, because no valuation fact was ever emitted for it to reverse — this holds regardless of how `JT-05` is eventually decided. | File `19` §7 | none — low-materiality, stated for completeness |
| `C-05` | A landed cost or price-difference amount arriving after the affected stock is fully released must never be silently absorbed into a phantom cost basis with no stock behind it — it must route to an explicit, Accounting-decided classification (candidate: COGS-type expense, or a clearing/suspense account pending reconciliation). Reference evidence is `CONFLICTING` on which of these two the reference ERP itself uses, and in at least one reported case, generates no journal entry at all — a control break this contract explicitly does not inherit. | File `21` §3.3; `CGS-U34`, `CGS-U36` | `JT-08`, `JT-04` |
| `C-06` | Where physical and financial timing differ at a period boundary (unbilled receipt, uninvoiced delivery), the reconciling mechanism is an Accounting-owned closing procedure that consumes Inventory facts (`HX-17`) — it is not a byproduct the Inventory-side movement-date guard produces on its own. The guard controls *when a fact may be dated*; it does not by itself supply the population-query surface, late-cost period authority, or closing-snapshot content Accounting still needs. | File `23` §5.2 (GAP-1/GAP-2/GAP-3) | `JT-06`, `JT-07` |
| `C-07` | A migration/opening replay must never originate a COGS posting — only an Inventory Asset (and matched suspense/equity-side) posting. Any COGS-labelled amount appearing in a migration context is either a carried, static comparative figure from the legacy system, or a defect — never a legitimate migration-time recognition event. | File `26` §4, §10 | `JT-11`/`G-5`, `GAP-FS-08` |
| `C-08` | A posting-level idempotency key, distinct from any Inventory movement-fact-level key, is required for every migration/opening/closing posting, because the unit of posting (an aggregate period entry under a Periodic-style policy) does not share cardinality with the unit of fact (a single movement) — Inventory-side fact idempotency does not, by itself, guarantee Accounting-side posting idempotency. | File `26` §5.1 (`AC-01`–`AC-04`) | `GAP-FS-08`; independent of how `T-1` is eventually ruled |
| `C-09` | Whatever triggers a reversal, correction, or migration posting — a human-run action, a scheduled job, or an AI-assisted tool — the reference-linkage requirement (`C-01`), the no-in-place-mutation rule (`C-02`), and the posting-level idempotency key (`C-08`) apply identically. No automated or AI-assisted path may be held to a weaker duplicate-effect standard than a human-run one. | File `26` §10; file `28` V-9 | AI Control/Human Oversight VETO alignment |

---

## 6. Explicit Non-Closures

These contracts close none of the following, which remain exactly as open as they were entering this session:

| Joint ID | Status |
|---|---|
| `JT-01` (valuation policy ownership) | Open — every contract clause above conditions on it without resolving it |
| `JT-02` (permitted costing methods & change rules) | Open |
| `JT-03` (continuous vs. periodic timing) | Open — `CGS-U01` is direct evidence it cannot be resolved by adopting reference behavior |
| `JT-04` (COGS recognition timing) | Open — `B-02` names this the contract's single largest unresolved fork |
| `JT-05`/`C-03` (return cost basis) | Open — `C-03` names this the package's single most material carried item |
| `JT-06` (late supplier bill after close) | Open |
| `JT-07` (period close design) | Open |
| `JT-08` (landed-cost eligibility/posting) | Open |
| `JT-09` (WIP recognition timing) | Open |
| `JT-10` (inter-company transfer treatment) | Open — corroborated, not reopened, by file `25` §2.7 |
| `JT-11`/`G-5` (opening-balance certification) | Open |
| `JT-12` (period lock policy) | Open |

---

## 7. Reconciliation With the Existing Handoff Register (`HX-*`)

| `HX-*` Row (Inventory Final Solution v1.0) | This Session's Contract Clause(s) |
|---|---|
| `HX-07` (receipt valuation fact) | `A-01`, `A-02` |
| `HX-08` (supplier bill price vs. receipt cost basis) | `A-04`, `C-05` |
| `HX-09` (issue/COGS fact) | `B-01`, `B-02` |
| `HX-10` (return facts) | `C-01`, `C-03` |
| `HX-11` (adjustment fact) | `B-03` |
| `HX-12` (scrap fact + destruction evidence) | `B-01`, `B-03` |
| `HX-13`/`HX-14` (landed cost bills / allocation) | `A-03`, `C-05` |
| `HX-15` (valuation policy) | `A-02`, `A-06` |
| `HX-16` (period lock) | `C-06` |
| `HX-17` (close valuation summary) | `C-06` |
| `HX-19`/`HX-20` (manufacturing consumption/output) | `A-07`, `B-04` |
| `HX-22` (inter-company transfer, two facts) | Corroborated (file `25` §2.7), not amended |
| `HX-24` (certified opening balances) | `A-08`, `C-07` |

No new `HX-*` row is proposed by this file. Every clause above is expressed as a requirement *on* an existing row, consistent with the instruction not to invent a second vocabulary.

---

## 8. Terminal Statement

These three contracts are candidates only. They are offered to the future Joint Accounting ↔ Inventory Cross-Proof session as a starting evidence base, tested where this research had evidence and honestly marked `HOLD` where it did not. No contract clause is approved, no Joint decision is closed, and no team is authorized to build against any clause above without a Joint session ratifying it first.

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
