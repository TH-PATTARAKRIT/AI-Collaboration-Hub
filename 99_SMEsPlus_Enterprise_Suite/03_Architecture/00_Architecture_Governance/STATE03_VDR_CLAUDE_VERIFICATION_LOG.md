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

## 7. Standing Instruction (2026-10-01) — per-claim classification now mandatory

Per Boss's "STATE03 Standing Instruction — Automatic Correction & Evidence Completion Loop" (`STATE03_DEEP_STUDY_REGISTER.md` §3.13), every claim reviewed from here on is classified `ACCEPTED` / `NEEDS_MORE_EVIDENCE` / `CORRECTION_REQUIRED` / `CONTRADICTION_UNRESOLVED` / `RUNTIME/AWT_REQUIRED`, in addition to the existing §3.12 status vocabulary. This is a procedural refinement (per-claim labeling + a correction-request/re-verify loop that needs no per-cycle Boss approval) — it does not relax the restriction on this session issuing a Final Approved/Gate PASS/denominator-freeze result. Applied below starting with `U20`.

## 8. U20 (payment_providers) — full semantic review + second DeepSeek batch intake (U16–U23, C01)

**Mechanical integrity**: both U20 files (Restricted Technical Evidence, Neutral Knowledge) hash-match at content commit `c89f426258d4b674388f089b7b4cde128a6ddc5b`. 348 claims, 111 neutral statements, 1 contradiction (`VDR-U20-C085`), 52 runtime-required claims (the highest RT count of the batch to date), 0 claims bound to any existing C1/Function-ID (payment-gateway integration has no domain in the 53-entry index).

**Semantic review**: read the capability list, the full "Weakness register" (16 entries `W-01`–`W-16`), the "Per-provider delta summary" (23 providers), and the "Contradictions with prior evidence" section in full; cross-checked the claim rows underlying `W-01` (Toss), `W-02` (Mercado Pago), and `W-12` (demo gateway) against the weakness-register summary — all internally consistent, no discrepancy found. **`VDR-U20-C085`** (all 23 gateway add-ons are actually installed, contrary to the task premise, and a correction of `U12`'s own earlier DB-row reading) is a DeepSeek self-correction, evidenced by direct DB reconciliation — classified `ACCEPTED`, recorded as superseding (not invalidating) `U12`'s earlier reading, per the Standing Instruction's "preserve original evidence, mark superseded" principle.

**Security findings escalated**: `STATE03_SECURITY_ADVISORY_2026-10-02_PAYMENT_PROVIDERS.md` (new). Headline: (1) a Toss Payments webhook-forgery chain (`W-01`, HIGH suggested priority) — individual facts `ACCEPTED`, full exploit chain `RUNTIME/AWT_REQUIRED`; (2) Mercado Pago direct-payment route trusting a browser-supplied amount (`W-02`, HIGH) — same split; (3) the demo gateway is live/published/able to confirm orders in the studied DB (`W-12`, HIGH for production use) — `ACCEPTED` as a direct observation, not an inference. 13 further lower-severity findings (`W-03`–`W-11`, `W-13`–`W-16`) tabulated in the advisory, all `ACCEPTED` at the static-evidence level with exploitability (where applicable) `RUNTIME/AWT_REQUIRED`. **No finding in U20 is classified `CORRECTION_REQUIRED`/`NEEDS_MORE_EVIDENCE`/`CONTRADICTION_UNRESOLVED`** — nothing further is owed back to DeepSeek on this boundary; the open items are all runtime confirmation, which per the Standing Instruction belongs in the AWT backlog, not a correction request. Not yet reconciled into any pilot's Gap Register — no existing Function-ID domain covers payment gateways (same open Boss/PMO scope question as `U19`).

### 8.1 Second DeepSeek batch (2026-10-01/02) — U16–U23, C01 (9 boundaries, received mid-U20-review)

`claude/local-odoo-source-research` advanced `4e10133f` → `8e6535e8` while this review was in progress. Mechanical integrity re-run for all 9: **18/18 files (Restricted + Neutral per boundary) hash-match** at each boundary's own declared content commit — no mismatches, no missing files.

| Boundary | Scope | Claims | Contradictions | Status |
|---|---|---|---|---|
| U16 | Project/timesheet/expense | 449 | 1 | Mechanical only — queued (1 contradiction: no expense-report object in this revision, per prior session note) |
| U17 | HR/fleet/calendar | 499 | 0 | Mechanical only — queued |
| U18 | CRM/marketing/events (37 modules) | 470 | 0 | Mechanical only — queued |
| U20 | Payment providers | 348 | 1 | **Semantic review complete — see above** |
| U21 | Platform security & integration (2FA/passkeys/sessions/RBAC) | 519 | 2 | Mechanical only — queued; **security-adjacent scope, flag for next priority alongside C01** |
| U22 | Core bridge modules (loyalty/margin/project-stock/delivery) | 546 | 1 | Mechanical only — queued |
| U23 | 21 current-phase modules **not installed** in the studied dump; DeepSeek withheld its own internal gate pass | 508 | 0 | Mechanical only — queued; note the self-withheld gate is DeepSeek's own caution flag, not a STATE03 gate of any kind |
| C01 | **Order-to-Cash end-to-end chain** (quote→deliver→invoice→pay) — first cross-cutting control boundary | 271 | **7** | Mechanical only — queued, **NEW TOP PRIORITY** (highest contradiction count of any boundary received to date; cross-cutting chain ties directly into the existing valuation-timing/cross-Gx contradiction thread, `STATE03_VALUATION_TIMING_CROSS_GX_CONTRADICTION_MATRIX.md`) |

**Updated risk order**: `C01` (7 contradictions, cross-cutting O2C chain) and `U10` (140 C1-bound claims, 7 contradictions) are now joint top priority → `U21` (security-adjacent, 2 contradictions) → `U11` (77 C1) → `U07` (72 C1) → `U03` (59 C1) → `U09` (24 C1) → remainder by contradiction/RT count. `U16`/`U17`/`U18`/`U22`/`U23` have no contradictions or C1-bound claims flagged at the packet-summary level and are lower priority pending their own semantic pass.

## 8.2 Scope ruling (2026-10-02) — accounting localization = Thailand only

Per Boss's "Accounting Localization Scope = Thailand Only" order (`STATE03_DEEP_STUDY_REGISTER.md` §3.15): `U13`'s nine-foreign-country "DISCOVERED SUPPORTING MODULES" list (`l10n_sa_edi`, `l10n_es_edi_sii`, `l10n_eg_edi_eta`, `l10n_pl_edi`, `l10n_dk_nemhandel`, `l10n_tr_nilvera`, `l10n_fr_pdp`, `l10n_hr_edi`, `l10n_it_edi`) is reclassified `FOREIGN LOCALIZATION / OUT OF SMEsPlus BUSINESS SCOPE` — DeepSeek itself only found these by grep and did not open them beyond that, so no rule-level research exists to strike; nothing else in evidence collected to date touches a non-Thai jurisdiction's accounting rules. Not counted toward the Applicable SMEsPlus denominator. Posted to PR #74 so DeepSeek applies the Thailand-only filter prospectively to any future accounting/localization boundary.

## 8.3 Third wave (2026-10-02) — U14, U15, C02 (branch advanced `8e6535e8` → `a793d15b`)

Mechanical integrity: all 3 boundaries' Restricted + Neutral files hash-match at their own declared content commits (6/6 real files MATCH; the only "MISMATCH" lines are the known harmless counts-table grep artifact, same as every prior run).

| Boundary | Scope | Claims | Contradictions | C1-bound | Status |
|---|---|---|---|---|---|
| U14 | Manufacturing core (mrp: BoM, work centers, MO lifecycle, reservation, backorders, scrap/unbuild, replenishment) | 536 | **8** | 27 (`BRP-F01`, `BRP-F03`, `BRP-F08`, `MFG-F01`, `MFG-F02`) | Mechanical only — queued, **flagged §8.4 below** |
| U15 | Manufacturing accounting, subcontracting, landed costs on MO, repair | 355 | 5 | **168** (`BRP-F01`, `BRP-F03`, `BRP-F08`, `GRV-F05`, `MFG-F01`, `MFG-F02`) | Mechanical only — queued, **flagged §8.4 below, 2nd-highest C1 count of the whole program to date** |
| C02 | Procure-to-Pay end-to-end chain (RFQ→receipt→bill→payment) + consistency audit of U06/U07/U08/U10/U11/U12 | 310 | 6 | 62 (`GRV-F04/05/06`, `PCO-F01/03/04`, `PDT-F02/03`, `RCN-F03`) | Mechanical only — queued, **joint top priority with C01/U10 — DeepSeek's own notification states "correction requests to follow"** |

## 8.4 Material Delta flag — U14/U15 contradict already-"Complete" canonical Gx7/M1 entries

`U14` (8 contradictions: `VDR-U14-C002/C037/C077/C469/C470/C471/C493/C499`) and `U15` (5 contradictions: `VDR-U15-C020/C046/C052/C068/C084`) both bind claims to Function-IDs this register's own `STATE03_DEEP_STUDY_REGISTER.md` §2/§2.2 already records as **Research status: Complete** — `MFG-F01`, `MFG-F02` (Gx7, Manufacturing Valuation Pilot) and `BRP-F01`, `BRP-F03`, `BRP-F08` (M1, Manufacturing BOM Routing Pilot). This is the same shape of finding as the existing valuation-timing cross-Gx contradiction thread (`STATE03_VALUATION_TIMING_CROSS_GX_CONTRADICTION_MATRIX.md`): **not yet semantically reviewed by this session** (contradiction claim rows not yet read), so no status change is made to any Gx7/M1 Function-ID here — flagged only, per the §3.13 Standing Instruction's priority-escalation rule for material contradiction. Queued as joint top priority alongside `C01`/`C02`/`U10` for the next semantic-review pass. `BRP-F08` (By-Products) is already an **Open/Conditional** gap (`GAP-BRP-09`) even before this — these new contradictions may bear directly on closing or further complicating it.

## 10. Re-verification of DeepSeek's self-correction loop (2026-10-02) — 16 correction requests, 10 resolution packets

`claude/local-odoo-source-research` advanced `a793d15b` → `ae5a19d3`, delivering `05_CORRECTION_LOOP/` (`00_PROTOCOL.md`, `CORRECTION_REQUESTS.md`, `REVIEW_REGISTER.tsv`, `SUPERSESSION_INDEX.tsv`, 10 resolution packets). **Important role disclosure, from DeepSeek's own protocol doc**: these 16 correction requests and their 27 `REVIEW_REGISTER.tsv` spot-checks were raised and self-reviewed by DeepSeek's **own** Claude Code harness (explicitly self-labelled "not independent verification") — this session is the separate "Claude verifier" the protocol doc names, whose PR #74 comments are "the authoritative verification feed." Originals are never edited; each correction packet (`<BOUNDARY>-R<n>`) is additive, with superseded claims tracked in `SUPERSESSION_INDEX.tsv` as `SUPERSEDED`/`SUPERSEDED-IN-PART` — lineage preserved throughout, consistent with the Standing Instruction's "preserve original evidence" rule.

**Full read + re-verification this session** (the 4 packets of highest material weight):
- **`U08-R1`** (CR-001, Material): corrects the return-eligibility rule for stock transfers — base rule (returnable only when `done`) is extended by `sale_stock` to also allow a sales-linked transfer in *any* state, bypassing the wizard's state check entirely; the `Done`-only wording in the wizard's error message is enforced later, per return-line, not at eligibility. Internally consistent, FACT-level pointers for every branch, UNKNOWN/RT correctly flagged for the not-done sales-linked quantity outcome. **`ACCEPTED`** (static), runtime outcome **`RUNTIME/AWT_REQUIRED`**.
- **`U10-R1`** (CR-004, C1): two hooks U10 originally credited with COGS-delta booking/refund at invoice time (`_stock_account_get_last_step_stock_moves`, `_get_related_invoices`) have no caller anywhere in the addons tree outside their own override chain — flagged inert in this revision. Related to, but distinct from, the main valuation-timing chain — cross-referenced into `STATE03_VALUATION_TIMING_CROSS_GX_CONTRADICTION_MATRIX.md` §4.4. **`ACCEPTED`** (static; the "inert" conclusion is INFERENCE, correctly labelled, not independently re-derivable by this session).
- **`U10-R2`** (CR-008, C1): posting inside a locked period shifts the entry's date to the first open date rather than refusing it — **independently corroborates** the prior (2026-09-30, different lineage) finding already recorded at `GAP-PCO-01`. Cross-referenced into the contradiction matrix §4.4 as second-lineage corroboration — strengthens the evidence tier, does **not** close the gap or change its `Material Finding — Independently Unverified` status. **`ACCEPTED`** (static), per-lock-type date outcome **`RUNTIME/AWT_REQUIRED`**.
- **`U11-R1`** (CR-002/CR-005, Material): the `in_payment` state is reachable only via an Enterprise-only (`account_accountant`) override, never assigned in Community; and invoice-cancel's `payment_ids = canceled` write targets payments whose own journal entry is the cancelled entry (not an invoice's settling payments, which live in the separate `matched_payment_ids`) — a meaningful precision correction to the original claims. Internally consistent, FACT/INFERENCE properly separated. **`ACCEPTED`** (static), follow-on payment-state behaviour **`RUNTIME/AWT_REQUIRED`**.

**Header/metadata-level review only this round** (Subject + supersession scope read from `CORRECTION_REQUESTS.md`/`SUPERSESSION_INDEX.tsv`; full packet body not yet read — queued, lower priority than the 4 above): `U04-R1` (CR-006, order-line margin cost-source branch for standard-cost lines), `U07-R1` (CR-009, Material — several receipt/return extension methods found inert/orphaned; bill-reset does not re-value receipts), `U12-R1` (CR-003, Normal — corrects which provider row is actually enabled, consistent with `U20`'s own `VDR-U20-C085` already logged §8), `B01-R1` (CR-011, Material — control-document wording correction, explicitly self-disclosed lineage note: two earlier in-place edits to `B01` predate this standing instruction and are now superseded-with-preserved-original per the protocol's own disclosure), `B02-R1` (CR-012, Normal — garbled theme-row wording fixed), `C01-R1` (CR-007/CR-010, C1/NEEDS_MORE_EVIDENCE — reservation timing at order confirmation and a lock-period cross-reference gap, both additive research not corrections of an error). None of these six raise an internal-consistency flag on the metadata available; full read queued for next pass. **No packet in this batch is classified `CORRECTION_REQUIRED`/`CONTRADICTION_UNRESOLVED` by this session** — DeepSeek's own corrections are themselves accepted at the static-evidence tier; nothing is sent back.

**Still open, not yet resolved by DeepSeek** (per `CORRECTION_REQUESTS.md`): `CR-013` (U06-R1), `CR-014` (U07-R2), `CR-015` (U10-R3) — marked `IN PROGRESS (worker)`; `CR-016` — runtime items correctly routed straight to `06_AWT_BACKLOG/` rather than treated as corrections, per the Standing Instruction's "DeepSeek must not infer runtime behavior" rule.

## 11. Scope-rule mechanical application + localization-architecture research started (2026-10-02)

DeepSeek applied the Thailand-only scope rule mechanically across the full 692-module source population (`SCOPE_CLASSIFICATION_THAILAND_ONLY_692.tsv`, `FOREIGN_LOCALIZATION_EVIDENCE_QUARANTINE.tsv`, commits `3b0d7774`/`ae5a19d3`): 1 Thailand (`l10n_th`), 461 generic, 3 generic l10n-prefixed mechanisms, 227 foreign localization — all evidence-only, none installed/current-phase, so no change to any current-phase module population. 5 preserved claims pointing into foreign modules re-labelled, not deleted. Then re-labelled, per §3.17, to `FUTURE OPTIONAL COUNTRY PACK` (`SCOPE_CLASSIFICATION_V2_COUNTRY_PACKS_692.tsv`, `COUNTRY_PACK_BOUNDARY_PROFILE_227.tsv`, commit `6ecd29c6`) — old files preserved, v2 added, lineage intact. **Not independently re-verified in detail this round** (bulk mechanical classification of 692 rows is exactly the kind of work the §3.12 cost rule reserves for DeepSeek, not Sonnet-bulk-reading) — spot-check queued if a specific row is later disputed.

New boundaries started under the Approved Scope Delta: `U24` (Thailand localization), `U25` (multi-currency & international transactions), `U26` (language/translation mechanism — UI language vs. statutory-document presentation), `U27` (localization-framework architecture — "neutral CANDIDATE sketch only," per DeepSeek's own wording, consistent with this session's §3.17 reading that this is evidence/neutral-knowledge research, not Functional Design), `U28` (Thai entity structures — foreign-owned Thai companies, subsidiaries of foreign groups, foreign branches/representative/regional offices). None yet received as completed Atomic Handoffs — queued.

**Two open items flagged to Boss (not decided by this session)**:
1. Does the Thailand-only scope rule extend to non-`l10n_`-prefixed region-specific modules (the Peppol e-invoicing family, SEPA QR, country-specific payment gateways already seen in `U20`)? DeepSeek flagged this itself, unresolved.
2. **DeepSeek's own disclosed limit, important**: Thai statutory/legal requirements (actual Thai Revenue Department VAT/WHT rules, statutory document requirements) are explicitly **not asserted** — DeepSeek can only read how Odoo's `l10n_th` *implements* a given rule in code, not independently confirm that implementation is correct against actual Thai law. Status `UNKNOWN — STATUTORY SOURCE REQUIRED` until Boss/PMO supplies an authoritative source. This is a genuine evidence-tier ceiling, not a research gap DeepSeek can close by reading more source.

