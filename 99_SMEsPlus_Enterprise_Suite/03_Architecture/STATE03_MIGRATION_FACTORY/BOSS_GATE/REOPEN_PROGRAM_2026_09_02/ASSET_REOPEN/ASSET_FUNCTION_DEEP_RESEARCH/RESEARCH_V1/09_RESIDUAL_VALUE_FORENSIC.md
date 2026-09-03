# 09 — Residual Value Forensic

Session: `SMEPLUS-26-09-03-ASSET-FUNCTION-DR-001` | Status: `EVIDENCE COLLECTION`

---

## 1. Scope

Per governing brief research object 07: does residual/not-depreciable value stay in book value, is it ever depreciated, what happens at full depreciation and at disposal, how is gain/loss on disposal computed. Reference-ERP behavior and IAS/TAS 16 principle are evaluated **separately**, not conflated, per instruction.

## 2. Reference-ERP Behavior

| Question | Evidence | Classification |
|---|---|---|
| Is residual value ever depreciated? | No. Documented formula: Depreciable Value = Original Value − Not Depreciable Value. The Not Depreciable Value is structurally excluded from the depreciation schedule's base from the start, not merely "left as a remainder at the end." | `FACT VERIFIED` |
| Does it stay in book value throughout the schedule and at the end? | Yes, by construction: since it was never part of the depreciable base, the asset's book value can never fall below it through ordinary scheduled depreciation. At full depreciation, book value = Not Depreciable Value exactly. | `FACT VERIFIED` (as a logical consequence of the documented formula) |
| What happens at disposal? | Documented generally: disposal generates an accounting entry recognizing the difference between disposal proceeds and remaining book value as a gain or loss. Exact posting mechanics (which accounts, whether the Not Depreciable Value portion is treated any differently from the depreciated portion in the gain/loss calculation) were not independently quoted in this session's retrieval. | `SUPPORTED INTERPRETATION` (existence of gain/loss-on-disposal mechanism) / `UNRESOLVED / EVIDENCE REQUIRED` (exact computation detail) |
| How is gain/loss on disposal computed (formula)? | Not independently quoted with a worked formula in this session's retrieval. The general accounting identity (Gain/Loss = Disposal Proceeds − Book Value at disposal date) is a standard accounting formula, not something unique to the reference ERP's documentation — this file does not claim the reference ERP invented it, only that it was not directly quoted from reference-ERP documentation in this session. | `UNRESOLVED / EVIDENCE REQUIRED` (reference-ERP-specific confirmation) |

## 3. IAS/TAS 16 Principle (Independent of Reference-ERP Behavior)

- IAS 16 (directly retrieved): the depreciable amount is defined as cost (or revalued amount) **less residual value**. Residual value is explicitly excluded from the amount depreciated — this is the accounting-standard-level rule, independently of any software implementation, and it matches the reference-ERP's documented mechanism in §2 (both exclude residual value from the depreciable base). This convergence is evidence the reference ERP's documented mechanism is a reasonable, standards-consistent implementation of the general principle — not evidence that the standard was derived from or requires exactly this software's mechanics.
- IAS 16 requires residual value and useful life to be **reviewed at least at each financial year-end**, with changes treated as a change in accounting estimate (prospective, not retrospective). This is a standards-level requirement not confirmed as a reference-ERP feature in this session — no documentation page located describing a "review and revise residual value" workflow distinct from the general "Modify Depreciation" action (file `07`). `UNRESOLVED / EVIDENCE REQUIRED` on whether the reference ERP's Modify action is positioned as fulfilling this annual-review requirement or is a separate, more general-purpose tool.
- Gain/loss on disposal under IAS 16 is defined as the difference between net disposal proceeds and the carrying amount — matching the general accounting identity referenced in §2, and recognized in profit or loss (not treated as revenue).

## 4. Full Depreciation and Disposal — Combined Reading

At full depreciation (before disposal), book value = residual/not-depreciable value, both under the reference ERP's documented mechanism and under IAS 16 principle — these converge. At **disposal**, book value (whatever it is at that date, whether fully depreciated to residual or still mid-schedule) is compared to proceeds to compute gain/loss — this is standards-consistent and plausible for the reference ERP, but not independently reference-ERP-confirmed in mechanism detail (§2).

## 5. SMEsPlus Candidate Semantics (Layer C)

`DESIGN CANDIDATE`: SMEsPlus should adopt the residual-value-excluded-from-depreciable-base pattern, since it is convergently evidenced by both the reference-ERP mechanism (`FACT VERIFIED`) and IAS 16 principle (`FACT VERIFIED`, standards-level) — this is one of the few items in this package with double-sourced confidence. Gain/loss-on-disposal computation should follow the standard accounting identity (proceeds − carrying value), which is a general accounting fact independent of any single system's implementation, not something requiring reference-ERP adaptation.

---

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
