# 02 — B-7 INDEPENDENCE PROVENANCE AUDIT

# `INDEPENDENCE NOT ESTABLISHED — ROUND 1 AND ROUND 2 ALIKE`

## `CHECKPOINT C`

Session: `[SMEPLUS-26-09-10-PHASE-PRETEST-B7R2-REMEDIATION-NEWSESSION-001]`
Branch: `architecture/account-phase-pretest-b7r2-remediation-2026-09-10-001`
Baseline read: `c91d58406b4ac504f2216e68b9fe16851eb23b2d` · Boss: **SOLE FINAL APPROVER**

> **This audit does not self-certify. Every statement below is a `git` measurement whose command is
> published beside it, and the instrument is shown to fire.**

---

## 0. THE QUESTION, AND THE ANSWER THAT IS WIDER THAN THE QUESTION

The convening prompt asks why **Independent OpenAI GPT-5.6 Sol** was appointed but **Claude Opus 5**
participated in the **Round 2** execution.

**The measurement answers that question and one more the prompt did not ask.**

> ## **The same defect is present in ROUND 1, at `5bd36d62`.**
>
> **B-7 has never been executed by an evidenced independent party. Neither round establishes
> independent assurance.**

This widening is not a re-scoping. `§13` of the convening prompt expressly requires
*"Round-1 independence validity"* to be determined. It is determined here, and the answer is negative.

---

## 1. INSTRUMENT

```
POPULATION : every commit reachable on the three branches carrying B-7 material
UNIT       : commit
PATTERN    : git log --format='%H|%an|%ae|%cn|%ce|%(trailers:key=Co-Authored-By,valueonly)'
PATH SET   : origin/architecture/account-phase-pretest-new-session-2026-09-10-001
             origin/audit/b7-independent-2026-09-10          (Round 1 channel)
             origin/audit/b7-round2-independent-2026-09-10    (Round 2 channel)
AUTHORITY  : the git object store — immutable, written by the executing party, not by this session
```

**Why this instrument and not the documents:** a session name, a prompt name, a branch name, a claimed
role and an executor's self-description are all written by the party whose independence is in question.
The commit trailer is written by the tooling at the moment of execution. It is the only authorship
evidence in the corpus that the audited party does not author as prose.

**Its limit, stated before the result:** a trailer is metadata, not an attestation. It can be absent when
a party did participate, and it is set by the client. It can therefore establish **contradiction** of a
claimed appointment; it cannot by itself establish who *did* execute. **Both conclusions below are
stated at the strength the instrument supports and no higher.**

---

## 2. MEASUREMENT — ROUND 2 (`d878a603`)

```
$ git log -1 --format='%H%n%an <%ae>%n%cn <%ce>%n%(trailers)' d878a603
d878a603a0613dac2616e47d1e87f9ee79af2424
AUTHOR    : TH.PATTARAKRIT SOLUTION SERVICE CO., LTD. <scgl.thailand@gmail.com>
COMMITTER : TH.PATTARAKRIT SOLUTION SERVICE CO., LTD. <scgl.thailand@gmail.com>
TRAILER   : Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
```

| Fact | Measured |
|---|---|
| Appointed executor (`17_` §0) | **Independent OpenAI GPT-5.6 Sol**, *"different vendor"* |
| Author display name | **`TH.PATTARAKRIT SOLUTION SERVICE CO., LTD.`** — **byte-identical to the canonical executor's own display name** on every commit of the challenged branch |
| Model attribution trailer | **`Claude Opus 5`** — the same model family as the challenged package |
| Vendor attribution for OpenAI / GPT-5.6 Sol anywhere in the commit record | **`0`** |

**`CORR2-IPA-01` — MATERIAL.** The Round-2 challenger commits under **the audited party's own corporate
display name** and carries **the audited party's own model attribution**. The appointment required a
different vendor. **The record evidences the same vendor and the same author identity.**

The Round-2 verdict discloses this itself, at its `§0`, before any finding. **That disclosure is
correct, was made against the discloser's interest, and is adopted.**

---

## 3. MEASUREMENT — ROUND 1 (`5bd36d62`) · THE FINDING THE PROMPT DID NOT ANTICIPATE

```
$ git log -1 --format='%H%n%an <%ae>%n%(trailers)' 5bd36d62
5bd36d62fc3e4c105996dd5560871ba7c8caaae5
AUTHOR  : B7 Independent Challenger <jabsung.s@gmail.com>
TRAILER : Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
```

**Compare against the canonical executor, measured on the challenged branch:**