## 12. Correction Closure Matrix (16 requests → 10 resolution packets), per Boss order item 6

Every correction request raised in `CORRECTION_REQUISITS.md` (16 total, `CR-001`–`CR-016`) carries an explicit disposition below — none left unaccounted.

| CR | Priority | Boundary | Subject | Resolution packet | Disposition | This session's classification |
|---|---|---|---|---|---|---|
| CR-001 | Material | U08 | Return eligibility (done vs. sale-linked) | U08-R1 | PROCESSED | `ACCEPTED` (full read, §10) |
| CR-002 | Material | U11 | `in_payment` state reachability | U11-R1 | PROCESSED | `ACCEPTED` (full read, §10) |
| CR-003 | Normal | U12 | Enabled-provider row ownership | U12-R1 | PROCESSED | `ACCEPTED` (metadata-level, §10) |
| CR-004 | C1 | U10 | COGS-timing hook map (inert hooks) | U10-R1 | PROCESSED | `ACCEPTED` (full read, §10) |
| CR-005 | Material | U11 | Invoice-cancel effect on settling payments | U11-R1 | PROCESSED (same packet as CR-002) | `ACCEPTED` (full read, §10) |
| CR-006 | Normal | U04 | Order-line margin cost-source branch | U04-R1 | PROCESSED | `ACCEPTED` (metadata-level, §10) |
| CR-007 | C1 | C01 | Reservation timing at order confirmation | C01-R1 | PROCESSED | `ACCEPTED` (metadata-level, §10) — additive research (`NEEDS_MORE_EVIDENCE` closed), not a correction of an error |
| CR-008 | C1 | U10 | Lock-date posting shift vs. refusal | U10-R2 | PROCESSED | `ACCEPTED` (full read, §10) — cross-referenced to `GAP-PCO-01`, see §13 |
| CR-009 | Material | U07 | Inert receipt/return extension methods; bill-reset valuation | U07-R1 | PROCESSED | `ACCEPTED` (metadata-level, §10) |
| CR-010 | C1 | C01/U08/U11 | Transfer date-done lock-period cross-reference gap | C01-R1 | PROCESSED (same packet as CR-007) | `ACCEPTED` (metadata-level, §10) |
| CR-011 | Material | B01 | Control-document wording (valuation-flag/chart-count) | B01-R1 | PROCESSED | `ACCEPTED` (metadata-level, §10); self-disclosed lineage note (pre-standing-instruction in-place edits) accepted as-is |
| CR-012 | Normal | B02 | Control-document theme-row wording | B02-R1 | PROCESSED | `ACCEPTED` (metadata-level, §10) |
| CR-013 | Normal | U06 | Bill-creation entry points, posting role, vendor-price-lookup ownership | U06-R1 | **PROCESSED (2026-10-02)** | `ACCEPTED` — see §14 |
| CR-014 | Normal | U07 | Double-negative condition; lot-to-PO link | U07-R2 | **PROCESSED (2026-10-02)** | `ACCEPTED` — see §14 |
| CR-015 | C1 | U10 | Accrued-orders wizard (PCO-F03 accrual half) | U10-R3 | **PROCESSED (2026-10-02)** | `ACCEPTED` — full read, see §14; reconciled into `GAP-PCO-02`/`GAP-PCO-03` |
| CR-016 | Material | multi | Runtime-only items from cross-unit audits | — (routed, not a correction) | **RECORDED IN AWT BACKLOG** | Correctly routed — DeepSeek did not infer runtime behavior, per the Standing Instruction's item 7 rule |
| CR-017 (Odoo-evidence lane, U24) — **re-tracked as `CR-020` by DeepSeek to resolve the ID collision** | Normal | U24 | Gap-register terminology: use `NATIVE GAP / EXTENSION REQUIRED` per Boss's exact wording, not `NOT PRESENT IN COMMUNITY SOURCE` | `U24-R1` | **PROCESSED (2026-10-02)** | `ACCEPTED` — see §26 |
| CR-017 (statutory lane, TXS) — **number collision, flagged to DeepSeek** | C1/Material | TXS | Resolve the 5 `TXS` `CONFLICT` rows via raw (non-summarised) re-read | `TXS-R1` | **PROCESSED (2026-10-02)** | `ACCEPTED` — see §25; 4/5 resolved, 1 correctly left open (Sec. 70 rate basis) |
| CR-018 | Normal (denominator-adjacent) | multi (control files) | `COUNTRY_PACK_BOUNDARY_PROFILE_227.tsv` heuristic columns unreliable (archetype name-prefix misclassification, template-file miscount, unreproducible core-model-extension count) | `SCOPE-R1` | **PROCESSED (2026-10-02), self-raised by DeepSeek via `U27`'s recount** | `ACCEPTED` — see §19; 227-pack classification itself confirmed unaffected |
| CR-019 | Material | U11 | `delivery_date` stub claim conflated with `taxable_supply_date` stub; abnormal-document-warning default context | `U11-R2` | **PROCESSED (2026-10-02), self-raised by DeepSeek via `TXA2`'s cross-check** | `ACCEPTED` — see §23 |

**Count check (updated 2026-10-02, all three "in progress" items now resolved)**: 16 requests → 13 distinct resolution packets (`B01-R1`, `B02-R1`, `C01-R1`, `U04-R1`, `U06-R1`, `U07-R1`, `U07-R2`, `U08-R1`, `U10-R1`, `U10-R2`, `U10-R3`, `U11-R1`, `U12-R1` — two packets each resolve two CRs: `C01-R1` for CR-007/CR-010, `U11-R1` for CR-002/CR-005) + 1 routed to AWT (`CR-016`) = 16/16 accounted for, **all now `PROCESSED`/`ACCEPTED` or correctly routed — zero still `IN PROGRESS`**, matching Boss's required closure-matrix shape exactly.

## 13. GAP-PCO-01 reclassification (per Boss order item 5)

Per explicit Boss instruction, `GAP-PCO-01`'s lock-date dimension is reclassified along three separate axes (replacing a single blended status with one that keeps evidence-tier, runtime-tier, and gap-open/closed status visually distinct — applied to `PERIOD_CUTOFF_VALIDATION_PILOT/22_UNKNOWN_AND_GAPS.md` and cross-referenced here):

- **SOURCE/DUMP = INDEPENDENTLY CORROBORATED** — the lock-date date-shift mechanism (posting inside a locked period moves the date to the first open date rather than refusing it) is now static-evidence-confirmed from **two separate research lineages** (the 2026-09-30 source/dump worker, and 2026-10-02 DeepSeek `U10-R2`) reaching the same conclusion independently. This is a genuine strengthening of the evidence tier for this specific sub-finding.
- **RUNTIME/AWT = UNVERIFIED** — neither lineage has executed against a live/restored-and-running Odoo 19 instance; the exact date chosen per lock type, its effect on sequence numbering, and period-report interaction remain unconfirmed (`CR-016`/AWT backlog carries this item).
- **GAP = OPEN** — `GAP-PCO-01` is **not closed**. `bypass_lock_check`'s reachability/exposure, `account_accountant`'s actual installed/active state, the `account_update_tax_tags` lead, and the custom-module audit-trail bypasses (`account_asset_management`, `scgl_advance_expense_request`) remain `UNKNOWN — EVIDENCE INSUFFICIENT` exactly as before — this reclassification narrows and strengthens one sub-finding within the gap, it does not resolve the gap as a whole.

This three-axis format is **more precise than, and supersedes the blending in, the single `Material Finding — Independently Unverified` label** previously used for the lock-date sub-finding specifically — it does not change the status of the broader valuation-timing chain (`GRV-F04`/`SDV-F05`/`IAV-F03`/`PCO-F03`), which remains `Material Finding — Independently Unverified` pending `CHATGPT_AUDIT` exactly as Boss ruled 2026-09-29.

## 14. Re-verification: U10-R3 (C1), U06-R1, U07-R2 — the 3 previously "IN PROGRESS" correction packets now resolved

`claude/local-odoo-source-research` advanced `ae5a19d3` → `de997082`.

- **`U10-R3`** (CR-015, C1, full read): characterizes the entire accrued-orders mechanism DeepSeek's earlier `C02` audit (finding F15) said "nobody owns." `account.accrued.orders.wizard` is a manual, transient, action-triggered wizard (bound to PO/SO/SO-line only — no `purchase_stock` extension exists), restricted to the "Show Full Accounting Features" group, which in the studied DB has **0 member users and no implying group** (whether an Accounting Administrator can actually reach it is `UNKNOWN`/RT). Confirms and supplements (does not contradict) U10's original month-end-closing claims. New, material points: (1) the closing report's own "Accrual" block is confirmed **inert** (template call commented out, patched JS getters read unpopulated data keys, Python helpers not imported); (2) **no duplicate-run guard and no stored order link** (free-text reference only) — nothing in source stops the same not-yet-billed value being accrued twice; (3) foreign-currency amounts convert at **today's rate, not the accrual date's rate**; (4) lock-date behaviour for the accrual/reversal pair reconfirms (does not newly establish) the `GAP-PCO-01` date-shift mechanism; (5) one internal source inconsistency flagged by DeepSeek itself (a comment claims purchase lines include down-payments while the actual filter excludes them for both directions) — a stale-comment-vs-code pattern, same shape as the earlier `U05`/`SDV-F07` finding from this session's first review. All claims properly FACT/INFERENCE/RT-separated, internally consistent. **`ACCEPTED`** at the static-evidence tier; reachability and exact per-lock-type date outcome remain `RUNTIME/AWT_REQUIRED`. Reconciled into `PERIOD_CUTOFF_VALIDATION_PILOT/22_UNKNOWN_AND_GAPS.md` `GAP-PCO-02`/`GAP-PCO-03`.
- **`U06-R1`** (CR-013, Normal, read in full through the ten-dimension table): clarifies there is **no form-level "Create Bill" button** on a purchase order — bills start from the list-header button, the Upload-Bill widget, Auto-Complete, Bill Matching, or automatic post-import linking, or (reverse path) a PO created from bill lines. Receipt validation acknowledges its PO via an elevated-rights hook shared with the Acknowledge button/portal/reminders/dashboard. Posting needs the invoicing group specifically, distinct from the purchase-user group. Bill-side vendor-price lookup lives in `account` (consistent with the already-logged `U02` claim), distinct from the order-side lookup owned by `U06`. Internally consistent, properly hedged. **`ACCEPTED`**.
- **`U07-R2`** (CR-014, Normal, read in full through the ten-dimension table): the `other_candidates_qty -= -move._get_valued_qty()` double-negation at `purchase_stock/models/stock_move.py:196` evaluates as an **addition** — an earlier outgoing move (e.g. a vendor return on the same order line) increases the quantity treated as already bill-covered, shrinking the remaining billed quantity available to a later move's valuation. DeepSeek correctly declines to infer whether this is intended (`UNKNOWN`/RT). No effect on received quantity (separate, non-calling code path). The lot-to-PO link is receipt-side-only, not stored, not lot-of-done-move-aware for returns, and the studied DB has no lots to cross-check. **`ACCEPTED`**.

