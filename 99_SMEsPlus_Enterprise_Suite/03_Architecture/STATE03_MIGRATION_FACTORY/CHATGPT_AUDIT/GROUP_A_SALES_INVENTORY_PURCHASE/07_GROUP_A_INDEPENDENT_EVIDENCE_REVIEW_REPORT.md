> GROUP A — Sales + Inventory + Purchase | Independent Evidence Reviewer | READ ONLY | No target design | Boss sole Final Approver
> Session: SMEPLUS-26-08-31-GRPA-SIP-IER-004 | Independent Evidence Review Report

# 07 — GROUP A INDEPENDENT EVIDENCE REVIEW REPORT

## 01 — What this review did differently from reading Team A's report

This review did not accept Team A's closure narrative on its own terms. It:

1. Independently re-opened every line-cited source-code excerpt for the two closed Critical technical findings
   (Purchase cancellation cascade; `_run_buy()`/MTO/`'buy'` registration) directly against the actual Odoo source
   on disk, not against Team A's quoted excerpts.
2. Independently restored the actual 65 MB `iTEST02` PostgreSQL dump into a **freshly created** local database
   (discovering and resolving a real tooling incompatibility along the way — see §03) and ran its **own** SQL
   queries against `ir_module_module`, `ir_model_fields`, `ir_model_data`, and the row-level `purchase_order`/
   `purchase_request` tables, rather than trusting the numbers in Team A's report.
3. Independently recomputed SHA-256 for all 19 evidence files against the frozen commit.
4. Independently confirmed the numbered governance-section citations (§5, §6, §12, §13, §15, §17, §19, §21, §22)
   scattered throughout Team A's evidence actually exist, with matching titles, in the governing prompt.
5. Independently searched the entire local volume (not just the extraction Team A was given) to confirm the three
   approval modules' source code is genuinely absent everywhere, not just from Team A's specific extraction.

## 02 — Cluster-by-cluster verdicts

| Cluster | Verdict | Full detail |
|---|---|---|
| A — R7 Purchase cancellation re-performance | **VERIFIED** | `02_GROUP_A_R7_R8_REPERFORMANCE_MATRIX.md` §01 |
| B — R8 Procurement→Purchase re-performance | **VERIFIED** | `02_GROUP_A_R7_R8_REPERFORMANCE_MATRIX.md` §02 |
| C — R6 Approval evidence boundary | **VERIFIED** | `03_GROUP_A_APPROVAL_EVIDENCE_BOUNDARY_REVIEW.md` |
| D — Fit-Gap neutrality / TBRAC | **NEUTRAL / SAFE**, one wording qualifier | `04_GROUP_A_FIT_GAP_NEUTRALITY_TBRAC_REVIEW.md` |
| E — Gate package / hash / gap consistency | **VERIFIED** | `05_GROUP_A_GATE_PACKAGE_AND_HASH_RECONCILIATION.md`, `06_GROUP_A_REMAINING_GAP_GATE_IMPACT_REGISTER.md` |

## 03 — The one material finding this review discovered on its own

Team A's corrective-session methodology note states PostgreSQL 16 (Homebrew) was used to restore the `iTEST02`
dump and encountered 18 isolated, ignorable restore errors. Independently attempting the identical restore with
PostgreSQL 16.15 failed immediately and completely with a hard archive-version-incompatibility error — the dump
was produced by PostgreSQL 18.4 and cannot be read by v16 tooling at all. Installing PostgreSQL 18 resolved this,
and the restore then produced 30 (not 18) ignored errors of the same category Team A described.

This is reported prominently because it is exactly the kind of thing an independent review exists to catch:
**a documented methodology detail that does not survive literal reproduction.** However, it resolves in Team A's
favor on substance: every single quantitative claim resting on that restoration — module install states,
versions, authors, field declaration types, row counts, percentages, and state-value distributions — was
independently reproduced **exactly**, via this review's own fresh restore and its own SQL queries, not by reading
Team A's numbers back. The most parsimonious explanation is that Team A's restoration genuinely happened and
genuinely queried this exact dump, using tooling that was not accurately described in the write-up (e.g. a
different or additionally-installed PostgreSQL major version), rather than that the row-level findings were
invented. See `03_GROUP_A_APPROVAL_EVIDENCE_BOUNDARY_REVIEW.md` §00a for the full account.

