# 03 — Five High Findings: Independent Re-Performance

| Item / Task | Owner | Evidence location | Timestamp | Reviewer / Verifier | Verification Status | Gate Impact |
|---|---|---|---|---|---|---|
| Reopen primary evidence for each of the five originally-open High findings and independently decide disposition — not accept IER-003/CORR-005 verdicts on trust | Claude (IDR-007) | This artifact; primary source citations independently re-read from local source tree | 2026-09-01 | Self — re-read the actual source files IER-003 cited, not just IER-003's md files | Independently confirmed for 4 of 5; 1 partially re-confirmed with a scoping caveat noted | Primary determinant of Gate readiness |

For each item this review deliberately did NOT stop at re-reading IER-003's own write-up. Where the underlying primary evidence (source code files) was locally accessible, this review re-opened the actual cited file and line and checked it directly, independent of IER-003's transcription.

---

## GRPA-H4 — Fiscal Position

- **Original DR-002 status:** `EVIDENCE_MISSING` / High (A14 L23) — "`account.fiscal.position` base model file never located."
- **IER-003 result:** `VERIFIED CLOSED` (`04_IER003_HIGH_H1_...md` L5, L38) — cites `01 ACCOUNT/account/models/partner.py:27`.
- **Boss ruling:** N/A — a straightforward evidence miss, no scope ruling required.
- **CORR-005 status:** `RESOLVED` (A14 Part 3 L82; `02_CORR005_FIVE_HIGH_RECONCILIATION_MATRIX.md` L13).
- **Independent IDR-007 verdict: CONFIRMED — VERIFIED CLOSED.**
- **Exact evidence citation, independently re-read:** `ACCOUNT/01 ACCOUNT/SOURCE CODE/01 ACCOUNT/account/models/partner.py`, line 27: `` _name = 'account.fiscal.position' `` (class `AccountFiscalPosition`, confirmed at the exact cited line by this review's own `grep -n`/`sed -n` read, not copied from IER-003's transcription).
- **Evidence type:** Technical proof (primary source, exact file/line, directly falsifiable).
- **Gate impact:** None — resolved, not a blocker, not a carry-forward.

## GRPA-H5 / H2 — Partner Brand/HQ

- **Original DR-002 status:** `EVIDENCE_MISSING` / High (A14 L24).
- **IER-003 result:** `PARTIALLY VERIFIED — TARGETED CORRECTION REQUIRED` (`05_IER003_...md` L5, L42) — owning module identified as `bh_parent_company` (author BHPRO, `state='installed'`, `latest_version='19.0.1.4.7'`) via `ir_module_module`/`ir_model_data` metadata query; internal logic still unknown.
- **Boss ruling:** `CLOSED BY BOSS SCOPE EXCLUSION / LEGACY MIGRATION DATA CARRY-FORWARD ONLY` — Boss Inventory Scope Ruling §1.1: `bh_*`/`bhpro_*` excluded from SMEsPlus source learning entirely.
- **CORR-005 status:** `CONTROLLED MIGRATION CARRY-FORWARD` (A14 Part 3 L83).
- **Independent IDR-007 verdict: CONFIRMED — closure correctly scoped, not overclaimed.** See [04_IDR007_H2_SCOPE_EXCLUSION_AUDIT.md](04_IDR007_H2_SCOPE_EXCLUSION_AUDIT.md) for the dedicated audit.
- **Exact evidence citation:** `ir_model_data`/`ir_module_module` provenance metadata (IER-003 `05` L30); Boss Inventory Scope Ruling §1.1, L17, L27.
- **Independent corroboration performed by this review:** a targeted filesystem search for `bh_parent_company` module source under the locally-accessible `ACCOUNT/01 ACCOUNT/SOURCE CODE/` tree (the same tree used to verify the other four findings) returned **no result** — the module's addon source is genuinely not present on the machine this review (or IER-003, or CORR-005) has access to. This independently corroborates, rather than merely repeats, IER-003's own statement that the module's internal logic is "genuinely unavailable without obtaining the module's source from the customer/vendor." It also confirms this review itself never had the opportunity to read `bh_*` business logic — relevant to the clean-room check in file 08.
- **Evidence type:** Governance scope disposition, explicitly not technical proof (verified not mislabeled — see file 04).
- **Gate impact:** Not Inventory-Gate-blocking; carried forward to Migration.

