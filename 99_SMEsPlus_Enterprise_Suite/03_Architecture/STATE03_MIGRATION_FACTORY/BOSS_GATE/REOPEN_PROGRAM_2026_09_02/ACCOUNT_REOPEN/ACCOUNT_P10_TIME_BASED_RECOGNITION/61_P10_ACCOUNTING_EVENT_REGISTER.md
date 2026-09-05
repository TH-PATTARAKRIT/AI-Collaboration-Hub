# P10 — ACCOUNTING EVENT REGISTER

Session: `SMEPLUS-26-09-05-ACC-P10-TBR-DECISION-INTEGRITY-EVIDENCE-REPAIR-001` · Layer 1

An **accounting event** is the decision that something must be recognised. It sits between the business event and the journal entry.

> **The governing fact for this whole register:** the peer that owns the ledger has established, at class **`A VERIFIED ABSENCE over its declared 22-root set`**, that **no accounting-event object exists**. P10 independently confirms none exists within its own declared reference root. **So every row below is a *conceptual* accounting event with no object to carry it.**

---

| ID | Accounting event | Triggered by | Recognition event produced | Object that carries it today | Class |
|----|------------------|--------------|----------------------------|------------------------------|-------|
| `AE-01` | An invoiced amount is deferred | `BE-03`/`BE-04` posting | One full-deferral event | **none** — two dates on a journal item | FACT VERIFIED |
| `AE-02` | A period's share is earned | `BE-05` | One recognition event per period | **none** | FACT VERIFIED |
| `AE-03` | An uninvoiced position is estimated | operator decision on `BE-06` | One accrual event | **none** — a transient wizard | FACT VERIFIED |
| `AE-04` | The estimate is superseded | the real invoice arriving | **none produced** — the reversal is pre-committed and unconditional | link to the accrual entry only | FACT VERIFIED |
| `AE-05` | Asset service potential is consumed | `BE-05` + `BE-07` | One depreciation event per board period | **asset + period-beginning date** — the strongest anchor of the four | FACT VERIFIED |
| `AE-06` | A schedule is corrected | `BE-08` | Domain-specific: stands / re-derived / catch-up | domain object where one exists | FACT VERIFIED |
| `AE-07` | A schedule is terminated | `BE-09` | Domain-specific | domain object | FACT VERIFIED |
| `AE-08` | A recognition cannot post into its period | `BE-10` | **None. The event is silently replaced by a different posting date** | nothing records it | FACT VERIFIED |
| `AE-09` | A recognition period is mutated with no lock present | `BE-12` | **None. Nothing detects it** | nothing | FACT VERIFIED (peer-sourced) |

## The Two Rows That Are the Package

`AE-08` and `AE-09` are accounting events that **produce no recognition event and leave no record**. They are the reason `T0-13` exists, and the reason `P10-D-02` is a decision rather than a defect report.

## Anchor Grades — corrected

| Mechanism | Anchor today |
|-----------|--------------|
| Loan amortisation | **line-level** — the entry resolves to one schedule row |
| Asset depreciation | **object + period** |
| Deferral, both paths | **move-set level** — the anchor set is carried, including on the grouped path |
| Accrual | **none** |

Anchoring is **graduated, not binary.** Only the accrual has none. This corrects an earlier P10 statement that three of eight had no anchor, and it matters because it makes retrofitting an identity **more** available than P10 first claimed.
