# SA_CORR2_08 — GOVERNANCE VERDICT NORMALIZATION
## CP-SA-C2-60 (second half) — GOVERNANCE CLAIMS CONTROLLED

Session: `[SMEPLUS-26-09-08-PHASE-SA-CORR2-XMOD-001]`
Governing law: master prompt §8 — *"search for prohibited or authority-confusing verdict wording
such as `PASS` where the constitution reserves final approval to Boss. Normalize wording so that
intermediate bodies report findings/readiness only."*

---

## 1. The finding that changes `SA13-F-01` and Boss Decision 3

`SA13-F-01` reported that the gate which authorized Phase SA entry *"declares a verdict the
constitution prohibits"*, and `SA19` §20 Decision 3 asks Boss to direct its disposition. The
implication a reader takes is that a session used a word it was forbidden to use.

**CORR2 read the instrument that commissioned that gate. It is a Boss ruling, and it mandates the
vocabulary.**

> **Boss approves the SMT + Secretary recommendation to proceed immediately with the One Final
> Independent Gate for Account Phase S.**
> **The technical team shall execute and summarize the final `PASS / HOLD` recommendation for Boss.**
> Boss is not required to inspect technical mechanics…
> — `.../ACCOUNT_FINAL_INDEPENDENT_GATE_2026_09_08/BOSS_APPROVAL_FINAL_INDEPENDENT_GATE_2026_09_08.md`, §"Boss ruling", line 12

and the execution prompt issued under it:

> `Verdict: \`PASS / FAIL / HOLD\` with exact evidence.` … `No narrative PASS without evidence.`
> — `.../GPT56SOL_ACCOUNT_PHASE_S_FINAL_INDEPENDENT_GATE_PROMPT_2026_09_08.md`, lines 115, 347

> **`C2-F-22`. The gate used the vocabulary Boss instructed it to use, in the role Boss assigned it —
> a *recommendation to Boss*, not an approval. `SA13-F-01`'s framing is corrected: this is not a
> session exceeding its authority. It is a contradiction between two Boss-level instruments** — the
> standing session constitution, which prohibits `PASS` in verdicts, and this Boss approval, which
> requires a `PASS / HOLD` recommendation.

**Only Boss can resolve which instrument governs.** Until then, **the 269-and-more affirmative `PASS`
occurrences are not evidence of misconduct**, and this register does not present them as such. That
matters: an accusation of constitutional breach against a gate that was following a Boss instruction
would be a serious and avoidable error in a pack Boss reads.

`SA13-F-01`'s underlying observation stands and is worth keeping: **the entry authorization is
expressed in a word that reads as approval**, and that reading has now propagated. What changes is
the owner of the defect and therefore the remedy.

---

## 2. Measurement, with its exclusion list published

| Clause | Declaration |
|---|---|
| POPULATION | v2 corpus, 3,789 blobs (U1) / 3,561 text paths (U2) |
| PATTERN A | `\bPASS\b`, case-sensitive → **1,011 blobs** — reported only to show the raw surface; it is not the finding |
| PATTERN B, verdict-shaped | `(^\|[\|:—–-] *\**\|= *\**\|✓ *\**)PASS\b` |
| EXCLUSION LIST | `may not \| must not \| never \| no PASS \| not declare \| prohibit \| forbidden \| reserved for \| does not \| shall not \| NOT SATISFIED \| not empowered \| 0 .?RC-PASS \| is not PASS` |
| POSITIVE CONTROL | `\bFAIL\b` → **352 blobs**. Fires |
| NEGATIVE CONTROL | `\bZZQQPASS\b` → **0** |
| **RESULT** | **273 blobs → 269 unique paths carry an affirmative `PASS` verdict** |

### 2.1 `C2-F-23` — this count cannot be published as a single number, and here is the proof

Two runs of this measurement in this session, over the identical population, differed:

| Run | Exclusion list | Blobs | Paths |
|---|---|---|---|
| Internal challenge | 12 terms | 294 | **289** |
| This register | the same 12 **plus** `0 .?RC-PASS` and `is not PASS` | 273 | **269** |

**Twenty paths, purely from two extra negation forms.** Both runs are correct given their lists;
neither is reproducible without it.

> **A count of prohibited wording is a count of *what a filter failed to exclude*. Publishing the
> number without the exclusion list publishes an artefact of the filter.** The programme's
> denominator rule needs a fifth clause for negation-shaped searches: **POPULATION + PATTERN +
> PATH SET + UNIT + EXCLUSION LIST.**

