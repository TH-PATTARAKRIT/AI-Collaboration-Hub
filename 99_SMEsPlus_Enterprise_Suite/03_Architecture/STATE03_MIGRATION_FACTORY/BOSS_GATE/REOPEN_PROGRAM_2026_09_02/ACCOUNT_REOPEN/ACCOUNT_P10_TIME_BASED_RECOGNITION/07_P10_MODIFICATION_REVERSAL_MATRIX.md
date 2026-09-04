# P10 — MODIFICATION AND REVERSAL MATRIX

Session: `SMEPLUS-26-09-04-ACC-P10-TBR-REV2-001` · Layer 1

---

## 1. Modification Support

| Change | Deferral | Depreciation | Loan | Accrual | Recurring |
|--------|----------|--------------|------|---------|-----------|
| Base amount, before any entry | free | free | free | n/a (transient) | free |
| Base amount, after entries exist | **only by resetting the source document** | supported, with catch-up | reset schedule and re-confirm | n/a | change the template forward |
| Window / duration | same as above | supported (duration change) | reset and re-confirm | n/a | change interval |
| Account | **blocked** (`E-P10-012`) | re-pointed on unlocked future entries only (`E-P10-030`) | reset and re-confirm | n/a | free |
| Pause and resume | not available | supported | not available | n/a | not available |
| Partial cancellation | not available | disposal of part | close wizard | n/a | end the recurrence |
| Catch-up delta into the current period | **not available** | supported via board recompute | absorbed by re-derivation | n/a | n/a |

## 2. The Deferral Modification Problem — `P10-F-08`

The only way to change an in-flight deferral is to reset the source document to draft, which reverses or unlinks **every** generated entry, including those already posted in closed months, and then re-derive the whole schedule (`E-P10-013`). Where the deferral groups more than one source document, even that is refused.

Consequences:
1. A correction to month 9 of a 12-month contract disturbs months 1–8.
2. Where months 1–8 are audit-trail protected, they are cancelled or reversed rather than removed, so the correction leaves a full duplicate-and-reverse trail across eight closed periods for a change affecting one.
3. Which of the three disposal outcomes applies is decided **per entry, not per schedule** (`E-P10-045`), so one contract's periods can be resolved by three different mechanisms with nothing recording that they were.

The class and search boundary of the negative "no catch-up mechanism exists" is stated exactly in `13_P10_NEGATIVE_CLAIM_REGISTER.md` `NC-04`. It is **not** class `A` for the whole system; it is class `A` bounded to the deferral mechanism in the declared reference root.

## 3. Reversal Semantics

| Mechanism | Reversal is… | Pre-committed? | Linked back? |
|-----------|--------------|----------------|--------------|
| Deferral | consequential — a reaction to the source document being drafted | no | via the move-to-move relation only |
| Accrual | **structural** — created at the same instant as the accrual (`E-P10-028`) | **yes** | yes, entry to entry |
| Depreciation | consequential — disposal or board rebuild | no | via the asset |
| Loan | consequential on cancel/draft; the long-term/short-term reclassification carries a **structural** next-day reversal | partly | yes |
| Recurring | none | n/a | n/a |

Two different meanings of "reversal" are in play and the product does not distinguish them:
- **Structural reversal** — part of the recognition pattern itself (the accrual's next-day reversal, the reclassification's next-day reversal). It is not a correction. It must never be treated as one.
- **Corrective reversal** — undoing something that should not have been recognised.

An SMEsPlus kernel must type these separately, because every reconciliation, every audit question and every duplicate control depends on knowing which one it is looking at. In the reference product they are indistinguishable in the ledger.

## 4. Cancellation

| Mechanism | Cancel path | What happens to posted entries |
|-----------|-------------|-------------------------------|
| Deferral | reset the source document | unlink, cancel or reverse, decided per entry |
| Accrual | none — reverse manually | remain |
| Depreciation | asset disposal or cancellation | future draft entries removed; posted entries remain; disposal entry created |
| Loan | dedicated cancel path, which **reverses first** | reversed correctly |
| Loan (schedule reset path) | schedule lines removed | posted entries **remain in the ledger with their back-link nulled** — they become invisible to the loan and to its own entry list |

The last row is a lineage-integrity defect confirmed by independent challenge and re-verified by the primary author: three of the four loan teardown paths reverse the generated entries first; the fourth does not, and the back-link field carries no deletion rule that would prevent the orphaning.

## 5. Backdating and Reopening

| Question | Answer | Evidence |
|----------|--------|----------|
| Can a source document be posted into a past open period with a deferral window that started earlier? | Yes; the full deferral entry takes the document's accounting date and the earlier months are recognised at their own month ends | `E-P10-008` and the reference test for the accounting-date case |
| Can generation target a locked period? | Grouped path refuses; validation path is silently re-dated | `E-P10-020`, `E-P10-036` |
| If a period is reopened, is anything re-derived? | See `NC-05` — no re-derivation mechanism found in the searched scope | `13_P10_NEGATIVE_CLAIM_REGISTER.md` |
| Is there any record that a period shift occurred? | No | `P10-F-05` |

## 6. What SMEsPlus Must Specify

1. A modification algebra with three explicit outcomes: *stands*, *re-derived*, *catch-up delta* — identical across all domains.
2. Typed reversals: structural vs corrective, and the rule that structural reversals are never treated as corrections.
3. A rule that teardown of a schedule must resolve its generated entries before the schedule is destroyed, enforced by the kernel and not by each domain.
4. Whether reopening a period re-derives suppressed recognition, and if so under whose authority.
