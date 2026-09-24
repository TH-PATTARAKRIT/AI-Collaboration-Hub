# SMEsPlus Community19 - RED TEAM G01-G04 Static Checkpoint R5

Date: 2026-09-25
Mode: A1 SOURCE/STATIC + QUESTION-GATE RECONCILIATION
Formal Coverage: NOT CALCULATED

## Environment
- Authorized Community19 desktop source device is OFFLINE in this run.
- Upstream Odoo 19.0 static anchor remains commit `8d05257d83f9128953f580a066db67c48fcdb96f`.
- Upstream source is not asserted byte-identical to the governed local Community19 package.

## G01 PLATFORM_BASE - verified A1 delta
New base source slices:
- `ir_sequence.py` = `920e0b2347f850b60c1bf8b392f82a2c7f964272`
- `ir_filters.py` = `b757f56628b2727b1ed5efa4a85dc333e8ee47a3`
- `res_currency.py` = `015ca78353c734949545d4364f500d4d57f32d9f`
- `ir_actions_report.py` = `7281c0820b0bdc76e445043441693524e42b2114`
- `ir_binary.py` = `e7feca93dc31cc8ee7228df68c1f169d2dcae340`
- `res_partner.py` = `502616ef7cb343716ce083465d390a04d0168b9c`

Verified static findings:
1. `ir.sequence` supports standard and no-gap numbering. No-gap uses row locking; source documentation still permits gaps after record deletion.
2. Sequence selection is company-sensitive and supports date-range subsequences.
3. `ir.filters` stores model/domain/context/sort with user-sharing, action scope and default-filter semantics.
4. Currency-rate selection is root-company aware, permits global fallback rows, enforces one rate per date/currency/company, and requires a positive rate.
5. Report actions bind to a model and support HTML/PDF/Text, group restrictions, domains, naming expressions and optional stored-output reuse.
6. `ir.binary` is the file/image streaming helper used by controller-facing delivery paths and relies on record access decisions before streaming.
7. `res.partner` enables automatic company checks and commercial-entity roll-up through `commercial_partner_id`.
8. These findings extend the base kernel map but do not prove runtime reachability or enforcement.

Disposition: G01 A1 ACTIVE / VERIFIED STATIC DELTA / BASE NOT COMPLETE.

## G01 QUESTION GATE
- W1-STD = FROZEN / VERIFIED for all 23 G01 modules.
- W1-B01 and W1-B02 = FROZEN / independently verified.
- W1-B03 has a frozen package and structural/testability QA PASS, but the independent verification record inspected still lists only B01 and B02. B03 remains HOLD for Runtime A2 pending eligibility reconciliation.
- Runtime A2 was NOT executed because the authorized runtime/source device is unavailable.

## G02 IDENTITY_ACCESS
- Exact controlled 11-row roster remains unrecovered.
- Recursive GitHub tree inspection confirms `GROUP_STRUCTURE_V2_CORE.tsv` is not present on the current `SMEsPlus` branch; only references to its controlled SHA-256 remain.
- Candidate reconstruction receives no canonical membership credit.
- No governed/frozen G02 question package is present.
Status: A1 ACTIVE / ROSTER RECONCILIATION / WAIT QUESTION.

## G03 MASTER_DATA
- Exact controlled 11-row roster remains unrecovered.
- `product`, `uom`, and `analytic` remain verified source anchors only.
- No governed/frozen G03 question package is present.
Status: A1 ACTIVE / ROSTER RECONCILIATION / WAIT QUESTION.

## G04 ACCOUNT_BASE
- Exact controlled nine-row roster remains unrecovered.
- ACCOUNT_BASE remains separated from ACCOUNT_PROCESS; no names are assigned by inference.
- No governed/frozen G04 question package is present.
Status: A1 ACTIVE / ROSTER RECONCILIATION / WAIT QUESTION.

## Integrity controls
- Source Presence != Runtime Reachability.
- Count equality is not row-membership proof.
- Upstream source is not governed local-package byte identity.
- No Evidence = No Progress.
- No A2/A3/MASTER transition without an exact governed, verified, frozen/eligible question package.
- No Formal Coverage until the Canonical Function-ID denominator is Boss-frozen.