```
$ git log --format='%h|%an|%ae' origin/architecture/account-phase-pretest-new-session-2026-09-10-001 -12
c91d5840|TH.PATTARAKRIT SOLUTION SERVICE CO., LTD.|jabsung.s@gmail.com
fec7c49b|TH.PATTARAKRIT SOLUTION SERVICE CO., LTD.|jabsung.s@gmail.com
94f23976|TH.PATTARAKRIT SOLUTION SERVICE CO., LTD.|jabsung.s@gmail.com
a5bdd625|TH.PATTARAKRIT SOLUTION SERVICE CO., LTD.|jabsung.s@gmail.com
8674f735|SMEs Core                                |jabsung.s@gmail.com
c94839e8|TH.PATTARAKRIT SOLUTION SERVICE CO., LTD.|jabsung.s@gmail.com
… 12 of 12 identical on the address
```

| Fact | Measured |
|---|---|
| Round-1 author **display name** | `B7 Independent Challenger` — **a role label** |
| Round-1 author **address** | **`jabsung.s@gmail.com`** |
| Canonical executor address on the challenged branch | **`jabsung.s@gmail.com`** — **identical, 12 of 12 commits** |
| Round-1 model attribution | **`Claude Opus 5`** — same family as the audited party |

**`CORR2-IPA-02` — MATERIAL.** **Round 1's independence is a display-name change on the audited party's
own account.** The address is the same account. The model attribution is the same family. **The only
element that differs between the "independent challenger" and the audited executor is the free-text
string a committer may set to any value.**

> **A role label is not an identity. Identity is the credential.**

---

## 4. THE CREDENTIAL — ONE ACCOUNT, THREE ROLES

```
$ gh auth status
github.com — Logged in to github.com account scglegacy · Active account: true
              Token scopes: 'gist', 'read:org', 'repo', 'workflow'
```

**One authenticated GitHub identity has push rights to the canonical branch, the Round-1 channel and the
Round-2 channel.** The three "parties" are three display names on one credential.

**This does not prove bad faith and is not offered as such.** It proves that **the apparatus contains no
mechanism by which independence could have been enforced, and none by which it can be verified after the
fact.** An audit control that cannot detect its own failure is not a control.

---

## 5. THE PACKAGE'S OWN ASSERTIONS, MEASURED AGAINST THE RECORD

```
$ grep -rn 'different vendor\|GPT-5.6 Sol\|Independent OpenAI' <frozen NEW_SESSION_2026_09_10 tree>
```

| Where | Asserts | Record |
|---|---|---|
| resume state | *"appointee **Independent OpenAI GPT-5.6 Sol**, new clean session, **different vendor**"* | **CONTRADICTED** |
| `17_` §0 | appoints GPT-5.6 Sol; requires *"different vendor"* independence | **CONTRADICTED at execution** |
| `08_` row `2` | exit condition `2` `SATISFIED — QUALIFIED` because *"`B7-F-13`'s circularity is **cured** — **an independent party has attacked it**"* | **THE GROUND FAILS** |
| `08_` row `15` | condition `15` **`FAIL — RE-OPENED`** — *"a completed challenge against a superseded package does not certify its successor"* | **CORRECT, and correct for a second reason the package did not state** |

**`CORR2-IPA-03` — MATERIAL.** **Exit condition `2`'s cure is withdrawn.** Its sole stated ground is that
an independent party attacked the figure. No independent party is evidenced to have attacked anything.

**`CORR2-IPA-04` — recorded in the executor's favour.** Row `15` re-opened condition `15` on
supersession grounds alone, against the executor's own interest, **before** the independence defect was
known. **The right answer was reached on a narrower ground than the facts supported.** The row stands and
is now over-determined.

---

## 6. HISTORICAL `EC-07` IMPACT

`EC-07` requires **two consecutive clean structurally independent passes**. The frozen package records
`EC-07` `0 / 2` throughout, and `R-D-01` re-places it to the Module and State 8-Criteria Exit Gates.

| Question | Answer |
|---|---|
| Did Round 1 count toward `EC-07`? | **NO** — the package never claimed it did (`08_` row `10`: *"an executed attempt with `6` successful falsifications — **not a clean pass**"*) |
| Does the independence defect change `EC-07`'s numerator? | **NO — it was already `0`** |
| Does it change anything downstream? | **YES — exit condition `2` only** (§5). `EC-07` is unaffected because the package never credited either round to it |

