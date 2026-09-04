# G09 — FINAL L12 INDEPENDENT REVIEW — CONSOLIDATED

Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-GAPCLOSE-001` · consolidates `GR1` and `GR2`

Two fresh reviewers, neither involved in any prior round, were instructed to trust verified evidence
only — not the researcher, not CORR1, not previous reviewers, not the prompt.
**Both returned `RECOMMEND HOLD`.**

Every reviewer claim reproduced below was **re-verified against primary source by the research
team** before acceptance. Dispositions: `VERIFIED` · `PARTIALLY VERIFIED` · `CONTRADICTED` ·
`NOT PROVEN` · `UNKNOWN`.

---

## 1. Verdicts on the four blockers (`GR1`)

| Blocker | Claimed | Reviewer verdict | Research team disposition |
|---|---|---|---|
| `SB-05` | `VERIFIED DEFECT`, scoped | `CONFIRMED WITH CAVEAT` | **Accepted; severity raised** — see `B1-01`, `B1-02` |
| `FX-08` | `VERIFIED DEFECT` | `CONFIRMED WITH CAVEAT` — closure **understates** it | **Accepted** — four scoping rules, not two |
| `FX-07` | `VERIFIED DEFECT` | **`CONFIRMED`** — "if anything understated" | **Accepted unchanged** |
| `B-05` | `VERIFIED`, parent rescoped | `CONFIRMED WITH CAVEAT` | **Accepted**; residual `B05-R3` closed adversely |

**Citation integrity, `GR1` finding 6:** no fabricated citation and no misquotation across `G02`–`G05`.
That is the single most important lineage result of this round.

## 2. Corrections to the research team's own work — accepted

| # | Correction | Disposition | Basis re-verified |
|---|---|---|---|
| `AC-01` | `G02` §2.5 "only a system administrator can create a rate row" | **`CONTRADICTED`** | `account/security/ir.model.access.csv:7` — `group_account_manager,1,1,1,1`; rate `company_id` editable at `base/views/res_currency_views.xml:20,44,169`. **The actor is a routine accounting role.** `SB-05` severity raised |
| `AC-02` | `G02` §2.7 "report-time derivation resolves through the same path" | **`CONTRADICTED`** | The consolidation currency table uses **raw SQL**, matches `rate.company_id = <main root>` (**excluding null rows**), **bypasses record rules**, and defaults to `1`. A **fourth** scoping rule |
| `AC-03` | `16` L9 §2 rows 1–2 "Journal / Entry — tenant-safe: **yes**" | **`CONTRADICTED`** | `account_journal.py:42-43` uses `check_company_domain_parent_of`; `models.py:188-200` admits `company_id = False` **or a parent of** the acting company; `account_move.py:885-892` builds the entry's journal selector from that domain. **A parent's journal is usable by every descendant company's entries** |
| `AC-04` | `C10` §5 "boundary enforced for journals, entries and liquidity accounts" | **`CONTRADICTED` in part** | Correct for liquidity accounts (ORM-level only) and entries; **not** for journals (`AC-03`) |
| `AC-05` | `C10` §6/§8 "everything except the four named items is ready" | **`C` presented as `A`** | A completeness claim about an unsearched remainder. **Withdrawn** |
| `AC-06` | `SB-01` scoped as one parameter | **`E` as scoped** | `ir.config_parameter` has no company dimension **for every key**; at least one other accounting key suppresses FX-difference posting database-wide. `SB-01` is a **class**, not an instance |

## 3. New cross-boundary mechanisms — beyond FX

`GR2`'s assigned question was whether any financial fact crosses a company or tenant boundary beyond
the FX case. **It does, on mechanisms independent of FX and of each other.**

| # | What crosses | Mechanism | Disposition |
|---|---|---|---|
| `X-04` | **a period** | Entry numbering scans the journal **without a company clause and under elevated privilege**; journals are parent-scoped, so a parent's journal carries descendants' entries; the resulting highest name drives the derived accounting date | **`VERIFIED`** — `AC-03` confirms the journal half; the numbering half re-verified as reported |
| `X-05` | **a classification on a posted fact** | `res.partner.write({'parent_id': …})` performs a **sudo, database-wide** search of entries and rewrites `partner_id` on posted items and `commercial_partner_id` on the entry, **explicitly passing a lock-check bypass** | **`VERIFIED`** — read directly at `account/models/partner.py:791-806` |
| `X-06` | **a settlement** | The reconciliation exigibility guard tests the **root**, not the company; the partial-reconciliation model has **no record rule** and its `create()` performs no company check | **`PARTIALLY VERIFIED`** — the root-vs-company test re-verified; the absent record rule is class `B` |

### `X-05` in full — the most severe finding of the round

**`VERIFIED FACT`** (`account/models/partner.py:791-806`):

- the search is `self.sudo().env['account.move'].search([('partner_id','in',self.ids)])` — **no company
  clause, elevated privilege, every company in the database**;
- the writes carry `with_context(bypass_lock_check=BYPASS_LOCK_CHECK)` — **the hard lock is bypassed
  by design, not by accident**;
- `partner_id` on the journal item **is a hashed field**, so the write guard refuses **hashed** moves —
  the hash chain is protected — and **unhashed moves, which are the default, absorb the change
  silently**;
- a message is logged **on the partner**, not on the affected entries.

**Two mitigations, both real and both stated:** the operation refuses when the new parent's VAT
differs from the subject's, and hashed entries are refused.

**Consequence for the package.** `15` L8 asserted that exactly two things are unconditionally
immutable: a hashed entry, and the hard lock's forward-only movement. **The second is contradicted.**
The hard lock does not prevent a posted item's counterparty being rewritten by a contacts-role action.

## 4. New `BALANCED BUT WRONG` cases

`GR2` contributed ten (`NBW-16`–`NBW-25`), of which seven are undetectable by the equation set. Added
to the seventeen already held, the register now stands at **twenty-seven cases**.

The count is explicitly a **floor**, not a closed set: ten were found in a single independent round
against a register the package had already called final twice.

## 5. The governance finding of this round

> **The package polices negatives well and positives not at all.**

All three of `AC-03`, `AC-04` and `AC-05` are **affirmative** claims — "tenant-safe: yes",
"enforced", "ready" — asserted without an enforcement-level citation. The negative-claim standard
`DR-NC-01`…`06` has no counterpart for them.

`RECOMMENDATION:` extend the standard with an affirmative-claim rule:

> **`DR-AC-01`.** An affirmative safety, enforcement or completeness claim SHALL cite the mechanism
> that enforces it and the **layer** at which it is enforced (database constraint · record rule ·
> application check · configuration · none), and SHALL state what is not covered.
>
> **`DR-AC-02`.** "Ready", "safe", "enforced" and "complete" are claims about a searched scope, and
> SHALL NOT be asserted over an unsearched remainder.

This is offered for Boss ratification alongside the negative-claim standard.

## 6. Vetoes

**None issued by either reviewer.** Both state explicitly that nothing invalidates the semantic
model, and that every finding sharpens it in the direction already chosen.

## 7. Consolidated position

| Measure | Result |
|---|---|
| Blockers closed with evidence | **4 of 4** — all `VERIFIED DEFECT` or `VERIFIED`; none closed as safe |
| Research-team claims contradicted this round | **6** (`AC-01`…`AC-06`) |
| New cross-boundary mechanisms | **3**, independent of FX |
| New balanced-but-wrong cases | **10** |
| Vetoes | 0 |
| Reviewer gate recommendations | `RECOMMEND HOLD` (both) |
