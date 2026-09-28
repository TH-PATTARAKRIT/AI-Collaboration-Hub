> Domain: INVENTORY_ADJUSTMENT_VALIDATION_PILOT (Gx4) | Business Trace | Documentation-Tier

# 06 — BUSINESS RULE REGISTER (Gx4)

---

### IAV-F01 — Physical count recording

- **WHAT**: A user enters a "Counted" quantity against a product (optionally scoped by location) on the Physical Inventory page, which lists all products with stock history, including negative-quantity ones.
- **WHY**: The system-recorded quantity must be reconciled against what physically exists.
- **BUSINESS RULE**: Recording a count is a separate step from applying it — entering a number does not itself change the authoritative quantity.
- **STATE**: System quantity (unchanged) + Counted quantity (entered, pending) → applied → system quantity updated.
- **DATA CONCEPT**: A count record ties a product (and location) to both a system quantity and a counted quantity, with the difference being the adjustment.
- **CONTROL**: None described at entry time — the control is at apply time (IAV-F02).
- **DEPENDENCY**: Feeds IAV-F02.
- **EVENT**: "Count recorded" (not yet applied).
- **RISK**: A count left unapplied has no effect — a design must not assume "counted" implies "corrected."
- **UNKNOWN**: Whether a count can be recorded against a specific lot/serial vs. only aggregate product quantity — `SOURCE/RUNTIME VERIFICATION REQUIRED`.

### IAV-F02 — Applying the adjustment

- **WHAT**: Committing one or many counted quantities as the new authoritative system quantity, either one line at a time (Apply) or in bulk with a recorded reason (Apply All, after selecting lines).
- **WHY**: A discrete commit step, mirroring the "validate" pattern seen in receipts/deliveries, prevents partial/accidental commits and supports recording *why* a bulk adjustment happened.
- **BUSINESS RULE**: Bulk application is the documented way to also ensure "reasons for adjustments are recorded" — implying single-line Apply may not require/capture a reason the same way.
- **STATE**: Pending count → applied → system quantity = counted quantity.
- **DATA CONCEPT**: An adjustment reason is a first-class, at least optionally trackable data point on a bulk application.
- **CONTROL**: This is the actual Stock-Truth-changing action; per documentation, it is followed immediately by the financial effect (see IAV-F03) with "no additional steps needed."
- **DEPENDENCY**: Feeds IAV-F03 directly.
- **EVENT**: "Adjustment applied."
- **RISK**: If reason-recording is genuinely optional/inconsistent between single and bulk apply, an audit-trail design relying on "every adjustment has a reason" would be wrong.
- **UNKNOWN**: Whether single-line Apply supports a reason field at all, or only Apply All does — `SOURCE/RUNTIME VERIFICATION REQUIRED`.

### IAV-F03 — Financial posting of the adjustment

- **WHAT**: Whether/when an applied inventory adjustment creates a GL-relevant entry.
- **WHY**: Same rationale as GRV-F04/SDV-F05 — a stock-quantity change with cost attached is a financial event.
- **BUSINESS RULE — THIRD DATA POINT ON THE OPEN CONTRADICTION**: Documentation states plainly, for this specific function, that changes "update the Balance Sheet as soon as they are applied, there are no additional steps needed after applying the counts." Unlike GRV-F04/SDV-F05, this claim is **not qualified** by a "manual vs. automatic valuation" distinction in the page found this round — raising the possibility that a manual physical-count adjustment behaves differently (posts immediately, always) from an ordinary receipt/delivery (which may defer to invoice time under the Gx2 finding). This is a **hypothesis, not a resolved fact** — see `GAP-IAV-01`.
- **STATE**: Adjustment applied → (claimed) immediate Balance Sheet effect.
- **DATA CONCEPT**: Same Stock Valuation account machinery as receipts/deliveries, applied to a count-derived delta instead of a movement-derived one.
- **CONTROL**: If genuinely immediate and unconditional, this would be the one Stock-Truth-changing event in this Deep Study that does *not* wait for a separate financial-transaction trigger — structurally different from GRV-F04/SDV-F05's documented (SDV) or claimed (GRV) deferral pattern.
- **DEPENDENCY**: Depends on IAV-F02 having applied.
- **EVENT**: "Balance Sheet updated."
- **RISK**: Treating all three "valuation timing" findings (Gx1, Gx2, Gx4) as necessarily consistent with each other would be a mistake — they may correctly describe three genuinely different mechanisms (movement-triggered, invoice-triggered, count-triggered), which is itself an important design-relevant finding once confirmed.
- **UNKNOWN**: Full runtime confirmation, and specifically whether valuation mode (manual/automatic) affects this function the way it affects GRV-F04, or whether adjustment posting is unconditional regardless of that setting.