**`CORR2-IPA-05` — recorded in the executor's favour.** **The package's conservatism contained the
damage.** Had either round been credited to `EC-07`, the defect would have propagated into a State-gate
criterion. It was not credited. **`EC-07` `0 / 2` is unchanged and remains correct.**

---

## 7. ROOT CAUSE

| # | Cause | Evidence |
|---:|---|---|
| **1** | **Independence was specified as a description, never as a verifiable set.** `17_` §0 names a vendor and a model. It defines **no artefact** the executing party must produce to evidence identity, and **no check** any later reader can run | `17_` §0; `0` identity artefacts in the Round-1 or Round-2 channels |
| **2** | **Appointment and execution share one credential.** No separate account, key, or channel-write restriction exists | `gh auth status`; three branches, one token |
| **3** | **The apparatus records the appointment, not the execution.** `20_PRETEST_PRE_B7_READINESS_AND_APPOINTEE_CARD.md` is an appointee card. **No counterpart execution card exists** | filename sweep of both audit channels |
| **4** | **The control that would have caught it was scoped to content, not to authorship.** Round 1 verified the manifest `24/24` after execution — an integrity control. **No control in either round tested *who executed*, until Round 2 volunteered it** | `5bd36d62` body |

> **Root cause, one sentence: independence was asserted in prose and never constituted as evidence,
> so the first party to look at the git record found it absent — and that party was the second-line
> challenger, not the apparatus.**

---

## 8. WHAT THIS DOES *NOT* ESTABLISH — stated because a negative must declare its limit

| Not established | Why |
|---|---|
| That any party acted in bad faith | **Nothing measured here supports that, and it is not claimed** |
| That GPT-5.6 Sol did not review anything | A trailer records the committing tool. **Absence of an OpenAI attribution is absence of evidence of participation, not evidence of absence** |
| That the Round-1 and Round-2 **findings** are wrong | **Authorship and correctness are different claims.** `01_` re-tests the findings on their own merits; `18 of 18` Round-1 findings were confirmed by the recovery, and `17` Round-2 findings are dispositioned in `11_` |

**Correct classification: `INDEPENDENCE NOT ESTABLISHED`, not `INDEPENDENCE VIOLATED`.**
The distinction is load-bearing: the remedy is to **constitute** independence, not to punish a party.

---

## 9. GOVERNANCE CLASSIFICATION APPLIED

| Artefact | Classified |
|---|---|
| `5bd36d62` Round 1 | **`B7R1-SECOND-LINE-CHALLENGE`** — findings admissible, **assurance NOT established** |
| `d878a603` Round 2 | **`B7R2-SECOND-LINE-CHALLENGE`** — findings admissible, **assurance NOT established** |
| Either as `EC-07` | **NO** |
| Either as `B7R2-INDEPENDENT-PASS` / `-HOLD` | **NO** |
| Either as FINAL ASSURANCE | **NO** |
| Both as audit lineage | **PRESERVED — `0` commits rewritten, `0` findings discarded** |

**Exit condition `15` (*B-7 completed independently*) remains `FAIL`, and its ground is now
**two** independent reasons: supersession (`08_` row `15`) and non-independence (this file).**

---

## 10. REQUIRED CORRECTION — carried into `16_`

Independence must be **constituted before execution and provable after it**:

1. **Identity recorded before evidence review** — vendor, model, session id, published as the rerun's first act.
2. **A separate credential.** A different git author address, not a display-name change.
3. **A separate channel** the executing party cannot push canonical writes from.
4. **An execution card**, counterpart to the appointee card, produced by the executing party.
5. **A post-hoc check any reader can run** — published as a command with its expected output.
6. **If identity cannot be evidenced: `STOP — INDEPENDENCE NOT PROVEN`. Do not execute the audit.**

---

## 11. CHECKPOINT

> ## `CHECKPOINT C — INDEPENDENCE DEFECT ESTABLISHED`
>
> **Round 2 `NOT INDEPENDENT` · Round 1 `NOT INDEPENDENT` — the second finding was not anticipated by
> the convening prompt and is the wider of the two** · `1` credential, `3` display names ·
> exit condition `2`'s cure **WITHDRAWN** · `EC-07` `0 / 2` **unchanged and never credited** ·
> `4` root causes · `0` commits rewritten · `0` findings discarded ·
> **`B7 INDEPENDENT ASSURANCE = NOT ESTABLISHED, BOTH ROUNDS`.**

No Evidence = No Progress. Never Skip Gate. Truth over Pass.
**Boss is the sole Final Approver.**
