> DOMAIN_01 — Accounting Core | Team A (Maker) | READ ONLY | No target design | Boss sole Final Approver

# 20 — CLASSIFICATION A–G

| Class | Meaning | Team B eligibility |
|---|---|---|
| A | Universal principle, safe, fully evidenced | Candidate after Audit+PMO+Boss gate |
| B | Cross-ERP common pattern, safe | Candidate after gate |
| C | Business/regulatory requirement, evidence-backed | Candidate after gate |
| D | Business fact needing confirmation | Candidate after gate + confirmation |
| E | Vendor-specific implementation | **RESTRICTED — must not become design** |
| F | Proprietary / black-box derived | **QUARANTINE** |
| G | Unknown / unevidenced | **Zero progress credit** |

| ID | Finding | Class | Fact status | Confidence | Clean-room | Migration relevance |
|---|---|---|---|---|---|---|
| F-01 | Every entry must balance | **A** | FACT | HIGH | SAFE | Must re-establish |
| F-02 | Accounts typed; type drives carry-forward | **A** | FACT | HIGH | SAFE | Must understand |
| F-03 | Correction by reversal preserves history | **A** | FACT | HIGH | SAFE | Must understand |
| F-04 | Period locking exists | **A** | FACT | HIGH | SAFE | Must understand |
| F-05 | Journals classify and control entries | **B** | FACT | HIGH | SAFE | Must carry |
| F-06 | Partial → full reconciliation | **B** | FACT | HIGH | SAFE | Must carry |
| F-07 | Multi-company / multi-currency boundaries | **B** | FACT | HIGH | SAFE | Must carry |
| F-08 | Money stored as exact decimal | **B** | FACT | HIGH | SAFE | Must match or better |
| F-09 | Ledger tamper-evidence expected | **C** | FACT (general) / UNCONFIRMED (Thai statutory force) | MEDIUM | SAFE | Must understand |
| F-10 | Gapless document numbering expected | **C** | UNCONFIRMED | MEDIUM | SAFE | Confirm externally |
| F-11 | Effective-date entry behaviour (customer layer) | **D** | UNVERIFIED | LOW | HOLD | Not analysed |
| F-12 | One table for all document types via `move_type` | **E** | FACT | HIGH | **RESTRICTED** | Do not inherit |
| F-13 | **Entry-level** balance in application only, suppressible; no DB mechanism (row-level CHECKs cannot aggregate; 0 triggers) | **E** | **VERIFIED FACT** (mechanism) | HIGH | **RESTRICTED** | Do not inherit; validate on migration |
| F-14 | Hash protection opt-in per journal | **E** | FACT | HIGH | **RESTRICTED** | Do not inherit |
| F-15 | Six lock-date fields + per-user variants | **E** | FACT | HIGH | **RESTRICTED** | Do not inherit |
| F-16 | Denormalized `parent_state` etc. | **E** | FACT | HIGH | **RESTRICTED** | Recompute, do not carry |
| F-17 | debit+credit+balance trio | **E** | FACT | HIGH | **RESTRICTED** | Normalize |
| F-18 | Enterprise accounting behaviour (accountant/reports/asset/budget) | **F** | UNOBSERVABLE | — | **QUARANTINE** | Cannot migrate from source |
| F-19 | Reporting engine behaviour | **F** | UNOBSERVABLE | — | **QUARANTINE** | Requires behavioural spec |
| F-20 | Actual posted-transaction behaviour at volume | **G** | UNKNOWN | — | — | **Zero progress credit** |
| F-21 | Thai statutory posting/close obligations | **G** | UNKNOWN | — | — | **Zero progress credit** |
| F-22 | Rounding / decimal-precision configuration | **G** | UNKNOWN | — | — | **Zero progress credit** |

| F-23 | Row-level DB CHECK constraints exist and are enforced (credit×debit=0; sign agreement; required account; empty presentation lines) | **D** | **VERIFIED FACT** | HIGH | SAFE | Understand — a real guarantee to match |
| F-24 | Zero triggers in the entire database | **E** | **VERIFIED FACT** | HIGH | SAFE | Explains the absence of a DB backstop |
| F-25 | Correction by reversal rather than deletion is peer-ERP practice (SAP B1 forbids deleting posted entries) | **D** | **VERIFIED FACT** (P4 triangulated) | HIGH | SAFE | Supports ADV-04 |
| F-26 | Peer ERPs express period control with far fewer controls (NetSuite: 3 states + 1 override permission) | **D** | **VERIFIED FACT** (P4 triangulated) | HIGH | SAFE | Supports ADV-03 |
| F-27 | Data-level balance of stored entries | **G** | **EVIDENCE_MISSING** | — | — | **Zero progress credit** |

Totals (CORR-001 corrected): **A 4 · B 4 · C 2 · D 4 · E 7 · F 2 · G 4 = 27 findings**
(prior round: 22; +5 from direct DB observation and triangulation)
