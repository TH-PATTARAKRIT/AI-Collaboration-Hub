# P08_ACCOUNT_IDENTITY_MODEL

Session `SMEPLUS-26-09-04-ACC-P08-R2R-REV2-001` · Layer 1 · scope model per `SMEPLUS-26-09-04-ACC-REV2-CORR1`

## 1. Identity in the benchmark

| ID | Statement | Class |
|---|---|---|
| `AID-01` | A ledger account's identity is an opaque surrogate key. The account number is not part of it. | FACT VERIFIED |
| `AID-02` | No database uniqueness exists on the account number. Uniqueness is an application check at save time, and the check is deferrable by a calling-context flag. | `A VERIFIED ABSENCE` for the database constraint, scope = the account model's constraint and table-initialisation definitions |
| `AID-03` | The uniqueness *scope* is the ancestor-or-descendant branch of the company tree. | FACT VERIFIED |
| `AID-04` | The *visibility* scope is downward only. Uniqueness and visibility therefore disagree, and a refusal can name an account the requester cannot see. | FACT VERIFIED (both mechanisms); SUPPORTED INTERPRETATION (the disclosure) |
| `AID-05` | Ownership is a **set** of companies, not one. | FACT VERIFIED |
| `AID-06` | The number is stored keyed by the **root** of the company tree, so all companies under one root share one number; the interface presents one row per company. | FACT VERIFIED |
| `AID-07` | Identity is destructible: an administrative merge repoints references by direct data manipulation and deletes the losing records. Only two conditions block a pair — shared company ownership, or both accounts carrying sealed entries. | FACT VERIFIED |
| `AID-08` | Nothing in the number-write path consults whether the account carries postings, although the system computes exactly that fact for search purposes. | `A VERIFIED ABSENCE`, scope = the account write path and its uniqueness routine |
| `AID-09` | Retirement is a forward-looking input block whose two posting checks are both suppressible by a calling-context flag; history is untouched. | FACT VERIFIED |
| `AID-10` | Deletion is refused whenever a posting, a tax mapping or a jurisdiction mapping references the account — but the item-to-account reference carries a database-level cascade, and the application guard is declared not to apply during module removal. | FACT VERIFIED; the cascade consequence is SUPPORTED INTERPRETATION |

## 2. Scope analysis (corrected model)

The benchmark collapses two objects that have different scopes.

| Object | Scope | Consequence |
|---|---|---|
| Account **definition** — what this account means, its classification, its reconcilability, its control status | `TENANT` | one definition, shared by every company of the tenant that uses it |
| Account **number as presented in a set of books** | `COMPANY` | each company may carry its own statutory number for the same definition |

The benchmark's root-keyed number is neither. It is an undeclared **company-group** scope sitting between the two, and it is the direct cause of `AID-06`: an interface that offers a per-company number over a per-group store cannot be correct in both directions.

`AID-SC-01` — Under the corrected model, `AID-04` is not merely an inconsistency; it is a scope error of class `SV-1`. Uniqueness and visibility must both be evaluated at the scope that owns the object. If the definition is `TENANT`-owned, both are tenant-wide and the asymmetry disappears. If the number is `COMPANY`-owned, uniqueness of the number is company-wide and a sibling's number is irrelevant.

`AID-SC-02` — `AID-07` (merge) and `AID-08` (unguarded re-code) are both class `SV-3`: a mutation performed at the definition scope reaches through and changes what company-scope posted facts report. Under `KRN-INV-05` neither is permissible in the form the benchmark implements them.

## 3. Requirements raised

| ID | Candidate requirement | Class |
|---|---|---|
| `P08-RQ-AID-01` | Account identity is explicit, immutable, and never re-used. A merge produces a **mapping**, never a deletion. | DESIGN CANDIDATE |
| `P08-RQ-AID-02` | The account number is an effective-dated attribute at `COMPANY` scope. Changing it opens a new validity period; it never rewrites the past. | DESIGN CANDIDATE |
| `P08-RQ-AID-03` | Uniqueness and visibility share one scope. | DESIGN CANDIDATE |
| `P08-RQ-AID-04` | Uniqueness is enforced at the persistence layer, not by an application check with a bypass flag. | DESIGN CANDIDATE |
| `P08-RQ-AID-05` | Retirement, re-classification and re-coding of an account carrying postings require an explicit restatement authorisation which is itself an auditable company-scope fact. | DESIGN CANDIDATE |
| `P08-RQ-AID-06` | No referential cascade may reach a posted financial fact. Deletion of a referenced master object is refused at the database, not by an application hook that module removal skips. | DESIGN CANDIDATE |

## 4. Open

`P08-U-AID-01` (Class D) — whether a classification change that flips the reconcilability flag bypasses the routines that maintain open-item residuals. Runtime confirmation required; the code path is read, not executed.
`P08-U-AID-02` (Class C) — migration of a per-company number model to or from a per-group store.
`P08-SC-U-02` — whether Thai statutory reporting requires a per-company account number. `HOLD / EVIDENCE REQUIRED`, routed to the Accounting-Tax track.
