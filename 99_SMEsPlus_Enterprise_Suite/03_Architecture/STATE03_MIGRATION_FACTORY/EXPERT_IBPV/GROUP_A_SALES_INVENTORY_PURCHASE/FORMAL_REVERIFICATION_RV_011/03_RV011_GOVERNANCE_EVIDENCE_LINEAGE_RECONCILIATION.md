> GROUP A — Sales + Inventory + Purchase Integrated Backbone | EXPERT IBPV — Formal Re-Verification RV-011

# 03 — GOVERNANCE EVIDENCE / BRANCH-LINEAGE RECONCILIATION

Document ID: `SMEPLUS-26-08-31-IBPV-GRPA-SIP-RV-011-D03`

## 00 — The Claim Under Test

CORR-010's own preflight document
(`CORRECTIVE_CORR_010/29_CORR010_PREFLIGHT_AND_FINDING_REPRODUCTION.md` §01, §02) states, for two cited
coordinates:

> "Canonical Governance Baseline at Prompt Creation | `36820bf574272fc1d818da178584fd4cec04826b` | **NOT FOUND.**
> `git cat-file -t` fails for this object in this repository."
>
> "Five-Unit readiness record `BOSS_GATE/GROUP_A_SALES_INVENTORY_PURCHASE/GROUP_A_CORR010_NON_ACCOUNTING_PRE_PROMPT_FIVE_UNIT_CHALLENGE.md`
> | — | **NOT FOUND** anywhere in the repository."

This deliverable independently tests that claim against the actual repository, per the governing prompt §3.4 and
§4 (RV11-08), rather than accepting or repeating it.

## 01 — Independent Result: Both Exist, on Canonical `SMEsPlus`

| Coordinate | Independent check | Result |
|---|---|---|
| Commit `36820bf574272fc1d818da178584fd4cec04826b` | `git cat-file -t 36820bf...` run against the fetched repository | `commit` — **exists**. |
| Same commit, reachability from canonical | `git branch -a --contains 36820bf...` | Returns `remotes/origin/HEAD -> origin/SMEsPlus`, `remotes/origin/SMEsPlus` — **on canonical `SMEsPlus`**, not on any other branch. |
| `GROUP_A_CORR010_NON_ACCOUNTING_PRE_PROMPT_FIVE_UNIT_CHALLENGE.md` | `git ls-tree -r --name-only 36820bf...` | File is present at exactly
`99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/BOSS_GATE/GROUP_A_SALES_INVENTORY_PURCHASE/GROUP_A_CORR010_NON_ACCOUNTING_PRE_PROMPT_FIVE_UNIT_CHALLENGE.md`,
committed by `36820bf...` itself. Content independently read in full — see §04 below. |

**Both coordinates exist in this repository.** CORR-010's "NOT FOUND" statements are factually incorrect as
statements about repository-wide existence.

## 02 — Root Cause, Independently Traced (Not Assumed)

The governing prompt §4 permits stating only the narrow fact if an exact cause cannot be proven:
`EVIDENCE EXISTS REMOTELY; IT WAS NOT VISIBLE/REACHABLE IN THE EXECUTOR'S AUDITED LINEAGE/LOCAL VIEW.` This
session went further and independently traced the exact mechanism, using only `git` ancestry commands — not
narrative inference:

1. **Is `36820bf...` an ancestor of the CORR-010 branch tip (`e44186448...`)?**
   `git merge-base --is-ancestor 36820bf... e44186448...` → **false.** This is the direct, mechanical explanation
   for the executor's `git cat-file -t` failure *if* that command was run from a checkout whose object database
   was populated only from the branch lineage it was working on (a shallow or branch-scoped fetch would produce
   exactly this symptom; a full `git fetch --all` against `origin`, as this session performed, does not).

