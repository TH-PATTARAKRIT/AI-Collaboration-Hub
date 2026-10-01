# STATE03 VDR — Claude Verification Log

> Maintained by: `STATE03 BUSINESS PROCESS VERIFICATION AND INTEGRATION CONTROLLER` (this session, Sonnet 5 High), per the 2026-10-01 Role Update (`STATE03_DEEP_STUDY_REGISTER.md` §3.12). Records this session's verification pass over DeepSeek's Atomic Boundary Handoff Packets (`TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/`, branch `claude/local-odoo-source-research`). **This log is a verification ledger, not a Gate PASS, not Formal Coverage, not a canonical denominator.** Boss is Sole Final Approver.

## 1. Batch received (PR #74, 2026-10-01, notification comments by `scglegacy`)

16 Atomic Boundaries exist in the packet commit `3fec382c` (`04_HANDOFF_PACKETS/`): `B00`, `B01`, `B02`, `U01`–`U13`. Notification comments for all 16 are now posted on PR #74 (`B00`–`B02`, `U01`–`U09` arrived first; `U10`–`U13` arrived a few minutes later in the same posting run — a timing lag, not an omission).

## 2. Mechanical Integrity — full batch (16/16 boundaries)

Verified: every file hash declared in each boundary's `HP_<ID>.md` packet against the actual file content at the packet's own declared "Content commit" on `claude/local-odoo-source-research` (read-only `git show`, no checkout, no merge — per repository-isolation rule).

**Result: 16/16 boundaries, all declared sha256 hashes MATCH actual content.** No missing files, no hash mismatches, across `B00`/`B01`/`B02` control artifacts and all 13 `U01`–`U13` Restricted-Technical-Evidence + Neutral-Knowledge file pairs.

Format note (not a gap, a difference in intake format): DeepSeek's packets do not use the exact artifact filenames Boss's role-update order specified (`batch_manifest.json`, `read_log.jsonl`, `claims.jsonl`, `contradictions.jsonl`, `unknowns.jsonl`, `runtime_required.jsonl`, `checkpoint.json`, `neutral_knowledge.md`, `executive_summary.md`). Instead each boundary ships one `HP_<ID>.md` packet (scope/commit/hash/counts table) plus, per boundary, one Restricted Technical Evidence `.md` (claims table with per-claim evidence pointer, confidence class, and CONTRA/RT flags) and one Neutral Knowledge `.md` (WHAT/WHY/BUSINESS RULE/STATE/VALIDATION/OPTIONALITY/CONFIGURATION/DEPENDENCY statements, cross-referenced to the claim IDs). Functionally equivalent coverage of the same intake contract (claims, contradictions, runtime-required, neutral knowledge are all present, just not split into the exact named files) — recorded as a format note, not rejected.

## 3. Clean-Room spot-check

`U05`'s Neutral Knowledge file (`02_NEUTRAL_KNOWLEDGE/U05_sales_invoicing_delivery_NEUTRAL.md`, 525 lines) scanned for vendor code/method/model leakage (Odoo file paths, `def`/model/`_inherit`/`_name` patterns, dotted model names): **zero hits** — clean. Not yet repeated for the other 12 `U`-boundaries (queued).

## 4. Semantic verification — boundary-by-boundary status

