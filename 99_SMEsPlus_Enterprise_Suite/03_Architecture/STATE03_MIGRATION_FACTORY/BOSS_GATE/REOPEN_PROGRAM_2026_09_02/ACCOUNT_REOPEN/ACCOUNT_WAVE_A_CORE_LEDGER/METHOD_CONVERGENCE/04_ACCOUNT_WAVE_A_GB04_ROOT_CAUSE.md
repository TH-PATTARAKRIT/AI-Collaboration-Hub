# 04 — ACCOUNT WAVE A — `GB-04` ROOT CAUSE ANALYSIS

Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-MC-001` · Layer 1 clean-room · cites `MCE-0NN`

`GB-04` as stated by the parent: *"The full extent of cross-boundary exposure is not characterised —
10 new cases in one round. Class `C — NOT YET SEARCHED`."*

The question this file answers is not *what was missed* but **why three rounds each declared
completeness and were each proved wrong by the next reviewer.**

---

## 1. The pattern to be explained

| Round | Declared | Then found by an independent reviewer |
|---|---|---|
| Core | Full-spectrum L1–L12 complete | 4 expert reviews + 1 challenge unit → the corrections that forced `CORR1` |
| `CORR1` | Reconciled, negatives rescoped, claims dispositioned | 2 fresh reviewers → further material findings |
| `GAPCLOSE` | 4 blockers closed, final review run | 2 fresh reviewers → **3** new cross-boundary mechanisms, **10** new balanced-but-wrong cases, **6** of the team's own claims contradicted |

`G10` §7.2 records the observation: *"every material self-correction came from a reviewer — never
from the author, including in the round that wrote the standard."* An observation is not a cause.

## 2. Candidate causes, tested rather than assumed

The round instruction lists eleven candidate causes. Each was tested against evidence.

| # | Candidate | Verdict | Basis |
|---|---|---|---|
| 1 | Missing denominator | **CONFIRMED — primary** | `MCE-013`: 0 of 19 material populations had a verified denominator before this round; the one enumerated population was author-derived |
| 2 | Incomplete source surface | **CONTRADICTED** | The addon was read; `MCE-001` shows the parent cited the largest units correctly. The surface was *available*, not absent |
| 3 | UI-only sampling | **CONTRADICTED** | The parent's citations are source-level throughout; `GR1` audited them and found no fabrication or misquotation |
| 4 | Source-only sampling | **PARTIALLY CONFIRMED** | Security artefacts (access rows, record-scoping rules) are *configuration*, not code. `MCE-004` — the decisive reconciliation finding — lives in configuration, and configuration was never enumerated |
| 5 | Missing database correlation | **CONFIRMED — contributing** | `P-15`: 11 storage-level constraints exist and were never listed against the 32 application-level hooks. The distinction *"enforced in the database vs enforced in the application"* is the exact distinction `DR-AC-01` was later invented to demand |
| 6 | Missing failure-state enumeration | **CONFIRMED — contributing** | `P-23`: 153 failure paths exist; the parent's edge-case register holds ~25. `FX-07` — a guard that tests only for zero — is a member of the 128 never listed |
| 7 | Missing tenant/company dimension | **CONFIRMED — contributing** | `P-21a`…`P-21e`: 5 mechanism populations, 211 sites, none enumerated. Every cross-boundary finding is a member |
| 8 | Missing cross-module boundary | **PARTIALLY CONFIRMED** | `P-20`: 38 modules produce ledger entries; the parent map names ~7 families. Most of the 31 belong to later Waves, so the effect on Wave A is limited |
| 9 | Missing event taxonomy | **CONTRADICTED as a cause** | The parent established positively that no event object exists. `P-18` is unbounded *by construction*. This is a finding, not a method defect |
| 10 | Non-systematic negative-claim search | **CONFIRMED — contributing** | `G06` itself proved it by finding 17 breaches six reviewers had walked past. `MCE-011` shows the fix was applied to 41.9% of the package |
| 11 | Reviewer discovery path not represented in the primary method | **CONFIRMED — this is the mechanism** | §3 |

## 3. The root cause, stated once

> **The primary method enumerated a taxonomy of business functions. Every material finding lived in
> a population of source mechanisms. A taxonomy of functions has no cell that a mechanism can
> occupy, so the author could not have found these findings by working harder at the method he had.**

The two surfaces, measured (`MCE-013`):

| The author's surface | The reviewers' surface |
|---|---|
| 155 hand-authored function rows | 750 methods · 397 fields · 153 failure paths · 132 access rows · 126 views · 93 privilege-elevation sites · 62 raw-SQL sites · 59 actions · 52 menus · 37 root-vs-company sites · 32 constraint hooks · 31 record-scoping rules · 11 scoping overrides · 11 storage constraints · 8 bypass tokens · 5 config keys |
| 1 population, author-derived | 19 populations, source-derived, **none of them enumerated** |

Take one row as the proof. `B-18` **"Multi-company isolation"** is marked `SC` — semantically covered
— with the note *"Journal-to-company is exclusive."* The row is not lazy; it is a correct statement
about the field. The finding that contradicts it — `AC-03` — is that the journal model declares a
**parent-inclusive company-scoping override**, so a parent's journal is admissible to a descendant
company's entry. That fact is a member of `P-21a`, a population of 11. There is no depth of thought
about the *function* "multi-company isolation" that surfaces an override the author never listed.
There is a one-line command that surfaces all 11.

The same reading applies to each of the others:

| Finding | Population it lives in | Could the 155-row taxonomy hold it? |
|---|---|---|
| `SB-05` null-company rate crosses companies | `P-16a` record-scoping rules + `P-10` field nullability | No |
| `FX-08` branch rate invisible to root resolver | `P-08a` rate scoping rules (6) | No |
| `FX-07` revaluation guard tests only zero | `P-23` failure paths (153) | No |
| `B-05` approval engine skipped under elevation | `P-21b` privilege-elevation sites (93) | No |
| `X-04` numbering scan without a company clause | `P-21b` + `P-21a` | No |
| `X-05` posted counterparty rewritten, lock bypassed | `P-21b` + `P-21e` bypass tokens (8) | No |
| `X-06` exigibility tests root; no rule on partial reconcile | `P-21c` (37) + `P-16a` (31) | No |
| `AC-01` routine role holds full rights on rates | `P-16` access rows (132) | No |
| `AC-02` raw SQL bypasses record scoping | `P-21d` raw-SQL sites (62) | No |
| `AC-03` parent-inclusive journal scoping | `P-21a` (11) | No |
| `AC-06` database-wide config key, no company dimension | `P-10a` config keys (5) | No |

**Eleven of eleven.** The correlation is total, and it is not a coincidence: a business-function
taxonomy is a description of *what the system is for*, and every one of these findings is about
*how the system is built*. They are answers to different questions.

## 4. The secondary cause: reviewers were the only enumeration engine

Independent review worked — nine reviewers, three rounds, every material correction. But review is a
**sampling** control, not an enumeration control. It finds instances; it cannot bound a population.
Using it as the primary discovery channel produces exactly the observed signature: each round finds
real findings, and no round can say how many remain.

`G10` §7.3 half-saw this — *"mechanical scanning catches the long tail"* — but applied it only to
negative claims. The generalisation was available and was not made: **mechanical scanning bounds a
population; review samples it; the two are not substitutes.**

## 5. Why the round that wrote the standard still failed

`CORR1` authored the negative-claim standard `DR-NC-01`…`06` and still shipped claims that `G06`
later had to rescope, and `G06` in turn applied its own scan to 45 of 64 files (`MCE-011`). The
lesson is narrow and important:

> A standard that is applied by the same judgement that produced the defect inherits the defect's
> blind spot. `DR-NC` was applied to *the files the author was thinking about*. The scope of the
> scan was itself author-derived — the same failure mode, one level up.

This is why `ER-24` (file `05`) fixes the scan's **denominator** to "every file in the package
manifest", not to a list.

## 6. Root-cause statement for the ledger

| Field | Value |
|---|---|
| Blocker | `GB-04` |
| Root cause | **Enumeration was performed over an author-derived taxonomy of business functions; all material findings inhabit source-derived mechanism populations, which were never enumerated.** |
| Primary contributing cause | Independent review used as the discovery engine rather than as verification of an enumeration |
| Secondary contributing causes | Configuration surface not treated as evidence (4) · storage-vs-application enforcement layer not distinguished (5) · failure paths not enumerated (6) · company-scoping mechanisms not enumerated (7) · negative-claim scan scope author-derived (10) |
| Not causes | Incomplete source access (2) · UI-only sampling (3) · missing event taxonomy (9) |
| Corrective action | Enumeration rules `ER-01` … `ER-27`, file `05` |
| Status of the blocker | **`GB-04` root cause CLOSED. `GB-04` exposure NOT closed** — 192 sites bounded, 9 assessed (file `03` §2) |

## 7. The transferable lesson

For every other SMEsPlus module, the test is one question asked before research begins:

> **Name the population, the command that counts it, and the number it returns.**

If the answer is a list someone wrote, the round will converge on that list and not on the system.
