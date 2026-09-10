# SC-24 — `FG-F-06` AUTHORITY COLLISION RECONCILIATION

## CP-SA-SC-180 — `FG-F-06` AUTHORITY COLLISION EXACTLY BOUNDED

Session: `[SMEPLUS-26-09-10-ACC-PHASE-SA-SMECORE-CONT-001]` · head consumed `2cfb57eb`
Executing body: **SMEs CORE** · Boss: **SOLE FINAL APPROVER**

> **This is an authority-conflict reconciliation, not a re-debate of Reading A vs Reading B.**
> **SMEs Core does not choose. `CF-D-01`: *"only Boss may state what a Boss ruling covers."***

---

## 1. Result

> # `NO EXPLICIT SUPERSEDING BOSS INSTRUCTION EXISTS. THE COLLISION IS EXACTLY BOUNDED AND ROUTED TO SC-AUTH-01.`

| Test | Result |
|---|---|
| An explicit Boss instruction selecting one reading **after both alternatives were on the record** | **`0` — searched, with a firing positive control (§3)** |
| Either record explicitly superseding the other | **`0` — neither cites the other's existence** |
| Either record issued in a context containing the other | **`0` — proven ABSENT both ways (`SC-23` §3)** |
| Downstream decisions relying on one of them | **16 Boss rulings + `SC-11` + `SC-12` + the `04_` prompt, all on `SC-BD-01`** |
| Downstream decisions relying on the other | **`0`** — `SC-CONTRA-01` produced preparation only, deliberately |
| **Disposition reachable by SMEs Core** | **NO — Boss authority** |

---

## 2. The nine-point proof, per record

| # | Element | **`SC-BD-01`** | **`SC-CONTRA-01`** |
|---:|---|---|---|
| **1** | Exact source text | *"`FG-F-06 = READING B — DOES NOT BIND THIS EXIT`"* | *"`FG-F-06 = READING A` … binds Phase SA exit to Phase Pre-Test Matrix. Proceed under `EC-07`. `B-7` becomes mandatory…"* |
| **2** | Author / authority | **Boss** — recorded by Executor 1 | **Boss** — recorded by Executor 2 |
| **3** | Timestamp | ruling issued against head `6d08bcc5` (02:18:06); **record published 07:53:13** | ruling issued against head `7eeb5d8e` (02:24:53); record published 08:23:35 |
| **4** | Parent context at issuance | `6d08bcc5` — **contained no Reading A record** (proven ABSENT) | `7eeb5d8e` — **contained no Reading B record** (proven ABSENT) |
| **5** | Scope | the `FG-F-06` scope question only | the `FG-F-06` scope question only — **identical scope** |
| **6** | Explicitly supersedes another ruling? | **NO** — no supersession clause; does not mention Reading A being ruled | **NO** — records the contradiction but **explicitly disclaims priority**: *"does not overwrite, withdraw, amend or supersede `SC-BD-01`, and does not claim priority over it"* |
| **7** | Did Boss actually intend a supersession? | **NOT ESTABLISHED** — §4 | **NOT ESTABLISHED** — §4 |
| **8** | Downstream decisions relying on it | **`SC-BD-02`…`SC-BD-10` (16 rulings), `SC-11`, `SC-12`, the `04_` prompt, `SC-13`…`SC-21`** | **none** — `SC-EC07-01`/`-02` are *preparation*, valid under either reading |
| **9** | What becomes invalid / provisional / historical if superseded | if `SC-BD-01` falls: the 16 rulings' **gate precondition** fails. **Their substance is untouched** — each was a Boss ruling on its own merits; what changes is whether the gate was open when they were made | if `SC-CONTRA-01` falls: `SC-EC07-01`/`-02` become **preparation held in reserve**. **Nothing is invalidated, because nothing was built on it** |

### 2.1 The asymmetry that matters, and it is not about which is right

> **`SC-BD-01` carries 16 downstream rulings. `SC-CONTRA-01` carries none.**
>
> **This is a consequence asymmetry, not an authority asymmetry.** It says which disposition is cheaper,
> not which is correct. **`05_` §3 forbids inferring from it**, and this file does not.
> **It is stated because Boss must know the cost of each disposition before choosing.**

---

## 3. The supersession search — executed, with a firing control

**POPULATION:** every Boss-authored prompt and decision record in the continuation directory (`0*.md`,
`SC-BD-*.md`, `SC-CONTRA-01`), plus the `05_` prompt.
**PATTERN:** `supersede` co-occurring with `FG-F-06` or `READING`.
**RESULT: `0` lines.**
**POSITIVE CONTROL:** `supersede` alone fires in **4** of the prompt files, so the token is live in the
corpus and the co-occurrence zero is a real zero.

