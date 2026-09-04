# 14 — LEVEL 7: ACCOUNTING CONTROL & INTERNAL CONTROL MATRIX

Layer 1 clean-room · Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-CORE-001`

## 1. Control ownership — the headline

Fourteen invariants were mapped. **Three are owned by the database.** All three are per-row checks on
a single item. **No cross-record invariant in the entire domain is enforced below the application
layer** — including the defining invariant of double-entry accounting.

| # | Invariant | Owner in reference | Failure mode | Recommended SMEsPlus owner |
|---|---|---|---|---|
| `IC-01` | **Debits equal credits** | **application, suppressible by context** | an unbalanced entry can be written | **storage — `Tolerance = 0`** |
| `IC-02` | Debit and credit are not both non-zero on an item | **database** | — | storage |
| `IC-03` | Balance and transaction-currency amount share a sign | **database** | — | storage |
| `IC-04` | An accountable item names an account | **database** | — | storage |
| `IC-05` | Entry number is unique | database, **partial** — posted entries only | drafts may duplicate | storage, unconditional |
| `IC-06` | Account code is unique within a company | **application, unlocked read** | duplicates under ordinary concurrency; **a conventional constraint is not expressible against the chosen storage** | modelling decision, upstream of the constraint |
| `IC-07` | Posted substance is frozen | **the calling module** — bypassed at seven production sites | a posted entry is editable by whoever suppresses the check | storage or event-sourced immutability |
| `IC-08` | A posted fact cannot be deleted | **configuration**, default off; bypass logs **outside the database** | posted facts deletable; deletion evidence leaves the tenant | unconditional |
| `IC-09` | Hashed fields cannot change | **application** — fails open for the canonical amount field | tamper-evident but not tamper-resistant | storage |
| `IC-10` | The hash detects tampering | application — **does not cover** transaction-currency amount, currency, tax, analytic, due date; **rounds at the wrong precision** | undetectable tampering | redesign required |
| `IC-11` | Locked periods reject postings | **not an invariant at all — the lock re-dates** | period attribution altered silently, sometimes with no lock set | explicit policy, per event class |
| `IC-12` | Reconciled amounts do not exceed residual | **nothing** | over-reconciliation structurally reachable | storage |
| `IC-13` | An account with history cannot be deleted | application guard, **bypassed by the merge's direct statement** | posted history retargeted; account row deleted; nothing logged | unconditional |
| `IC-14` | Every posting has a measurement | **nothing — absence resolves to 1.0** | par conversion, silently | **halt — `Tolerance = 0`** |

## 2. Segregation of duties

| Duty | Reference position | Assessment |
|---|---|---|
| Create an entry | invoicing-level permission | — |
| **Approve an entry before posting** | **no such step exists** | maker-checker is absent from the core ledger |
| Post an entry | the same invoicing-level permission as creation | **maker and poster are the same role** |
| Un-post (destroying matches and analytic lines) | the same permission | no elevation for a destructive act |
| Delete an entry mid-sequence | accounting-manager elevation, or a company mode flag | partial control |
| Set or move a lock date | company-settings permission | **no distinct closing authority** |
| Reopen a period | **the same permission as closing** | closing and reopening are one duty |
| **Grant a lock exception** | accounting manager | — |
| **Revoke a lock exception** | **the same accounting manager, via elevated privilege that bypasses the read-only access rule** | **grant and revoke are one duty — no segregation at all** |
| Merge accounts | accounting manager, one action, **no approval, no log, no undo** | **no control whatsoever** |
| Enable or disable integrity hashing | configuration; one-way once entries exist | acceptable |
| Disable the numbering/date control | **system administrator, and in a shared database the effect is not confined to one tenant** | a SaaS boundary matter |

**Assessment.** The reference model has **no maker-checker anywhere in the core ledger**, and the two
override controls (lock exception, merge) are each held entirely within a single role. `IC-07`,
`IC-08` and `IC-13` are all defeated by mechanisms available to that same role.

## 3. Override and exception controls

| Control | Justification required? | Expiry? | Scope | Logged? | Reversible by |
|---|---|---|---|---|---|
| Lock exception | **optional free text** | **optional — may be permanent** | **may apply to every user** | yes, on the company record with before/after values | the granting role |
| Deletion-protection bypass | none — a context flag | n/a | per call | **to the application log, outside the database** | n/a |
| Posted-freeze bypass | none — a context flag | n/a | per call, used routinely | no | n/a |
| Balance-check suppression | none — a context flag | n/a | per call | no | n/a |
| Deprecated-account bypass | none — a context flag | n/a | per call | no | n/a |
| Numbering/date control disable | none beyond the permission | n/a | **the whole database** | as a configuration change | yes |
| Account merge | **none** | n/a | permanent | **no** | **no** |

`INFERENCE:` the pattern is consistent and worth naming. The reference model implements its
accounting controls as **application checks with named suppression flags**. That is a reasonable
engineering pattern for a framework, and an unreasonable one for a ledger, because the suppression is
invisible to the accounting record. A control whose bypass leaves no accounting trace is not an
internal control; it is a convenience.

## 4. Audit evidence available

| Question an auditor asks | Answerable? | Basis |
|---|---|---|
| What is posted now? | yes | the ledger |
| Was this entry changed after posting? | **only for hashed entries, only for hashed fields, and not for the canonical amount field** | `IC-09`, `IC-10` |
| Was an entry deleted? | **only from the application log, if the bypass was used** | `IC-08` |
| Was a period reopened? | partly — a tracked field change, with no artefact | `GAP-G01` |
| Who overrode a lock, and why? | who: yes. why: **optional** | `EV-021` |
| Was an account merged, and what was it before? | **no — nothing is recorded** | `COR-08` |
| Did this posting use a real exchange rate? | **no — a par conversion is indistinguishable from a real one** | `COR-14` |
| Was this entry ever matched, to what, by whom? | **no matching history exists** | `GAP-E02` |
| What did this account mean on that date? | **no — no temporal validity** | `GAP-A03` |

**Five of nine audit questions are unanswerable from the ledger.** For SMEsPlus this is the control
agenda, and each maps to a decision in file 22.

## 5. `Tolerance = 0` candidates

Under constitution principle 13, the following are proposed to Boss as candidates for zero tolerance.
This is a **recommendation for Boss decision**, not a designation this session may make.

| # | Candidate | Why |
|---|---|---|
| `T0-01` | Entry balance invariant | the defining rule of double entry, currently suppressible |
| `T0-02` | A posting without a measurement | silent par conversion produces a valid-looking wrong ledger |
| `T0-03` | Deletion or rewrite of a posted accounting fact | covers both the deletion bypass and the merge |
| `T0-04` | Tenant isolation of ledger data and controls | see file 16 |
| `T0-05` | Over-reconciliation | settlement exceeding the obligation |

## CHECKPOINT L7

| Item | Record |
|---|---|
| Scope completed | 14 invariants with ownership; segregation of duties; 7 override controls; audit answerability; 5 zero-tolerance candidates |
| Verified findings | 3 of 14 invariants are storage-owned, all per-row; no maker-checker exists; grant and revoke of overrides are one duty; 5 of 9 audit questions unanswerable |
| Contradictions | `CONTRA-05` (balance suppressible), `CONTRA-11` (override grant/revoke unsegregated) |
| Unknowns | Whether the suppression flags are reachable from an external interface requires an executed test, not source reading — `GAP-C04` |
| Risks | The suppression-flag pattern is systemic, not incidental |
| Next research target | Level 8 — identity and immutability |

`CHECKPOINT L7 RECORDED — CONTINUING AUTOMATICALLY.` Not Boss approval.
