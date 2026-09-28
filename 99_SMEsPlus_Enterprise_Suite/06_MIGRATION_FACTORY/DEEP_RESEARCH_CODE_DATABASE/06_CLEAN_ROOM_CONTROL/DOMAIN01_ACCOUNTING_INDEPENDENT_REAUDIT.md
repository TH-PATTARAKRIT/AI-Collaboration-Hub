# DOMAIN_01 Accounting Core — Independent Re-Audit

Session: `[SMEPLUS-26-08-28-DEEP-CD-001]`  
Audit Date: 2026-08-29 Asia/Bangkok  
Auditor: ChatGPT L99 — Independent Clean-Room / Evidence Gate Review  
Source Evidence Commit: `947af38ae728a22e3305e8923a0b8d38a9a3c99b` (`SMEsPlus`)  
Status: **HOLD / RETURN TO TEAM A FOR CORR-002**  
Team B: **NOT AUTHORIZED**

## 1. Audit Scope

Re-audit the latest DOMAIN_01 Accounting Core Team A Part 1 + corrective evidence + Sonnet Part 2 synthesis without reopening proprietary implementation for target design.

The audit tests:

1. evidence accessibility and lineage;
2. direct database structural evidence;
3. provenance consistency;
4. classification consistency;
5. clean-room sanitization of Team B candidate input;
6. regulatory-source quality;
7. data-level / behavioral proof;
8. database object-count reconciliation;
9. commit-chain integrity;
10. readiness for any downstream clean-room gate.

## 2. Evidence Reviewed

Primary evidence anchors at/through commit `947af38...`:

- `DOMAIN_01_ACCOUNTING_CORE/DATABASE_OBJECT_INVENTORY.md`
- `DOMAIN_01_ACCOUNTING_CORE/DATABASE_DATA_PROFILE.md`
- `DOMAIN_01_ACCOUNTING_CORE/18_CROSS_VENDOR_ANALYSIS.md`
- `DOMAIN_01_ACCOUNTING_CORE/19_PROVENANCE_REGISTER.md`
- `DOMAIN_01_ACCOUNTING_CORE/20_CLASSIFICATION_A_G.md`
- `DOMAIN_01_ACCOUNTING_CORE/24_EVIDENCE_COMPLETENESS.md`
- `DOMAIN_01_ACCOUNTING_CORE/25_TEAM_A_DOMAIN_STATUS.md`
- `DOMAIN_01_ACCOUNTING_CORE/SONNET_DEEP_SYNTHESIS/03_ACCOUNTING_PRINCIPLE_REGISTER.md`
- `.../08_CROSS_SOURCE_TRIANGULATION.md`
- `.../10_CLASSIFICATION_REASSESSMENT.md`
- `.../13_TEAM_B_CANDIDATE_INPUT.md`
- `.../14_SONNET_EVIDENCE_COMPLETENESS.md`
- `.../15_TEAM_A_PART2_STATUS.md`

## 3. Independent Findings

| Audit ID | Finding | Result | Gate Impact |
|---|---|---|---|
| AUD-D01-01 | Latest Part 2 evidence pack is accessible and explicitly declares Team B not activated | PASS WITH CONTROL | Supports continued clean-room audit only |
| AUD-D01-02 | Direct DB structural evidence is materially stronger than the historical fallback: `pg_restore -l` census includes 5,141 FK constraints, 1,860 constraints, 1,808 indexes, 2,763 tables and 0 triggers | PASS WITH CONTROL | Reduces DR-GAP-007 but does not close count-definition drift |
| AUD-D01-03 | Provenance code taxonomy is inconsistent between Part 1 provenance register and cross-vendor / synthesis artifacts | HOLD | Canonical provenance taxonomy required before sanitized handoff |
| AUD-D01-04 | `13_TEAM_B_CANDIDATE_INPUT.md` still mixes evidence classes: exact-decimal storage and additive correction are presented too strongly as business/accounting facts even though Part 2 reclassified them as ERP/computing common patterns | HOLD | Candidate input must be re-sanitized and relabeled |
| AUD-D01-05 | Thai regulatory evidence quality improved, but narrow e-Tax / tax-invoice requirements must not be generalized to the general ledger or all invoices | PASS WITH CONTROL / HOLD FOR BROAD CLAIMS | Thai statutory closure remains open |
| AUD-D01-06 | No customer row data were read in the controlled DB profile; data-level proof that committed entries actually satisfy debit=credit remains absent | HOLD | DR-GAP-011 / DR-GAP-012 remain open |
| AUD-D01-07 | Direct index count 1,808 differs from historical 1,714; constraint taxonomy also differs from historical 6,682 headline | HOLD | Reconciliation by object taxonomy required |
| AUD-D01-08 | Clean-room separation is preserved: Team B not activated; vendor-specific implementation remains quarantined; Part 2 uses sanitized candidate input | PASS WITH CONTROL | Supports audit continuity, not Team B authorization |
| AUD-D01-09 | Part 2 records unresolved continuation-baseline commit `b2e5a2ab7f820fee351475d84a4b3c7eceb3ded3` | HOLD | Commit-chain discrepancy must be dispositioned |

## 4. Required CORR-002

Team A must produce a correction pack that does all of the following without overwriting prior forensic history:

1. **Canonical provenance taxonomy** — one stable definition for P1…Pn and a crosswalk for prior artifacts.
2. **Candidate-input relabeling** — separate ACCOUNTING PRINCIPLE, REGULATORY REQUIREMENT, ERP COMMON PATTERN, OBSERVED REFERENCE BEHAVIOR, INFERENCE and UNKNOWN.
3. **Thai source correction** — anchor narrow tax-invoice / e-Tax claims to official Revenue Department / ETDA sources and keep unsupported broad claims open.
4. **DB object census reconciliation** — reconcile 1,808 vs 1,714 indexes and define how historical `constraints=6,682` relates to direct `CONSTRAINT=1,860` plus `FK CONSTRAINT=5,141` and any other counted object classes.
5. **Commit-chain disposition** — identify whether `b2e5a2a...` is stale, external, rewritten or erroneous; do not silently substitute another SHA.
6. **Evidence completeness refresh** — distinguish mechanism proof, structural proof, data-level proof, operational/behavioral proof and statutory proof.
7. **Domain status refresh** — remain `HOLD / READY FOR RE-AUDIT` until the correction evidence is inspectable.

## 5. What This Audit Does Not Authorize

- no Team B activation;
- no target schema freeze;
- no coding or implementation;
- no source-body research beyond existing authorization;
- no merge, release or deployment;
- no conversion of ERP common patterns into requirements without an independent design decision;
- no broad Thai statutory claim beyond the exact scope supported by evidence.

## 6. Gate Verdict

```text
DOMAIN_01 ACCOUNTING CORE — INDEPENDENT AUDIT
= HOLD / RETURN TO TEAM A FOR CORR-002
```

This is not a rejection of the research pack. Structural and clean-room evidence is substantial, but the remaining classification, provenance, data-level and count-definition issues prevent promotion to a downstream approval gate under `No Evidence = No Progress` and `Never Skip Gate`.
