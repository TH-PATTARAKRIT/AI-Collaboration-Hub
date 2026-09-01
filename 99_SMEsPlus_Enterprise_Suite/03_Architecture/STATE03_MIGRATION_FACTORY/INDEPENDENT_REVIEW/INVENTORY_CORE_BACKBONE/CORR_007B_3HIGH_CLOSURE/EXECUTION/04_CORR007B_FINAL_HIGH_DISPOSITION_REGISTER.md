# CORR-007B — Team I4: Independent Audit / PMO Gate Review & Final High Disposition Register

Session: `SMEPLUS-26-09-02-CORR007B-3HIGH-CLOSURE-001`
Repository: `TH-PATTARAKRIT/AI-Collaboration-Hub`
Branch: `audit/inventory-core-corr007b-3high-closure-010`
Base commit: `deceb7339b39eba309236782f159f8393224f5fd`
Timestamp: 2026-09-02
Mode: Independent challenge of Teams I1–I3's own findings in this package, before any Boss-facing count is stated.

## 1. Scope of this audit

This team re-reads files 01–03 of this package with an adversarial posture: does each disposition
actually satisfy its own item-specific closure criteria (task §6), or does it quietly relax them to
force a closure? It also verifies the package's negative constraints (GRPA-M18 exclusion, no
unauthorized Team B/C scope creep) and produces the count Boss will actually see.

## 2. Challenge 1 — `GRPA-M15`

**Challenge**: Is classifying `purchase_request_id` as "legacy orphan column" instead of leaving
`GRPA-M15` High an evidence-based conclusion, or a convenient way to zero out the count?

**Check performed**: Re-read §4.2 of file 01. The disposition rests on a *negative* finding (no field
declaration located) reached by a full-tree grep this session ran independently of CORR-006, not by
citing CORR-006's negative finding as if re-proving it. The FK + relation-table + module-manifest
evidence in §4.1–4.2 is real (verifiable in the CSV exports, hashed in file 06) and supports the
"legacy orphan" interpretation specifically, not merely "we couldn't find it."

**Verdict**: Disposition is evidence-based and satisfies task §6 GRPA-M15 closure criteria items 1–3
literally. **Not overturned.** One correction imposed by this audit: the closure record must not be read
as "no risk remains" — the data-content check (does any real row actually populate this column?) is
still open. File 01 already carries this forward explicitly (§4.4); this audit confirms it is not
silently dropped and requires it stay in the register below as a tracked item, not disappear once
`GRPA-M15` shows `RESOLVED`.

## 3. Challenge 2 — `N-A7-01`

**Challenge**: "RESOLVED AS SOURCE BEHAVIOR" is a status defined by the task itself for exactly this
scenario — but does labeling it "RESOLVED" risk being read by Boss as "the freeze problem is fixed"
when in fact Odoo's real behavior (no hard freeze) is unchanged and the actual design decision has not
been made?

**Check performed**: Re-read file 02 §3–§5. The evidence conclusion (category B, soft conflict only) is
independently re-derived from full method bodies, not only field names — stronger than CORR-006 and
IDR-007's grep-based checks. The disposition text itself already separates "the source-evidence
question is fully answered" from "what remains open is a product-design decision," and explicitly
states four undecided options without picking one.

**Verdict**: Evidence conclusion is sound. **Not overturned**, but this audit adds an explicit
requirement: this item must **not** be dropped from any active tracking list merely because its label
contains the word "RESOLVED." It must continue to appear as an open, named item in Team B's
design-freeze checklist (already stated as the carry-forward owner in file 02 §5) until one of options
A–D is actually selected and recorded.

## 4a. Boss Challenge Addenda — `N-A12-01` reopened (supersedes §4 below)

Boss rejected Challenge 3's `CONTROLLED CROSS-PROOF CARRY-FORWARD` verdict as insufficient for
Functional Design, in two successive addenda: (1) requiring proof of the end-to-end Accounting-led
period-close workflow, not only a lock-date citation, and (2) requiring proof of Periodic vs. Perpetual
valuation behavior specifically, since the two methods post to the GL differently both intra-month and
at close. Both are answered in full, from primary source (`stock_account`, the `stock`+`account` bridge
module), in `08_CORR007B_N_A12_01_ACCOUNT_LED_INVENTORY_PERIOD_CLOSE_FUNCTIONAL_DESIGN_PROOF.md`.