### IAV-F04 — Scrap / Inventory Loss location + Loss Account

- **WHAT**: Scrapping goods moves them to a location typed "Inventory Loss," which can carry its own dedicated **Loss Account** (documented example: a "Scrapped Goods" journal/account), distinct from the general Stock Valuation account.
- **WHY**: Businesses want scrapped/written-off inventory visible on the Profit & Loss report under its own line, not blended into ordinary stock valuation movements.
- **BUSINESS RULE**: "Scrap entries are posted based on the product category, valuation accounts, and scrap/inventory loss location" — i.e., the posting is a function of *both* the product's own category configuration *and* the destination location's configuration, not either alone.
- **STATE**: Stock (on-hand) → scrapped → Inventory Loss location, valuation entry posted against the Loss Account (if configured) or the general valuation account (if not).
- **DATA CONCEPT**: A location's "Loss Account" is optional — its absence doesn't block scrapping, it just means scrapped value doesn't get its own P&L line.
- **CONTROL**: Configuring a dedicated Loss Account is how a business gets scrap visibility; not configuring it is a valid (if less visible) alternative.
- **DEPENDENCY**: Independent of IAV-F01/F02 — scrap is its own action, not a physical-count adjustment.
- **EVENT**: "Goods scrapped," "Loss recognized" (if Loss Account configured).
- **RISK**: A design treating "adjustment" and "scrap" as the same accounting event would miss this dedicated-account distinction.
- **UNKNOWN**: Whether scrap posting timing follows the same "immediate" pattern as IAV-F03 or defers like GRV-F04 — not evidenced this round.

### IAV-F05 — Cycle count scheduling

- **WHAT**: A per-location "Inventory Frequency" (in days) automatically schedules the location's next count date after an adjustment is applied there; a global default annual count date (31 December) applies where frequency is unset (0).
- **WHY**: Different storage locations warrant different count cadences (e.g., high-value or high-turnover locations counted more often).
- **BUSINESS RULE**: Requires the Storage Locations feature enabled; frequency is set per-location, not globally (beyond the default annual date).
- **STATE**: Count applied at a location → next scheduled date computed from that location's Inventory Frequency.
- **DATA CONCEPT**: Scheduling is a location-level attribute, not a product-level one.
- **CONTROL**: Purely a scheduling/reminder mechanism — no evidence it blocks or gates anything.
- **DEPENDENCY**: None on other functions in this Gx.
- **EVENT**: "Next count date computed."
- **RISK**: None identified — lowest-risk function in this Gx (matches its C3 criticality).
- **UNKNOWN**: Whether missing a scheduled count date has any system consequence (notification only, or something stronger) — `SOURCE/RUNTIME VERIFICATION REQUIRED`.

### IAV-F06 — Reversal / correction of an applied adjustment

- **WHAT / WHY / BUSINESS RULE / STATE / DATA CONCEPT / CONTROL / DEPENDENCY / EVENT / RISK**: Not evidenced this round — no documentation page specifically addressing "undo an applied inventory adjustment" was retrieved.
- **UNKNOWN**: Entire function is `DOCUMENTATION/SOURCE/RUNTIME VERIFICATION REQUIRED`. The most direct available finding is inference: since an adjustment is itself just a quantity-setting action, a correction would presumably be a second inventory adjustment recording the corrected quantity — but this is not documented as a distinct "reversal" mechanism the way Reverse Transfer / Credit Note are for receipts/deliveries. Recorded as an open gap, not assumed.
