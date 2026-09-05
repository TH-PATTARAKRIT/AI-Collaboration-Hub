# P11 — C4 · ERROR POPULATION RECONCILED

`[SMEPLUS-26-09-05-ACC-P11-CORE-RECON-CORR1-001]` · CP-P11C04 · Layer 1 clean-room

> **Recommendation only. Boss is the sole Final Approver.**

---

## 1. Denominator, declared and executed — not taken from the prompt

`POPULATION` every entry in `P11_RESEARCH_ERROR_AND_REVISION_LOG.md` · `PATTERN`
`^## \`P11-E-nn\`` · `PATH SET` that one file at `43195fd` · `UNIT` one error entry.
**Controls run first: positive 1, negative 0.**

> **Executed count: `29`.** The prompt's stated 29 **reproduces**. `P11-E-04` is retained inside the
> population as an entry but is classified **method observation, not an error** — the log has always
> said so, and the 29 is the id count, not an error count. **True error count: 28.**

## 2. Classification

| id | Class | One-line |
|---|---|---|
| `E-01` | arithmetic / publication | headline contradicted its own table |
| `E-02` | scope | superseded tenant+company-everywhere assumption |
| `E-03` | ranking / selection | glob excluded `P10` from its declared population |
| `E-04` | **not an error** — method observation | a peer worktree changed between two reads |
| `E-05` | **decision-authority** | Boss ruling `D-01` inverted and attributed to the ruling that superseded it |
| `E-06` | **decision-authority** | an undecided decision package listed among governing controls |
| `E-07` | arithmetic | trace-lane headline contradicted itself in one sentence |
| `E-08` | interpretation | accounting-standard requirements presented as Thai statute |
| `E-09` | evidence-population | two of TAS 2 ¶13's four requirements dropped |
| `E-10` | interpretation | `DC-09` overclaimed as novel |
| `E-11` | interpretation (logic) | the stated subledger rule was not the rule applied |
| `E-12` | **tool-capability** | intake script inert by construction |
| `E-13` | scope | negative-claim boundary declared once, not applied package-wide |
| `E-14` | evidence-population | the round's premise expired mid-session |
| `E-15` | **denominator** | a count published without its declared population |
| `E-16` | **denominator** | `T0-13` scoped from its occasion; owed enumeration never performed |
| `E-17` | **extraction** (secondary source for primary) | attribution published without opening the file cited two lines earlier |
| `E-18` | **denominator** | actor count inherited from a peer, never executed |
| `E-19` | **denominator** | a declared half asserted rather than enumerated |
| `E-20` | interpretation | correct finding, overstated consequence — **unplaced by agreement with `P07`** |
| `E-21` | **decision-authority** | a classification adopted for a partly wrong reason (deference) |
| `E-22` | **tool-capability** | an incapacity asserted about a peer and never tested |
| `E-23` | interpretation | internal contradiction in P11's method proposal |
| `E-24` | **tool-capability** | a cost classification resting on an untested capability claim |
| `E-25` | **tool-capability** | a capability test that stopped at the first failing tool |
| `E-26` | **publication / lineage** | correction register claimed corrections never made |
| `E-27` | **tool-capability** | the audit that found `E-26` failed the same way first |
| `E-28` | ranking / selection | evidence base chosen by traversal order |
| `E-29` | publication / lineage | `E-28` restated; original preserved |

## 3. Distribution

| Class | Count |
|---|---|
| tool-capability | **5** |
| denominator | **4** |
| interpretation | **5** |
| decision-authority | **3** |
| publication / lineage | **2** |
| ranking / selection | **2** |
| evidence-population | **2** |
| scope | **2** |
| arithmetic | **2** |
| extraction | **1** |
| *not an error (method observation)* | 1 |

> **The two largest classes — tool-capability (5) and denominator (4) — are nine of twenty-eight, and
> every one of the nine is a claim about *what P11 could see*, not about accounting.** That is the
> shape of this package's error profile and it is stable across the whole session: **P11's accounting
> reasoning was rarely wrong; its statements about its own evidence base repeatedly were.**

## 4. Changed by CORR1

| Change | Detail |
|---|---|
| Re-classified | **`E-16` → denominator**, on `P07`'s ruling that an owed-but-unattempted enumeration is inside Class 2. Previously *"neither class"* |
| Restated | **`E-28`** via `E-29` (C1) — original preserved unchanged |
| Added | **0.** CORR1 adds no new error to this register; `P11-F-12` is a **finding**, not an error |
| Withdrawn | **0** |

**`E-26` remains the highest-severity entry**, and its repair — `X2-F06` — is **still open** as
`P11-B-17`. **No error is closed by CORR1**, and improved wording closes nothing.
