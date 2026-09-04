# G10 — ACCOUNT WAVE A — FINAL GATE REPORT

Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-GAPCLOSE-001`
**Supersedes `CORR1/C10`, which superseded parent file `26`.**
Wave A — Core Ledger & Closing · 2026-09-04

---

## 1. What this round was asked to do, and what happened

Close four named gate blockers, verify Jira publication, re-run the affected Levels, and run a fresh
final independent review.

**All four blockers are closed with evidence. None closed as safe — all four are confirmed defects.**
The fresh review then found **three further cross-boundary mechanisms**, **ten further
balanced-but-wrong cases**, and **contradicted six of the research team's own claims**, including
three affirmative safety claims.

---

## 2. Final dispositions — the four blockers

| # | Blocker | Final disposition | Evidence |
|---|---|---|---|
| `SB-05` | Null-company FX rate crosses company and tenant boundaries | **`VERIFIED DEFECT`** — severity **raised** | `G02` + addendum `B1`. Matched for every company; record rule **explicitly permits** it; **no database boundary**; creatable by any **accounting manager**, not only a system administrator |
| `FX-08` | Branch-scoped rate invisible to a root-scoped resolver | **`VERIFIED DEFECT`** | `G03`. Writer stores the acting company; resolver reads the root. Confirmed on both sides; **four** distinct scoping rules exist over one rate table |
| `FX-07` | Revaluation control contaminated by the par fallback | **`VERIFIED DEFECT`** | `G04`. The report resolves through the same path and guards **only against zero**; `1.0 ≠ 0`, so a par revaluation is presentable and postable |
| `B-05` | Approval engine exists and is bypassable | **`VERIFIED`** — parent finding **rescoped, not withdrawn** | `G05`. Studio engine can gate the posting action, **cannot gate `write`**, and is **skipped under elevated privilege** — a path reachable through online-payment post-processing |

---

## 3. What the fresh review added

### Three cross-boundary mechanisms independent of FX

| # | What crosses | Disposition |
|---|---|---|
| `X-04` | a **period** — parent-scoped journals plus a company-blind, elevated numbering scan | `VERIFIED` |
| `X-05` | a **classification on a posted fact** — a contact re-parent rewrites `partner_id` on posted items **in every company**, with an explicit **hard-lock bypass** | `VERIFIED` |
| `X-06` | a **settlement** — the exigibility guard tests the root, not the company; the partial-reconciliation model has no record rule | `PARTIALLY VERIFIED` |

### The finding that changes the immutability model

`X-05` contradicts `15` L8. The package held that **two** things are unconditionally immutable: a
hashed entry, and the hard lock's forward-only movement. **The hard lock is bypassed by design** on
this path. Hashed entries are still refused, so **one** unconditional immutability survives.

### Six of our own claims contradicted

`AC-01` … `AC-06` in `G09`. Three are **affirmative** claims — "tenant-safe: yes", "enforced",
"everything else is ready" — asserted without an enforcement-level citation.

---

## 4. Coverage

Percentages only where a verified denominator exists.

| Measure | Value | Denominator |
|---|---|---|
| **Wave A function coverage** — semantically covered | **67.1%** (104 of 155) | the enumerated Wave A scope A–H (`02`) |
| **Wave A evidence coverage** | **95.5%** (148 of 155) | as above; the 7 without are findings of absence, each now scope-bounded (`G06`) |
| **Contradiction resolution** | **100%** (16 of 16 registered contradictions resolved or explicitly bounded) | `20`, `C13` |
| **Blocker closure** | **100%** (4 of 4 closed with evidence) | this round |
| **Reviewer claims verified** this round | 4 blockers + 6 self-corrections + 3 crossings re-verified | `G09` |
| **Remaining unknown count** | **41** | 31 carried from `C13` §6, **less 4 closed** this round, **plus 14** newly opened by `G06`, `G09` and the two reviews |
| Negative claims rescoped | **26** across the programme | `G06` §7 |
| Balanced-but-wrong cases | **27**, explicitly a floor | `G08` + `G09` §4 |

---

## 5. Gate recommendation

> # `RECOMMEND HOLD`

**Recommendation only. Boss is the sole Final Approver.**

### The decision rule that applies

The Boss instruction is explicit: *if a tenant-isolation or cross-tenant financial-integrity issue
remains materially unverified, `RECOMMEND HOLD`, and `CONDITIONAL PASS` shall not be used to bypass
`Tolerance = 0`.*

That rule is triggered, and by more than the FX case:

1. `SB-05` — a **verified** cross-company/cross-tenant measurement crossing, creatable by a routine
   accounting role, with no database boundary.
2. `X-05` — a **verified** cross-company rewrite of a **posted** fact that **bypasses the hard lock**,
   reachable with contacts rights and no accounting rights.
3. `X-04`, `X-06` — a period and a settlement crossing, one verified and one partially.
4. `AC-06` — `ir.config_parameter` is a **database-wide** store with no company dimension for every
   key it holds, and at least one accounting key suppresses FX-difference posting for every tenant.

### Why not `CONDITIONAL PASS`

Because the conditions would be exactly the `Tolerance = 0` items, and the instruction forbids that
use. Two of the four crossings were unknown at the start of this round; a third round found them in
one pass. The remainder is not characterised well enough to attach conditions to.

### Why not `FAIL`

**No veto was issued by any of the nine independent reviewers across three rounds.** Both final
reviewers state explicitly that nothing invalidates the semantic model and that every finding
sharpens it in the direction already chosen. The research is deep, its citations were audited and
found free of fabrication or misquotation, and its `REJECT`/`EXTEND` decisions all rest on positive
findings of observed behaviour.

### What the hold is on

Not the semantic model. **The hold is on the affirmative safety claims and the company/tenant
boundary**, which three rounds have now shown to be broader and weaker than each round believed.

---

## 6. Remaining blockers — exact

| # | Blocker | Class | What would close it |
|---|---|---|---|
| `GB-01` | Cross-company/cross-tenant measurement crossing via null-company rates | `VERIFIED DEFECT` | A Boss decision on the SMEsPlus boundary model (`TI-07`), not more research |
| `GB-02` | Cross-company rewrite of a posted fact bypassing the hard lock (`X-05`) | `VERIFIED DEFECT` | As above; plus a decision on whether master-data edits may ever touch posted facts |
| `GB-03` | Four inconsistent company-scoping rules over one rate table, one bypassing record rules | `VERIFIED DEFECT` | `TI-07` |
| `GB-04` | The full extent of cross-boundary exposure is **not characterised** — 10 new cases in one round | **`C — NOT YET SEARCHED`** | A bounded, systematic boundary audit of the accounting domain |
| `GB-05` | Affirmative safety claims across the package are unaudited | governance | Adopt `DR-AC-01`/`DR-AC-02` (`G09` §5) and re-audit the affirmative cells |

`GB-04` is the honest one. The package has three times declared a set of findings complete and three
times had material additions found by independent review. **The correct conclusion is not that the
current list is right; it is that the enumeration method has not yet converged.**

---

## 7. Governance findings for Boss attention

1. **Negatives are now controlled; positives are not.** Twenty-six over-scoped negatives were found
   and rescoped. All three affirmative-claim contradictions this round were "yes / enforced / ready"
   cells with no enforcement-level citation. `DR-AC-01`/`DR-AC-02` proposed.
2. **Independent review is the only control that has ever worked here.** Three rounds, nine
   reviewers, and every material self-correction came from a reviewer — never from the author,
   including in the round that wrote the standard.
3. **Mechanical scanning catches the long tail.** `G06` found 17 unbounded negatives that six
   reviewers had walked past. Both controls are needed; the scan is cheap and should be mandatory
   pre-gate.
4. **Cheap residuals should be closed before a gate, not carried to it.** Two items left
   `NOT YET SEARCHED` yielded findings on the reviewer's first search.
5. **`Tolerance = 0` candidates now number six** — the five in `C10` plus `T0-06`: no cross-company
   rewrite of a posted fact.

---

## 8. Terminal state

> ## `ACCOUNT WAVE A — HOLD WITH EXACT REMAINING BLOCKERS`
>
> Five blockers: `GB-01` … `GB-05`. Four are verified defects requiring a Boss design decision rather
> than further research; the fifth is an uncharacterised remainder requiring a bounded boundary audit.
>
> The four original blockers are **closed with evidence**. The semantic model is **intact and
> unvetoed after three adversarial rounds**.

**Not declared:** final approved · final freeze · Wave A closed · any gate movement · any
implementation authorisation. **Wave B has not started. No source code was modified.**