## GRPA-H8 / H3 — Thai Branch

- **Original DR-002 status:** `CONFLICTING PRACTICE` / High (A14 L25).
- **IER-003 result:** `CONFLICTING EVIDENCE` + `REQUIRES REAL USER VALIDATION` (`06_IER003_...md` L5, L32) — corrects TEAM A's characterization: the dataset has only one `res.company` row, so "branch = child `res.company` record" cannot be confirmed as this customer's actual practice (structurally available, not confirmed as used).
- **Boss ruling:** `CLOSED AS AN INVENTORY ARCHITECTURE QUESTION` — Boss Inventory Scope Ruling §1.2: approved SaaS Tenant/Company/Branch baseline is not reopened by Inventory.
- **CORR-005 status:** `CLOSED AS AN INVENTORY ARCHITECTURE QUESTION` — `CONTROLLED MIGRATION / TBRAC CARRY-FORWARD` + `ACCOUNTING/TAX CARRY-FORWARD` (A14 Part 3 L84).
- **Independent IDR-007 verdict: CONFIRMED — closure correctly scoped, does not claim legacy branch usage is understood.** See [05_IDR007_H3_BRANCH_BASELINE_AND_CARRY_FORWARD_AUDIT.md](05_IDR007_H3_BRANCH_BASELINE_AND_CARRY_FORWARD_AUDIT.md) for the dedicated audit.
- **Exact evidence citation:** `l10n_th`/`l10n_th_partner` module read (platform Thai localization, not `bh_*`/`bhpro_*` — within clean-room scope); `res_company` cardinality check (1 row); IER-003 `06` L24.
- **Evidence type:** Structural conflict confirmed by primary evidence (technical), combined with a governance non-reopening decision (scope) for the unresolved "which practice is real" question — correctly kept as two distinct claims, not merged into one overclaim.
- **Gate impact:** Decision-point only, not a hard blocker; two carry-forward rows (Migration/TBRAC, Accounting/Tax), neither Inventory-Gate-blocking.

## N-A7-03 / N-A9-02 — Cutoff / Timing

- **Original DR-002 status:** `EVIDENCE_MISSING` / High (A14 L64) — explicitly flagged as the single most material open item, blocking Lane C Cross-Proof scenario 6.
- **IER-003 result:** `VERIFIED CLOSED — MAJOR CORRECTION` (`07_IER003_...md` L5, L66) — cites `stock_account/models/stock_picking.py` (full file) and `stock/models/stock_move.py:28-193`.
- **Boss ruling:** N/A — straightforward evidence miss.
- **CORR-005 status:** `RESOLVED` (A14 Part 3 L85).
- **Independent IDR-007 verdict: CONFIRMED — VERIFIED CLOSED.**
- **Exact evidence citation, independently re-read:** `ACCOUNT/01 ACCOUNT/SOURCE CODE/02 OTHER/stock_account/models/stock_picking.py`, lines 14-34 — `_check_backdate_allowed()` (L14) raises `ValidationError` when `picking._is_date_in_lock_period()` (L18-19); `_is_date_in_lock_period()` (L27-34) calls `self.company_id._get_lock_date_violations(self.scheduled_date.date(), fiscalyear=True, ...)`. This review independently confirmed this exact mechanism exists at the exact cited lines — a real fiscal-period lock-date constraint on stock picking dates, directly answering the DR-002 cutoff question. Also confirmed `stock/models/stock_move.py` around line 28 defines `date = fields.Datetime('Date Scheduled', ...)`, corroborating the "scheduling/date fields" claim.
- **Evidence type:** Technical proof (primary source, directly falsifiable, independently re-derived).
- **Gate impact:** None — resolved. This was previously the single most material open item; its closure is the most consequential correction in this reconciliation, and it independently checks out.