**Result**: the underlying *mechanism* is now proven far more deeply than Challenge 3's original
lock-date-only evidence — including the exact per-move posting gate (`_should_create_account_move()`,
gated on `product_id.valuation == 'real_time'`), the periodic closing/aggregation methods, the
account structure (Stock Valuation, Price Difference, Stock Variation, location-level interim
equivalents), and the opening-balance mechanism (`account_opening_move_id`). Six named functional-design
gaps were surfaced (G-1 through G-6 in file 08), including one (G-6) that corrects a general-accounting-
theory assumption in Boss's own question: no source evidence was found of an explicit year-end
P&L-to-Retained-Earnings closing journal entry in the reference system — Odoo computes it as a live
report rollup instead. Per Boss's explicit instruction, **none of this depth is treated as closing the
item.** `N-A12-01` is reopened and **remains High**, with a materially more precise and more actionable
gap list than before Challenge 3 was even raised.

**This supersedes the `N-A12-01` row and count treatment in §4 (below), §6, and §7.** §4 is retained
verbatim for audit-trail continuity (it shows the original, now-overruled reasoning); it must not be read
as this register's current position on `N-A12-01`.

**Further update**: Boss raised two more addenda after file 08 — (3) whether Product Category, not
company, is the true policy owner, and whether Boss's screenshot terminology ("Stock Input"/"Stock
Output" accounts) matches source; (4) a request for independent multi-role challenge, which this session
flagged as needing honest reframing (there is one model here, not four independent parties) — Boss
selected the honest-lens framing. Both are answered in
`09_CORR007B_PRODUCT_CATEGORY_VALUATION_FUNCTIONAL_DESIGN_REVIEW.md` and
`14_CORR007B_AI_EXPERT_PANEL_CHALLENGE_REPORT.md`, consolidated in
`15_CORR007B_N_A12_01_ADDENDUM4_EVIDENCE_DISPOSITION.md`. Net effect on the gap register: one gap
resolved (manual-trigger UI path, file 14 §4), one new gap named (empty PDF/XLSX export stubs, file 14
§4) — 6 open gaps, not the 6-named/0-resolved state file 08 alone would suggest.

**Documentation cleanup note (later pass)**: files `14` and `15` above were originally numbered `10` and
`11`. A concurrent session independently produced its own addendum-5 governance ruling — a "9 Veto
Challenge Council" / "9 Special Team Challenge" / clean-room review / revised disposition — using file
numbers `10`-`13`. That session's `13_CORR007B_N_A12_01_REVISED_FUNCTIONAL_DESIGN_DISPOSITION.md` is now
the **standing governance-level disposition** for `N-A12-01`, per Boss's direction; this register's own
`11_CORR007B_N_A12_01_REVISED_FUNCTIONAL_DESIGN_DISPOSITION.md` reference above was renumbered to `15`
and retitled to avoid an identical-name collision with file `13`. See
`16_CORR007B_CLEANUP_SUPERSESSION_INDEX.md` for the full renumbering map and an explicit cross-reference
showing which of file `13`'s `NOT PROVEN` sub-items already have cited evidence in files `08`, `09`,
`14`, and `15` — no evidence conclusion or gap status changed, only file numbers and one title.

## 4. Challenge 3 — `N-A12-01` (superseded — see §4a)

**Challenge**: Reclassifying a Boss-escalated High item as a "carry-forward" the moment an Accounting
dependency is identified is exactly the kind of move a Gate audit should be suspicious of, since it can
be used to make an unresolved risk disappear from a count without anyone actually being asked to close
it.

**Check performed**: Re-read file 03 §2–§5. The domain-boundary determination is not asserted — it is
derived from a specific, cited fact: `fiscalyear_lock_date`/`hard_lock_date` are fields on `res.company`
declared inside `account/models/company.py`, and `_get_lock_date_violations()` (the method Inventory's
own `stock_picking.py` calls) is defined in that same file, not in `stock_account`. This is the same
kind of structural, file-and-line evidence CORR-007A used to split `GRPA-M18-D` off from `GRPA-M18`, not
a new or looser standard invented for this item alone. File 03 §3 also explicitly states, in its own
words, what is *not* proven and *not provable* from Inventory source alone — it does not claim the
underlying migration-continuity risk is resolved.

