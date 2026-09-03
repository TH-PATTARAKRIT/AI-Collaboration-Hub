# 18 — Event-to-GL Matrix

Session: `SMEPLUS-26-09-03-ASSET-FUNCTION-DR-001` | Status: `CONSOLIDATED MATRIX`

---

Columns per governing brief: Business Event | Source Module | Financial Event | Debit | Credit | Off-Balance | Production Cost Effect | Evidence. No SMEsPlus account codes are prescribed anywhere in this file — Debit/Credit columns name account *concepts*, consistent with clean-room rule #4.

| Business Event | Source Module | Financial Event | Debit | Credit | Off-Balance | Production Cost Effect | Evidence |
|---|---|---|---|---|---|---|---|
| Asset acquired via qualifying vendor bill | Asset / Vendor Bill | Capitalization | Fixed Asset (concept) | Accounts Payable / Bank | No | None at acquisition | `SUPPORTED INTERPRETATION` — file `05` §2 |
| Scheduled depreciation entry posted | Asset Model / Asset | Periodic expense recognition | Depreciation Expense (concept) | Accumulated Depreciation (concept) | No | Only if depreciation is separately routed into overhead/WIP — not confirmed as automatic (file `12`) | `FACT VERIFIED` (mechanism exists) / `UNRESOLVED` (production-cost linkage) — file `07`, `12` |
| Asset modified (value increase) | Asset | Value adjustment | Fixed Asset (concept) | Depreciation Expense / Accumulated Depreciation (unconfirmed exact pairing) | No | Prospective schedule change only | `SUPPORTED INTERPRETATION` — file `07` §2 |
| Asset modified (value decrease) | Asset | Value adjustment | Depreciation Expense (concept, per documentation: "posts a new Journal Entry for the Value Decrease") | Fixed Asset / Accumulated Depreciation (unconfirmed exact pairing) | No | Prospective schedule change only | `FACT VERIFIED` (that an entry posts) / `UNRESOLVED` (exact account pairing) — file `07` §2 |
| Asset disposed, proceeds > book value (gain) | Asset | Derecognition | Cash/Bank + Accumulated Depreciation (concepts) | Fixed Asset + Gain on Disposal (concepts) | No | None (statutory), unless a Hypothesis-C-style off-balance charge was separately running (file `10`) | `SUPPORTED INTERPRETATION` — file `09` §2 |
| Asset disposed, proceeds < book value (loss) | Asset | Derecognition | Cash/Bank + Accumulated Depreciation + Loss on Disposal (concepts) | Fixed Asset (concept) | No | Same as above | `SUPPORTED INTERPRETATION` — file `09` §2 |
| Equipment created (no Asset link) | Maintenance | Operational record only, no financial event | n/a | n/a | n/a | None documented | `FACT VERIFIED` (no financial event triggered) — file `04` |
| Maintenance Request raised/completed | Maintenance | Not confirmed to generate a financial event by itself; any related spare-part purchase would post via ordinary vendor-bill accounting, independently | Ordinary expense/asset account per the purchase, not per the maintenance request | Accounts Payable / Bank | No | Not confirmed to affect production cost (file `06`) | `CONTRADICTED` (of an automatic maintenance→GL/production-cost event) — file `06` |
| Fully depreciated asset continues in productive use | Asset / Equipment | No statutory financial event (depreciation has stopped, per IAS 16) | n/a (statutory) | n/a (statutory) | Yes, if Hypothesis C / post-depreciation formula (file `13`) is adopted: Dr Internal Equipment Usage Cost | Cr Internal Equipment Usage Offset (both Off-Balance, candidate) | Internal/management visibility only, no statutory production-cost effect | `FACT VERIFIED` (no statutory event) / `DESIGN CANDIDATE` (off-balance event) — file `10`, `13`, `14` |
| Work center operation performed (labor/machine-time) | Manufacturing | Cost absorption into operation/MO cost | WIP (concept) | Work Center Cost absorption / labor clearing (concept, not independently re-verified fresh this session) | No | Direct — rate × duration, documented mechanism | `FACT VERIFIED` (mechanism, file `12`) / `SUPPORTED INTERPRETATION` (exact GL pairing, carried context) |
| Depreciation notionally attributed to Work Center (Hypothesis A, if adopted) | Asset↔Work Center (candidate link) | No reference-ERP precedent; would require new mechanism | Depends entirely on SMEsPlus design choice — not evidenced | Depends entirely on SMEsPlus design choice — not evidenced | Possibly, depending on whether SMEsPlus treats it as statutory overhead absorption (real GL) or internal-only (off-balance) — an open design question this file does not resolve | Would be direct if implemented, per Hypothesis A's own premise | `CONTRADICTED` (of existing mechanism) / `DESIGN CANDIDATE` (if built) — file `11`, `21` |

---

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