| Boundary | Scope | Contradictions | C1-bound claims | Status |
|---|---|---|---|---|
| B00 | Checkpoint reconciliation | 1 | 0 (control) | Mechanical only — content not yet read |
| B01 | Source↔DB reconciliation | 1 | 0 (control) | Mechanical only — content not yet read |
| B02 | Test/theme classification | 0 | 0 (control) | Mechanical only — content not yet read |
| U01 | Base platform | 0 | — | Mechanical only — queued |
| U02 | Product/UoM/analytic | 0 | — | Mechanical only — queued |
| U03 | Mail/audit foundation | 0 | 59 | Mechanical only — queued (highest non-contradiction C1 count among notified boundaries; priority) |
| U04 | Sales order | 1 | — | Mechanical only — queued |
| **U05** | **Sales invoicing/delivery** | **2** | **81** | **Semantic spot-check done — see §5 below** |
| U06 | Purchase order | 3 | 7 | Mechanical only — queued |
| U07 | Purchase receiving | 2 | 72 | Mechanical only — queued |
| U08 | Stock transfers | 6 | 3 | Mechanical only — queued |
| U09 | Stock quants/lots/adjustments | 2 | 24 | Mechanical only — queued |
| **U10** | **Stock valuation & landed costs** | **7** | **140** | **Mechanical only — queued, TOP PRIORITY (highest contradiction count AND highest C1-bound claim count in the whole batch; squarely in STATE03's existing valuation-timing/COGS contradiction thread)** |
| U11 | Account entry lifecycle, lock dates | 4 | 77 | Mechanical only — queued (2nd-highest C1-bound claim count; ties to the existing `bypass_lock_check`/lock-date residual-risk thread) |
| U12 | Payments & reconciliation | 2 | 0 | Mechanical only — queued (highest runtime/AWT-required count: 32) |
| U13 | Tax/chart/currency/l10n_th/e-invoicing | 2 | 6 | Mechanical only — queued |

No boundary has completed 100% semantic verification of its C1-bound claims yet. **Risk order, updated now the full batch is notified**: `U10` (140 C1-bound claims, 7 contradictions — top priority) → `U05` (done) → `U11` (77 C1) → `U07` (72 C1) → `U03` (59 C1) → `U09` (24 C1) → remainder by contradiction/RT count.

**`U19` (out-of-sequence boundary, received 2026-10-01 at a later packet commit `bde3962b`)**: scope `website_community` (public website/mail/blog/forum/livechat/events/newsletter surface). 0 contradictions, 0 C1-bound claims (no existing Function-ID matches a public-website capability — DeepSeek itself flagged every claim `FUNCTION MAPPING REQUIRED`), 13 runtime-required. Despite 0 C1-bound claims, this boundary's content raised **security-relevant findings** escalated out of normal queue order — see §6.

## 5. U05 (Sales invoicing/delivery) — first semantic spot-check

Both of U05's flagged contradictions read, cross-checked against `02_NEUTRAL_KNOWLEDGE/U05_sales_invoicing_delivery_NEUTRAL.md` for internal consistency and Clean-Room compliance:

- **VDR-U05-C146** (bound to `SDV-F07`, Return after invoicing via Credit Note, **C1**): claims the in-code docstring at the cited pointer says a line's billed quantity should fall only for credit notes generated from the order itself, but the actual behavior (per the worker's own static trace) has no such restriction — a credit note created directly from an invoice also lowers the order line's billed quantity, which can make the order propose re-billing already-credited goods. The Neutral Knowledge statement `[N-U05-109]` states this plainly and labels it as a contradiction between the inline comment and the traced behavior, without naming the vendor method/file. Internally consistent between the restricted and neutral layers; **directly refines `SALES_DELIVERY_VALIDATION_PILOT/22_UNKNOWN_AND_GAPS.md` → `GAP-SDV-05`** (previously: "Credit Note amount derivation (automatic vs. manual) not evidenced") — reconciled there, see that file's own update.
- **VDR-U05-C191** (bound to `SDV-F01`, Delivery routing config, C3): claims Odoo 19's `sale_stock` has no `procurement.group` model — `stock.reference` plays that structural role instead, with the old procurement-group concept surviving only as a stale comment. Lower criticality (C3, not C1); relevant background for any future cross-document-linking design question (adjacent to `GAP-RCN-01`'s audit-chatter-sync thread) but not reconciled into a specific Gap-ID this round — noted here for traceability.

**Verification status assigned**: `CONDITIONALLY VERIFIED CANDIDATE` for both claims — internally consistent (restricted claim ↔ neutral statement ↔ packet-level count all agree), Clean-Room compliant, and the claim is plausible on its face, but **this session has no access to the actual Odoo 19 source tree or the restored database** (that access belongs to DeepSeek's local environment only, per Clean-Room/repository-isolation rules) and so cannot independently re-derive the cited source pointer itself. Full confirmation remains `RUNTIME/AWT REQUIRED` or a job for an independent reviewer (`CHATGPT_AUDIT`) with its own source access. Not `CLAUDE-VERIFIED CANDIDATE` — that status is reserved for claims this session can mechanically confirm itself (e.g. the hash-integrity results in §2).

## 6. U19 (website_community) — security findings escalated out of queue order

Mechanical integrity: both files hash-match at content commit `e4a14969`. Clean-Room: not yet scanned (queued). Despite carrying 0 C1-bound claims (no existing Function-ID applies — a public-website domain does not yet exist in the canonical Function-ID index), the technical evidence contains a dense cluster of public-route security findings in **Odoo 19 Community-core** modules (`website`, `mail`, `mail_group`, `rating`, `html_editor`, `im_livechat`) — not a custom module this time. Per the same escalation precedent as `STATE03_SECURITY_ADVISORY_2026-09-30.md` (which covered custom modules only), a separate advisory was written rather than waiting behind the normal C1/contradiction-ordered queue: `STATE03_SECURITY_ADVISORY_2026-10-01_COMMUNITY_CORE_WEBSITE.md`. Headline items: (1) `google_recaptcha` is installed with no secret key configured, so every `captcha=`-gated public route in this unit currently passes unconditionally — a single configuration gap that silently defeats bot/abuse protection across multiple routes at once; (2) the generic website-form-to-record endpoint is public, CSRF-exempt by design for anonymous sessions, and (given finding 1) effectively uncaptcha'd, while creating records with elevated rights; (3) a public link-preview route fetches an arbitrary caller-supplied URL server-side with no private-address/scheme filtering shown — an SSRF-shaped code path. Full list, including lower-severity items, in the advisory. Not yet reconciled into any pilot's Gap Register — no existing domain covers public-website capabilities (see advisory §6); flagged as a scope question for Boss/PMO (does STATE03 need a public-website/community Gx, or is this out of SMEsPlus's current scope entirely).

## 7. What this log is not

Not a Gate PASS, not Formal Coverage, not a canonical denominator, not Final Approved, not a V-Level assignment. `N/A — DENOMINATOR NOT VALIDATED` applies to any implied percentage. Boss remains Sole Final Approver.