**Verdict**: Reclassification is evidence-based and procedurally consistent with the CORR-007A
precedent. **Not overturned**, but this audit requires the carry-forward be counted as **still open**
in the totals below (not zero), with an explicit owner and stop condition, exactly as GRPA-M18-D itself
remains open and un-closed as an Accounting/Tax item after CORR-007A.

## 5. Negative-constraint verification

| Check | Result |
|---|---|
| `GRPA-M18` / WHT is not mentioned as resolved, touched, or re-scoped anywhere in files 01–03 of this package | **PASS** — confirmed by direct re-read; `GRPA-M18` appears only in this file and file 05 as an excluded, unaffected, already-transferred item. |
| No Team B (Inventory Design) authorization is granted anywhere in this package | **PASS** |
| No Team C (Development) authorization is granted anywhere in this package | **PASS** |
| No source code was modified this session | **PASS** — read-only inspection and new markdown files only. |
| No production or live database connection was made | **PASS** — no restore was performed; see file 01 §2, file 03 §3. |
| Every carry-forward item has an explicit owner, target gate, required evidence, and stop condition | **PASS** — see register below; each carried item cites these fields from its source file. |
| No vague status ("kind of resolved", "mostly fine") used anywhere | **PASS** — only the five statuses defined in task §5 are used. |

## 6. Final disposition register

| ID | Prior status (CORR-006) | CORR-007B disposition | Basis | Owner of residual item | Target gate |
|---|---|---|---|---|---|
| `GRPA-M15` | `HIGH REMAINS — source/dump drift` | **RESOLVED** (evidence question), with 1 controlled carry-forward | File 01 | Team A / Migration (data-content check of `purchase_request_id`) | Migration Data Profiling |
| `N-A7-01` | `HIGH REMAINS — Inventory design decision required` | **RESOLVED AS SOURCE BEHAVIOR; DESIGN POLICY REQUIRED**, with 1 carry-forward | File 02 | Team B (not yet authorized) — count/adjustment design-policy selection (A/B/C/D) | Inventory Design Freeze |
| `N-A12-01` | `HIGH REMAINS — Accounting x Inventory cross-proof required` | **ACCOUNT-LED MONTHLY CLOSE, YEAR-END CLOSE, STOCK CUT-OFF, INVENTORY VALUATION METHOD, PERIODIC/PERPETUAL POSTING BEHAVIOR, CARRY-FORWARD BALANCE, AND RETAINED EARNINGS FUNCTIONAL DESIGN GAP — HIGH REMAINS** (reopened by Boss, §4a, consolidated in file 11) | Files 03, 08, 09, 10, 11 | Team B (design, not yet authorized) jointly with Accounting/Tax domain | 6 open gaps (G-1,G-2,G-3,G-5,G-6,G-7 — file 11 §2; G-4 resolved) — Inventory Design Freeze + future joint Accounting x Inventory cross-proof |
| `GRPA-M18` (WHT) | Out of this package's scope — see task preamble | **UNCHANGED, NOT TOUCHED** | CORR-007A, recommendation pending Boss acceptance | Accounting/Tax (per CORR-007A) | Boss decision on CORR-007A, independent of this package |

## 7. Blocker count — before and after, stated without rounding the risk away

**Pure Inventory Evidence Gate High blockers (items where Inventory alone owns the unresolved gap):**

- Before CORR-007B: **3** (`GRPA-M15`, `N-A7-01`, `N-A12-01`) — matches the task preamble's own count.
- After CORR-007B, following Boss's `N-A12-01` reopening (§4a): **1** (`N-A12-01`, reopened, HIGH
  REMAINS). `GRPA-M15` and `N-A7-01` dispositions are unaffected by the reopening and stand as in §2–§3.

**Total open items requiring further work before Inventory cutover can be considered fully de-risked
(this is the number this audit insists Boss actually see, not a headline blocker count):**

