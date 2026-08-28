> DOMAIN_01 — Accounting Core | Team A PART 2 (Sonnet Deep Logical Synthesis)
> Session SMEPLUS-26-08-29-MIG-A-D01-SONNET-001 | Continues Fable Part 1, does not replace it

# 00 — SONNET SYNTHESIS INDEX

## ⚠ COMMIT-CHAIN CLAIM — SELF-CORRECTED THIS ROUND (SONNET-CORR-001)
The prior version of this file claimed `b2e5a2ab7f820fee351475d84a4b3c7eceb3ded3` "does not
exist anywhere in this repository." **That claim was wrong, and the error was mine.**

**Root cause, confirmed:** the working clone used to verify the commit chain was created with
`git clone --depth 1` (a shallow clone), which fetches only the branch tip with no ancestor
history. `git log --oneline` on that clone showed exactly 3 commits — not because the
repository has 3 commits, but because a depth-1 clone cannot show more. I treated that
truncated log as proof of absence. **This is the same class of error the CORR-001 round
retracted for the CHECK-constraint claim: absence in a derived, incomplete instrument is not
absence in the system** — except this time I made it myself, in the same session that had just
documented the lesson.

**Corrected, independently re-verified this round** by unshallowing the clone
(`git fetch --unshallow`) and confirming via both local git and the GitHub API directly:

| SHA | Cited as | Verification |
|---|---|---|
| `b2e5a2ab7f820fee351475d84a4b3c7eceb3ded3` | A0/A1 Evidence | **CONFIRMED PRESENT** — direct parent of `c441443`; message: "Team A A0/A1 expert deep-research inventory pack" |
| `c44144387061f3cd48665d499641ce0da540a731` | A0/A1 Closure | CONFIRMED PRESENT |
| `3026575f842aaf97a128263fabb2fdf99d41639d` | Fable Accounting Corrective Evidence | CONFIRMED PRESENT |
| `45d9758b61508e33dc05d9c343b6fb34a6e5bf0c` | Corrective Closure | CONFIRMED PRESENT |
| `947af38ae728a22e3305e8923a0b8d38a9a3c99b` | Sonnet Deep Logical Synthesis | CONFIRMED PRESENT |

All five commits form a single linear chain on branch `SMEsPlus` (376 commits total reachable
from tip as of this correction). **No evidence was ever missing from the repository; my
verification method was.**

## ARTIFACTS IN THIS DIRECTORY
| # | File | Content |
|---|---|---|
| 00 | SONNET_SYNTHESIS_INDEX.md | This file |
| 01 | DEEP_LOGIC_SYNTHESIS.md | Narrative synthesis + conceptual business logic model |
| 02 | CRITICAL_FINDING_REASONING.md | 13-point independent reasoning, all 6 critical findings |
| 03 | ACCOUNTING_PRINCIPLE_REGISTER.md | Principle vs requirement vs pattern vs vendor behaviour, separated |
| 04 | BUSINESS_INVARIANT_REGISTER.md | 6 invariants, each with failure consequence and current status |
| 05 | GENERIC_BUSINESS_RULE_REGISTER.md | 13 rules, vendor-name-free |
| 06 | STATE_EVENT_LOGIC_ANALYSIS.md | Neutral lifecycle vs vendor state machine |
| 07 | MATHEMATICAL_REASONING.md | 8 formalized models incl. 1 new finding (unconstrained balance column) |
| 08 | CROSS_SOURCE_TRIANGULATION.md | 9/9 A6 targets, 11 real citations |
| 09 | EXCEPTION_FAILURE_ANALYSIS.md | 17 scenarios, 4 newly surfaced unknowns |
| 10 | CLASSIFICATION_REASSESSMENT.md | 3 independent reclassifications, documented |
| 11 | RESIDUAL_UNKNOWN_REGISTER.md | 20 open items, zero progress credit |
| 12 | REFERENCE_TO_ADVANCEMENT_REGISTER.md | 8 advancement candidates, 1 new (ADV-07) |
| 13 | TEAM_B_CANDIDATE_INPUT.md | Sanitized, vendor-name-free candidate set |
| 14 | SONNET_EVIDENCE_COMPLETENESS.md | Controlled metrics; commit-chain check |
| 15 | TEAM_A_PART2_STATUS.md | §29 quality self-test; stop condition |
| — | FABLE_SONNET_DISAGREEMENT_REGISTER.md | 3 documented disagreements |

## RELATIONSHIP TO PART 1
Part 1 (Fable) found and proved. Part 2 (this directory) understands, challenges, and
synthesizes. **No Part 1 artifact is modified or overwritten** — per directive §26, all
disagreement is recorded as disagreement, not silent correction.

## HEADLINE RESULT
The domain's six critical findings reduce to one underlying design posture: every guarantee
the reference system provides (balance check, tamper-evidence, lock enforcement, correction
discipline) **exists but is revocable** — application-suppressible, opt-in, bypassable, or
simply not the only available path. Full reasoning: `01_DEEP_LOGIC_SYNTHESIS.md`.

## STATUS
```
READY FOR CHATGPT INDEPENDENT AUDIT
```
Team B NOT activated. No SMEsPlus design produced. STEP remains TBD / BASELINE LINKAGE REQUIRED.
