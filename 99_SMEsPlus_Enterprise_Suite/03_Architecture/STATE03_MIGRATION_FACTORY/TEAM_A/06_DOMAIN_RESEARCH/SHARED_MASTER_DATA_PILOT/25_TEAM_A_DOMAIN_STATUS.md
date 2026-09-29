> Domain: SHARED_MASTER_DATA_PILOT | Status and Stop Point

# 25 — TEAM A DOMAIN STATUS

| Function | Criticality | Target V | Actual V | Status |
|---|---|---|---|---|
| SMD-F01 Party/Contact | C2 | V4/floor V3 | V2 (this pilot); source-tier Carry-forward reference exists | **Carry-forward** — primary evidence is `GROUP_01_SALES_INVENTORY_PURCHASE`'s `PTY-*` series, not this pilot |
| SMD-F02 Product Template/Variant | **C1** | V5/floor V4 | V2 (this pilot); source-tier Carry-forward reference exists | **Carry-forward** — `GAP-SMD-02` resolved by reference (`PRD-09`/`10`) |
| SMD-F03 UoM Category/Conversion | **C1** | V5/floor V4 | V2 (this pilot); source-tier Carry-forward reference exists; `GAP-SMD-05` now source-verified | **Carry-forward** — `GAP-SMD-03` resolved by reference (`UOM-07`); `GAP-SMD-05` **resolved 2026-09-30** via direct source-code verification (`EV-SMD-06`) — no `uom.category` model in actual Odoo 19 Community source, confirmed independently of `GROUP_01`'s DB-schema finding |
| SMD-F04 Access Rights/Groups | **C1** | V5/floor V4 | V2 → source-code-tier for the composition rule (2026-09-30) | **This pilot's own primary contribution** — confirmed not covered by the Carry-forward track. `GAP-SMD-04` resolved at documentation tier 2026-09-29 (`EV-SMD-05`), **refined at source-code tier 2026-09-30** (`EV-SMD-06`, `base`/`sale` sample): composition confirmed; superuser/`sudo()` bypass of record rules newly discovered and added to the AWT backlog |

## M3 SELECTED-SLICE CHECKPOINT — CLOSED (2026-09-29, per Boss's "STATE03 M3 Shared Master Then Sales Delta Continuation" instruction)

**Not a claim that Shared Master Data (Wave 1) is complete.** Only the 4 functions originally selected (Party, Product Template/Variant, UoM, Access Rights) were researched this slice. A material, same-day self-correction was applied: 3 of those 4 (`SMD-F01`–`F03`) were found, on deeper scope-collision review, to already be covered at a higher (source-code+DB) evidence tier by the separately-authorized `GROUP_01_SALES_INVENTORY_PURCHASE` track — reclassified Carry-forward, not restarted or duplicated. Only `SMD-F04` (Access Rights/Groups) is confirmed genuinely new. Two of this pilot's own three original gaps (`GAP-SMD-02`, `GAP-SMD-03`) were closed by reference to that same track, not independently re-derived. One new gap (`GAP-SMD-05`) was disclosed, not resolved — a terminology/implementation tension between this pilot's public-documentation source and the other track's actual-codebase evidence.

**Not expanded into Accounting-owned master domains** (Pricing, Tax Master, Payment Terms, Fiscal Calendar, Currency, Dimension) per Boss's explicit instruction — none of those were researched this pass, and `Pricing`/`Tax`/`Payment Terms`/`Currency`/`Analytic` are additionally now known (via the same Carry-forward reference check) to already be covered by that other track's own Phase 1 rollup (`PRC-*`, `TAX-*`, `PAY-*`, `CUR-*`, `AN-*`) — a further reason not to duplicate them here.

## Source-code verification round (2026-09-30, per Boss's "STATE03 Odoo Clean-Room Source & Dump Deep Study" prompt)

Boss provisioned direct, read-only access to the actual Odoo 19.0.post20260921 Community source (previously unavailable to this cloud session — see `STATE03_ODOO_CLEAN_ROOM_SOURCE_ACCESS_PROBE.md`) via a separate local Claude Code session running on Boss's own Mac. This cloud session never read the source directly; it received only business-language findings plus file+line evidence pointers, relayed by Boss, which is what this pilot's own files now cite as `EV-SMD-06`. Clean-Room scope was enforced by both the local session's own instructions and by Boss personally confirming the excluded folders (`addons_Extramodule`, `Extra_Module_scgl`, `addons_smeplus`, and others) before work began — none were opened.

Result: `GAP-SMD-05` closed (no `uom.category` model exists); `GAP-SMD-04` refined (composition rule confirmed for a `base`/`sale` sample, not exhaustive; a materially important new finding — superuser/`sudo()` execution bypasses record rules entirely — added to `06_BUSINESS_RULE_REGISTER.md` and the AWT backlog). No open items remain in this pilot except `GAP-SMD-01` (non-blocking).

## Next action

Priority moves to Sales delta-intake per Boss's instruction §2 — see `STATE03_SALES_DELTA_INTAKE.md`.

## Stop point

`DOCUMENTATION STUDY COMPLETE (1 of 4 functions primary, now partly source-verified; 3 of 4 Carry-forward) / READY FOR PHASE A REPORT`. Ready for `CHATGPT_AUDIT`; not ready for `BOSS_GATE` pending `STATE03_BOSS_GATE_QUEUE.md` items.