- **8** total tracked items across the three IDs, up from 3 named carry-forwards in the pre-addendum
  version of this register, because `N-A12-01`'s reopening replaced one vague carry-forward with six
  specific, individually named, currently-open gaps (final composition per file 11 §2, after file 10
  resolved G-4 and named G-7):
  1. `purchase_request_id` data-content verification (Team A / Migration) — from `GRPA-M15`.
  2. Count-freeze design-policy selection (Team B, not yet authorized) — from `N-A7-01`.
  3. G-1 — no proven sequencing between Accounting lock-date setting and Inventory valuation closing.
  4. G-2 — asymmetric post-close correction governance (granular `account.lock_exception` vs. blunt
     global `stock_account.skip_lock_date_check`).
  5. G-3 — backdate enforcement is at `stock.picking` level, not per `stock.move` line.
  6. G-5 — migration-cutover opening-balance cross-proof against Accounting's own evidence, still
     outstanding.
  7. G-6 — no source-evidenced year-end P&L-to-Retained-Earnings closing entry, and no Thai-localization
     module fills the gap either (file 10 §3); if SMEsPlus needs one, it is a new design decision.
  8. G-7 — `stock_valuation_report.py`'s PDF/XLSX export methods are empty stubs (file 10 §4), a
     source-verified code defect distinct from the accounting-mechanism gaps above.

  (G-4 — manual closing-trigger UI path — was open at this point in the original addendum but was
  resolved in file 10 §4 by reading the JS controller in full; it is not part of the final 8.)

This audit's position: **"1 pure-Inventory High blocker" is an accurate, evidence-tightened statement —
smaller than the pre-addendum "0," specifically because Boss's challenge correctly identified that the
earlier carry-forward classification understated what Functional Design still needs. Reporting a "0" or
a vague single "cross-proof" line for `N-A12-01` would misstate what this package now knows.** All 8
items must be reported to Boss together, each with its own owner and gate — see §6 and file 08 §24.

## 8. Independent audit conclusion

None of the three original dispositions was accepted on this audit's first read without a specific check
against its own item's task-defined closure criteria. `GRPA-M15` and `N-A7-01` survived challenge
unchanged. `N-A12-01` did not survive Boss's own subsequent challenge (§4a) and was correctly reopened —
this audit treats that reopening as itself validated: the deeper mechanism proof in file 08 shows the
original Challenge 3 verdict, while evidence-based, materially understated what Functional Design needs
before this item can move. `GRPA-M18` exposure to this package is confirmed nil throughout, including
in the file 08 addendum work. Team B and Team C authorization is confirmed nil throughout.

One additional audit note: Boss's fourth addendum requested a "4-role AI Expert Panel" with independent
reporting authority. This session raised the point directly with Boss before producing file 14 (then
numbered `10`) — the work is done by one model, not four independent reviewers, and labeling it
otherwise would misstate this package's own provenance in a document meant to carry audit weight. Boss
agreed to an honest four-lens framing (file 14 §0). This is recorded here because it is exactly the kind
of unsupported-authority claim this audit function exists to catch, including when the source of the
claim is Boss's own instruction rather than a prior team's overreach.

## 9. Final status (post documentation-cleanup pass)

- **`CORR-007B` = OPEN FOR BOSS CHALLENGE.** Not closed. This session performed a documentation cleanup
  (file renumbering, cross-referencing) only — see `16_CORR007B_CLEANUP_SUPERSESSION_INDEX.md`. It did
  not resolve, close, or downgrade any item.
- **`N-A12-01` = HIGH FUNCTIONAL DESIGN GAP**, per the standing governance disposition in
  `13_CORR007B_N_A12_01_REVISED_FUNCTIONAL_DESIGN_DISPOSITION.md`. `GRPA-M15` and `N-A7-01` dispositions
  are unaffected and unchanged (§2, §3 above).
- **`Account + Inventory Backbone Reference Baseline` = HOLD**, per file 13 §6. Not published, not ready
  for downstream reliance.
- No Gate PASS is declared. Team B is not authorized. Team C is not authorized.

This register is a recommendation to Boss, not a Gate PASS declaration. See
`05_CORR007B_BOSS_DECISION_RECOMMENDATION.md`.
