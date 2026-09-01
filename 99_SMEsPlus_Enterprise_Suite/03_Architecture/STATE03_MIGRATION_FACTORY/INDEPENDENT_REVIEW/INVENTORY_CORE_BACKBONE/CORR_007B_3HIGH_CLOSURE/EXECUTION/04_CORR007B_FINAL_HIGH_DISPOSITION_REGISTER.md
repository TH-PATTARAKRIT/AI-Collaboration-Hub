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

## 4. Challenge 3 — `N-A12-01`

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
| `N-A12-01` | `HIGH REMAINS — Accounting x Inventory cross-proof required` | **CONTROLLED CARRY-FORWARD** (Accounting x Inventory cross-proof) | File 03 | Team A jointly with Accounting/Tax domain | Future joint Accounting x Inventory cross-proof session |
| `GRPA-M18` (WHT) | Out of this package's scope — see task preamble | **UNCHANGED, NOT TOUCHED** | CORR-007A, recommendation pending Boss acceptance | Accounting/Tax (per CORR-007A) | Boss decision on CORR-007A, independent of this package |

## 7. Blocker count — before and after, stated without rounding the risk away

**Pure Inventory Evidence Gate High blockers (items where Inventory alone owns the unresolved gap):**

- Before CORR-007B: **3** (`GRPA-M15`, `N-A7-01`, `N-A12-01`) — matches the task preamble's own count.
- After CORR-007B, if Boss accepts all three dispositions: **0.**

**Total open items requiring further work before Inventory cutover can be considered fully de-risked
(this is the number this audit insists Boss actually see, not the headline 0):**

- **3** — unchanged in count, each recategorized with a named owner and gate:
  1. `purchase_request_id` data-content verification (Team A / Migration).
  2. Count-freeze design-policy selection (Team B, not yet authorized to start).
  3. Accounting x Inventory fiscal-year cross-proof (Team A + Accounting/Tax, joint session not yet
     scheduled).

This audit's position: **0 pure-Inventory High blockers is an accurate statement about evidence
completeness for the Inventory domain specifically. It is not a statement that 3 real open items have
disappeared.** Both numbers must be reported to Boss together; reporting only the "0" would misstate
what this package actually established.

## 8. Independent audit conclusion

None of the three dispositions was accepted on this audit's first read without a specific check against
its own item's task-defined closure criteria. All three survived challenge. No item was elevated back
to High, and none was found to require elevation beyond where Teams I1–I3 placed it. `GRPA-M18` exposure
to this package is confirmed nil. Team B and Team C authorization is confirmed nil.

This register is a recommendation to Boss, not a Gate PASS declaration. See
`05_CORR007B_BOSS_DECISION_RECOMMENDATION.md`.
