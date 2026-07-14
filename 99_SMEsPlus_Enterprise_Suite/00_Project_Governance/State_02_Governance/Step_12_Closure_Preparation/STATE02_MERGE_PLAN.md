# STATE 02 — MERGE PLAN (PREPARATION — NO MERGE PERFORMED)

Status: **PLAN ONLY — PENDING BOSS AUTHORIZATION** · Prepared By: Claude Code · 2026-07-14 (UTC)

> No merge is performed by this document. Execution occurs **only** on Boss's signed decision
> (`../Step_11_Boss_Decision/06_BOSS_DECISION_FORM.md`).

---

## 1. Verified merge target

| Field | Value |
|---|---|
| **Merge target branch** | `claude/state02-step09-10-execution` (**PR #30**) |
| Contains verified commit | `b6e9ac083a8a33993600f9490475726ffefaf995` (L99-verified) |
| Into (base) | `SMEsPlus` (`bc591f31…`) |
| Merge-base | `bc591f31…` (target is a clean descendant of SMEsPlus) |
| Expected merge type | Clean / fast-forwardable (no conflicts; descends from SMEsPlus) |

**DO NOT use PR #24 as the merge target.** PR #24 head `af6e4c2` lacks the EV-D06/D14/D17 corrections
(verified this cycle) and would regress State 02. The verified content is on PR #30 (and its ancestor
PR #29).

## 2. PR sequence & merge order

| Order | PR | Action | Note |
|---|---|---|---|
| 1 | (precondition) | Boss signs closure decision (form 06) + confirms target = PR #30 | Gate for everything below |
| 2 | **#30** | Merge `claude/state02-step09-10-execution` → `SMEsPlus` (no squash; preserve history) | Publishes verified State 02 governance + Step 08 alignment + Step 09/10/11/12 record |
| 3 | #29 | Auto-superseded (its content is an ancestor of #30) — close as merged-via-#30 or leave | Housekeeping (Boss) |
| 4 | #24 | Superseded by the verified reconciliation — close (do **not** merge) | Housekeeping (Boss) |
| 5 | #28 | Step 08 post-merge evidence — merge only if Boss wants it in baseline (independent of closure) | Optional |

- **No squash** (preserve traceability/commit history, per order).
- Step 09 verified evidence is **not modified**.

## 3. Post-merge finalization (Boss / authorized)

1. Record the **Final Merge Commit** SHA in `STATE02_CLOSURE_CONFIRMATION.md` §5.
2. Boss applies the **effective-closure signature** (date, time, signature).
3. If State 03 released: publish `STATE03_ACTIVATION_NOTE.md`.
4. Optionally add the governance lock note to the Governance Index (Boss-authorized).

## 4. Rollback plan

| Scenario | Rollback |
|---|---|
| Merge needs reverting (pre-propagation) | `git revert -m 1 <merge_commit>` on `SMEsPlus` (creates a clean inverse commit; preserves history) |
| Wrong target merged (e.g., PR #24) | Immediately `git revert -m 1 <merge_commit>`; re-merge PR #30; record incident |
| SMEsPlus moved before merge | Re-fetch; re-check merge-base; if diverged, rebase target on new SMEsPlus and **re-run Step 09 verification** before merge (do not merge a re-based, unverified tree) |
| Closure signed against wrong commit | Correct `STATE02_CLOSURE_CONFIRMATION.md` §5 with the actual final merge commit; Boss re-signs |

No force-push. No history rewrite. Reverts are additive.

## 5. Risk assessment

| ID | Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|---|
| R1 | Merging PR #24 regresses verified fixes (EV-D06/D14/D17) | Medium (named in prior order) | High | Pin target to PR #30/`b6e9ac0`; explicit "not PR #24" gate in form 06 |
| R2 | SMEsPlus advances before merge → divergence | Low | Medium | Re-check merge-base at execution; re-verify if rebased |
| R3 | L99 caveat: no independent local byte-level hash | Known | Low | Optional local `sha256sum -c` by a cloneable-env party (CF-10-01) before merge |
| R4 | Publishing baseline before closure signed | Low | Low | Sequence per Boss decision (Option A vs C); closure §5 records final merge commit |
| R5 | Step 08 own step-gate still HOLD | Known | Low | State 02 closure does not require Step 08 step-gate; classifications already aligned |

## 6. Controls

No merge, close, lock, or State-03 release is performed here. Merge target is the **verified** content
(PR #30), never PR #24. Boss is the sole Final Approver.