Worked example from inside this very measurement: the **three paths with the widest branch
multiplicity (12 branches each)** all match Pattern B — and on inspection all three are
**negations** (`0 RC-PASS`, `READY is not PASS`, `Prohibited PASS / closure wording … 0 matches`).
An unfiltered report would have named the corpus's most scrupulous documents as its worst offenders.

### 2.2 Distribution

Branch multiplicity of the 269 paths: 230 on 1 branch, 27 on 2, and 12 paths on 4–12 branches.
**Roughly 130 of the 269 exist only on `origin/SMEsPlus`** and were invisible to this round's first
corpus frame (`C2-I-02`) — including the repository front page, which reads
`**State 01:** **CLOSED — PASS WITH CONTROL**`.

**The densest concentration — 18 paths — is the Final Independent Gate directory**, and §1 explains
why: it was instructed to use the word.

---

## 3. The seven CORR1 findings accepted-and-uncorrected — now dispositioned

`SA20` §4 listed eight findings *"accepted and carried as open, not yet corrected"*. One (`SA13` §6)
was corrected at `K2-03`. The remaining seven are closed here.

| `SA20` §4 finding | CORR2 disposition |
|---|---|
| The three convergence claims are one classification expressed three times; `SA06`/`SA07`/`SA04` cite `SA05`/`SA01` in their own status columns | **CLOSED — and it is worse than accepted.** `SA_CORR2_06` §1 (`C2-F-16`): they shared not a classification but an **undeclared pattern**. `SA07` §4's convergence is withdrawn in full |
| `SA07` §4's *"one-to-one"* seven-item mapping is wrong — 2 of 7 do not correspond | **CLOSED — moot.** All seven `UNKNOWN` rows are re-adjudicated; the set no longer exists (`SA_CORR2_06` §2) |
| `SA04-F-01`'s *"two independent measurements"* is the same defect, uncorrected | **CORRECTED BY POPULATION** — `K2-09` below |
| `SA04-F-01`'s *"every route with an Accounting endpoint is evidenced"* is broken by R-27 in the same paragraph | **CORRECTED** — `K2-09`. And R-27 Service→Accounting is itself now `PARTIAL` (`SA_CORR2_06` `AR-26`) |
| `SA13` §4.2 declares `G-01`/`XD-06` *"closed"* while `SA14` registers it `OPEN` | **CLOSED — `XD-06` is OPEN**, and `SA_CORR2_06` §6 states the three obligations its contract must carry. `K2-10` |
| `SA12` §4 says "Four" Nature DNA determinations; there are eight | **CORRECTED** — `K2-11`. There are now **eleven** (`ND-01`…`ND-11`) |
| `SA11-F-03`'s §5/§6 wording still asserts the absence that §7.1 corrects | **CORRECTED** — `K2-12` |
| `SA05-F-01`'s *"closing five domains closes all seven"* is asserted and untested | **TESTED, AND FALSE** — `SA_CORR2_02` §5 (`C2-F-06`): four natures, four different causes, only one of which research can close |

---

## 4. Governance wording corrected in this round

Applied **by population**, scoped by claim class.

| # | Correction | Target | Verified |
|---|---|---|---|
| `K2-09` | `SA04-F-01`'s *"two independent measurements agreeing"* withdrawn — the two share `SA01`/`SA05` **and** an undeclared pattern; and *"every route with an Accounting endpoint is evidenced"* narrowed, since R-27 breaks it in the same paragraph | `SA04` §2 | universal removed |
| `K2-10` | `SA13` §4.2's *"the design position is closed"* on `G-01`/`XD-06` corrected — the **ruling** is closed, the **contract** is open | `SA13` §4.2 | consistent with `SA14` `XD-06` |
| `K2-11` | `SA12` §4's *"Four"* corrected to the actual count, and the set extended to eleven | `SA12` §4 | count matches the enumerated list |
| `K2-12` | `SA11` §5's heading and sentence corrected in place, so `SA11-F-03` no longer asserts the absence `SA11-F-04` narrowed | `SA11` §5 | §5 and §7.5 now agree |
| `K2-13` | `SA13-F-01` re-framed per `C2-F-22` — a contradiction between two Boss instruments, not a session breach | `SA13` §3 | the Boss ruling is quoted in place |
| `K2-14` | `SA15-F-02`'s *"a ruled boundary with no assured flow"* qualified — all five decisions carry `APPROVED DIRECTION / DETAIL DESIGN PENDING` (`N-15`) | `SA15` §6 | matches the decision bodies |

---

## 5. Other authority-confusing verdicts — measured

