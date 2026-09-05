# P06_ACCOUNTING_EVENT_REGISTER.md

**Session:** P06 Bank-to-Reconcile — TARGETED CONTINUATION
**Classification:** LAYER 2 — AUDIT QUARANTINE
**Companion to:** `32_P06_BUSINESS_EVENT_REGISTER.md` (business layer) and `05_P06_EVENT_TO_GL_MATRIX.md` (the 31-row GL mapping, which remains the detailed evidence).

---

## 1. Purpose

For each accounting event in P06: what business fact created it, which company owns the effect, whether the event is reversible, and whether the reversal preserves history. The constitution's requirement is *"historical financial truth must not be silently overwritten"* — this file tests exactly that.

---

## 2. The register

| ID | Accounting event | Created by (business fact) | Effect owner | Reversible? | **Preserves history?** |
|---|---|---|---|---|---|
| AE-01 | Outstanding receipt/payment recognised | BE-03 decision to settle | COMPANY | yes | **no** — editing 10 fields rewrites the counterpart lines (PSM-F-25) |
| AE-02 | Bank line posted on ingestion | BE-06 / BE-07 | COMPANY | yes | **no** — `force_delete` path hard-deletes (attack A7) |
| AE-03 | Suspense recognised | BE-18 | COMPANY | yes | yes, while it stands |
| AE-04 | Match committed | BE-09 | COMPANY | yes | **no** — the entry is cleared and rebuilt (RM-F-01) |
| AE-05 | Obligation discharged | BE-10 | COMPANY | yes | partials are unlinked, not superseded |
| AE-06 | Difference written off | BE-11 | COMPANY | yes | yes |
| AE-07 | Exchange difference realised | BE-15 | COMPANY | **reversed, not deleted** | **yes** — and reset-to-draft is refused (`account_move.py:5343-5345`) |
| AE-08 | Cash-basis tax recognised | BE-10 | COMPANY | **reversed, not deleted** | **yes** — a second permanent marker survives the undo (`:5344-5350`) |
| AE-09 | Early-payment discount taken | BE-10 | COMPANY | yes | yes |
| AE-10 | Transit leg recognised | BE-16 | COMPANY | yes | **no link between the two legs** |
| AE-11 | Cash over/short recognised | BE-25 | COMPANY | yes | yes |
| AE-12 | Advance recognised | BE-19 | COMPANY | yes | yes (invoice-shaped) |
| AE-13 | Opening plug on first bank sync | — (no business fact) | COMPANY | yes | **no** — a posted line with no counterpart (BER-F-15) |
| AE-14 | Withholding deducted at settlement | BE-24 | COMPANY | yes | **HOLD — statutory**, routed to P07 |

**AER-F-01 — Exactly two accounting events in P06 preserve history under reversal, and they are the two the reference deliberately protected.**
AE-07 and AE-08 are reversed rather than deleted, and both are barred from reset-to-draft. Every other event in the register can be undone in a way that leaves no record of what was undone.
**The reference therefore demonstrates that it knows how to do this** — it does it for tax and FX. It simply does not do it for matching, settlement, or the bank line itself. That is a design choice, not a limitation, and it is the sharpest available argument for `P06-B-15` and attack A5.

**AER-F-02 — AE-13 is an accounting event with no business fact behind it.** The opening plug is created when a journal's first online sync finds a balance difference. It is the only row in this register whose "created by" column is empty, and it is posted.

---

## 3. Reversal / correction behaviours, consolidated

Per constitution §3.11, the full lifecycle vocabulary and what the reference supplies:

| Lifecycle step | Supplied? | Note |
|---|---|---|
| CREATE / POST / CONFIRM | partly | CONFIRM has no object (BE-08) |
| PARTIAL | yes | partial reconciles |
| MATCH / RECONCILE | yes | destructive (RM-F-01) |
| UNRECONCILE | yes | **unguarded** (PC-F-06) |
| CANCEL | yes | `action_cancel`, no cause |
| REVERSE | yes | destroys the match silently (A5) |
| RETURN / BOUNCE | **NOT FOUND in v18** | present in a v14 custom module |
| CORRECT | via reverse or via re-date | the re-date path resequences posted entries (`P06-B-37`) |
| BACKDATE | yes | unguarded on the reconcile path |
| CLOSE | yes | lock dates, cascading |
| REOPEN | yes for soft locks | hard lock is one-way |
| LOCKED PERIOD | see `28_` | RECONCILE and UNRECONCILE proceed regardless |

---

# End
