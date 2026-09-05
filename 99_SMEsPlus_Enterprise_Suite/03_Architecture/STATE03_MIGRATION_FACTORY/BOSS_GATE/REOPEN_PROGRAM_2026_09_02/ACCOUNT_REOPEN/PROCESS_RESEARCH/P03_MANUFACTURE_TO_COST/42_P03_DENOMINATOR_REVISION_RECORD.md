# 42 — P03 DENOMINATOR REVISION RECORD

**LAYER 2 — AUDIT QUARANTINE.** The prior error is preserved verbatim, not deleted.

---

## 1. The original statement, verbatim

P03#01, `01_P03_PROCESS_MAP.md` §3, as first written:

> *"## 3. The two cost injection points, stated precisely
> Everything in the chain reduces to exactly two writers:"*

## 2. Analysis of the error

| Field | Content |
|---|---|
| **Implicit unit** | *A function that changes the carrying value of inventory* — real, correct, and **never written down** |
| **Why incomplete** | `smeplus-denominator-completeness-rule` requires POPULATION + PATTERN + PATH SET + UNIT. Three were declared elsewhere in the package; the **unit was not**. A reader could not reproduce the count or compare it to anyone else's |
| **Aggravating factor** | The same package had already caught an arithmetic denominator error in itself (`C-07`, `02` §2, 11+8≠20) **in the same session**. The lesson was on file and the same class recurred three files away |
| **P04's unit** | Own rate field **or** own driver quantity **or** own destination ledger — disjunctive, broader, equally legitimate |
| **P04's count** | **7** under that unit — P04's own corrected figure. 9 under a posting-artefact unit; 6 under a per-computation unit |

## 3. The second error — P03 propagated a number it had not verified

P03#02 `25` §2 recorded P04's count as **nine**.

- P04's **message** said nine.
- P04's **pushed branch** said seven, and had said so before `25` was written — `06` §2.3:
  *"Corrected after independent challenge. Executed strictly, the unit declared in §2.1
  yields SEVEN, not nine."*

P03 cited the summary and not the source. The rule that would have caught it —
`smeplus-peer-intake-discipline` — was already on file: **a peer's message is a summary; a
peer's pushed branch is the source.** The branch was one `git fetch` away and P03 did not
fetch it until this round.

**Recorded as `RE-P03-11`.** Both errors are the same family: a count accepted without its
unit, then a unit accepted without its source.

## 4. Corrected denominator statement

> **Four units, four counts, all published, none supersedes another:**
> **U1** writer of inventory carrying value → **2** (conversion cost) / **8** (all inventory value, `28` §2)
> **U2** monetisation path → **7**
> **U3** posting artefact → **9**
> **U4** monetary computation → **6**
>
> The governing unit depends on the question: **U1 for product cost, U2 for the
> monetisation surface, U3 for duplicate records.** `27` §5.

## 5. Affected findings, and the effect on each

| Affected | Effect |
|---|---|
| `01` §3 | Unit declared inline; original wording preserved in this file |
| `02` §2 | Count corrected to 11+8+1 (`C-07`); caveat added (`AASP-03`) |
| `25` §2 | **"nine" is wrong.** Corrected to seven, with the four-unit table |
| `25` §3 | *"P03 rates this higher than P04"* — **withdrawn**; it conflated a denominator question with a ledger question (`29` §6, `RE-P03-12`) |
| `28` §2 | U1 appears as **8**, not 2 — same unit, **different population**; stated inline so it is not read as an inconsistency |
| **AAS+ veto, second limb** | **Materially affected.** The proof must run against three units, not one — `38` |
| **Architecture conclusion** | Unchanged. Five of the nine paths never touch inventory value, so no architecture conclusion rested on the wrong number |

## 6. The count that was nearly published wrong a third time

An `awk` row-counter used in this round returned a uniform `9` for every table queried,
including tables that were empty. It was **detected before publication** because the figure
was implausibly identical across unrelated tables, and replaced with a parser that was then
validated against a positive control.

**Recorded as `RE-P03-13`** — a near-miss, not a published error. It is recorded because
`smeplus-totals-are-unverified-claims` holds that controls validating *findings* do not
validate the *arithmetic describing them*, and because the failure mode here — a counter
that returns a plausible number for every input — is the one least likely to be caught by
review of the conclusion.

## 7. Standing correction to P03's method

> Every count in every future P03 artefact states its unit **in the same sentence as the
> number**. A number without its unit is not published, even in a heading, even in a
> summary line.

`23` §6's finding inventory and `21` §1's completeness table were both re-checked against
this rule when `23` was regenerated in this round.
