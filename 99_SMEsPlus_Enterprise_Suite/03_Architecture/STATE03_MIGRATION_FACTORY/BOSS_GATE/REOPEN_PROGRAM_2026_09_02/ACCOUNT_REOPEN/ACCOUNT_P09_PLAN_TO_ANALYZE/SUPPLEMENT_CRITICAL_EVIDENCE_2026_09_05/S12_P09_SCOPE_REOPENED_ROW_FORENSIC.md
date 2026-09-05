# S12 — P09_SCOPE_REOPENED_ROW_FORENSIC

**Checkpoint:** `CP-P09S12` · **Layer:** 1 — clean-room.

---

## 1. THE ROW

| Field | Content |
|---|---|
| **Original finding** | *"wrong company attribution — NOT REACHED BY THIS DEFECT. A symmetric pair is always within one company."* Closed on that basis |
| **The inversion relied on** | a **bare universal** with no declared boundary — the exact construction the programme's negative-claim standard forbids. It was closed because no counter-example had been looked for, and stated as though none could exist |
| **Why the closure was invalid** | a reviewer found an untested path: when an entry is mirrored into a second company, the mirror **keeps precisely the company-less axis values** and drops the company-scoped ones. Company-less axis values are the **shared, tenant-level cost objects** |
| **The consequence** | one economic event produces, on **one shared axis value**, records in **two different companies with opposite signs**. On any tenant-level view they partly cancel — while both records are individually well-formed and correct |

## 2. THE SCOPE ANALYSIS

| Scope | Determination |
|---|---|
| **ownership** | the axis value is **TENANT**-scoped where it carries no company — the reference makes the company field optional, so a shared axis value is a supported state |
| **execution** | **COMPANY** — each record is created by, and belongs to, its own posting company |
| **financial** | **COMPANY** — each company's ledger is correct and undisturbed |
| **management attribution** | **TENANT** — and this is where the failure lands. Two company-scoped records aggregate on one tenant-scoped object with no marker |
| **cross-company behaviour** | cancellation is **partial**, not full — the two amounts differ by the inter-company margin |

**The failure is a scope-boundary crossing at the *aggregation* step**, not at ownership, execution or financial scope. It is a distinct defect class from the intra-entry symmetric pair: **separate entries, separate companies, partial cancellation.**

## 3. FINAL STATUS

> **`P11 RECONCILIATION REQUIRED`**

Not `CLOSED` — the mechanism is verified but its incidence is unmeasured. Not merely `OPEN — SCOPE EVIDENCE REQUIRED` — the scope question is answered; what is unresolved is **who owns a tenant-level aggregate over company-scoped records**, and that is a cross-process determination P09 cannot make alone.

Conditions for closure: inter-company rules enabled in a real deployment **and** at least one company-less axis value appearing in a mirrored allocation. **Neither has been measured.**

## 4. WHAT THIS CHANGES IN THE PACKAGE

`AI11`'s attack matrix closed the "wrong company attribution" row. **That closure is withdrawn and the row is re-opened.** The base package's `MA-10` — no implicit widening from company scope to a wider scope — **now has a concrete witness** rather than being a precautionary rule.

## CHECKPOINT
**`CP-P09S12` — COMPLETE — EVIDENCE VERIFIED.** Row re-opened, scope decomposed, routed to P11. Auto-continue.
