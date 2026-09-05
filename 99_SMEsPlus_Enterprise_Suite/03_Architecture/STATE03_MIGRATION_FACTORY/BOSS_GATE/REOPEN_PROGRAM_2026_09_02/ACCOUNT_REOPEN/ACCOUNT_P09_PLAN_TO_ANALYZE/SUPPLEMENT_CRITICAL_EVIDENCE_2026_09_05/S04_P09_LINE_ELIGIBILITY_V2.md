# S04 — P09_LINE_ELIGIBILITY_V2

**Checkpoint:** `CP-P09S04` · **Layer:** 1 — clean-room.

---

## 1. THE PRIOR STATEMENT, AND ITS VERDICT

Prior: *"Line eligibility is by allocation assignment alone. No account-type, row-type, context, company, plan, distribution-model or event-type filter on the creation path."*

**Verdict from an independent challenge tasked to disprove it: `CONFIRMED WITH CAVEAT`.** The chain verifies line-for-line. **Three of the seven "no filter" assertions do not survive as stated**, and one of them is materially wrong.

## 2. THE SEVEN ASSERTIONS, ADJUDICATED INDIVIDUALLY

| Assertion | Verdict |
|---|---|
| no **account-type** filter | **CONFIRMED**, class A. The only account-type test anywhere is on the *assignment* path, not creation |
| no **row-type** filter | **CONFIRMED WITH CAVEAT** — none on creation; but the default-population compute is row-type-conditional on one of its two branches |
| no **context** filter | **CONTRADICTED for the validation limb.** A context flag is exactly a context filter; it gates whether validation runs |
| no **company** filter | **CONTRADICTED for one plan; CONFIRMED for all others.** See §3 — the sharpest result of this checkpoint |
| no **plan** filter | **CONFIRMED** |
| no **distribution-model** filter | **CONFIRMED** — rules are consumed at assignment, never at creation |
| no **event-type** filter | **CONFIRMED** — the event category is *written* and never *tested* on this path |

## 3. THE COMPANY FINDING — CORRECTED, AND SCOPE-AWARE

Company consistency between a costed row and the analytic accounts named in its allocation **is enforced — for exactly one plan.**

The privileged plan's column is a **statically declared** relational field carrying a company check, and the model enables automatic company validation. Every other root plan's column is created at runtime as a **manual field record**, and the platform's manual-field instantiator **has no company-check attribute at all** — an exhaustive pattern over that file returns **zero** occurrences, class A.

> **Company consistency is enforced on the privileged plan and is structurally unenforceable on every other plan.** Not "absent" — *unenforceable through that mechanism*.

This supersedes the prior blanket "no company filter". It also refines the prior round's finding, which had the mechanism right but stated the conclusion as a flat absence rather than as a **one-of-N boundary**.

## 4. TWO SILENT FILTERS THE PRIOR STATEMENT MISSED

| ID | Filter | Why it matters |
|---|---|---|
| **EL-1** | **a silent existence filter.** Before computing amounts, the creation path browses the allocation's account ids and keeps only those that still exist. A dangling id — and the allocation carrier has no referential integrity, so dangling ids are an expected state — is **silently skipped**: no error, no log, and its share of the amount is silently dropped or redistributed | **an allocation can be partly voided with no trace**. This is a creation-path filter, so the phrase "no filter" was never literally true |
| **EL-2** | **a move-state filter on a second creation path.** Creation has **three** callers, not one. The distribution-edit path restricts itself to rows whose parent entry is **posted** | eligibility on that path is *assignment **and** posted state* |

## 5. THE VALIDATION GATE — DOUBLY INERT, AND WORSE THAN RECORDED

The obligation check is gated twice: by an execution-context flag **and** by a row-type filter. The challenge measured the flag's setters exhaustively:

- **exactly one** non-test setter in application code;
- **thirteen** setters in interface button definitions — including the posting buttons.

> **Mandatory-plan validation runs when a human presses Post, and does not run on a programmatic post** — scheduled posting, imported documents, interface-driven automation, recurring entries.

This *strengthens* the prior finding and gives it a mechanism the prior round did not have.

## 6. THREE ELIGIBILITIES — SEPARATED, AS THE DIRECTIVE REQUIRES

The package risked conflating these. They are three populations with three admission rules.

| Eligibility | Admission rule | Consequence |
|---|---|---|
| **CREATION** | the row carries an allocation **and** at least one named account still exists **and** the amount is non-zero at the row's currency precision | no account-type, plan, rule or event-type condition |
| **REPORT** | the record names a general account; the shadow view then **hardcodes** a product row-type and a **posted** state onto every row it emits | records with no general account are **invisible** to financial reports — which excludes the entire operational-measurement population |
| **BUDGET** | a **hard account-type gate** — income or expense only — plus an event-category test and a company test | **a record on a balance-sheet account is created, is reported, and is structurally invisible to every budget** |

> **No statement of the form "created ⇒ reported ⇒ budgeted" is supportable.** This is the conflation the directive anticipated, and it is now closed.

It also explains `S02` exactly: the 226,612 balance-sheet-account records are creation-eligible, report-eligible, and budget-**ineligible**.

## CHECKPOINT

**`CP-P09S04` — COMPLETE — EVIDENCE VERIFIED.** Eligibility restated with three corrections and two newly-found silent filters; the three eligibilities separated. Auto-continue.
