# P10 — BUSINESS EVENT REGISTER

Session: `SMEPLUS-26-09-05-ACC-P10-TBR-DECISION-INTEGRITY-EVIDENCE-REPAIR-001` · Layer 1

A **business event** is something that happens in the business. It is not an accounting entry, and it is not a recognition event. This register exists so that the three are not conflated — the conflation of the last two is P10's root-cause finding.

---

| ID | Business event | Scope | Producer | Does it create a recognition obligation? | Class |
|----|----------------|-------|----------|------------------------------------------|-------|
| `BE-01` | A service is contracted for a period | **TENANT** — a customer/contract fact | `P02` | Yes — it establishes the window | FACT VERIFIED |
| `BE-02` | A service is purchased for a period | **TENANT** | `P01` | Yes | FACT VERIFIED |
| `BE-03` | A customer is invoiced in advance | **COMPANY** | `P02` | Yes — it establishes the base | FACT VERIFIED |
| `BE-04` | A supplier invoices in advance | **COMPANY** | `P01` | Yes | FACT VERIFIED |
| `BE-05` | Time passes across a period boundary | **PLATFORM** — it happens to everyone | none | **Yes — this is the defining P10 event** | FACT VERIFIED |
| `BE-06` | Goods or services are delivered but not yet invoiced | **COMPANY** | `P01`/`P02` | Yes — an accrual obligation | FACT VERIFIED |
| `BE-07` | An asset is acquired and capitalised | **COMPANY** | `P04` | Yes — a depreciation obligation | FACT VERIFIED |
| `BE-08` | A contract is modified mid-term | **TENANT** | `P01`/`P02` | Yes — it changes an in-flight schedule | FACT VERIFIED |
| `BE-09` | A contract is cancelled mid-term | **TENANT** | `P01`/`P02` | Yes | FACT VERIFIED |
| `BE-10` | A period is closed | **COMPANY** | `P08` | No — but it **constrains** the posting of recognition | FACT VERIFIED |
| `BE-11` | A closed period is reopened | **COMPANY** | `P08` | Undetermined — no mechanism re-derives suppressed recognition | SUPPORTED INTERPRETATION |
| `BE-12` | A document's date is edited upstream | **COMPANY** | `P01` and others | **No obligation — but it silently mutates an existing recognition period.** The lock-free path | FACT VERIFIED (peer-sourced, corroborated) |

**`BE-05` is the event P10 exists for**, and it is the only one in the register with no producer: nothing in the business causes it and no document records it. That is why recognition needs a schedule and why its events have no natural anchor — a fact the anchor forensic reaches from the other direction.

**`BE-12` is the one that should not be in this register at all.** A clerical edit is not a business event with an accounting consequence, and it produces one. It is recorded here because leaving it out would hide it.