## 04 — Audit VETO challenge questions — answered

1. *Do the exact source references support closure of Purchase cancellation and procurement→Purchase findings?*
   **Yes** — independently re-opened at the cited lines, exact match including two precise line-number citations.
2. *Does row-level dump evidence support the claimed ownership/installation/historical use of the three approval
   modules?* **Yes** — independently re-derived from a fresh restore, not read from Team A's report.
3. *Does the evidence distinguish "module exists/installed/historically used" from "internal workflow verified"?*
   **Yes** — Team A's own register (file 07 §04, file 08 §03a) already draws this line explicitly, and this
   review confirms the workflow-logic half genuinely cannot be resolved (module source confirmed absent
   machine-wide).
4. *Is `to_check_level` treated only as an observed DB state where source is unavailable?* **Yes** — correctly
   labeled "SUPPORTED INFERENCE from live data, not directly-read source" in Team A's own text.
5. *Are SHA-256 claims reproducible and accurately scoped?* **Yes**, fully reproducible; the scoping note (files
   17/18 cannot self-hash) is accurate and was self-corrected by Team A before this review began.
6. *Does any stale statement in the Gate package contradict CORR-003 results?* **No** newly-found stale
   statement; the one that existed was already caught and fixed by Team A (see finding in §05 of the hash file).
7. *Is any executor self-declaration being treated as independent verification?* **No** — every material
   technical claim in Clusters A/B/C was re-derived from primary evidence by this review itself, not accepted on
   Team A's word.

## 05 — TBRAC challenge questions — answered

Customer-specific historical patterns (e.g. the 96.9%-single-default-user pattern on `level1_user_id`) are kept
explicitly separated from any Thailand-wide claim throughout files 11/12 — independently confirmed by this
review's line-by-line pass (`04_GROUP_A_FIT_GAP_NEUTRALITY_TBRAC_REVIEW.md` §01). One Fit-Gap rationale sentence
(item 15) lapses into an unqualified general-business-practice claim — flagged, not Gate-blocking.

## 06 — EXPERT IBPV / IDTM / IESA advisory challenge questions — answered (advisory only, not formal verification)

- **IBPV**: lifecycle/event/handoff facts for cancellation and procurement→Purchase are sufficiently evidenced for
  downstream design work (independently confirmed). Approval trigger/state/permission/SoD semantics remain
  genuinely unknown pending module source — correctly registered, not blocking. The evidence handoff stays at the
  business-semantic level; ADAPT/EXTEND/REJECT/UNKNOWN labels are explicitly non-authoritative.
- **IDTM**: cancellation and procurement findings are precise enough (exact file+line, exact guard conditions) to
  become future test-oracle inputs. Approval workflow remains a genuine test-oracle gap at button/transition
  level, correctly so.
- **IESA**: the package exposes cross-domain risk (no DB CHECK constraints anywhere in the domain; wide
  shared-table pattern; method-name collisions) without claiming production readiness. Approval remains a
  system-level control dependency with unverified internal workflow — correctly preserved as such, not
  converted into a target architecture decision anywhere in the pack.

## 07 — Conclusion

Team A's post-CORR-003 GROUP A evidence package for Sales + Inventory + Purchase survives independent,
adversarial re-performance — including a full from-scratch database reproduction of its single most important
finding — with no Critical or Gate-blocking discrepancy found. One methodology-documentation inaccuracy (§03) and
one wording-qualifier item (Fit-Gap #15) are recorded as corrective notes. See
`08_GROUP_A_EVIDENCE_GATE_RECOMMENDATION_TO_BOSS.md` for the formal recommendation.
