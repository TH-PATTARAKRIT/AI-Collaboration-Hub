# P11 — UNIFIED CONTRADICTION REGISTER

Session `SMEPLUS-26-09-04-ACC-P11-CORE-RECON-REV2-001` · Layer 1 clean-room

> **Recommendation only. Boss is the sole Final Approver.**
> Per `EC-05`, every material contradiction is dispositioned with traceable lineage. **No material
> contradiction may remain merely as an unresolved difference of opinion.**

---

## 1. Contradictions P11 found **between** packages

These are the ones only a cross-process reconciliation can find. Each is a disagreement between two
published artefacts, not inside one.

| id | Contradiction | Package A | Package B | Disposition |
|---|---|---|---|---|
| `P11-C-01` | **The `AASR` design package's parent baseline predates the parent's own closure.** `AASR` (`7c0a3ce`, 13:57) carries no `FINAL_CLOSURE/` and no `GB08_DECISION/`; the parent `MCC` branch (`7884077`, 21:16) carries both — 15 and 10 files. `AASR` therefore designed against a baseline that did not yet include `MCU-04`'s closure as a `VERIFIED DEFECT`, the `GB-08` package, or `FC-F1`…`FC-F5` | `SL-02` | `SL-01` | **`HOLD — CONTRADICTION`.** `AASR`'s own terminal state (`PROVISIONAL / NON-CANONICAL`, `AASR-VETO-01` upheld) is **correct and self-protecting** — it declares itself unusable. But `AASR`'s `V-SYS-2` finding — *"consumed the parent's findings but not the parent's corrections"* — **now applies to `AASR` itself**, one level up. `GB-06`'s fifth instance |
| `P11-C-02` | **`RISK-COGS-01` said the COGS research had not been executed; it had.** The package exists at `a959327` with 37 deliverables and a terminal `HOLD` | Inventory v2.0 | `SL-15` | **`CLOSED — EVIDENCE VERIFIED`.** Already corrected as `R4-D-01`. Carried here because the *remedy* changed with it: re-commissioning the research would achieve nothing |
| `P11-C-03` | **`BC-02` element 10 requires company **and** tenant context on every material handoff; the corrected constitution requires only what the object's scope demands** | `BC-02` | `SMEPLUS-26-09-04-ACC-REV2-CORR1` | **`CLOSED — DESIGN RESOLUTION VERIFIED`.** All ten material Inventory→Accounting handoffs create a financial effect and are therefore `COMPANY`-scoped, where both contexts remain mandatory. **The 10-of-10 failure stands unchanged** (`RV-05`) |
| `P11-C-04` | **Wave A `TI-01` forbids any configuration having database-wide effect; the corrected constitution requires a `PLATFORM` scope that legitimately does** | `SL-01` `16` §6 | correction §2 | **`CLOSED — DESIGN RESOLUTION VERIFIED`** as `RV-01`/`SCP-02`. `SB-01`'s severity is unchanged |
| `P11-C-05` | **The programme has no declared output path.** Six sibling sessions were observed writing to **six different** package locations; this session's is a seventh | peer clones | — | **`HOLD — BOSS DECISION REQUIRED`.** See `P11-F-01` |
| `P11-C-06` | **`M-02` is auto-reversed on unmatch; `M-03` is not stated to be** — two rows of one table, read against each other | `SL-01` `08` | `SL-01` `08` | **`UNRESOLVED — EVIDENCE REQUIRED`** (`DC-07`, `SR-04`). Recorded as an **unknown**, not a defect |
| `P11-C-07` | **Inventory-to-GL agreement is asserted at the closing boundary; the subledger test `S2` asks for a stated agreement rule at a stated moment — the two are compatible only if the posture is disclosed** | `SL-07` `17` §5 area 10 | `P11_SUBLEDGER_ARCHITECTURE.md` | **`CLOSED — DESIGN RESOLUTION VERIFIED`**: the report must disclose which posture it measures. Already a non-blocked disclosure requirement in `SL-07` |

## 2. Contradictions carried from the packages, unresolved

Carried without amendment. **P11 resolves none of them and does not weaken any.**

| id | Carried contradiction | Owner | Status |
|---|---|---|---|
| `CONTRA-01a/01b` | Fiscal-year semantics | Wave A | carried |
| `CONTRA-02` | Identifier-arithmetic ceiling (`SB-02`) | Wave A | carried |
| `CONTRA-03` | — | Wave A | carried |
| `CONTRA-04` | **Generated consequences attributed to the wrong period** | Wave A + `P07` | carried; reinforced by `PC-01` |
| `CONTRA-05` | **The entry-balance invariant is switchable** (`COR-07`) | Wave A | carried; **`T0-12`, most severe open item** |
| `FC-F1` | **`MCC_00` §1 count contradicts its own §2 dispositions** — closes ten ids and counts nine | Wave A FC | **newly opened and standing open**; `MCC_00` governs by rule |
| `FC-F5` | (per `SL-01` §7 criterion 2) | Wave A FC | **newly opened and standing open** |
| `MCC_00` backlog | The 14-item correction backlog, **now ≥18** | Wave A | **uncleared** |
| `JT-02` | Price-difference account scope | Inventory ↔ `P01` | unresolved |
| `JT-08` | Three incompatible landed-cost behaviours, one a documented failure mode | Inventory | unresolved, **Audit VETO retained** |
| `RC-V-01` | Ruling-consolidation veto | Inventory MTI | carried |
| `AAS-V-02` | Condition satisfied but **not discharged** | Inventory MTI | carried |
| `AASR-VETO-01` | Independent design veto, **upheld** | Wave A AASR | carried |
| AAS+ veto on costing implementation start | `BLK-07` unresolved | Asset | **carried — no costing implementation may begin** |

## 3. Position

| Measure | Count |
|---|---|
| Contradictions found **between** packages by P11 | **7** |
| Of those, **closed** by P11 | **4** (`P11-C-02`, `P11-C-03`, `P11-C-04`, `P11-C-07`) |
| Of those, **held** | **3** (`P11-C-01`, `P11-C-05`, `P11-C-06`) |
| Contradictions **carried** unresolved from the packages | **14** |
| Contradictions **resolved** by P11 from the carried set | **0** |
| Standing vetoes across the evidence base | **4** — `AASR-VETO-01`, `RC-V-01`, `AAS-V-02`, Asset AAS+ costing veto |

**Four standing vetoes, none discharged.** A gate pack that did not say so on its own contradiction
register would be the defect the `GB-06` series exists to prevent.
