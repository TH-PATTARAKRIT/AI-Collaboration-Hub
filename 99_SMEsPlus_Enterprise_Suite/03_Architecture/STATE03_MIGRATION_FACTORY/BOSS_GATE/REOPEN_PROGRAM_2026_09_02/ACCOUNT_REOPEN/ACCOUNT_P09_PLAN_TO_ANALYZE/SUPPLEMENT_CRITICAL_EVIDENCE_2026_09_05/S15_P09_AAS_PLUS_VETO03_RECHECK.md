# S15 — P09_AAS_PLUS_VETO03_RECHECK

**Checkpoint:** `CP-P09S15` · **Layer:** 1 — clean-room.

---

## 1. THE AUTHORITATIVE WORDING, RETRIEVED NOT INFERRED

Read from the AAS+ consolidation at the baseline commit:

> **`AAS+-VETO-03`** — *no SMEsPlus asset, accrual, deferred-recognition or cash-basis design may allocate a balance-sheet row into the management ledger.*
> **Grounds:** verified in source, verified in deployed data at 98.57 %, and contrary to the reference product's own declared margin-ledger intent.
> **Scope:** design adoption only.

## 2. THE FOUR TESTS THE DIRECTIVE REQUIRES

| Test | Result |
|---|---|
| **does the TH-F-01 retraction affect it?** | **No.** The veto never rested on TH-F-01 — it was raised on the source mechanism, the measured annihilation, and the declared intent. All three survive. The retraction removes a *localization* claim the veto does not use |
| **does the denominator correction affect it?** | **No.** The veto is about a **design rule**, not a count. Whether the writes number 45, 82 or 83 lexical matches does not change whether a balance-sheet row should be allocated |
| **does the zeroing / double-counting evidence affect it?** | **Yes — it strengthens it.** The zeroing is now measured in deployed data; the double-count is confirmed as a distinct mechanism; and `S11` shows the two can conceal each other in a single cost-centre figure |
| **does the version-basis defect affect it?** | **Yes, and decisively — it strengthens it further.** See §3 |

## 3. THE VERSION FINDING MAKES THE VETO MORE NECESSARY, NOT LESS

The veto's original grounds assumed the consequence was confined to net-balance surfaces, because the version-18 budget gate excludes balance-sheet accounts.

**In the version-19 build the project actually ships, that gate explicitly admits fixed, current and non-current asset types.** The protection the veto's scope statement implicitly relied on **does not exist on the target platform**.

> **A design that allocates a balance-sheet row is worse on the shipping version than on the version the veto was written against.**

## 4. ONE THING THAT WOULD HAVE WEAKENED IT — AND DOES NOT

The cash-basis reclassification (`S08`) establishes that for **that** mechanism the cancellation is arguably **required**, because the cost was already attributed by the originating document. That is a genuine counter-example to a naive reading of the veto.

**It does not weaken the veto**, because the veto forbids *allocating a balance-sheet row into the management ledger* — and the correct treatment of the cash-basis case is **not to allocate either leg**, which the veto already implies. **The counter-example argues for the veto, not against it.**

**The veto's wording is nonetheless refined for the record:** it should be read as *"…may allocate a balance-sheet row into the management ledger, or rely on cancellation to neutralise one that was allocated."* Cancellation-as-a-design is the failure mode the cash-basis case exhibits.

## 5. FINAL STATUS — EXACTLY ONE

> ## **`VETO STRENGTHENED`**

Grounds added since it was raised: the annihilation is measured in a live deployment; the shipping platform version **removes** the surface protection the original grounds assumed; and a second, independent mechanism can conceal the first in the same figure.

**Scope unchanged: design adoption only.** It blocks no research, no peer process, and no Boss decision.

## CHECKPOINT
**`CP-P09S15` — COMPLETE — EVIDENCE VERIFIED.** Auto-continue.