**Second shape:** the `05_` prompt was read for a reading selection. It names both readings at lines 98–99,
127–128 and 156–157, and its §3 **instructs the executor to find a supersession rather than asserting one**:
*"If repository evidence contains a clear explicit Boss instruction selecting one reading after both
alternatives were known, treat that as the controlling superseding ruling."* **It selects neither.**

> **`0` explicit superseding Boss instructions exist. The `05_` prompt's preferred closure path is
> therefore unavailable, and its fallback applies: prepare `SC-AUTH-01`.**

---

## 4. Boss intent — the admissible evidence, and why it is not a disposition

**`05_` §3.7 requires this executor to address whether Boss actually intended a supersession. Two pieces of
evidence exist, and they point in opposite directions.**

| Evidence | Points toward | Weight |
|---|---|---|
| **The `05_` prompt applies `8C-001` as governing this exit throughout** — §4 *"`EC-05` MUST CLOSE BEFORE ANY `EC-07` CLEAN-PASS SEQUENCE"*; §5 *"resolve the `EC-04` phase-boundary problem **without lowering the standard**"*; §11 the `EC-07` sequence; §13 Terminal A *"READY FOR STRUCTURALLY INDEPENDENT `EC-07` REVIEW"*; §14 item 4 *"`EC-01`..`EC-08` evidence status"* in the final exit pack | **Reading A** — under Reading B these criteria would not gate this exit at all, and §§4, 5, 11, 13, 14 would be largely moot | **Substantial but IMPLICIT.** It is Boss applying the criteria, not Boss ruling the scope question |
| **The `04_` prompt** (08:21) directed remediation of the Reading B path's `TERMINAL D` gap, i.e. Boss continued driving that path **after** the Reading A instruction | **Reading B** | **Substantial but IMPLICIT** — and `04_` does not mention `FG-F-06` |

> **Both are inferences about intent from downstream instructions, and they conflict.**
> **`05_` §3 forbids resolving on inference:** *"Do not infer that Reading A controls merely because it is
> stricter. Do not infer that Reading B controls merely because it opens the gate. Do not infer that the
> later record controls merely because it is later."*
>
> **SMEs Core therefore records both and disposes of neither.**

---

## 5. Classification of the two records under the `05_` §3 taxonomy

| Taxonomy class | `SC-BD-01` | `SC-CONTRA-01` |
|---|---|---|
| original Boss instruction | **yes** — a Boss ruling on `FG-F-06` | **yes** — a Boss ruling on `FG-F-06` |
| execution-context interpretation | no | no |
| explicit Boss-authored ruling | the **ruling** is Boss's; the **record** is executor-authored | identical |
| executor-authored record of a Boss ruling | **yes** | **yes** |
| later correction | **no** — could not correct what it could not see | **no** — same |
| true supersession | **NO** | **NO** |
| historical lineage only | **not determinable by SMEs Core** | **not determinable by SMEs Core** |

> **Both records fall in the same classes. The taxonomy does not separate them.** That is the finding —
> the collision is not resolvable by classification, only by authority.

---

## 6. What this file explicitly does NOT do

1. **Does not choose a reading**, silently or otherwise.
2. **Does not rank the records** by recency, strictness, or downstream weight.
3. **Does not re-open the Reading A / Reading B merits** — `SC-09`, `SC-10` §9 and `SC-04` §6 hold the
   substantive analysis and are unchanged.
4. **Does not touch any of the 16 rulings**, and does not assert they are void or safe.
5. **Does not modify `SC-BD-01`** — byte-identity verified.

---

## 7. Bounded escalation

> **The collision is now exactly bounded: one question, two named records, all nine proof elements
> established, `0` supersessions found, and the consequence of each disposition stated.**
>
> **Routed to `SC-AUTH-01 — FG-F-06 COLLISION DISPOSITION`.** That card asks **only** which record controls
> prospectively and what becomes of the other. **It does not re-ask the Phase SA design question.**

---

## 8. Checkpoint

> ## `CP-SA-SC-180 — FG-F-06 AUTHORITY COLLISION EXACTLY BOUNDED`
> **9 of 9 proof elements established per record · `0` explicit superseding Boss instructions, searched
> with a firing control · issuance contexts proven **symmetrically blind** · both records classify
> identically under the taxonomy · intent evidence found on **both** sides and disposed of on neither ·
> consequence of each disposition stated · **`0` readings chosen** · routed to `SC-AUTH-01`.**

No Evidence = No Progress. Never Skip Gate. Only Boss may state what a Boss ruling covers.
Boss remains the sole Final Approver.
