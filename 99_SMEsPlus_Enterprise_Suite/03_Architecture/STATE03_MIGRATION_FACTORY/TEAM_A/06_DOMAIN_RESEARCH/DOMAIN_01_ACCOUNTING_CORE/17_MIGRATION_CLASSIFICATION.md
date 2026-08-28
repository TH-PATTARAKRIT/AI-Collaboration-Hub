> DOMAIN_01 — Accounting Core | Team A (Maker) | READ ONLY | No target design | Boss sole Final Approver

# 17 — MIGRATION CLASSIFICATION

| ID | Item | Migration relevance | Rationale |
|---|---|---|---|
| MC-01 | Chart of accounts | **MUST CARRY** — business data | Customer's own account structure |
| MC-02 | Account types / groups | **MUST UNDERSTAND** — semantics | Drives year-end and reporting behaviour |
| MC-03 | Journals | **MUST CARRY** — business config | Classification and numbering |
| MC-04 | Journal entries + items | **MUST CARRY** — the ledger itself | Core financial history |
| MC-05 | Balance invariant | **MUST RE-ESTABLISH, NOT INHERIT** | Source has no DB enforcement (BR-03); migrated data must be verified |
| MC-06 | Entry lifecycle | **MUST UNDERSTAND** | Three states; reversal is a relationship |
| MC-07 | Reversal linkage | **MUST CARRY** — relationship data | Audit continuity |
| MC-08 | Reconciliation state | **MUST CARRY** — derived but material | Partial/full matching history |
| MC-09 | Lock dates | **MUST UNDERSTAND** — config | Six controls; period-close semantics |
| MC-10 | Lock exceptions | **MUST UNDERSTAND** — audit | Override history |
| MC-11 | Hash chain / secure sequence | **DO NOT CARRY** — vendor mechanism | Tamper-evidence is implementation-specific; the *requirement* carries, the mechanism does not |
| MC-12 | `parent_state`, `journal_id` on line, `company_currency_id` | **DO NOT CARRY** — derived | Recompute in target |
| MC-13 | debit/credit/balance trio | **NORMALIZE** | Redundant representation |
| MC-14 | `move_type` overloading | **DO NOT INHERIT** — vendor packaging | One table for all document types is a vendor choice, not a requirement |
| MC-15 | Analytic lines | **DEFER** — partially coupled | In scope only where directly coupled |
| MC-16 | Enterprise-module behaviour | **CANNOT MIGRATE FROM SOURCE** | Black-box; requires behavioural specification |

**Classification is migration relevance only. No target design is expressed or implied.**
