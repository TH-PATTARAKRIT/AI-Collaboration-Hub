> DOMAIN_01 — Accounting Core | Team A PART 2 (Sonnet) | Input: committed Part 1 evidence | No SMEsPlus design

# 06 — STATE / EVENT LOGIC ANALYSIS

## SEPARATING VENDOR TECHNICAL STATE FROM NEUTRAL BUSINESS LIFECYCLE

### Vendor technical state (as implemented — Class E, quarantined from Team B verbatim)
`state ∈ {draft, posted, cancel}`, transitions via `action_post` / `button_draft` /
`button_cancel`, plus an orthogonal `payment_state`, plus a denormalized `parent_state` copied
onto every line, plus a separate relationship field `reversed_entry_id` that is NOT a state.

### Neutral business lifecycle (what the states actually represent, stripped of field names)
```
RECORDED    — the fact has been captured but is not yet a ledger commitment; freely editable
COMMITTED   — the fact is now part of the ledger; has (or should have) a permanent identity
              and, once externally reported, should not be silently mutable
VOIDED      — the fact is retained but marked as not to be counted
CORRECTED   — NOT a state of the original fact. It is a NEW fact, linked to the one it corrects,
              that offsets it. The original remains COMMITTED, unchanged.
```
**Key reasoning point.** The vendor's three-state model conflates two genuinely different
business questions into one field:
1. *Is this fact part of the ledger yet?* (RECORDED vs COMMITTED)
2. *Should this fact still count?* (active vs VOIDED)

`cancel` answers question 2, but the guard on `button_draft` (accepts `posted` OR `cancel`)
treats question 1 as **reversible from either answer to question 2** — i.e., the model does not
distinguish "never should have counted, still shouldn't" from "counted correctly and should
stay that way." This is the structural root of CF-06.

## IS RESET/REOPEN EVER LEGITIMATE?
A genuinely neutral answer, not a vendor-inherited one: **yes, conditionally.** A data-entry
mistake caught *before* the fact has been consumed by anything outside the entity's own books
(no bank reconciliation against it, no VAT return filed referencing it, no financial statement
issued that includes it) is arguably safe to correct in place — the "harm" of mutability is
that it breaks a chain of trust to something *external* that already relied on the original
value. Once that external consumption has happened, correction must be additive (reversal),
never destructive.

**The reference system's guard does not know the difference.** `button_draft`'s condition is
purely status-based (`state in ('posted','cancel')`) — it has **no concept of "has this fact
been consumed downstream."** This is a sharper, more precise statement of the CF-06 weakness
than "posted history is mutable": the actual defect is that the invariant that *should* gate
mutability (external consumption) is not the invariant that *does* gate it (raw status).

## WHAT CREATES A NEW ACCOUNTING FACT VS MUTATES AN EXISTING ONE
| Action | Creates new fact? | Mutates existing fact? | Evidence |
|---|---|---|---|
| Post an entry (`action_post`) | YES — the entry becomes a ledger commitment | no | SE-10 |
| Reverse an entry (`_reverse_moves`) | YES — a new, linked move | no (original untouched) | SE-08/09 |
| Reset to draft (`button_draft`) | no | **YES — mutates a committed fact** | SE-11/12 |
| Cancel (`button_cancel`) | arguably YES (a "this doesn't count" fact) | marks, does not delete | SE-11 |
| Reconcile (partial/full) | YES — a new matching fact | no | DB inventory |

Only ONE action in this table mutates a previously-committed fact in place, and it is exactly
the action that peer-ERP practice (SAP B1) forbids for posted documents.

## EVENTS — WHAT SHOULD BE IMMUTABLE FROM AN AUDIT PERSPECTIVE
An event log recording *that* an entry was posted, reversed, reset, or reconciled — with actor,
timestamp, and before/after values — is itself the thing that must be append-only, regardless of
whether the underlying record is mutable. The reference system has an **optional** version of
this (chatter/`tracking=True` via the `mail` module), not a **forced** one. A neutral business
lifecycle model should treat the event log as non-negotiable and separate from whatever
mutability rules govern the record itself.

## DO NOT COPY THE VENDOR STATE MACHINE INTO A TARGET LIFECYCLE
Per directive §11, this analysis stops at the conceptual model above. No target states, no
target transitions, no target field names are proposed. What is carried forward is the
*business question* the vendor's states answer imperfectly — not the vendor's answer.