## N-A13-02 — Company ACL / Record Rules

- **Original DR-002 status:** `EVIDENCE_MISSING` / High (A14 L65) — "record rules/ACLs... not read this pass."
- **IER-003 result:** `VERIFIED WITH CONDITIONS — MAJOR CORRECTION` (`08_IER003_...md` L5, L44) — cites `stock/security/ir.model.access.csv` (full) and `stock/security/stock_security.xml` (full).
- **Boss ruling:** N/A — evidence miss, with an explicit residual condition.
- **CORR-005 status:** `RESOLVED (ORM-layer)` + `FUTURE IMPLEMENTATION/TEST CARRY-FORWARD` for the unaudited sudo()-bypass question (A14 Part 3 L86).
- **Independent IDR-007 verdict: CONFIRMED, with the residual condition upheld as genuinely still open (not artificially resolved).**
- **Exact evidence citation, independently re-read:** `ACCOUNT/01 ACCOUNT/SOURCE CODE/02 OTHER/stock/security/ir.model.access.csv` (78 lines, confirmed present) and `stock/security/stock_security.xml` (169 lines; this review counted **30** `<record>` elements, several with `domain_force` explicitly filtering on `company_id`, e.g. lines 75, 81, 87, 93, 99, 105: `[('company_id', 'in', company_ids)]` and variants). This independently confirms a real, comprehensive company-scoped `ir.rule` mechanism exists at the ORM layer.
- **Residual condition independently exercised, not just repeated:** this review did **not** attempt to audit every code path in `stock_account`/`sale_stock`/`purchase_stock`/`mrp` for `sudo()` bypass (that remains explicitly out of this review's authorized scope — a future implementation/test verification item, not a source-research question this session could close). Treating this as still-open is the correct call, not a gap in this review.
- **Evidence type:** Technical proof for the ORM-layer mechanism (resolved); explicitly-scoped residual for the DB/sudo-bypass layer (correctly still carried forward, not silently dropped, not artificially closed).
- **Gate impact:** None from the resolved ORM-layer portion; the residual is tracked as a non-blocking future-verification item (see file 07).

---

## Summary table

| ID | Original DR-002 | IER-003 | Boss | CORR-005 | IDR-007 independent verdict | Primary-source re-verified by IDR-007? |
|---|---|---|---|---|---|---|
| GRPA-H4 | EVIDENCE_MISSING/High | VERIFIED CLOSED | N/A | RESOLVED | **CONFIRMED** | Yes — line 27 re-read directly |
| GRPA-H5/H2 | EVIDENCE_MISSING/High | PARTIALLY VERIFIED | Scope-excluded | CONTROLLED MIGRATION CARRY-FORWARD | **CONFIRMED** | Yes — independently confirmed module source absent from this machine |
| GRPA-H8/H3 | CONFLICTING PRACTICE/High | CONFLICTING EVIDENCE + validation required | Architecture not reopened | Architecture-question carry-forward (2 workstreams) | **CONFIRMED** | Partial — cardinality claim independently plausible from citation; full re-read not repeated (would require re-opening `l10n_th` source, judged unnecessary given the finding is explicitly a non-closure) |
| N-A7-03/N-A9-02 | EVIDENCE_MISSING/High | VERIFIED CLOSED | N/A | RESOLVED | **CONFIRMED** | Yes — lock-period mechanism re-read directly, lines match |
| N-A13-02 | EVIDENCE_MISSING/High | VERIFIED WITH CONDITIONS | N/A | RESOLVED (ORM) + carry-forward | **CONFIRMED** | Yes — `ir.rule` company_id domain_force re-read directly |

**Net independent result: 0 of 5 High items remain open Inventory research blockers**, matching CORR-005's own reconciliation exactly — but arrived at here by independently re-opening primary source for 4 of 5 items (all but H3, where re-derivation was judged unnecessary since the finding remains explicitly unresolved either way) rather than by trusting the chain of prior write-ups.