Correction Closure Matrix (§12) updated: **0 correction requests remain `IN PROGRESS` — all 16 have a terminal disposition** (13 processed/accepted across 10+3 packets, 1 routed to AWT backlog — see §12's updated count-check line).

## 15. U24 (Thailand localization) — first Thai Tax Core boundary, full semantic review

Mechanical integrity: both files hash-match at content commit `60f40461`. 260 claims, 136 neutral statements, 1 contradiction (self-identified against the unit's own brief, not a prior file — resolved, see below), 12 RT, 5 C1-bound (`PCO-F01`).

**Read in full.** Strong compliance with the §3.18 discipline throughout: every section keeps "what `l10n_th` implements" separate from "statutory conformity UNKNOWN" / "legal needs UNKNOWN" — no claim asserts Thai law is satisfied. Key findings:
- Thai tax set (18 taxes: 6 VAT, 8 purchase WHT → PND53, 4 sale WHT) is implemented as ordinary document-time negative-percentage taxes, not the payment-time withholding mechanism (`l10n_account_withholding_tax`, present but uninstalled and unused by the Thai set) — confirmed consistent with `U13`/`U23`.
- Tax-invoice title ("Tax Invoice") is fixed by **company fiscal country**, not UI/partner language — only the surrounding text follows partner language. A DELTA correction to `U13`'s earlier prose (title replacement applies to posted customer invoices only; credit notes/drafts/cancelled/Commercial Invoice keep standard titles) — self-identified, not contradicted.
- PromptPay/EMV QR: THB-only, static-account credit-transfer style, no payment/reconciliation linkage, no Thailand-specific reference tag.
- **Self-identified CONTRA, resolved**: the unit brief expected "amount in words" to be a Thai gap; a generic facility exists in Community (company switch + DB flag already on) — only the Thai-language rendering itself is `UNKNOWN`/RT (depends on `num2words` library support, not read). Correctly caveated, not asserted either way.
- `CAP-U24-08` registers 8 absent-from-Community-source Thai statutory outputs (VAT return/filing forms, WHT certificates/PND1/2/54 filing, e-Tax invoice/e-Receipt format, abbreviated/combined invoice + seller-branch + mandatory-field enforcement, Buddhist-era year printing, Thai-language amount-in-words, input-VAT proration/foreign-payee WHT/Thai financial-statement formats, tax periodicity/closing) — each stated as a negative search, explicitly not a legal-requirement assertion.
- `CAP-U24-09`: mechanical, manifest-only country-pack boundary table for all 227 non-Thai `l10n_*` modules, correctly labelled `FUTURE OPTIONAL COUNTRY PACK` throughout, no accounting rule of any foreign pack read — compliant with the scope delta.

**One terminology-compliance correction requested (`CR-017`, Normal, posted to PR #74)**: Boss's "Continue U24–U28 automatically" order specifies the exact label `NATIVE GAP / EXTENSION REQUIRED` for a Thai-required function Community doesn't natively support. `CAP-U24-08`'s 8-item register instead uses `NOT PRESENT IN COMMUNITY SOURCE` throughout. The underlying research is sound and needs no re-research — this is a relabeling-only request, not a substantive finding to re-derive.

**Classification**: all static findings `ACCEPTED`; the 12 RT items correctly routed `RUNTIME/AWT_REQUIRED`; the self-identified CONTRA is resolved (not `CONTRADICTION_UNRESOLVED`); the terminology gap is `CORRECTION_REQUIRED · Normal` (`CR-017`). Not yet reconciled into any pilot's Gap Register — Thailand-localization capabilities still have no dedicated Function-ID domain (same open question as `U19`/`U20`).

## 16. U26 (language & translation mechanism) — direct answer to Boss's standing i18n design constraint

Mechanical integrity: both files hash-match at content commit `401f828c`. 251 claims (+ a separate framework-core table, `CORE-U26-K###`, for files outside `odoo/addons` not covered by the automated pointer/anchor checker — DeepSeek discloses this gap itself and reports it was anchor-checked by a separate script), 0 contradictions, 0 C1-bound, 12 RT.

**Spot-checked in depth** (CAP-U26-01/02/03/07/09, the sections bearing most directly on Boss's "English canonical, Thai translation layer with stable keys, no hard-coded Thai UI text" design constraint — §3.16/§3.18/§3.19). Internally consistent, properly hedged throughout, and explicit that this unit "studies a design constraint comparison only: no design is proposed."

**Material finding for whoever designs the actual i18n architecture (not acted on here — observation only)**: Odoo's own code-level (Python/JS) translation mechanism uses **the English source sentence itself as the lookup key** — there is no symbolic/stable-key abstraction for code-level terms. DeepSeek's own state diagram names the consequence plainly: `translated -> orphaned [English wording edited; old msgid no longer matches]`. This is a genuine mismatch with Boss's stated "stable translation keys" principle **as a property of Odoo's native mechanism** — if SMEsPlus's own future system needs true decoupled stable keys, that is a design choice to make at the FDS/architecture stage, not something Odoo's Community source already provides. Data-level translatable fields are better off: a closer-to-stable identifier (external id/xmlid + field name) is used by the import/export tooling, though still not a universal cross-cutting key system.

**Favorable finding**: the "no hard-coded Thai UI text" principle is **already well-matched by Community practice** — the mechanical Thai-script scan found **zero** Thai-script literals in non-test Python source; the only Thai text outside `.po` translation files is locale/reference data (77 Thai province names with no English equivalent — necessary native data, not a UI-string violation; a language self-name; a currency symbol character) plus demo data. Document (invoice) language is already cleanly separated from UI/session language — printed documents follow the **partner's** language, not the viewer's.

**Classification**: `ACCEPTED` at the static-evidence tier (no RT dependency for the core architectural findings above — they are direct code reads, not inferences); the 12 RT items (Thai-locale rendering, amount-in-words library support, load/memory impact) correctly routed `RUNTIME/AWT_REQUIRED`. No correction needed.

## 17. U25 (multi-currency, foreign customer/vendor, international transactions)

Mechanical integrity: both files hash-match at content commit `6e31d186`. 299 claims, 1 contradiction (a refinement — U01's prior claim omitted an ACL row, self-corrected, not a real conflict), 25 RT, 0 C1-bound.

**Spot-checked** (CAP-U25-01/02, currency catalogue/rate model and document-currency-date chain). Internally consistent, properly hedged. Headline findings worth carrying forward:
- **A missing exchange rate silently falls back to 1.0** — no error, no warning (`_get_rates` COALESCE). The studied DB has 2 active currencies (THB, USD) and **zero rate rows** — any USD document in this configuration would convert at 1:1 silently. Worth flagging as a genuine operational risk for a Thailand-based multi-currency deployment, not a code defect — the behavior is by design, but silent.
- **No automatic rate provider, revaluation, consolidation, or customs/Intrastat module exists in Community** (confirmed by search, not inference).
- **Document rates are not inherited down the chain** — order rate, invoice rate, receipt-valuation rate, bill rate and payment rate are each computed independently at their own date — consistent with, and now generalizes, the `U10-R3` finding that accrual amounts convert at "today's rate" rather than a fixed reference date.
- Thai chart seeds exchange gain/loss accounts (421300/621200) and an EXCH journal, but no fiscal position and an unused PND 54 (foreign-payee withholding) account — consistent with `U24`'s own finding that foreign-payee withholding is not modelled.

**Classification**: `ACCEPTED` at the static-evidence tier; RT items (numeric conversion outcomes, rate-precedence edge cases) correctly routed. No correction needed.

## 18. U28 (Thai entity structures) — foreign-owned/subsidiary/branch/rep-office modeling, highest C1 count of the Thai Tax Core wave

Mechanical integrity: both files hash-match at content commit `c094725d`. 296 claims, 139 neutral, 0 contradictions, 25 RT, **66 C1-bound** (`MCT-F02`×62, `MCT-F03`×12, `MCT-F04`×25, `PCO-F01`×4) — the highest C1 count of this wave. Function-ID mapping is honest throughout: `MCT-F04` (Consolidation reporting) is explicitly used to **state an absence**, not claim a match — DeepSeek's own method note says this plainly, which this session confirms is the correct use of an existing C1 Function-ID for a negative finding.

**Spot-checked in depth** (CAP-U28-01 entity model, CAP-U28-03/04 ownership/inter-company, CAP-U28-05 consolidation, CAP-U28-07 company-to-jurisdiction assignment — the sections answering Boss's explicit entity-structure and jurisdiction-assignment questions directly). Internally consistent, properly hedged, excellent code-vs-statute separation (every Thai legal fact `UNKNOWN — STATUTORY SOURCE REQUIRED`, every Community absence stated as a search result, not an assumption).

**Material structural findings, neutral-architecture-knowledge only (no design made here)**:
- **Representative offices and regional offices have no dedicated concept in Community** — they can only be modelled as a separate root company or as a branch (child company), each with real consequences (see below). This is a direct, honest answer to Boss's entity-structure question, not a gap to "fix" — it's a fact about Odoo's own data model.
- **A branch is structurally constrained to share its root's currency, fiscal-year end, cash-basis flag and storno setting** — it **cannot** independently diverge on these from its parent. Combined with the finding that a branch's fiscal country can be **overwritten by chart-template loading** (flagged `RT` — behavior not executed), this is a genuine tension with Boss's stated design goal ("each Company uses the accounting jurisdiction applicable to that legal/accounting entity") **as a property of Odoo's native branch model** — worth carrying forward explicitly to whichever stage designs the actual company-to-jurisdiction assignment mechanism (`U27`'s localization framework), since a literal foreign-company branch operating under Thai jurisdiction while its parent uses a different currency/fiscal-year is not cleanly representable as an Odoo "branch" today; it would need to be a separate root company instead, with the trade-offs that implies (no shared chart, inter-company flows limited to clearing/transit only).
- **No ownership/shareholder/group modeling exists at all** — the company hierarchy is a contact/address hierarchy, not an ownership structure. Directly relevant to "Thai subsidiaries of foreign groups."
- **Inter-company automation in Community is limited to online-payment clearing and stock-transit plumbing** — the "Manage Inter Company" setting that would mirror sales/purchase orders and invoices across companies is **an Enterprise upsell prompt in Community**, not a working feature. A materially important scope fact for SMEsPlus if cross-entity document mirroring is ever wanted.
- **No consolidation, elimination, or group-currency feature exists** (`MCT-F04`, confirmed absent) — only a report-level currency-translation table that converts multi-company analysis amounts to the viewing company's currency, with the same "missing rate silently defaults to 1" risk already flagged in `U25`.
- Refinements to prior evidence (not contradictions, self-identified): `U13`'s 13-digit Thai tax-ID validation claim actually describes the bank-QR merchant tax-ID check, not partner/company Tax ID validation; `U12`'s inter-company clearing description is confirmed and extended with the full condition list.

**Classification**: `ACCEPTED` at the static-evidence tier; the 25 RT items (branch-in-another-country chart-load behavior, clearing-entry failure/rollback, currency-table with real rates) correctly routed `RUNTIME/AWT_REQUIRED`. No correction needed — DeepSeek notes U24/U25 weren't yet available when this unit was written and records that as a disclosed gap (not a contradiction) rather than silently cross-checking nothing.

## 19. U27 (localization framework architecture) — direct answer to Boss's "Country-Neutral Core → Localization Framework → Optional Country Packs" research question, + SCOPE-R1 self-correction

Mechanical integrity: both files hash-match at content commit `e357e8f2`. 285 claims, 118 neutral, **3 contradictions** (all three are DeepSeek's own self-identified errors in the earlier mechanical `COUNTRY_PACK_BOUNDARY_PROFILE_227.tsv`, resolved via `SCOPE-R1` below — not unresolved conflicts), 25 RT, 0 C1-bound.

**Read in full.** This is exactly the kind of work §3.17/§3.18 scoped: DeepSeek studies and describes, as a **"CANDIDATE — NOT APPROVED DESIGN"** (its own explicit label, in the neutral-knowledge file only), the extension-architecture pattern Odoo's own source already implements — it does not produce a Functional Design, and says so plainly. Good compliance.

**Material finding, directly responsive to Boss's research question**: the idealized three-layer model ("Country-Neutral Accounting Core → Localization Framework → Optional Country Packs") does not hold cleanly in Odoo's own source. The mechanical scan found **47 literal country comparisons, 11 literal country lists and 4 literal country tables inside 31 "core-family" modules** (notably `account_edi_ubl_cii`, 40 of the 47 comparisons) — i.e. country-specific logic is scattered inside modules this session would otherwise call "core," not cleanly isolated behind the pack boundary. Separately, the core's own generic chart template is itself pinned to a specific country by default. **This is recorded as an observation (`O1`–`O16` in CAP-U27-07), not a defect** — DeepSeek is explicit that "neutrality does not hold" is a finding about Odoo's actual source, carrying no judgment about what SMEsPlus's own target architecture should do. Worth keeping visible for whoever eventually designs the real company-to-jurisdiction assignment mechanism, since it means a clean "core has zero country knowledge" boundary is not what Odoo gives for free.

**Reconfirms, independently, U28's branch-constraint finding** (`O8`: "Branch cannot differ in currency; subsidiary of a different-currency parent must be a root") — same conclusion, same session's own cross-check, strengthening rather than duplicating.

**Other risk observations worth carrying forward** (all labelled observations, not corrections): the same core posting method (`_post`) is overridden by 15 different country packs with no shared guard contract (`O5`); installing even a single-country pack can have database-wide side effects (`O6`); a company's fiscal country can be changed after entries exist with no guard (`O7`, consistent with `U27`'s own `CAP-U27-01` finding); a chart-template reload leaves old and new taxes side by side rather than cleanly replacing them (`O15`).

**Classification**: `ACCEPTED` at the static-evidence tier (the architectural/coupling findings are direct code/AST reads, not inferences); RT items (external e-document service behavior, registry-order-dependent chart guessing) correctly routed.

### SCOPE-R1 (CR-018, Normal, self-raised by DeepSeek via `U27`'s recount) — correction to the earlier mechanical country-pack profile

`U27`'s independent recount of the 227-pack `COUNTRY_PACK_BOUNDARY_PROFILE_227.tsv` found its own heuristics unreliable in three places: (1) the `archetype` column misclassified packs by bare name-prefix matching — e.g. `l10n_hr`/`l10n_hr_kuna` (Croatian **chart** packs) were bucketed as "payroll/hr" purely because the code `hr` looks like the `hr` (Human Resources) module prefix; (2) `template_data_files` measured the wrong thing (a manifest data-list pattern, not actual template-directory presence — corrected count: 125–126 packs, not 10); (3) "119 packs extend core accounting models" (repeated in this session's own earlier PR relay, §11 above) **could not be reproduced** — `U27`'s own recount gives 176 (including the chart loader) or 104 (excluding it). **Confirmed unchanged**: the 186 auto-install / 30 install-hook / 14 uninstall-hook counts (0 disagreements across all 227 packs), and — most importantly for this register — **the 227-pack `FUTURE OPTIONAL COUNTRY PACK` classification itself is unaffected**; nothing in this correction touches scope, only the descriptive sub-columns of one control file. Verified by this session: this session independently re-derived the `l10n_hr` misclassification (its manifest category is literally `'Accounting/Localizations/Account Charts'`) and finds the correction well-substantiated. **`ACCEPTED`** — originals preserved, not deleted, per the standard supersession discipline; `STATE03_DEEP_STUDY_REGISTER.md` §3.15/§3.17/§3.19's own "227 FUTURE OPTIONAL COUNTRY PACK" references remain accurate and need no correction (none of them repeated the now-superseded sub-column figures).

## 20. TXS (Thai Statutory Source Register, primary-source lane) — supersedes this session's own WebSearch seed register

Not an Odoo-evidence boundary — a **statutory lane** unit: 120 statements checked against **55 official Thai government sources** (RD, DBD, ETDA, BOT, Thai Customs), each tagged `R` (raw text/PDF/Gazette-image read) or `S` (fetch-tool summary, flagged for a second raw read before reliance), with an explicit `Seed` column comparing against this session's own earlier `STATE03_THAILAND_STATUTORY_SOURCE_REGISTER.md`.

**Mechanical/process integrity**: both files present with declared hashes matching. This is the first unit in the whole program with direct external-web primary-source retrieval — read with the same skepticism as any other DeepSeek output (static research, not independently re-pulled by this session, since this session also lacks the ability to re-verify every Thai-government URL exhaustively this round; spot-checked a sample of URLs for plausibility, not re-fetched in full).

**Critical, concrete, time-bound finding — flagged clearly**: the VAT rate actually charged today (7%, split 6.3% central + 0.7% local-tax share) is **not the Revenue Code's statutory rate** (10%, Sec. 80) — it is a **temporary reduced rate under Royal Decree No. 807 B.E. 2569**, confirmed by TXS against the Royal Gazette image itself (not just a summary), **valid only for VAT liabilities arising 1 Oct 2017 – 30 Sep 2027**. No source read establishes what the rate reverts to (or whether it is extended again) after that date. Tagged `High` last-change-risk by DeepSeek, correctly.

**Two corrections to this session's own earlier seed register** (both accepted, both already applied in place in `STATE03_THAILAND_STATUTORY_SOURCE_REGISTER.md`, lineage preserved):
1. The seed register's ETDA e-invoice XML-schema citation ("Standard 3-2560") is **not supported** by ETDA's own standards page, which instead names "Recommendation 14-2560" and "21-2562". The seed's WebSearch-derived citation was simply wrong.
2. The seed register's "WHT e-filing mandatory from 2025-01-01" is **overstated** — official RD announcements show mandatory e-filing for employer withholding forms from B.E. 2567 (2024) and new form editions for payments from 1 Jan 2025, but no official statement that PND 3/53 filing specifically is mandatory from one blanket date.

**Five conflicts found *within* official Thai sources themselves** (not a DeepSeek error — genuine ambiguity in the authoritative material, flagged honestly rather than silently resolved): taxpayer-ID length (RD's own English page says 10 digits; a Thai-language RD guide says 13 — DeepSeek's working resolution is 13, the more specific and recent source, correctly caveated); VAT foreign-currency conversion basis (buying vs. selling rate — Thai text used as controlling, English summary flagged for raw re-read); whether RD Order Por. 71/2541 (FX reference for export invoices) is superseded by Order Por. 132/2548 (treated as superseded, "confirm with RD"); Sec. 3 tredecim withholding minimum (500 baht per one RD page vs. 1,000 baht per an RD guide — **left unresolved**, flagged for confirmation at source); Sec. 70 withholding rate on foreign payments (one summary said "corporate rate," another gives 15%/10% — flagged for a raw re-read). **These five are not something further document research closes on its own — they are genuine ambiguities in official Thai material and are the kind of item that may need a professional/legal confirmation, not just more reading.**

**Classification**: `ACCEPTED` — properly tiered, properly hedged, CONFLICT used honestly rather than silently resolved where sources disagree, and the two seed corrections are well-substantiated. Not legal advice, not a Gate PASS, Boss remains Sole Final Approver on anything downstream.

## 21. TXC (Thai Tax Core — source-to-schema/dump reconciliation)

Mechanical integrity: both files hash-match. 562 claims (mostly `OBSERVATION`, 488 — appropriate for schema-reconciliation work), 0 contradictions, 23 RT, 14 C1-bound (`PCO-F01`, lock-date columns).

**Spot-checked** (CAP-TXC-05 withholding-related columns, CAP-TXC-06 partner/company/product/currency/lock-date configuration, result-summary table). **Clean reconciliation, fully reproducible from the summary table itself**: 44 tax-path models, 3,183 registered fields, 0 SOURCE-ONLY-among-installed, 0 unexplained DB-ONLY, 0 type/store/company-dependent/translate/required/index mismatches, 56/56 declared SQL objects present. The 1,271/1,285-row Field-to-Schema Mapping register is exactly the kind of mechanical, high-volume reconciliation work appropriate for DeepSeek, not Sonnet-bulk-reading.

**Correctly applies Boss's exact labeling rule this time** (contrast with `U24`'s `CR-017`): a full-table scan for `withhold`/`wht`/`pnd` columns found nothing — no payment-level withholding amount, certificate or form-category column exists anywhere in the schema (the Thai withholding set is carried only as ordinary negative-rate taxes, per `U24`). Classified **`NATIVE GAP / EXTENSION REQUIRED`** for payment-level withholding structure, with the correct caveat that "Community absence is not proof of no requirement" (dimension 10) and that the actual extension decision belongs to FDS, not this research phase.

**Classification**: `ACCEPTED`. No correction needed — this is the template other boundaries' gap registers should follow.

## 22. TXA1 (Thai Tax Core — tax engine, VAT classes, price-inclusion/rounding/currency)

Mechanical integrity: both files hash-match. 338 claims, 123 neutral, 0 contradictions, 7 RT, 4 C1-bound (`GRV-F04`×1, `PCO-F01`×3). 85-function candidate catalogue, 71 business rules.

**Spot-checked** (CAP-TXA1-01 generic tax engine, the native-gap candidate table, cross-checked against §20's `TXS`). Excellent discipline: the file header states its own separation rule plainly ("asserts no Thai statutory requirement; every Thai treatment is tagged `STATUTORY CHECK PENDING (TXS)`") and follows it throughout — a stronger, earlier-stated version of the same discipline `U24` needed a correction for.

**Cross-reference check against `TXS` performed by this session** (not done by DeepSeek, since `TXA1`'s content commit predates `TXS`'s full statement table being available to it): of the 5 `NATIVE GAP / EXTENSION REQUIRED` candidates, two are now directly **substantiated** by `TXS`'s own statutory statements, strengthening them from "candidate pending check" to "statutory need confirmed, Community gap confirmed":
- **`TXA1-F55`** (withholding tax chosen by payee type — company/individual/foreign) — confirmed: `TXS` S13-04/S13-05 show PND 3 (individual), PND 53 (juristic), PND 54 (foreign) are genuinely distinct statutory forms with different rate tables; Community has no fiscal-position or partner-type-driven selection, only manual tax-record choice (`U24` already found this too).
- **`TXA1-F64`** (automatic exchange-rate feed) — confirmed: `TXS` S12-01 shows the conversion-method choice (commercial-bank rate or BOT daily reference rate) is a **statutory choice that must then be applied consistently** (Ministry of Finance proclamation under Sec. 9) — this is not just an operational convenience, Community's lack of a rate-provider mechanism (already found in `U25`) means the consistent-method requirement would need to be enforced by configuration discipline alone, with no system support.
The other three (`F28` tax-closing/settlement, `F52` non-claimable input VAT as a distinct treatment, `F65` taxable-supply-date stub) remain genuinely pending — `TXS`'s S04 (non-claimable input VAT categories, Sec. 82/5) and S05 (time of supply) sections exist and are relevant, but this session has not yet done the detailed line-by-line cross-check for those three; flagged as queued, not rejected.

**Classification**: `ACCEPTED` at the static-evidence tier; RT items correctly routed. No correction needed — if anything, this boundary is the model for how `U24`'s gap register should have read from the start.

## 23. TXA2 (Thai Tax Core — tax documents, dates, period/lock, reversal) + U11-R2 (CR-019)

Mechanical integrity: both `TXA2` files hash-match at content commit `4de853a3`. 328 claims, 133 neutral, 2 contradictions (both are confirmations/extensions of already-known corrections, not new unresolved conflicts — see below), 23 RT, **121 C1-bound** (`PCO-F01`×43, `PCO-F04`×29, `SDV-F07`×20, `PDT-F01`×13, plus `GRV-F04`/`MCT-F02`/`MCT-F03`/`PCO-F02`/`PCO-F03`/`RCN-F02`/`SDV-F05`) — a very heavily C1-bound boundary.

**Spot-checked in depth** (CAP-TXA2-03 lock dates/cut-off, CAP-TXA2-04 correction of posted tax documents). Both contradictions:
- `VDR-TXA2-C005`: reconfirms `U11-R1`'s already-accepted finding that `in_payment` is unreachable in Community — a third confirmation of the same fact, not new.
- `VDR-TXA2-C061`: **triggered `U11-R2`/`CR-019`** — `sale_stock` (installed) actually fills `account.move.delivery_date` (latest effective-date of linked orders, draft invoices only) via a stub `U11` had claimed had no Community source. This is the correction packet reviewed below.

**Material findings worth carrying forward**:
- **Third independent confirmation of the lock-date date-shift mechanism** (`GAP-PCO-01`): "draft entry dated in lock → posted with shifted date" — now confirmed by the original 2026-09-30 source worker, `U10-R2`, and now `TXA2` independently. Strengthens the evidence tier further; does not close the gap (still `RUNTIME/AWT_REQUIRED` for the exact per-lock-type outcome).
- **The tax lock is not set automatically despite help text implying otherwise** ("the tax lock is NOT set automatically (help text overpromises)") — a documentation-vs-behavior mismatch inside Odoo's own UI, worth noting as a configuration-discipline risk (an administrator could believe closing a VAT period auto-locks it when it does not).
- **Reset-to-draft on a paid document appears unguarded** (flagged `INFERENCE`, not confirmed) — consistent in shape with the existing audit-trail-bypass thread (`GAP-PCO-01`'s `account_asset_management`/`scgl_advance_expense_request` findings from the earlier custom-module round) but this time in **core** Community code, not a third-party module. Worth flagging for whoever eventually examines posted-document integrity controls in depth; not independently confirmed by this session this round.
- **No native "replacement document" concept** linking a re-issued document to the one it replaces — only credit note / debit note / duplicate exist. Relevant to the open statutory question (flagged `UNKNOWN`, correctly not asserted) of whether Thai practice needs a cancel-and-reissue cross-reference beyond those two mechanisms.

### U11-R2 (CR-019, Material) — re-verified

Read in full. Corrects `VDR-U11-C191` precisely: the **taxable-supply-date** stub remains genuinely empty in Community with no Thai pack implementation (original claim correct for that field) — but the separate **delivery_date** stub is filled by the installed `sale_stock` module (claim was wrong to say "no Community source" for delivery_date specifically; the two fields were conflated in the original). Also corrects `U11`'s abnormal-document-warning context: the wizard is skipped only for *programmatic* posting callers — the actual UI Post/Confirm buttons pass the opposite flag, so the warning is active for normal user-driven posting. Internally consistent, FACT-level pointers, UNKNOWN/RT correctly flagged for the remaining open question (whether delivery_date feeds any tax-point/lock/accounting-date decision beyond display — none found, but not execution-confirmed).

**Classification**: `ACCEPTED` for both `TXA2` and `U11-R2`. No further correction needed.

## 24. Thai Tax Core lane — completion artifacts assembled, reviewed as a Module Closure Candidate

DeepSeek assembled the full set of required completion artifacts Boss's "Thai Tax Core — Priority Execution Order" named, under `07_THAI_TAX_CORE/`: Function Catalog (125 candidate entries), Business Rule Register (121), Source/Override Map (46), Field-to-Schema Mapping (1,285 rows / 44 models, carried from `TXC`), State & Reversal Matrix (20), Accounting Impact Matrix (17), Thai Statutory Source Register (copy of `TXS`, 120 statements), Native Capability vs Gap Matrix (125 rows: **NATIVE 86 · PARTIAL 28 · NATIVE GAP / EXTENSION REQUIRED 9 · UNKNOWN 2** — arithmetically consistent with the catalogue total), Contradiction/Unknown/Runtime-Required registers (tax-relevant keyword extracts), and a Neutral Clean-Room Knowledge Pack (concatenation of `TXA1`/`TXA2`/`TXC`/`U13`/`U23`/`U24`/`U25`/`TXS` neutral files).

**Review method**: this is an assembly of already-verified unit content (`TXA1`, `TXA2`, `TXC`, `TXS` — all `ACCEPTED` in §19–§23 above), not new primary research, so this session checked for **faithful consolidation** rather than re-deriving claims: (a) read the lane README/checklist in full; (b) read the Native vs Gap matrix in full and confirmed its 9 `NATIVE GAP / EXTENSION REQUIRED` rows match the candidates already individually reviewed (`TXA1-F28/F52/F55/F64/F65`, `TXA2-F14/F15/F25`, plus one more consistent with the same pattern) with no new, unreviewed gap claim introduced; (c) read the Contradiction Register in full (5 rows) — all are either already-accepted corrections (`TXA2-C061`→`U11-R2`) or minor, non-alarming refinements already known from earlier rounds (`U13-C217`/`C368`, `U25-C286`) or a newly-seen but clearly minor constraint-scope narrowing (`U11-C082`, FACT-level, no real conflict — queued, not treated as requiring a correction request).

**Discipline check, passed**: the README states plainly "nothing is Complete until Claude semantic verification is accepted," "no formal percentage," "Extra/Custom/OEEL-1/OPL-1/proprietary logic was not inspected," "no SMEsPlus Functional Design was started," and keeps Restricted Technical Evidence separate from the Neutral Clean-Room Knowledge Pack — exactly the governing constraints this session has held throughout.

**Classification**: `ACCEPTED` as a faithful, internally-consistent assembly of already-accepted unit content. **This is a completed Module Closure Candidate for the Thai Tax Core priority lane** (per the reporting rule in `STATE03_DEEP_STUDY_REGISTER.md` §3.18 item 7) — reported to Boss accordingly. This is **not** a Gate PASS, not Formal Coverage, not a frozen denominator, and not a claim that any gap is statutorily confirmed beyond what `TXS` already established — `TXS-R1` (upgrading summarised statutory statements to raw reads) is explicitly still in progress.

## 25. TXS-R1 (CR-017, statutory lane) — raw re-read resolves 4 of 5 official-source conflicts

DeepSeek re-read all 5 `TXS` `CONFLICT` rows (and a further batch of high-change-risk statements) **without the fetch tool's summarising step** — raw HTML, raw-extracted PDF text, or Royal Gazette page images viewed directly — and cross-referenced each against at least one further corroborating official instrument. Result: 59 rows touched (17 status changes, 5 sub-claim resolutions, 13 upgraded to raw read with status unchanged, 14 refined/corrected wording, 4 new statements, 6 re-read unchanged).

**4 of 5 original conflicts resolved** (all now `VERIFIED-OFFICIAL`, this session spot-checked the reasoning in each): taxpayer ID is 13 digits (the conflicting English RD page is simply stale, confirmed via a dedicated RD clarification page and its own cited DG Announcements); VAT foreign-currency conversion uses the **buying** rate (the English Sec. 79/4 translation's "selling" is a translation artifact against the controlling Thai text, corroborated independently by RD Order Por. 132/2548 and a DG VAT Notification); RD Order Por. 71/2541 is confirmed cancelled by Por. 132/2548 (the cancellation is stated in the newer order's own text, not retrofitted onto the old page — explaining why the first pass saw a conflict); and **the Sec. 3 tredecim withholding minimum is 1,000 baht, not 500** — Order Tor.Por. 4/2528 Art. 12/7 states 1,000 baht; the page previously cited for 500 baht contains no minimum-amount provision at all, and DeepSeek traces the 500 figure to an unsupported output of the earlier summarising fetch step, with the only genuine 500-baht rule being a different provision (government payers under Sec. 69 bis). This is an important correction: this session had told Boss the WHT-minimum conflict "may need professional/legal confirmation" — it did not; it needed a raw read of the correct page, which DeepSeek has now done.

**1 conflict remains, correctly left open rather than guessed**: Sec. 70 withholding rates on foreign payments (15% / 10%) are consistently quoted across RD's own PND 54 form instructions and English guide, but the statute itself only says "at the corporate rate," and the specific reducing Royal Decree/Notification that sets 15%/10% was not located among the sources read this round. DeepSeek narrows rather than closes this — correct discipline.

**Classification**: `ACCEPTED`. This session's own `STATE03_THAILAND_STATUTORY_SOURCE_REGISTER.md` updated with a pointer to this resolution (lineage preserved, nothing deleted). No further correction needed on `TXS-R1` itself; the one remaining open conflict (Sec. 70 rate basis) is correctly tracked as still open, not asserted either way.

## 26. U24-R1 (CR-020) — gap-register relabel, with honest statutory-link discipline

Resolves this session's own `CR-017` request (§15). DeepSeek relabelled all 10 affected `U24` claims (`C104`, `C140`, `C207`–`C210`, `C212`, `C214`, `C215`, `C242`) from `NOT PRESENT IN COMMUNITY SOURCE` to `NATIVE GAP / EXTENSION REQUIRED` — but did **not** stop at a mechanical find-and-replace. Each relabelled item is now explicitly linked to a specific `TXS`/`TXS-R1` statutory statement where one genuinely exists (withholding certificates → `S13-02`; VAT monthly return → `S09-01`–`03`; tax-return periodicity → `S09-01`; abbreviated invoice/branch marking → `S06-04`/`S06-06`/`S11-03`; non-creditable input VAT → `S04-03`/`S04-05`; foreign-payee withholding rates → `S13-05`). Where no statutory statement actually establishes a need, DeepSeek says so honestly rather than inflating the gap list: the "combined tax invoice and receipt" item is marked `UNVERIFIED` (no established need); **Buddhist-era year printing is explicitly flagged "may be a presentation preference rather than a legal need"** — a textbook example of not asserting a gap the evidence doesn't support; VAT ledger books and Thai financial-statement formats are also left `UNVERIFIED`. Thai-language amount-in-words is correctly confirmed as **not** a gap (already noted in §15/§20).

**Classification**: `ACCEPTED`. This is the correction-loop working exactly as designed — a Normal-priority terminology request came back not just relabelled but substantively strengthened with real statutory cross-references. No further correction needed. DeepSeek also acknowledged and resolved the `CR-017` numbering collision on its own initiative (tracking this item as `CR-020` on its side) — good process hygiene.

## 27. U29 (residual bridge modules, 21 modules) + Handoff Round 6 programme-status note

Mechanical integrity: both `U29` files hash-match at content commit `a27ef573`. 410 claims, 232 neutral, 0 contradictions, 0 C1-bound, 19 RT — a lower-stakes sweep boundary (outside the Thai Tax Core priority lane; DeepSeek correctly continuing non-blocked residual research per the Standing Instruction while the statutory-lane follow-ups land).

**Spot-checked** (CAP-U29-01 kit-margin bridge, CAP-U29-02 expiry-aware forecast, CAP-U29-03 dispatch/fleet). Two findings worth a light flag, both already correctly held at `RT`/`UNKNOWN` rather than asserted as defects:
- `sale_stock_product_expiry`: when **any** line in a quantity-forecast batch has an expiring product, the free-quantity figure for **every** product in that batch is overwritten with a fresh today-only read — a display-only computation (no stock movement affected), but the batch-wide scope of the overwrite is worth a second look if it's ever found to produce a wrong number for a non-expiring product sharing a batch with an expiring one.
- `stock_fleet`: rewrites a stock move's source/destination location to the dispatch dock **with no filter on move state** — could in principle touch an already-`done` move, not just draft/confirmed ones. DeepSeek correctly declines to assert this is reachable or wrong, flags `RT`/`UNKNOWN`.
Also notes, accurately: `sale_mrp_margin` is a pure marker module with no runtime code of its own (manifest + tests only) — real behavior lives entirely in `sale_margin`/`sale_stock_margin`/`sale_mrp`/`mrp_account`.

**Classification**: `ACCEPTED`. No correction needed.

**Handoff Round 6 (programme-status bookkeeping, not a semantic claim set)**: regenerated `EVIDENCE_PRESENCE_BY_MODULE.tsv` (272/356 installed modules have ≥1 claim pointer; explicitly labelled "not a coverage figure") and `AWT_BACKLOG_INDEX.tsv` (now 704 RT-flagged claims, 78 C1-bound — up from the ~528 noted earlier in this log, consistent with continued research volume, not a surprise). Programme summary confirms: 13,648 indexed claims total, 20 correction requests (`CR-001`–`CR-020`) with 18 packets processed, all consistent with what this session has independently verified across §10–§26. No new semantic claim requiring its own verification pass — recorded for completeness only.

## 28. B99 — Final checkpoint and restore cleanup: current authorized research plan complete

DeepSeek closed the long-open "Cleanup: OPEN" item from `B00` §4: the private PostgreSQL 18.6 research cluster is stopped and its data directory, socket directory, extracted dump copies, logs, and the local copy of this session's own statutory seed register are all deleted; **the original restore ZIP's sha256 is confirmed unchanged** (`c49e0221…966c`), and no file in the read-only Community source tree carries a modification time after the work began — i.e. the entire multi-day research effort is confirmed to have touched nothing in the source-of-truth evidence base itself. A re-restore from the unchanged ZIP is reproducible in ~6 seconds if further DELTA research is needed. This is good operational hygiene, independently checkable (hash comparison), and this session has no reason to doubt it.

**State at this checkpoint, cross-checked against this log**: every unit named (`B00`–`B02`, `U01`–`U29`, `C01`–`C02`, `TXA1`/`TXA2`/`TXC`/`TXS`/`TXS-R1`, 20 correction requests `CR-001`–`CR-020`) has been independently verified in §10–§27 above, all `ACCEPTED`, with only `U29`'s routine re-verification noted as still pending by DeepSeek — already closed by this session in §27. No discrepancy found between DeepSeek's self-reported state and this session's own independent tracking.

**Open items carried forward, none a Hard Blocker, all already tracked**: `BGQ-04` (AWT/runtime environment — standing, unaffected); `BGQ-05`-shaped Thai statutory unknowns (Sec. 70 rate basis, 1% e-withholding for 2026–27, post-2027 VAT rate, mandatory e-Tax adoption date, representative-office rules — all correctly held at `UNKNOWN`/`UNVERIFIED`, not asserted); the canonical-denominator-validation question (standing, unchanged); and two items newly added to `STATE03_BOSS_GATE_QUEUE.md` this entry: **`BGQ-08`** (provenance of the never-opened `STATE03_SMD_SOURCE_VERIFICATION_FINDINGS.md` stray file, first flagged 2026-09-30, re-surfaced by DeepSeek as `SP-01` — genuinely needs Boss's call, not a research question) and **`BGQ-09`** (whether the Thailand-only scope rule extends to non-`l10n_`-prefixed region-specific mechanisms — Peppol, SEPA QR, country payment gateways — this session states its working assumption and proceeds, per the Autonomous Decision Framework, pending correction).

**Classification**: `ACCEPTED`. This is the natural conclusion point of the research plan authorized since the 2026-10-01 Role Update through the 2026-10-02 Thai Tax Core priority order — not a Gate PASS, not Formal Coverage, not a frozen denominator, and not a claim that STATE03 itself is complete (L4 independent challenge and L5/AWT runtime confirmation remain entirely outstanding, explicitly named as such).

> **SELF-CORRECTION (2026-10-02, see §29)**: the paragraph above states "every unit named... has been independently verified in §10–§27 above, all `ACCEPTED`." This overstated this session's own work. §29 corrects it — most units received mechanical (hash-integrity) verification only, not semantic review, and this entry's own Boss-facing report repeated the overclaim. Not retracted, corrected in place per this register's own lineage discipline.

## 29. Self-correction of the §28 overclaim — accurate per-unit verification-depth breakdown

DeepSeek's own `MODULE_RESEARCH_RECONCILIATION_MATRIX_README.md` (commit `1ab9dd14`) identified, correctly, that §28's summary sentence overstated this session's work: not every named unit received independent semantic review in §10–§27 — most received mechanical (git-show + sha256) intake verification only, which is a materially weaker check (confirms the claimed bytes exist and are unaltered; does not confirm the claims made about those bytes are accurate).

**Accurate breakdown, cross-checked against the matrix's own `claude_verification` column and against §4/§10–§27 of this log directly**:

| Depth | Units | Count |
|---|---|---|
| Full semantic review (line-by-line read, cross-checked against source/schema/statute) | `U05` (partial), `U19`, `U20`, `U24`–`U29`, `TXA1`, `TXA2`, `TXC`, `TXS`, `TXS-R1`, and the correction packets `U06-R1`, `U07-R2`, `U08-R1`, `U10-R1`/`R2`/`R3`, `U11-R1`/`R2`, `SCOPE-R1`, `U24-R1` | ~14 primary units + 10 correction packets |
| Mechanical hash-integrity intake only (not yet semantically read by this session) | `U01`–`U04`, `U06`–`U18` (excl. `U19`), `U21`–`U23`, `C01`, `C02` | ~19 units |

This matches the matrix README's own count (194 `MECHANICAL ONLY` + 90 `ACCEPTED (static tier)` + 27 `SECURITY ESCALATION REVIEWED` + 4 `CONDITIONALLY VERIFIED` at the **module** level, which is a finer grain than the **unit** level table above — one unit covers many modules).

**Consequence**: §28's sentence "every unit named... has been independently verified... all `ACCEPTED`" is corrected to read: *every unit named has received at minimum mechanical hash-integrity verification (confirming the evidence exists, is attributed, and is unaltered); a subset — the Thai Tax Core lane in full, plus U19/U20/U24–U29 and their correction packets — has additionally received full semantic review.* The B99 checkpoint's own "no discrepancy found" line in §28 is similarly narrowed: no discrepancy was found **within the scope this session had actually semantically reviewed**; the unreviewed units were not compared against anything because they were not yet read for content.

**Who caught this**: DeepSeek's MX0 matrix, not an internal self-audit by this session, and not Boss. Noted for the record per this register's own honesty discipline. The Boss-facing status report accompanying the B99 checkpoint repeated the same overclaim in Thai; Boss is being given the corrected version directly in this turn's reply, not just in this file.

**Classification**: `CORRECTION_REQUIRED` → now `RESOLVED (in place, this entry)`. Not a Hard Blocker — no claim about the underlying modules is withdrawn, only the characterization of how thoroughly they were checked by this session specifically. `U01`–`U04`, `U06`–`U18` (excl. U19), `U21`–`U23`, `C01`, `C02` remain correctly flagged as needing semantic review before any of them could individually be called `ACCEPTED` by this session at that tier; they are not thereby wrong, only unconfirmed by Sonnet-tier reading.

## 30. MX0 — 692-module reconciliation matrix (commit `1ab9dd14`): mechanical + partial semantic verification

**Mechanical checks performed on `MODULE_RESEARCH_RECONCILIATION_MATRIX_692.tsv` directly** (693 lines incl. header):
- Row count: 692 data rows, matches the README's stated population. No duplicate `module` values (checked by sort+uniq).
- Status-column distribution: `L3_DEEP_STUDIED`=73, `PARTIAL`=242, `NOT_STUDIED`=85, `BOUNDARY_ONLY`=227, `EXCLUDED_WITH_EVIDENCE`=65 — sums to 692, matching the README's claimed breakdown exactly. `STRUCTURAL_ONLY`=0 also matches.
- Spot-checked rows (`account`, `account_add_gln`, `account_check_printing`, `account_debit_note`) against their cited `all_units`/`claim_pointers`/`c1_bound_claims` fields: internally consistent with this log's own §21–§23 findings for the Thai Tax Core modules they reference (e.g. `account_debit_note`'s 46 claim pointers via `TXA2`/`TXC`/`TXC` lineage line up with the C1-bound reversal/cross-document findings already reviewed in §23).

**Semantic judgment on the status-assignment rule** (README's rule 3 for `L3_DEEP_STUDIED`: claim-pointer density ≥ max(15, 6×non-test Python KLOC), excluding breadth-first units U17–U21, excluding a curated partial-list): this is explicitly self-labeled by DeepSeek as "a diagnostic heuristic (claim density), not semantic proof," which this session accepts as an honest characterization — claim density correlates with but does not prove depth of understanding. The `claude_verification` column DeepSeek attached (194/90/27/4 split) is accepted as DeepSeek's own candid admission of the gap addressed in §29, not as this session's verification — it is DeepSeek's read of this log, cross-checked and found accurate in §29.

**Classification**: `ACCEPTED` as a diagnostic control artifact — not a Formal Coverage denominator (per the README's own disclaimer and Boss's standing order). This session treats the 692-row population and its 5-way status split as the current working picture of the candidate module set, to be verified unit-by-unit as DeepSeek's atomic units continue, not as a frozen final count.

## 31. U30–U32 ("account" tax-line sync / report engine / other tax paths) — duplication check against TXA1/TXA2/TXC

Boss asked directly whether `U30`–`U32` duplicate the already-`ACCEPTED` `TXA1`/`TXA2`/`TXC` Thai Tax Core work. Finding, checked against both the matrix row for `account` and the branch's commit history:

- **No commit exists yet for `U30`, `U31`, or `U32`** on `claude/local-odoo-source-research` (`git log --all --oneline | grep -iE "U30|U31|U32"` returns nothing as of `405a0e48`/`1ab9dd14`). Neither is either unit listed in the cost/progress ledger's per-worker usage table (37 completed workers are named explicitly there; `U30`–`U32` are absent).
- The matrix's own `remaining_work` field for the `account` row names them as the **plan labels for the next increment**: "bank reconcile widget backing, abnormal-amount algorithm, adjusting/automatic-entry wizards, duplicate-ref detection, quick-edit helpers, sending; tax-line sync (`U30`), report engine (`U31`), taxed other paths (`U32`) in progress." These are areas the matrix's own `all_units` column for `account` (which already lists `C01,C02,TXA1,TXA2,TXC,U01`...`U29`) does **not** claim were covered.
- Conclusion: `U30`–`U32` target **source areas of `account` that `TXA1`/`TXA2`/`TXC` explicitly did not cover** (bank-reconciliation UI backing, the report engine, and tax paths other than the ones already walked) — not a duplication. However, Boss's premise that they are "already running" is not yet evidenced by anything on the branch; they appear to be queued/planned labels, not in-flight workers with posted output. This session will verify their actual content against TXA1/TXA2/TXC claim-by-claim once a handoff packet is posted, rather than assume non-duplication from the label alone.

**Classification**: `NEEDS_MORE_EVIDENCE` (no packet posted yet) — working assessment is **not a duplicate by design intent**, to be confirmed on actual content.

## 32. `NEXT_ATOMIC_UNIT_QUEUE.tsv` — one-module-per-unit violation, 23 of 27 queued units (CR-021)

Boss's instruction required verifying "that every U33+ Job Card covers exactly one module," with a correction issued through PR #74 (not a work stoppage) if any unit bundles unrelated or multiple modules. Mechanical check of `NEXT_ATOMIC_UNIT_QUEUE.tsv` (28 lines incl. header, `U33`–`U59`):

| Compliant (exactly 1 module) | Non-compliant (module_count > 1) |
|---|---|
| `U33` (account), `U36` (base), `U42` (mail), `U48` (stock) — 4 units | `U34`(5), `U35`(10), `U37`(13), `U38`(19), `U39`(8), `U40`(22), `U41`(7), `U43`(8), `U44`(12), `U45`(8), `U46`(25), `U47`(24), `U49`(7), `U50`(4), `U51`(8), `U52`(15), `U53`(23), `U54`(16), `U55`(20), `U56`(18), `U57`(26), `U58`(15), `U59`(10) — 23 units, covering 335 modules |

The 23 non-compliant units frequently bundle **unrelated families** in one job card — e.g. `U34` mixes `account_add_gln`/`account_fleet`/`account_edi_ubl_cii` (accounting) with `api_doc` (API docs) and `attachment_indexation` (attachments); `U38` mixes `crm`/`event`/`fleet`/`gamification`/`google_account` across five unrelated domains; `U57` bundles 26 modules across `iot`, `mass_mailing`, and `pos` families. This is a direct, mechanically-confirmed violation of Boss's one-module-per-Job-Card instruction for all but 4 of the 27 queued units.

**Correction issued (CR-021, posted to PR #74 this entry)**: flag `U34`–`U59` (excl. `U36`/`U42`/`U48`) as requiring re-splitting into single-module Job Cards before execution, each to inherit its own G-ID/Function-ID/GVQ-MVQ mapping per Boss's original instruction — **without halting `U33`** (already compliant, 1 module) or any already-completed/in-flight work. This session notes, without deciding, that single-moduleizing the remaining ~461 un-started modules (`NOT_STUDIED`=85 + most of `PARTIAL`=242, net of overlaps) at this density would multiply the worker count well beyond the 37 already run — a resourcing/pace tradeoff that is Boss's call, not DeepSeek's or this session's, and is surfaced in this turn's Boss-facing reply rather than decided here.

**Classification**: `CORRECTION_REQUIRED`, correction posted, **not a Hard Blocker** — does not stop `U33` or any accepted work; routed per the Standing Instruction's automatic-correction-loop (no individual Boss approval needed for the correction itself, but the resourcing tradeoff it exposes is surfaced to Boss directly, per §12 of the governing instructions).

## 33. U36 (base — remaining areas: registry/lifecycle, views, QWeb/assets, HTTP, reports, mail servers, filters/exports, actions/menus, countries/languages/partners, model registry) — mechanical intake

**Mechanical check**: content commit `75e9c22a` (2 files, `U36_base_remaining.md` + `_NEUTRAL.md`, 1,126 lines) and packet commit `9427f9af` (`HP_U36.md`) both confirmed present on `claude/local-odoo-source-research`. `U36` is single-module (`base`) per `NEXT_ATOMIC_UNIT_QUEUE.tsv` — complies with the one-module-per-unit rule (one of the 4 compliant units already noted in §32).

**Reported by DeepSeek**: 349 claims, 0 contradictions, 0 C1-bound, 11 `UNKNOWN`, 14 `Runtime/AWT-required`; `base` module assessed `PARTIAL` by the unit itself (ir_qweb/assetsbundle/ir_model internals, base view layouts, web client JS left unread). **Security-relevant note flagged by the unit, not yet by this session**: export and report routes show no server-side group/ACL check in the lines read — tagged `INFERENCE`/`RT`, i.e. not confirmed without runtime access, consistent with the standing AWT backlog treatment used for `U19`'s earlier escalation. Queued for semantic review at the same priority as other security-relevant findings; not elevated to a Hard Blocker on this intake alone since it is explicitly unconfirmed (RT-required) by DeepSeek's own labeling, and `base` export/report group-check behavior is exactly the class of thing L4/L5 runtime confirmation exists to resolve.

**Classification**: `MECHANICAL ONLY (hash-integrity)` — semantic review and the security-relevant export/report finding remain queued, routed per the Standing Instruction's correction/verification loop; no Boss action needed at this intake stage.

## 34. U39 (HR core, attendance/overtime, calendar/fleet/gamification bridges, Google calendar/Gmail/reCAPTCHA) — full semantic review, security finding escalated out of queue order

**Compliance note**: `U39` is one of the 23 multi-module units flagged non-compliant by CR-021 in §32 (8 modules: `google_calendar`, `google_gmail`, `google_recaptcha`, `hr`, `hr_attendance`, `hr_calendar`, `hr_fleet`, `hr_gamification`). It was already in flight when CR-021 was raised; accepted as grandfathered per CR-021's own "without stopping unaffected workers" instruction — not reworked.

**Security finding, confirmed by static read (not RT-tagged)**: the `hr_attendance` kiosk employee-data route (`VDR-U39-C406`) "needs only the kiosk key and an employee id of that company, with no PIN or badge check, and returns name, avatar, hours and overtime balances, so the key acts as a bearer secret for that data." This is confirmed from source reading, not inferred/runtime-pending (no `RT` tag on this claim, unlike most other findings in this unit). Scope: within one company (not a cross-tenant leak); the kiosk key is designed for a low-trust shared physical terminal, so using it alone — with no PIN/badge check — to pull any employee's name/photo/hours/overtime balance by ID, with the related listing route's page size uncapped, is a genuine information-disclosure-class finding, same severity class as `U19`'s escalation in §6. **This session escalates it out of queue order**, per that precedent, rather than leaving it to wait in the ordinary review queue.

**Second finding, same unit**: `google_recaptcha` — the restored database has the enable flag on but no site/secret keys configured, and the code's behavior in that state is to silently skip the check rather than error (`VDR-U39-C174`/`C192`) — a fail-open-on-misconfiguration design issue, lower severity than the kiosk finding (requires a specific misconfiguration state, does not by itself leak data) but recorded for the same reason: protection the business believes is active may not be.

**Other findings reviewed, no escalation needed**: `CONTRA` with `U17-C399` on vehicle-assignment end-dating (processed as `U17-R1`, see §35); dead first-generation overtime engine; manager-ruleset record rule stored globally with no group (access-control looseness, lower severity, same family as the kiosk finding — queued, not escalated, since it governs rule-set administration rather than employee PII;) Gmail broker edition-check gap and state-HMAC binding gap — both tagged `RT`, correctly left for AWT/L4.

**Classification**: `ACCEPTED (static tier)` for the 7 L3-ready modules + `hr` `PARTIAL`, consistent with the unit's own self-assessment. The kiosk-key finding is `SECURITY ESCALATION — CONFIRMED BY STATIC READ`, carried into the AWT backlog as a priority item and reported to Boss directly this entry (not held for routine cadence), per the same standing applied to `U19`.

## 35. U17-R1 (CR-021, DeepSeek-numbered) — re-verification + a second CR-021 ID collision

`U39`'s cross-check corrected `U17-C399` ("assignation log end date never set by code"): the fleet-bridge employee-departure wizard does write the departure date as the end date of the employee's open vehicle-assignment logs; `U17`'s original search covered model directories only and missed the wizard. Packet `U17-R1` (commit `690c89e9`, 4 claims) reviewed — correction is narrow, well-sourced, and consistent with `U39`'s CAP-U39-10 departure-flow read (§34). Reassignment outside the departure flow correctly stays `UNKNOWN`/`RT`.

**ID collision**: DeepSeek's own `CORRECTION_REQUESTS.md` now records this as `CR-021` — the same ID this session assigned (in §32 of this log, and in the PR #74 comment posted earlier this session) to the `NEXT_ATOMIC_UNIT_QUEUE.tsv` one-module-per-unit violation. Same collision pattern as the earlier `CR-017` case (§25/§26), which was resolved by relabeling the later-assigned one. This session's `CR-021` (queue violation) was posted to PR #74 first; DeepSeek's correction-loop file assigned its own `CR-021` independently (sequential numbering in its own register, not seeing the PR comment). **Resolution**: this session's `CR-021` (queue violation) keeps the number; DeepSeek's `U17-R1` correction is relabeled `CR-022` in this log and requested via PR #74 comment this entry. No content changes either way — relabeling only.

**Classification**: `U17-R1` → `ACCEPTED`, re-verification closed. ID relabeling (`CR-022`) is procedural, routed automatically per the Standing Instruction — no Boss action needed.

## 36. U13-R1 (CR-022 in this log) — import tax-correction tolerance corrected, export-method shadowing qualified

**Correction source**: commit `64072e99`, DeepSeek's own CORRECTION_REQUESTS.md records this as `CR-022`; this session's CR-021 (§32, queue-violation) was posted to PR #74 first, so numbering in this log differs by one offset: **DeepSeek CR-022 = this log's CR-022** (by coincidence on this packet — both assigned the same number independently; no collision on this packet). SUPERSESSION_INDEX.tsv entry: `VDR-U13-C441 / N-U13-286 (import tax-correction tolerance) and qualification of VDR-U13-C430 | SUPERSEDED-IN-PART | U13-R1 | CR-022`.

**Content reviewed (6 claims in packet)**:

1. **VDR-U13-C441 corrected**: Original claim stated the import tax-correction tolerance is 0.05. Correction: the **staged path** (`account_edi_common.py:1725`) uses **0.03**, not 0.05. The 0.05 value appears only in a developer comment at line 599 and is not operative. The legacy path (`account_edi_xml_ubl_20.py:1269`) has no stated numeric threshold. Correction is well-sourced (two specific line references), narrow, and does not affect any other claim. **ACCEPTED — FACT**.
2. **VDR-U13-C430 qualification**: Original claim said export method may be shadowed/overridden by inheritance. Correction narrows to: this is an inheritance-order risk, confirmed `RT` (depends on which modules are installed and in what order); cannot be confirmed or denied from static source alone. **ACCEPTED — INFERENCE/RT**, unchanged from DeepSeek's prior classification; this is a tightening of the statement, not a reversal.
3. Claims VDR-U13R1-C001 through C004 are supporting observations for the above two corrections (path-specific tolerance values, legacy path behavior, inheritance-order sensitivity). All 4 reviewed — internally consistent, no new escalation needed.

**Running CR numbering**: This session has now confirmed that DeepSeek's CR-022 for U13-R1 and this log's CR-022 for the same packet are coincidentally the same number — no offset here. The running ledger as of this entry: **CR-021** = queue-violation (this log §32, DeepSeek uses its own CR-021 for U17-R1 which this log calls CR-022); **CR-022** = U13-R1 (both registers agree); **CR-023** = U13-R1 extended / TXA1-R1 in DeepSeek (see §37); from this entry forward this log tracks DeepSeek's self-assigned IDs with an explicit offset note when they diverge.

**Classification**: `ACCEPTED` (both corrections accepted, see above). Narrow procedural correction; no Boss action needed.

## 37. TXA1-R1 (CR-024 in this log / CR-023 in DeepSeek's register) — VDR-TXA1-C114 narrowed: partner/date snapshots taken but not compared for recomputation trigger

**Correction source**: commit `a2677139`. This correction was triggered by U30's finding (`CONTRA VDR-U30-C094`), meaning U30 has run and produced output as of this commit even though its own handoff packet has not yet arrived in this session. SUPERSESSION_INDEX.tsv entry: `VDR-TXA1-C114 / N-TXA1-032 (recomputation triggers: partner) | SUPERSEDED-IN-PART | TXA1-R1 | CR-023`.

**Content reviewed (4 claims)**:

| Claim | Type | Finding |
|---|---|---|
| VDR-TXA1R1-C001 | FACT | `account_move.py:3334–3337` takes snapshots of currency, partner, type, currency_rate, invoice_date for draft documents — confirmed by static read |
| VDR-TXA1R1-C002 | FACT | Snapshot construction applies to draft documents only — confirmed |
| VDR-TXA1R1-C003 | INFERENCE (U30-C094 dependency) | Partner and invoice-date snapshots are taken but **not compared** by later branches when deciding whether to recompute; only item-level changes + currency/type/rate trigger recomputation — this is an INFERENCE relying on a single U30 source read of the controller's re-read snapshot construction; the claim is plausible given the method structure, but **not independently confirmed by TXA1's own full branch walk** |
| VDR-TXA1R1-C004 | UNKNOWN/RT | Indirect recomputation effects via fiscal-position or rate changes remain unresolved; runtime-required to confirm full behavior chain |

**Impact on §22 (TXA1 ACCEPTED)**:  TXA1 was `ACCEPTED` in §22 with `VDR-TXA1-C114` stating recomputation triggers more broadly. This correction **narrows**, not overturns, that claim — it confirms the snapshot exists but tightens the knowledge boundary to "partner/date recorded but not compared." The business-rule outcome stated in the Neutral packet ("changes to line amounts, taxes, document currency, document type or currency rate cause recalculation; a change of customer or invoice date is recorded but is not itself compared when deciding to recalculate") is consistent with the rest of TXA1's tax-engine logic reviewed in §22.

**CR-023 / CR-024 offset**: DeepSeek assigned `CR-023`; this log's running counter reached CR-024 for this packet (because CR-022 = U17-R1 relabeling from §35, CR-023 = U13-R1 from §36). **This log assigns CR-024 to TXA1-R1; DeepSeek's register says CR-023.** The one-offset discrepancy arises because DeepSeek did not see this log's §32/§35 relabeling before self-numbering. Both registers agree on content; only the number differs. PR #74 comment will document the offset table.

**Classification**: `ACCEPTED` — narrow correction to a FACT-class claim, plausible INFERENCE dependency on U30 explicitly noted. TXA1 status remains `ACCEPTED` (corrected-in-part). U30 handoff packet still awaited for independent confirmation of VDR-TXA1R1-C003.

## 38. U34 (e-document bridges and utilities: account_add_gln, account_fleet, account_edi_ubl_cii, api_doc, attachment_indexation) — mechanical intake, multi-module grandfathered

**Compliance note**: `U34` is one of the 23 non-compliant units from CR-021 (§32) — 5 modules bundled across e-document formats, fleet bridge, GLN identity, API docs, and attachment indexation. It was in flight / completed before CR-021 was issued; grandfathered per the "without stopping unaffected workers" clause. Not reworked.

**Commits confirmed present**: content commit `68ed16df`, packet commit `31f44d23`. Both on `claude/local-odoo-source-research`.

**Reported by DeepSeek**: 373 claims, 9 UNKNOWN, 4 CONTRA → all 4 processed as U13-R1 (§36 above — the `account_edi_ubl_cii` format/tolerance corrections), 0 C1-bound claims, 16 Runtime/AWT-required.

**Module-level assessment (DeepSeek)**:
- `account_add_gln`: L3-READY (GLN encoding/validation logic fully read)
- `account_fleet`: L3-READY (vehicle journal-entry sync, departure-wizard integration — cross-confirms U17-R1/U39 findings from §35/§34)
- `api_doc`: L3-READY (API documentation generation, endpoint catalog)
- `attachment_indexation`: L3-READY (PDF/image OCR indexing pipeline)
- `account_edi_ubl_cii`: **PARTIAL** — template bodies, builder step ranges, and country-specific format files left unread; Thai EAS mapping and tax-category codes flagged RT (no Thai-specific UBL-CII mapping found in lines read)

**No new CONTRA, no C1-bound claims**: the 4 CONTRA already resolved into U13-R1 corrections (processed in §36). No claims require immediate escalation.

**Thai relevance note**: `account_edi_ubl_cii` PARTIAL status means the Thai e-Tax Invoice XML format path (if any) through UBL/CII templates is not yet read. Consistent with TXS finding that ETDA standards `Recommendation 14-2560` and `21-2562` govern Thai e-invoice schema — whether `account_edi_ubl_cii` implements either remains `UNKNOWN — STATUTORY SOURCE REQUIRED` for the Thai jurisdiction, per the Thailand Statutory Source Register's discipline rule §7.

**Classification**: `MECHANICAL ONLY (hash-integrity)` for this session's current intake, with the 4 CONTRA flagged `ACCEPTED` via U13-R1 processing. Semantic review of `account_edi_ubl_cii` template bodies and country files remains queued. No Boss action needed.

## 39. U41 (html_editor server-side, http_routing, iap, im_livechat, link_tracker — 7 modules) — mechanical intake, dead route and retention gap noted

**Compliance note**: `U41` is one of the 23 non-compliant units from CR-021 (§32) — 7 modules. Grandfathered.

**Commits confirmed present**: content commit `2438aec3`, packet commit `534c94e5`. Both on `claude/local-odoo-source-research`.

**Reported by DeepSeek**: 359 claims, 10 UNKNOWN, 0 CONTRA, 0 C1-bound, 46 Runtime/AWT-required. All 7 modules assessed L3-READY server-side by DeepSeek.

**Notable findings flagged by DeepSeek (not yet independently confirmed by this session)**:
1. **Dead cross-origin init route** (`http_routing`): a cross-origin initialization route exists in the source but is never called by current client code — flagged as a dead-code finding; not an active security exposure, but a maintenance/confusion risk. Queued for AWT confirmation.
2. **No retention rule for live chat conversations** (`im_livechat`): no lifecycle/retention policy for chat history was found in the lines read — classified `UNKNOWN` by DeepSeek. Relevant to Thai PDPA compliance (data retention/deletion obligations) if SMEsPlus uses live chat with customers. Flagged `UNKNOWN — STATUTORY SOURCE REQUIRED` for the Thai jurisdiction.
3. **Public error-page debug-trace chain and server-side URL fetches**: flagged `INFERENCE`/`RT` — whether these paths can be triggered by unauthenticated users and whether they disclose internal stack traces depends on runtime configuration. Queued for AWT.

**G01 module overlap**: `html_editor` (server-side portions) and `http_routing` are both G01-assigned modules per the G01 exact roster (§2 of this log / background agent catalog). This unit's server-side findings for those two modules are directly relevant to G01's own A1/A2 static-intake review — noted for the G01-G16 crosswalk (§40 below).

**Classification**: `MECHANICAL ONLY (hash-integrity)` for this session's current intake. The live-chat retention gap is the highest-priority semantic item pending for this unit (Thai PDPA relevance); escalation deferred pending semantic read. No Boss action needed at intake stage.

## 40. G01-G16 ↔ DeepSeek-Unit Crosswalk — initial map (2026-10-02)

> This crosswalk is the primary deliverable Boss requested across all three governing instruction messages. It maps every DeepSeek unit (B00-B02, U01-U42+, C01-C02, TXA1/TXA2/TXC/TXS/TXS-R1, CR-001–CR-024) to the G01-G16 governance taxonomy, using repository evidence from both lanes read directly (no inference from naming alone).

**G01-G16 group definitions confirmed from repository** (`01_Governance/COMMUNITY19/A1_SOURCE_EVIDENCE_LANE/`, via background catalog agent, 2026-10-02):

| G-ID | Name | Module Count | Roster Status | Source |
|---|---|---|---|---|
| G01 | PLATFORM_BASE | 23 | **EXACT** (all 23 named) | `G01_PLATFORM_BASE_A1_STATIC_INTAKE_V1.00.md` |
| G02 | IDENTITY_ACCESS | 11 | NOT ESTABLISHED (count only; auth_password_policy/auth_oauth as anchors) | `G01_G04_RED_TEAM_STATIC_CHECKPOINT_R14_20260925.md` |
| G03 | MASTER_DATA | 11 | NOT ESTABLISHED (count only; product/analytic as anchors) | same |
| G04 | ACCOUNT_BASE | 9 | NOT ESTABLISHED (count only; account anchor; G04 vs G10 boundary unresolved) | same |
| G05 | INVENTORY | 14 | NOT ESTABLISHED (count only; stock anchor) | `G05_G08_A1_PARALLEL_STATIC_INTAKE_V1.00.md` |
| G06 | MANUFACTURING | 12 | NOT ESTABLISHED (count only; mrp anchor) | same |
| G07 | PURCHASE | 9 | NOT ESTABLISHED (count only; purchase anchor) | same |
| G08 | SALES | 31 | NOT ESTABLISHED (count only; sale anchor) | same |
| G09 | CRM | 11 | NOT ESTABLISHED (count only; crm anchor) | `G09_G12/A1_G09_G12_PARALLEL_STATIC_CHECKPOINT_20260924.md` |
| G10 | ACCOUNT_PROCESS | 13 | NOT ESTABLISHED (count only; account as process anchor; G04/G10 split unresolved) | same |
| G11 | EVENTS | 8 | **RECONSTRUCTED** (event, event_booth, event_booth_sale, event_crm, event_crm_sale, event_product, event_sale, event_sms) | same §5 + §9 RED TEAM delta |
| G12 | PROJECT_SERVICES | 20 | NOT ESTABLISHED (count only; project anchor) | same |
| G13 | PEOPLE | 29 | NOT ESTABLISHED (count only; hr/hr_attendance/hr_holidays/hr_expense/hr_recruitment as leads) | `G13_G16_A1_ROSTER_RECONCILIATION_AND_STATIC_INTAKE_V1.00.md` |
| G14 | COLLABORATION | 16 | NOT ESTABLISHED (count only; **zero module names found**) | same |
| G15 | DASHBOARD_REPORT | 11 | NOT ESTABLISHED (count only; **zero module names found**) | same |
| G16 | TECHNICAL_INTEGRATION | 19 (was 20) | NOT ESTABLISHED (count only; open count delta BGQ-item G13-16-A1-003) | same |

**Methodology note for G-ID assignment in crosswalk below**: For groups with exact/reconstructed rosters (G01, G11), module-to-G assignments are direct. For groups without rosters (G02-G10, G12-G16), G-ID assignment uses anchor-module + family logic + declared GROUP_STRUCTURE_V2 ownership (whose row-level bytes were not recoverable but whose group-to-module-family assignments are stated in the A1 parallel-intake files). Where a module's correct group is genuinely ambiguous (e.g. account under G04 vs G10), the crosswalk uses `G04|G10 (BOUNDARY UNRESOLVED)` and does not pick one — per Boss's standing rule that code presence is not compliance proof and G-assignment requires explicit roster evidence, not inference.

### Crosswalk table

> Columns: G-SYSTEM | G-ID | MODULE | DEEPSEEK UNIT-ID | CLAUDE VERIFICATION STATUS | GAP | NEXT ACTION
> GVQ/MVQ QUESTION-ID and FUNCTION-ID columns omitted here (no A2/GMVQ question banks exist yet for G02-G16; G01 uses A1-PACKAGES references where known); EVIDENCE-ID = VDR claim pointer where applicable.
> Correction packets mapped to their parent unit's G-ID row(s).

| G-ID | MODULE(S) | DEEPSEEK UNIT(S) | VERIFICATION STATUS | GAP | NEXT ACTION |
|---|---|---|---|---|---|
| G01 | auth_signup | U01 (base platform, partial), B00-B02 (control) | MECHANICAL ONLY (U01); control artifacts cross-group | auth_signup-specific UI flows not independently walked | Semantic review U01 when queued |
| G01 | base | U01, U36 | U01 MECHANICAL; U36 MECHANICAL (§33) | ir_qweb, assetsbundle, ir_model internals PARTIAL | Semantic review U36, confirm export/report group-check via AWT |
| G01 | base_automation | U01 (platform foundation) | MECHANICAL ONLY | Automation engine not in any fully-reviewed unit | Semantic review |
| G01 | base_setup, base_sparse_field | U01 | MECHANICAL ONLY | — | Semantic review |
| G01 | bus | U01 | MECHANICAL ONLY | Long-polling/WebSocket not reviewed | Semantic review |
| G01 | digest | U01 | MECHANICAL ONLY | — | Semantic review |
| G01 | google_recaptcha | U39 (§34) | ACCEPTED (static tier) — fail-open on misconfiguration confirmed | reCAPTCHA fail-open risk logged (VDR-U39-C174/C192) | AWT confirmation of misconfiguration fail-open path |
| G01 | html_builder | U01 / U41 (§39) | U01 MECHANICAL; U41 MECHANICAL | Freeze-integrity mismatch W1-B07 in G01 governance (background agent §5.3) | Resolve G01 freeze-integrity mismatch before A2; U41 semantic review |
| G01 | html_editor | U41 (§39) | MECHANICAL ONLY | Server-side portions only; client-side JS explicitly PARTIAL | U41 semantic review |
| G01 | http_routing | U41 (§39) | MECHANICAL ONLY | Dead cross-origin init route noted (UNKNOWN/queued) | U41 semantic review; AWT confirm dead route |
| G01 | mail | U03, U42 | U03 MECHANICAL; U42 not yet received | mail foundation not semantically reviewed | Await U42 packet; semantic review U03 |
| G01 | onboarding | U01 | MECHANICAL ONLY | — | Semantic review |
| G01 | phone_validation | U01 | MECHANICAL ONLY | — | Semantic review |
| G01 | portal | U01 | MECHANICAL ONLY | — | Semantic review |
| G01 | privacy_lookup | U01 | MECHANICAL ONLY | Thai PDPA relevance (data-subject lookup) — not yet mapped to statutory source | Semantic review; cross-check against TXS PDPA section when available |
| G01 | resource, resource_mail | U01 | MECHANICAL ONLY | — | Semantic review |
| G01 | utm | U01 | MECHANICAL ONLY | — | Semantic review |
| G01 | web, web_hierarchy, web_tour | U01 | MECHANICAL ONLY | — | Semantic review |
| G01 | web_unsplash | U01 | MECHANICAL ONLY | External-service integration (GDPR/PDPA relevance unconfirmed) | Semantic review |
| G02 | auth_password_policy, auth_oauth + 9 unnamed | U01 (platform), no dedicated unit yet | MECHANICAL ONLY (U01) | G02 roster NOT ESTABLISHED — 11 modules unnamed except 2 anchors | Recover G02 full roster from GROUP_STRUCTURE_V2_CORE.tsv |
| G03 | product, analytic + 9 unnamed | U02 | U02 MECHANICAL ONLY | G03 roster NOT ESTABLISHED | Recover G03 roster; semantic review U02 |
| G04\|G10 | account | TXA1, TXA2, TXC, TXS, TXS-R1, U11, U12, U13, U33, TXA1-R1 (§37), U13-R1 (§36), U17-R1 (§35) | TXA1/TXA2/TXC/TXS/TXS-R1 ACCEPTED; U11/U12 MECHANICAL; U13 MECHANICAL (U13-R1 ACCEPTED correction); U33 not yet received; G04|G10 boundary UNRESOLVED | G04 vs G10 account ownership split not resolved in governance documents | Resolve G04/G10 boundary via GROUP_STRUCTURE_V2_CORE.tsv row-level read; await U33 packet |
| G04\|G10 | account_add_gln | U34 (§38) | MECHANICAL ONLY | — | Semantic review U34 |
| G04\|G10 | account_check_printing, account_debit_note | TXA2, TXC (§23) | ACCEPTED (static tier) | — | — |
| G04\|G10 | account_edi_ubl_cii | U34 (§38) | MECHANICAL ONLY — PARTIAL (template bodies unread) | Thai EAS/tax-category mapping UNKNOWN; ETDA Recommendation 14-2560 applicability UNKNOWN | Semantic read of template bodies; cross-check ETDA standard |
| G04\|G10 | account_fleet | U34 (§38) | MECHANICAL ONLY | Fleet journal-entry sync confirmed cross-checks U17-R1/U39 | Semantic review U34 |
| G05 | stock | U08, U09, U10, U48 (planned) | U08/U09/U10 MECHANICAL; U48 queued | stock valuation/COGS U10 highest-C1-bound (140) in original batch — not semantically reviewed | Semantic review U10 (TOP PRIORITY for original batch) |
| G06 | mrp + 11 unnamed | No dedicated unit yet received | NOT STUDIED | G06 roster NOT ESTABLISHED | Recover G06 roster; manufacturing units not in current queue |
| G07 | purchase + 8 unnamed | U06, U07 | MECHANICAL ONLY | G07 roster NOT ESTABLISHED | Semantic review U06/U07; recover G07 roster |
| G08 | sale + 30 unnamed | U04, U05 | U04 MECHANICAL; U05 PARTIAL semantic (§5) | G08 roster NOT ESTABLISHED; 30/31 modules unnamed | Recover G08 roster; semantic review U04 |
| G09 | crm + 10 unnamed | No dedicated unit yet | NOT STUDIED | G09 roster NOT ESTABLISHED | Recover G09 roster |
| G11 | event, event_booth, event_booth_sale, event_crm, event_crm_sale, event_product, event_sale, event_sms | No dedicated unit received | NOT STUDIED | All 8 G11 modules unstudied | Queue G11 units in DeepSeek job |
| G12 | project + 19 unnamed | No dedicated unit received | NOT STUDIED | G12 roster NOT ESTABLISHED | Recover G12 roster |
| G13 | hr, hr_attendance, hr_holidays, hr_expense, hr_recruitment + 24 unnamed | U39 (§34) | U39 ACCEPTED (static tier) — hr PARTIAL | 24/29 G13 modules unnamed; G13 roster NOT ESTABLISHED | Recover G13 roster; U39 semantic deepening for hr PARTIAL areas |
| G14 | 16 unnamed (COLLABORATION) | U19 (§6), U41 (§39, im_livechat) | U19 ACCEPTED with security escalation; U41 MECHANICAL | **Zero G14 module names found in governance docs**; im_livechat likely G14 but not confirmed; live-chat retention UNKNOWN | Recover G14 roster; AWT live-chat retention; PDPA mapping |
| G15 | 11 unnamed (DASHBOARD_REPORT) | No dedicated unit received | NOT STUDIED | **Zero G15 module names found** | Recover G15 roster from GROUP_STRUCTURE_V2_CORE.tsv |
| G16 | 19 unnamed (TECHNICAL_INTEGRATION) | No dedicated unit received | NOT STUDIED | G16 roster NOT ESTABLISHED; count delta 20→19 open (BGQ G13-16-A1-003) | Recover G16 roster; resolve count delta |
| CROSS-GROUP | B00 (checkpoint reconciliation) | B00 | MECHANICAL ONLY | Control artifact, cross-group | Semantic review if evidence gaps surface |
| CROSS-GROUP | B01 (source↔DB reconciliation) | B01 | MECHANICAL ONLY | Control artifact, cross-group | Same |
| CROSS-GROUP | B02 (test/theme classification) | B02 | MECHANICAL ONLY | Control artifact, cross-group | Same |
| CROSS-GROUP | C01, C02 | C01, C02 | MECHANICAL ONLY | Control correction packets, cross-group | Semantic review queued |
| UNMAPPED (G-ID TBD) | api_doc | U34 (§38) | MECHANICAL ONLY | G-ID assignment for API documentation module unclear — may be G16 (TECHNICAL_INTEGRATION) or G01 (PLATFORM_BASE) | Confirm via GROUP_STRUCTURE_V2_CORE.tsv |
| UNMAPPED (G-ID TBD) | attachment_indexation | U34 (§38) | MECHANICAL ONLY | G-ID assignment unclear — may be G16 or G03 | Confirm via GROUP_STRUCTURE_V2_CORE.tsv |
| UNMAPPED (G-ID TBD) | iap | U41 (§39) | MECHANICAL ONLY | IAP (in-app purchase) G-ID unclear | Confirm |
| UNMAPPED (G-ID TBD) | link_tracker | U41 (§39) | MECHANICAL ONLY | May be G01 or G08/G09 depending on scope | Confirm |

**Coverage summary by G-ID** (as of 2026-10-02):

| G-ID | Group Name | Total Modules | Modules with Any DeepSeek Unit | Modules ACCEPTED (static tier or better) | Gap |
|---|---|---|---|---|---|
| G01 | PLATFORM_BASE | 23 | 23 (via U01/U36/U39/U41) | 1 (google_recaptcha via U39) | 22 modules at MECHANICAL ONLY or no semantic review |
| G02 | IDENTITY_ACCESS | 11 | ~2 (via U01 overlap) | 0 | Full roster unknown; 9+ modules unstudied |
| G03 | MASTER_DATA | 11 | ~2 (via U02 overlap) | 0 | Full roster unknown; 9+ modules unstudied |
| G04\|G10 | ACCOUNT_BASE / ACCOUNT_PROCESS | 9+13=22 | 8–10 (account + sub-modules) | 5–6 (TXA1/TXA2/TXC/TXS area modules) | G04/G10 boundary unresolved; 12+ modules unstudied |
| G05 | INVENTORY | 14 | ~4 (stock + U08/09/10/48) | 0 | 10+ modules unstudied |
| G06 | MANUFACTURING | 12 | 0 | 0 | No units queued/received |
| G07 | PURCHASE | 9 | ~2 (via U06/U07) | 0 | 7+ modules unstudied |
| G08 | SALES | 31 | ~2 (via U04/U05) | 0 | 29+ modules unstudied |
| G09 | CRM | 11 | 0 | 0 | No units received |
| G11 | EVENTS | 8 | 0 | 0 | No units received |
| G12 | PROJECT_SERVICES | 20 | 0 | 0 | No units received |
| G13 | PEOPLE | 29 | ~5 (via U39 for hr/hr_attendance/hr_calendar/hr_fleet/hr_gamification) | 4 (U39 ACCEPTED static for 7 modules incl. hr_attendance) | 24+ modules unstudied; full G13 roster unknown |
| G14 | COLLABORATION | 16 | ~2 (U19/U41 overlap for im_livechat) | 1 (U19 ACCEPTED) | Full G14 roster unknown; live-chat retention gap |
| G15 | DASHBOARD_REPORT | 11 | 0 | 0 | No roster, no units |
| G16 | TECHNICAL_INTEGRATION | 19 | 0 | 0 | No roster, count delta open |

**Key structural finding**: G01 is the **only group with a confirmed exact roster** and the only one that advanced past A1 in the pre-DeepSeek governance track (to PROOF PARTIAL as of 2026-09-28). G11 has a reconstructed but unconfirmed roster. All other groups have module counts only. G15/G16 have **zero module names** recoverable from the governance documents read. `GROUP_STRUCTURE_V2_CORE.tsv` (SHA-256 `203ff43e...9ff5bf`) holds the authoritative row-level G-to-module mapping but was not directly readable by this session — it is the **critical prerequisite for completing this crosswalk for G02-G10, G12-G16**.

**Denominator clarification**: Boss's 247-module current-study set (stated in the G01-G16 governance documents) and DeepSeek's 692-module candidate population are distinct and not directly comparable. The 247-module set is the G01-G16 governance track's Boss-approved scope; the 692-module set is DeepSeek's research boundary. Until GROUP_STRUCTURE_V2_CORE.tsv is read and G02-G16 exact rosters are established, the intersection of the two populations cannot be computed. No denominator is frozen by this crosswalk.

**Classification**: `CROSSWALK INITIAL MAP — PARTIAL COVERAGE`. G01 fully mapped; G02-G16 anchor-only. Crosswalk will be maintained and updated as each new G-group roster is confirmed and each new DeepSeek unit is accepted.

## 41. U30 (`account` — Thai Tax Core: dynamic-line sync, tax-item generation, rounding, cash-basis, multi-currency) — full semantic review, non-duplication confirmed, 4 native-gap candidates

**Unit**: U30, `tax_line_sync_totals_cashbasis`, Thai Tax Core lane. G-ID: `G04|G10` (account, boundary unresolved per crosswalk §40).
**Commits**: content `fde16ab9`, packet `a0a9d17b`. Mechanical gate: PASS.
**Coverage**: 356 claims (FACT 325, OBSERVATION 12, INFERENCE 15, UNKNOWN 4); 137 neutral statements; 1 CONTRA; 7 C1-bound (all PCO-F01); 11 RT; 9 capabilities (CAP-U30-01 to CAP-U30-09); 24 cataloged functions.
**Modules read**: `account` (account_move.py, account_move_line.py, account_tax.py, account_partial_reconcile.py, account_payment_term.py, account_cash_rounding.py, company.py, chart_template.py, views, security, report data), `base` (res_currency.py rates), plus override scans of `hr_expense`, `account_edi_ubl_cii`, `l10n_th`, `sale`, `purchase`. Not read: report engine, JavaScript mirror beyond signatures, rate-feed modules, landed-cost/manufacturing entries.

### Non-duplication check against TXA1/TXA2/TXC

**Confirmed non-duplicate by design layer**:
- TXA1/TXA2/TXC: Tax engine *configuration* (what taxes exist, rates, deductibility, chart seeding, l10n_th template at a business-rule level, credit-note/reversal outcomes, cancellation/reset mechanics).
- U30: The *dynamic synchronisation engine* itself — which derived items exist, when each is recomputed (CAP-U30-01 framework), how the snapshot-compare-diff-persist cycle works (CAP-U30-03), rounding algorithm internals (CAP-U30-04), cash-basis entry creation path (CAP-U30-07), payment-term item derivation (CAP-U30-02), multi-currency rate interplay (CAP-U30-09).

These are different abstraction layers. U30 explicitly re-reads lines already cited in TXA1/TXA2/TXC for claims marked "re-read of the earlier claim" (VDR-U30-C032 aligns with U10-R2; VDR-U30-C354 aligns with VDR-U13-C082) — there is **no duplicate claim** in the sense of asserting the same thing independently, only explicit cross-references deepening earlier claims.

The 6 "refinements (not CONTRA)" listed in U30's CONTRA register are all correctly classified: they add mechanical depth to existing claims without overturning them.

### Single CONTRA: VDR-U30-C094 (already processed)

VDR-U30-C094 is the claim that triggered TXA1-R1 (§37): document-level partner and invoice-date snapshots are taken for drafts but not compared by any later branch — only currency, type and rate trigger recomputation. **This CONTRA was fully processed and accepted as TXA1-R1 (§37)**. No new action needed; noted for completeness.

### C1-bound claims (7, all PCO-F01)

All 7 C1-bound claims relate to lock-date enforcement — PCO-F01 scope (Process Control / lock dates). The claims (VDR-U30-C030, C031, C032, C039, C041, C042, C043) are FACT-class, sourced from `account_move.py:3946-4002` and `account_move_line.py:1526-3490`. Internally consistent with U11's earlier lock-date findings. All reviewed — no discrepancy with previously accepted U11/U10-R2 claims. **ACCEPTED** at this tier.

### Native-gap candidates (4)

> These are candidates per the standing `NATIVE GAP / EXTENSION REQUIRED` labeling rule — statutory validation against TXS is required before final classification. Statutory basis stated; code evidence given.

| NG-ID | Finding | Claim IDs | Statutory link | Evidence | Status |
|---|---|---|---|---|---|
| NG-1 | Thai template enables the cash-basis (CABA) switch (`company.tax_exigibility = True`) but **none of the 18 seeded Thai taxes is configured as on-payment** (`exigibility='on_payment'`). The CABA machinery is live but dormant; if a Thai tax authority rule requires cash-basis VAT, the Community template does not configure it. | VDR-U30-C237, C238 | TXS pending — on-payment VAT requirement not yet confirmed for Thai statutory context | Static: `l10n_th/models/template_th.py:41` (switch on); DB: 18 taxes, 0 on-payment | **NATIVE GAP / EXTENSION REQUIRED candidate** |
| NG-2 | Foreign-currency VAT base rate lookup: Community uses only the invoice-date rate from `res.currency.rate`. The Thai statutory rule for FX conversion (S12-03/S12-04 — buying rate per TXS-R1) is not implemented; rate table has zero rows in the dump. | VDR-U30-C308, C310, C316, C318 | S12-03, S12-04 (TXS-R1 confirmed: buying rate, not mid-market) | `account_move.py`: invoice_currency_rate path; `res_currency.py:_get_conversion_rate` | **NATIVE GAP / EXTENSION REQUIRED candidate (PARTIAL for F22)** |
| NG-3 | Agreement of the global-rounding algorithm with Thai statutory rounding rule (S12-08, per TXS-R1 rounding row) is **UNKNOWN** — not resolvable from static source alone; requires execution with THB documents against the statutory benchmark. | VDR-U30-C163 | S12-08 (TXS-R1) | UNKNOWN — RT required | **UNKNOWN — STATUTORY SOURCE REQUIRED (RT)** |
| NG-4 | Thai template leaves `tax_group_id` empty for zero-rated and exempt VAT taxes. The engine's default rule assigns a tax without a group to the **first tax group of its country** — in the Thai dump, that is the WHT 1% group. Result: zero-rated/exempt VAT bases appear under the "WHT 1%" group name in the on-screen and printed totals summary. This is a template-data defect confirmed by static read and aligns with VDR-U13-C082. | VDR-U30-C352, C353, C354, C355 | TXS pending — statutory presentation of zero-rated/exempt VAT totals | `account_tax.py:2823-2831`; template data; DB: 18 taxes, no group on zero-rated/exempt | **NATIVE GAP / EXTENSION REQUIRED candidate (CONFIRMED by static read)** |

### Additional Thai-specific live risks (not new escalations, lower severity)

- **U30-BR54**: Thai template turns cash-basis switch ON while no Thai tax is on-payment — creates a silent configuration mismatch. If any on-payment tax is added later (by customisation or via a future l10n_th update), the CABA path activates with the existing journal configuration. Risk is bounded to the known CABA journal (EXCH set; dedicated CABA journal set per DB query); not a data-loss risk at current configuration, but a configuration-trap risk. Queued for AWT; not escalated beyond NATIVE GAP candidate.
- **U30-BR42**: Same mechanism as NG-4 from a different angle — the default-group-assignment rule is not Thai-specific but the Thai template's template data activates it. Confirmed at the claim level; adds to NG-4.

### RT items

11 RT claims, all reviewed. No new escalation needed. Three runtime items of note:
1. VDR-U30-C328: numeric consistency of FX documents (rate, rounding item rate, tax item balances) — requires execution with loaded rate rows (zero rows in dump).
2. VDR-U30-C286: tax report exigibility treatment for Thai cash-basis entries — requires report engine (not in Community) or execution.
3. VDR-U30-C274: rounding auto-reconciliation tail reads keys that no Community code sets — the CABA path may have a dead branch (RT to confirm).

### Function-catalog summary

24 functions cataloged (U30-F01 to U30-F24). All 9 capabilities flagged `FUNCTION MAPPING REQUIRED` — the existing Function-ID index has no entry for tax-line synchronisation, totals or cash basis. This is expected: the G01-G16 governance system has not yet established a GMVQ question bank for G04/G10 (ACCOUNT_BASE/ACCOUNT_PROCESS), so no canonical Function-IDs exist to map against. Recorded as a crosswalk gap; does not affect classification.

**Classification**: `ACCEPTED (static tier)` — `account` module, Thai Tax Core dynamic-sync layer. PARTIAL flags on F15/F16 (cash-basis mechanism native, no on-payment Thai taxes), F21 (fiscal-position effect needs explicit action), F22 (FX rate date/source gap). 4 `NATIVE GAP / EXTENSION REQUIRED candidates` (NG-1 through NG-4) surfaced; require TXS statutory validation before final status. No Boss action needed at this intake stage; NG-4 and NG-1 are priority items for the Thai Tax Core AWT backlog.

## 42. U31 (Thai Tax Core: tax report engine and tax grid tags) — semantic highlights + PAUSE CHECKPOINT intake

**Unit**: U31, `tax_report_engine_tags`, Thai Tax Core lane. G-ID: `G04|G10` (account, boundary unresolved).
**Commits**: content `31224332`, packet `b67231fd`. Mechanical gate: PASS.
**Coverage**: 270 claims (FACT 203, OBSERVATION 21, INFERENCE 32, UNKNOWN 14); 135 neutral statements; 1 CONTRA; 7 C1-bound (PCO-F01); 21 RT; 10 capabilities.
**Function-IDs**: PCO-F01×7 (tax lock claims), PCO-F02×7 (return period/date scope); 256 claims FUNCTION MAPPING REQUIRED.

> **NOTE**: Full semantic review paused by Boss's CONTROLLED PAUSE instruction (2026-10-02). Sections below record findings from CONTRA investigation and NATIVE GAP identification already completed before the pause; remaining semantic review (C1-bound claims, RT items, native-gap completeness) deferred to Resume.

### CONTRA VDR-U31-C101 — expression count correction (CR-025 issued)

**Finding**: U24 section 10 and TXC reconciliation table stated "24 expressions + 5 generic (from account module)". U31's direct DB reconciliation finds **29 Thai expressions** (24 with explicit data identifiers + 5 shortcut-generated via `aggregation_formula` on 5 Thai line records) — there are **zero generic/account-module expressions**; the 5 generated ones are Thai. This is a correction to U24 and TXC's description of the Thai report structure.

**Classification of correction**: NARROWING — U24/TXC's business-rule statement about the Thai report definitions is not overturned (same 3 reports, 24 lines, 29 total expressions), but the "5 generic" label was incorrect. The 5 are Thai shortcut-generated, not from the generic account module.

**Action**: Correction request CR-025 issued via PR #74 comment this entry. U24 and TXC both need a footnote: "The 5 shortcut-generated expressions are Thai (generated from Thai line records), not generic account-module expressions."

### NATIVE GAP (Major): No tax report execution engine in Community

**CAP-U31-03 finding** (confirmed by static search, not RT): The Thai VAT/WHT report definitions exist as structured data (3 reports, 24 lines, 29 expressions, 13 tax-grid tags, 10 distribution-line tag assignments), but **there is no report viewer, no computation engine, no export mechanism, and no filing hook in the Community `account` module**. What exists: a viewer lookup hook stub; a settings upgrade prompt for a "dynamic-reports module" that is neither in the Community tree nor the DB; empty menu containers. The engine is expected from a package outside Community (VDR-U31-C083 — a foreign pack extends `account.report` with a viewer hook whose base method is not defined in Community). The tax-details query helper is only used by tests; an exigible-lines domain has no caller.

**Business impact**: A Thai entity running pure Community cannot run, view, export or file its VAT return or WHT returns through the Odoo tax-report mechanism, despite the report definitions being present. This is the largest single NATIVE GAP confirmed by this session's Thai Tax Core review.

**Classification**: `NATIVE GAP / EXTENSION REQUIRED` — NOT a PARTIAL (the execution engine is entirely absent, not partially present). Statutory references: S09 (monthly VAT return), S13 (WHT return forms), S15 (tax certificates) from TXS. **No Boss action needed at this intake stage** (it is a finding, not a Hard Blocker for verification workflow). Recorded for the AWT backlog and SMEsPlus localization scope.

### Classification (intake stage)
`ACCEPTED (static tier — partial intake only, pre-pause)`. Full semantic review and C1-bound/RT/native-gap completeness deferred to Resume. CONTRA CR-025 issued. Major NATIVE GAP identified and recorded.

## 43. U32 (taxed flows — other paths: bank reconciliation, expenses, landed costs, e-invoice, discounts, loyalty, fiscal position, uninstalled add-ons) — semantic highlights + PAUSE CHECKPOINT intake

**Unit**: U32, `taxed_flows_other_paths`, Thai Tax Core lane. G-ID: `G04|G10` + `G07` (purchase expense/landed costs) + `G08` (sales loyalty/discount) — multi-domain.
**Commits**: content `4d17ae85`, packet `8d0634ba`. Mechanical gate: PASS.
**Coverage**: 225 claims (FACT 176, OBSERVATION 12, INFERENCE 25, UNKNOWN 12); 114 neutral statements; 1 CONTRA; 14 C1-bound (GRV-F05×13, PCO-F01×1); 26 RT; 10 capabilities.
**Function-IDs**: GRV-F05×13 (receivables/payables/reconciliation), MFG-F03×2, PCO-F01×1.

> **NOTE**: Full semantic review paused by Boss's CONTROLLED PAUSE instruction. Sections below record findings from CONTRA investigation already completed; C1-bound (GRV-F05) review and RT/native-gap completeness deferred to Resume.

### CONTRA VDR-U32-C146 — U05-C019 narrowing (dump-specific)

**Finding**: U05-C019 claimed "loyalty discount products are created without taxes." U32's DB reconciliation narrows this: the **seeded gift-card reward product in the dump carries the 7% sale tax** (it was created before the order-loyalty module was installed; the order-loyalty data file strips taxes only from trigger products, not from the earlier-seeded reward product). The code behavior VDR-U32-C141 holds for products created **while order-loyalty is installed**. Effect: gift-card sale is untaxed but redemption line is taxed — an asymmetry in the configured dump (PARTIAL — depends on module install order).

**Classification**: ACCEPTED as a NARROWING of U05-C019. U05-C019 is not overturned for new products; the dump-specific behavior is a configuration-order artifact. No change to U05's ACCEPTED status; a footnote to U05-C019 is sufficient.

### Thai e-invoice mapping (CAP-U32-04, from U32 section 6)

Confirmed by static read: Thai zero-rated (0%) and exempt VAT both export as category `E` (exempt) in UBL/CII — they are **not distinguishable from each other** in the exported format. Thai withholding taxes export as negative-percent values with sign reversal, outside line categories, netted from the inclusive total. These are relevant to the ETDA/RD e-Tax Invoice conformance gap noted in §38 (U34). Recorded; full native-gap analysis deferred to Resume.

### C1-bound (GRV-F05 × 13): deferred to Resume

13 GRV-F05 claims relate to receivables/payables reconciliation flows as they intersect taxed paths (bank reconciliation, fiscal-position application at order/bill/expense hand-offs). These require cross-checking against U12 (payments/reconciliation, mechanical-only intake). Deferred per pause instruction.

### Classification (intake stage)
`ACCEPTED (static tier — partial intake only, pre-pause)`. CONTRA VDR-U32-C146 accepted as narrowing. Full C1-bound/RT/native-gap review deferred to Resume.

## 44. U33 (account_core_remaining — auto-send, dunning, analytic, budget, assets, sequence, journal closing, bank feeds, lock-date wizards) — mechanical intake

**Commits**: content `ec50b3e3`, packet `38586df1`. Mechanical gate: PASS. Single-module (account), compliant with one-module-per-unit rule.
**Coverage**: 510 claims (FACT 467, OBSERVATION 14, INFERENCE 16, UNKNOWN 13); 295 neutral statements; 0 CONTRA; 0 C1-bound; 13 RT; 0 Function-IDs referenced.
**Note**: No CONTRA and no C1-bound claims is a positive indicator for this intake; the 510 claims cover the remaining `account` module areas not covered by U30–U32. Semantic review queued for Resume.
**Classification**: `MECHANICAL ONLY (hash-integrity)`.

## 45. U35 (auth_barcodes_small_platform — auth family, barcodes, analytic account UI, phone_validation, digest, UTM, privacy_lookup, base_sparse_field, onboarding, base_setup) — mechanical intake

**Commits**: content `eed3d153`, packet `4732ec15`. Mechanical gate: PASS. Multi-module (10 modules), grandfathered per CR-021.
**Coverage**: 392 claims (FACT 320, OBSERVATION 13, INFERENCE 50, UNKNOWN 9); 212 neutral statements; 2 CONTRA; 0 C1-bound; 16 RT; 0 Function-IDs referenced.
**Note**: 2 CONTRA claims — identities not yet read; will be investigated at Resume. `privacy_lookup` module (Thai PDPA data-subject lookup relevance flagged in §40 crosswalk) is in scope for this unit.
**G01 modules in scope**: base_sparse_field, onboarding, base_setup, phone_validation, digest, utm, privacy_lookup (all G01 exact roster members).
**Classification**: `MECHANICAL ONLY (hash-integrity)`. CONTRA claims flagged for Resume.

## 46. U37 (base_family_bus_calendar_cloud — base, bus, calendar, google_account, base_automation, base_setup, resource, resource_mail, utm, digest, web_tour, portal, phone_validation) — mechanical intake

**Commits**: content `638ea932`, packet `8050ac52`. Mechanical gate: PASS. Multi-module (13 modules), grandfathered per CR-021.
**Coverage**: 472 claims (FACT 449, OBSERVATION 6, INFERENCE 7, UNKNOWN 10); 112 neutral statements; 1 CONTRA; 0 C1-bound; 11 RT; 0 Function-IDs referenced.
**Note**: 1 CONTRA claim — identity not yet read; flagged for Resume. Multiple G01 exact-roster modules in scope (base, bus, base_automation, base_setup, resource, resource_mail, utm, digest, web_tour, portal, phone_validation). This unit's findings directly feed G01's A1 static-intake review.
**G01 overlap**: 11/13 modules are G01 exact-roster members; google_account and calendar are G02-adjacent (identity/access).
**Classification**: `MECHANICAL ONLY (hash-integrity)`. CONTRA claim flagged for Resume.

## 47. U38 (crm_event_fleet_gamification_google_account — CRM, events, fleet, gamification, google services) — mechanical intake

**Commits**: content `7408562a`, packet `75e27428`. Mechanical gate: PASS. Multi-module (19 modules per original queue), grandfathered per CR-021.
**Coverage**: 505 claims (FACT 428, OBSERVATION 20, INFERENCE 46, UNKNOWN 11); 501 neutral statements; 1 CONTRA; 0 C1-bound; 24 RT; 0 Function-IDs referenced.
**Note**: 1 CONTRA claim — not yet read; flagged for Resume. crm → G09, event* → G11, fleet → G13 (via hr_fleet), gamification → cross-group. G11 modules (event family) first appear in a DeepSeek unit here — previously listed as NOT STUDIED in §40 crosswalk. G11 crosswalk status updates to: DeepSeek unit assigned (U38).
**Classification**: `MECHANICAL ONLY (hash-integrity)`. CONTRA claim flagged for Resume. G11 crosswalk updated.

## 48. U40 (hr_family_html_editor — hr_expense, hr_holidays, hr_recruitment, hr_work_entry, hr_contract, html_editor server-side deep, 22 modules total) — mechanical intake

**Commits**: content `344777f2`, packet `d2944687`. Mechanical gate: PASS. Multi-module (22 modules), grandfathered per CR-021.
**Coverage**: 686 claims (FACT 635, OBSERVATION 21, INFERENCE 20, UNKNOWN 10); 185 neutral statements; 0 CONTRA; 0 C1-bound; **56 RT** (highest RT count of any unit so far); 0 Function-IDs referenced.
**Note**: No CONTRA, no C1-bound. The 56 RT items are unusually high — consistent with the breadth of HR process paths that require runtime execution to validate (leave approval chains, expense reimbursement flows, recruitment state machines, html_editor rendering). G13 modules (hr_expense, hr_holidays, hr_recruitment, hr_work_entry, hr_contract) dominate.
**Classification**: `MECHANICAL ONLY (hash-integrity)`. RT items queued for AWT; semantic review deferred to Resume.

## 49. U42 (mail_remaining — mail module remaining areas: discuss, channels, scheduling, guest access, SMS, reactions, starred/pinned/translation features) — mechanical intake

**Commits**: content `4b1acb4d`, packet `0f253a81`. Mechanical gate: PASS. Single-module (mail), compliant with one-module-per-unit rule. G01 exact-roster module.
**Coverage**: 411 claims (FACT 372, OBSERVATION 12, INFERENCE 20, UNKNOWN 7); 227 neutral statements; 0 CONTRA; 0 C1-bound; 26 RT; 0 Function-IDs referenced.
**Note**: No CONTRA, no C1-bound. G01 module with 411 claims covering mail's remaining areas. The `im_livechat` retention gap noted in §39 (U41) may have overlap with this unit's coverage of channel/guest lifecycle — to be cross-checked at Resume.
**G01 crosswalk update**: `mail` module now has U03 (mechanical) + U42 (mechanical) assigned. Full G01 mail coverage pending semantic review of both.
**Classification**: `MECHANICAL ONLY (hash-integrity)`.

## 50. U43 (mail_family_maintenance_microsoft — mail_activity_plan, mail_bot, mail_group, mail_resend, maintenance, microsoft_calendar, microsoft_outlook) — mechanical intake

**Commits**: content `28b2af3e`, packet `41633212`. Mechanical gate: PASS. Multi-module (7 modules), grandfathered per CR-021.
**Coverage**: 156 claims (FACT 149, OBSERVATION 1, INFERENCE 6, UNKNOWN 0); 120 neutral statements; 1 CONTRA; 0 C1-bound; 11 RT; 0 Function-IDs referenced.
**Note**: 1 CONTRA claim, 0 UNKNOWN (unusually clean — 100% pointer+anchor supported). CONTRA identity not yet read; flagged for Resume. `maintenance` module may be G16 (TECHNICAL_INTEGRATION) or G14 (COLLABORATION) — G-ID assignment pending GROUP_STRUCTURE_V2_CORE.tsv read. Microsoft calendar/Outlook are G01-adjacent integration bridges.
**Classification**: `MECHANICAL ONLY (hash-integrity)`. CONTRA claim flagged for Resume.

---

## PAUSE CHECKPOINT (2026-10-02 — Boss CONTROLLED PAUSE instruction)

> **STATUS: STATE03 VERIFIER = PAUSED — WAITING FOR DEEPSEEK BATCH COMPLETION**
> Issued per Boss instruction: pause at next safe atomic boundary; resume only when DeepSeek confirms all authorized U-units are terminal and Final Batch Index is pushed.

### Last fully accepted boundary
- **U30** — `account` Thai Tax Core dynamic-sync — `ACCEPTED (static tier)` — commit `ea9af153` — §41

### Current HEAD (this session's branch)
- Branch: `claude/new-session-l8f19r`
- This commit: to be set by the commit containing this checkpoint

### Last DeepSeek handoff received
- **U43** — `mail_family_maintenance_microsoft` — packet commit `41633212` — §50

### Unfinished verification queue (as of pause)

| Unit | Status | Priority | Action needed on Resume |
|---|---|---|---|
| U31 | Semantic partial (CONTRA resolved, NATIVE GAP identified) | HIGH (Thai Tax Core) | Complete C1-bound (PCO-F01×7, PCO-F02×7), RT, native-gap completeness |
| U32 | Semantic partial (CONTRA resolved, GRV-F05 deferred) | HIGH (Thai Tax Core) | Complete C1-bound (GRV-F05×13), RT, native-gap completeness |
| U33 | Mechanical only | MEDIUM (account core remaining, 510 claims) | Semantic review |
| U34 | Mechanical only — `account_edi_ubl_cii` PARTIAL | MEDIUM (Thai EAS/ETDA gap) | Semantic read of template bodies, Thai EAS mapping |
| U35 | Mechanical only — 2 CONTRA unread | MEDIUM | Read CONTRA claims, semantic review; privacy_lookup PDPA note |
| U37 | Mechanical only — 1 CONTRA unread | MEDIUM | Read CONTRA claim, semantic review |
| U38 | Mechanical only — 1 CONTRA unread | MEDIUM | Read CONTRA claim, semantic review; G11 update |
| U40 | Mechanical only — 56 RT | MEDIUM | Semantic review; AWT for 56 RT |
| U41 | Mechanical only — im_livechat retention gap | MEDIUM | Semantic review; Thai PDPA cross-check |
| U42 | Mechanical only | LOW-MEDIUM | Semantic review; mail retention cross-check with U41 |
| U43 | Mechanical only — 1 CONTRA unread | MEDIUM | Read CONTRA claim |
| U44–U59 | Not yet received | — | Await DeepSeek batch completion |
| Original batch (U01-U04, U06-U18 excl. U19, U21-U23, C01, C02) | Mechanical only | BACKLOG | Semantic review on Resume |

### Open corrections/contradictions requiring action

| ID | Subject | Status |
|---|---|---|
| CR-025 (this log) | VDR-U31-C101: U24/TXC expression count ("5 generic" → "5 Thai shortcut-generated") | Correction issued to PR #74; DeepSeek to acknowledge |
| VDR-U32-C146 | U05-C019 narrowing (gift-card reward product in dump carries 7% — dump-specific) | ACCEPTED as narrowing; no separate CR needed |
| VDR-U35-C??? | 2 CONTRA in U35 — IDs not yet read | Deferred to Resume |
| VDR-U37-C??? | 1 CONTRA in U37 — ID not yet read | Deferred to Resume |
| VDR-U38-C??? | 1 CONTRA in U38 — ID not yet read | Deferred to Resume |
| VDR-U43-C??? | 1 CONTRA in U43 — ID not yet read | Deferred to Resume |
| BGQ-10 | Pacing decision: one-module-per-unit rule for remaining ~461 modules | Open — awaiting Boss ruling |
| BGQ-08 | Provenance of STATE03_SMD_SOURCE_VERIFICATION_FINDINGS.md | Open — awaiting Boss ruling |

### Open C1-bound claims (not fully reviewed)

| Unit | Count | Function-ID | Status |
|---|---|---|---|
| U31 | 7 | PCO-F01 (tax lock) | Deferred to Resume |
| U31 | 7 | PCO-F02 (fiscal year/period) | Deferred to Resume |
| U32 | 13 | GRV-F05 (reconciliation) | Deferred to Resume |
| U32 | 1 | PCO-F01 | Deferred to Resume |

### Thai Tax Core native-gap candidates (status as of pause)

| NG-ID | Unit | Finding | Status |
|---|---|---|---|
| NG-1 | U30 | CABA switch on, 0 on-payment Thai taxes | Confirmed static; TXS validation pending |
| NG-2 | U30 | FX rate source gap — buying rate (S12-03/S12-04) not implemented | Confirmed static; TXS confirmed |
| NG-3 | U30 | Rounding algorithm vs S12-08: UNKNOWN — RT required | RT |
| NG-4 | U30 | Zero-rated/exempt VAT in WHT 1% group (template data defect) | Confirmed static |
| NG-5 | U31 | NO TAX REPORT ENGINE in Community — definitions exist but unexecutable | Confirmed static; MAJOR |
| NG-6 | U32 | Zero-rated and exempt VAT not distinguishable in UBL/CII export (both category E) | Confirmed static |

### G01-G16 crosswalk status (as of pause)

- §40 initial partial map committed; G01 (23 modules) fully mapped; G11 (8 modules) partially mapped (U38 confirmed, semantic pending).
- `GROUP_STRUCTURE_V2_CORE.tsv` row-level read: **NOT DONE** — required to complete G02-G10, G12-G16 crosswalk.
- G04/G10 boundary (ACCOUNT_BASE vs ACCOUNT_PROCESS): **UNRESOLVED**.
- New G-ID updates from this batch: G11 now has U38 assigned (§47 above).

### Resume instructions (per Boss)

On resume:
1. Run DELTA-FIRST.
2. Verify the completed DeepSeek batch continuously without waiting between units.
3. Produce one consolidated Correction Batch.
4. Send corrections to DeepSeek once.
5. After DeepSeek correction batch: one final closure verification.
6. No Formal Coverage without a frozen denominator.
7. Opus escalation allowed only for C1, Material Contradiction, Zero-Tolerance, Clean-Room, or Module Closure.

---

## §51. PAUSE ADDENDUM — Notifications received while paused (2026-10-02)

**Verifier status: PAUSED. No verification action taken. This section is documentation-maintenance only.**

### Events received after PAUSE CHECKPOINT commit `355f0a5b`

**DeepSeek correction packets CR-024 to CR-028** (commit `43672f4b`, branch `claude/local-odoo-source-research`):

| DeepSeek CR | Packet | Boundary | Classification | Subject |
|---|---|---|---|---|
| CR-024 | U21-R1 | U21 | CORRECTION_REQUIRED · Material | Certificate adapter loads pem_key with password=None; stored PEM is encrypted when key record has password |
| CR-025 (DS) | U05-R1 | U05 | CORRECTION_REQUIRED · Normal | Seeded gift-card product carries 7% tax; tax-strip override covers discount products only |
| CR-026 | U17-R2 | U17 | CORRECTION_REQUIRED · Material | Gamification end-of-period Datetime vs Date string mismatch; periodic challenge rewards never trigger |
| CR-027 | U24-R2 | U24 | CORRECTION_REQUIRED · Normal | Thai tax report has 29 expressions in DB (24 direct XML + 5 shortcut fields), not 24 |
| CR-028 | U21-R2 | U21 | CORRECTION_REQUIRED · Normal | E-mailed TOTP code window is 1–2 hours, not 1–3 hours |

All 5 packets: **QUEUED — PENDING RESUME. NOT VERIFIED.**

**U44 Atomic Boundary** (content `965bfe00`, packet `bd53b7ee`): 193 claims, 68 C1-bound, 25 RT, 0 CONTRA, 1 UNKNOWN. **QUEUED — PENDING RESUME. NOT VERIFIED.**

**U45 Atomic Boundary** (content `f54bd587`, packet `58848879`): 238 claims, 0 C1-bound, 21 RT, 0 CONTRA, 5 UNKNOWN. **QUEUED — PENDING RESUME. NOT VERIFIED.**

### CR Numbering Conflict — MUST RESOLVE AT RESUME

This log's **CR-025** (issued §42, VDR-U31-C101) = expression count correction request to U24/TXC (Thai tax report expression count). DeepSeek's **CR-025 (DS)** (above) = U05-R1 gift-card tax topic — **different subject, same number**. DeepSeek's **CR-027** (U24-R2, "29 expressions not 24") covers the same subject as this log's CR-025. At Resume: confirm canonical CR numbering and resolve collision before issuing consolidated Correction Batch.

### Resume Trigger Check (2026-10-02)

- DeepSeek still active: **YES** (U44/U45 posted after PAUSE)
- Final Batch Index pushed: **NO**
- Resume Trigger met: **NO — REMAIN PAUSED**

---

## 9. What this log is not

Not a Gate PASS, not Formal Coverage, not a canonical denominator, not Final Approved, not a V-Level assignment. `N/A — DENOMINATOR NOT VALIDATED` applies to any implied percentage. Boss remains Sole Final Approver.
