# SMEsPlus Community19 G01-G04 Checkpoint R9

Date: 2026-09-25
Mode: A1 Source Evidence + Question Gate + Roster Reconciliation
Formal Coverage: NOT AUTHORIZED

## G01 PLATFORM_BASE
A1 source anchor: odoo/odoo 19.0 at 8d05257d83f9128953f580a066db67c48fcdb96f.

New static slices verified:
- ir_fields.py blob 88d3af97950673e5cb1db18df7c9ae5b5f21bcaf
- res_config.py blob 504644162d067988dd7d3dcb90cd7e1a065c9fc3

Static observations:
- Import conversion is field-type aware and preserves nested error paths.
- Properties import validates structure and typed values.
- Datetime import converts from active timezone to UTC.
- Configuration settings separate default, group, module and parameter-backed behavior.
- Configuration module changes are deliberately ordered at transaction end.

Status: A1 ACTIVE / BASE NOT COMPLETE.

## Question Gate
W1-STD remains FROZEN / VERIFIED.
W1-B01 remains FROZEN / ELIGIBLE.
W1-B02 remains FROZEN / ELIGIBLE.

W1-B03 was independently replayed from current repository bytes:
- digest SHA-256 1ba4226db5739143130e0afc1757e3aaa3c0cf1f934ccf3349a907d0c64d74ec, 40 unique QIDs, MATCH.
- portal SHA-256 91b63eef1df5426f22d4bc0b296dc05cb4b3e9e1d7e1b09e38370c5d03963d3a, 40 unique QIDs, MATCH.
- utm SHA-256 af28ded258ac26abbd3962e019dc41754e5c0b46b3c3b8f5d0834e942f756ecd, 40 unique QIDs, MATCH.
- Standard 55 SHA-256 f6726f111932aecce4432daf3e412d0c9de3291fa45fa8908e9e89ee79cb540d, 55 unique QIDs, MATCH.
- B03 manifest SHA-256 74ba2caeaf9a4450ff126256df5e1a7b8bdd4018b2907248b9ccec0e5bbb565e.
- B03 freeze replay 1247c218ba4e2e6a57e259427030f4350881da56a5a28c59901a20f8b2d3a5d3, MATCH.

W1-B03 disposition: FROZEN / INDEPENDENT INTEGRITY VERIFIED / ELIGIBLE.

Authorized Community19 runtime device is offline, so A2 was NOT EXECUTED. Reconciliation, A3 and MASTER do not advance.

## G02 IDENTITY_ACCESS
Governed count 11. Exact row-level roster not recovered. No governed/frozen G02 question bank exists in current GMVQ tree.
Status: A1 ACTIVE / ROSTER RECONCILIATION / WAIT QUESTION.

## G03 MASTER_DATA
Governed count 11. Exact row-level roster not recovered. Existing product/uom/analytic references remain anchors only. No governed/frozen G03 question bank exists.
Status: A1 ACTIVE / ROSTER RECONCILIATION / WAIT QUESTION.

## G04 ACCOUNT_BASE
Governed count 9. Exact row-level roster not recovered. No governed/frozen G04 question bank exists.
Status: A1 ACTIVE / ROSTER RECONCILIATION / WAIT QUESTION.

## Roster Evidence
Controlled historical roster pointer: GROUP_STRUCTURE_V2_CORE.tsv
Recorded SHA-256: 203ff43e7844a734de5e9aaebb91529e46dd7998423d4d5772999ed0db9ff5bf.
The TSV bytes are still unreachable, so this historical hash was not freshly recomputed.

## Controls
No Evidence = No Progress.
Source Presence != Runtime Reachability.
No A2/A3/MASTER without exact governed verified frozen/eligible questions.
Formal Coverage remains prohibited until the Canonical Function-ID denominator is Boss-frozen.