| Verdict | Blobs | Affirmative uses |
|---|---|---|
| `PRODUCTION READY` | 21 | **0** |
| `READY FOR PRODUCTION` | 40 | **0** |
| `GO LIVE` / `GO-LIVE` (uppercase) | **0** | — |
| `SIGNED OFF` / `SIGN-OFF` | 5 | **0** — all *"required"* or *"open"* |
| `CERTIFIED` (uppercase) | 23 | **7 lines across 6 paths** — §6 |
| `APPROVED` | 316 | near-zero non-Boss-attributed; 3 candidates, §7 |

All 61 `PRODUCTION READY` / `READY FOR PRODUCTION` hits were read individually. **Every one is a
prohibition or a declaration of non-declaration**, e.g. *"Claude must not mark `APPROVED`, `PASS`,
`BUILD READY`, `RELEASE READY`, or `PRODUCTION READY`"*.

`GO LIVE` is a **controlled zero**: uppercase → 0 blobs while case-insensitive `go[ -]live` → 29
blobs, all lowercase prose (*"before any production go-live decision"*). **The instrument fires; the
verdict genuinely does not exist.**

---

## 6. `C2-F-24` — `B-35` is recorded as both `CERTIFIED` and `NOT CERTIFIED`

| Side | Blobs | Verbatim |
|---|---|---|
| Affirmative | **5** | `**Status: CERTIFIED for the published B-35 control set.**` · `Status: **PASS — B-35 CERTIFIED**` · `- GATE-05 B-35: **PASS / CERTIFIED**` |
| Negative | **4** | `**STILL NOT CERTIFIED — \`B-35\` stands**` · `\`RC-05\` WAS NOT RUN AND IS NOT CERTIFIED` |

**The same object carries opposite terminal words in the same corpus, and no register reconciles
them.** Independently of which is right, the word itself is the problem: Boss decision `04` reserves
certification to a qualified independent body —

> `GRAO-03 — DESIGNER MUST NOT SELF-DECLARE INDEPENDENT CERTIFICATION.`
> `GRAO-05 — SECURITY SCANNING, VAPT, ISO CERTIFICATION AND SOC ATTESTATION ARE DISTINCT ASSURANCE ACTIVITIES.`

— and `B-35` is an **internal instrument control set**. Under `GRAO-03`/`GRAO-05` the correct word
for what was done is **verified**, not **certified**.

**Normalization recommended, not applied.** These files belong to another gate and this session has
no authority to edit another gate's verdict. Carried to `SA_CORR2_13` as the **same** Boss governance
item as §1 — one vocabulary ruling settles both.

---

## 7. `APPROVED` by a non-Boss body — three candidates, and only one is a real finding

Of 316 blobs, verdict-shaped and non-Boss-attributed reduces to about 50 lines; nearly all are
**records of Boss's approval** or baselines with a named `Final Approver: Boss`.

| Path | Line | Assessment |
|---|---|---|
| `43_STEP030211_EXECUTION_LOG.md` | `**Scope Confirmation: APPROVED**` | **A session's own execution log, no approver named**, immediately after its own list of gates not passed. **Self-approval in form.** The one genuine candidate |
| `14_STEP030204_SCOPE_CONFIRMATION.md` | six rows `APPROVED` | **Attributed** — header carries `**Final Approver:** Boss` and `## 1. Boss Authorization Confirmation`. Not flagged |
| `10_STATE02_CLOSURE_RECOMMENDATION.md` | `S02-FINAL-001: APPROVED AND APPLIED` ×4 | A **recommendation** document using terminal approval vocabulary. Routine wording correction |

**Only the first is escalated, and only as a PMO item.** Reporting three where one holds would repeat
the defect this register exists to correct.

---

## 8. Instrument notes for any resumer

Published because each cost this session real time or would have corrupted a published figure.

1. The interactive shell's `grep` is a **wrapper with `--ignore-files`**; a bash-invoked `grep` is
   not. The two disagree — one pattern returned 28 blobs under the wrapper and 32 under the plain
   binary. **Use one binary and say which.** The wrapper also rejects some complex expressions
   outright, which reads like a zero if the exit status is not checked.
2. **Do not batch patterns through a shell array loop** here; it corrupts the path column
   (one run reported 320 paths against 1 matching blob). Single-pattern invocations only.
3. A **case-insensitive** search is the default in the corpus helper and is wrong for acronyms
   (`COSO` / `Ecosoft`).
4. One file with a `.md` extension is a **Word document**; extension is not format.
5. **A diff-based corpus cannot answer an every-branch presence question.** Use a per-branch
   `git rev-parse '<branch>:<path>'` lookup.

---

`CP-SA-C2-60 — GOVERNANCE AND STANDARDS CLAIMS CONTROLLED (execution status).`

Checkpoint completion is **not** Boss approval.

Boss remains the sole Final Approver. No Evidence = No Progress. Never Skip Gate.