2. **Where does the TEAM B GROUP A corrective lineage actually fork from canonical `SMEsPlus`?**
   `git merge-base e44186448... origin/SMEsPlus` → `8f5fa522a3f1a3553584eb5d5063238eec6a88a2` ("audit(domain-01):
   record COA-G01 CORR2 independent re-audit") — a Domain-01 (Accounting Core) commit, not a GROUP A commit. The
   entire TEAM B GROUP A design-through-CORR-010 lineage (`b98a3b9f` → ... → `e4418644`) is a **linear side-chain**
   that forked from canonical `SMEsPlus` at this single point and was never rebased or merged back from canonical
   at any subsequent step.

3. **What landed on canonical `SMEsPlus` after that fork point, before `36820bf...`?**
   `git rev-list --count 8f5fa522...^..36820bf...` (canonical-only commits between the fork point and the
   governance commit) → **22 commits**, independently confirmed by direct `git log` of that range — a sequence of
   Domain-01/Accounting-Core (`COA-G01R2-CORR3`, `CORR4`, `CORR5`) governance and evidence-closure commits,
   entirely unrelated to GROUP A, followed by `36820bf...` itself (the GROUP A Five-Unit approval, filed under
   `BOSS_GATE/`, committed directly to canonical alongside the Domain-01 governance stream rather than into the
   GROUP A working lineage).

## 03 — Correct Classification

**`GOVERNANCE EVIDENCE EXISTS — CROSS-BRANCH TRACEABILITY / LINEAGE VISIBILITY ISSUE.`**

This is not `EVIDENCE DOES NOT EXIST`. The mechanism, independently reconstructed from git ancestry alone (not
inferred from the executor's own account): this repository's actual governance workflow commits Boss/PMO
approval and gate artifacts directly onto canonical `SMEsPlus`, while long-running corrective work for a single
domain group (GROUP A) proceeds on a linear side-lineage that forked from canonical at one point early in the
GROUP A workstream and was never subsequently re-synced from canonical. Any governance commit landing on
canonical *after* that fork point — including `36820bf...` — is therefore structurally unreachable from a
checkout of the GROUP A side-lineage alone, even though the object and its content are fully present and
resolvable in the same repository via `origin/SMEsPlus` directly. This is a repository-integration/branch-hygiene
pattern, the same general class of issue Formal IBPV RV-009 independently found for the unrelated TEAM A
evidence-citation gap (RV-009 Deliverable 11, item C4) — not a fabrication, corruption, or evidence-destruction
event.

This session does not claim certainty about *why* the executor's own environment reported the object as entirely
absent rather than as "not on this branch" (a shallow fetch, a branch-scoped clone, or a `git log`-only check
without `git fetch --all` would each independently produce that exact symptom, and this session cannot
distinguish between them from repository evidence alone). What is proven, not guessed, is the structural fact in
§02 above: the object is on canonical, the executor's branch never includes it, and the two facts are fully
sufficient to explain a "not found" result without requiring evidence fabrication, deletion, or corruption on
anyone's part.

## 04 — Content Verification — the Five-Unit File Says What the RV-011 Governing Prompt Claims It Says

The file's content (read in full from `36820bf...`) matches the RV-011 governing prompt §4's description exactly:
a Boss-directive Five-Unit challenge authorizing narrow non-Accounting closure of CORR-010's target findings
(`FV006-EVT-004`, `FV006-EVT-005`, `FV006-EVT-001`, RV-009 B1–B8), with Audit VETO status `NO VETO — PROCEED WITH
NARROW NON-ACCOUNTING CLOSURE`, and explicit HOLD preservation for A1 (Accounting/AR-AP) and A2 (legacy approval
internal logic). Independently confirmed: this is the authorization CORR-010's own scope (§3 of its evidence
files, cross-checked against Deliverables 04–09 below) is in fact consistent with, even though the CORR-010
executor could not see the document itself.

## 05 — Correction to the Record

CORR-010's `29_CORR010_PREFLIGHT_AND_FINDING_REPRODUCTION.md` §02 and
`37_SESSION_SMEPLUS-26-08-31-MIG-B-GRPA-SIP-CORR-010_CLOSURE.md` are **historical executor observations** — per
the governing prompt's instruction, this session does not edit them to say something different. This deliverable
**supersedes** their "NOT FOUND" characterization for all downstream purposes: any future reader consulting
RV-011 evidence should treat the classification in §03 above, not CORR-010's own text, as the current, correct,
independently-verified statement of governance-evidence status.

## 06 — Verdict

**`VERIFIED WITH CONDITIONS`** — resolved as a repository-integration/branch-lineage-hygiene item, not a design
defect and not evidence of missing Boss authorization. **Condition (PMO-actionable, not TEAM B or IBPV-actionable):
rebase or merge the canonical `SMEsPlus` governance stream into the GROUP A working lineage** (or equivalently,
ensure GROUP A corrective branches periodically re-sync from canonical) so that future executors checking out a
GROUP A branch do not need cross-branch archaeology to see governance commits landing on canonical during a
long-running domain workstream. This mirrors the disposition already recorded for the unrelated TEAM A
evidence-lineage gap (RV-009 D11 item C4) and is carried forward identically in Deliverable 11 below as item C5.
