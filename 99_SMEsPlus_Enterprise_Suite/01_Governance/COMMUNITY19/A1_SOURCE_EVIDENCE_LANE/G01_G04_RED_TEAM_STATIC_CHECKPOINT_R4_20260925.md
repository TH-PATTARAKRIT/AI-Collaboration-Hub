# SMEsPlus Community19 - RED TEAM G01-G04 Static Checkpoint R4

Date: 2026-09-25
Mode: A1 SOURCE/STATIC + QUESTION-GATE RECONCILIATION
Formal Coverage: NOT CALCULATED

## Environment
- Authorized Community19 desktop device remains OFFLINE.
- Upstream Odoo 19.0 static anchor remains commit 8d05257d83f9128953f580a066db67c48fcdb96f.
- Upstream source is not asserted byte-identical to the governed local Community19 package.
- Governed counts remain G01=23, G02=11, G03=11, G04=9.

## G01 PLATFORM_BASE - verified A1 delta
New source slices:
- res_groups.py = e69accc22b676fccb5d0372e5312f259b1599f6b
- ir_module.py = 6d69e795dbb3b87b72a740d992d66f7b4d798c07
- res_users.py = 9d42d77ae8ec19028c99b3c668294569ded3a86a
- ir_model.py = ca0c48b566843ece9948c8c5e7f759714a3faf8e

Verified findings:
1. Group membership is modeled with explicit and transitively implied relationships.
2. Group definitions include consistency checks for mutually incompatible user categories.
3. Model-access metadata, record rules, menus and views are linked to group definitions as separate control surfaces.
4. Module metadata exposes lifecycle states for install, upgrade and removal.
5. Module metadata records dependencies, exclusions, country relationships and automatic-install semantics.
6. Installation and removal paths contain explicit administrative and state-transition controls.
7. Dependency traversal supports both upstream and downstream relationships, so direct manifest dependencies are not the complete dependency graph.
8. These are static source findings only and do not establish runtime behavior.

Disposition: G01 A1 ACTIVE / VERIFIED STATIC DELTA / BASE NOT COMPLETE.

## G01 Question Gate
- W1-STD: all 23 G01 modules, Standard 55 = FROZEN / VERIFIED.
- W1-B01: base, mail, web = FROZEN and independently verified.
- W1-B02: auth_signup, base_automation, bus = FROZEN and independently verified.
- W1-B03: digest, portal, utm = FROZEN, but independent verification eligibility remains unresolved.
- Runtime A2 was not executed because the authorized runtime/source device is unavailable.

## G02 IDENTITY_ACCESS
Roster-recovery search was repeated. No controlled row-level GROUP_STRUCTURE_V2_CORE.tsv membership was recovered. The R3 candidate reconstruction remains candidate-only and receives no canonical membership credit.
Status: A1 ACTIVE / ROSTER RECONCILIATION / WAIT QUESTION.

## G03 MASTER_DATA
Roster-recovery search was repeated. Existing evidence still supports product, uom and analytic as source anchors, but the exact governed 11-name roster remains unrecovered.
Status: A1 ACTIVE / ROSTER RECONCILIATION / WAIT QUESTION.

## G04 ACCOUNT_BASE
Roster-recovery search was repeated. Exact governed nine-name membership remains unrecovered. ACCOUNT_BASE remains separated from ACCOUNT_PROCESS.
Status: A1 ACTIVE / ROSTER RECONCILIATION / WAIT QUESTION.

## Integrity controls
- Static declaration is not runtime proof.
- Candidate roster count equality is not canonical roster proof.
- Upstream source presence is not governed local-source byte identity.
- No Evidence = No Progress.
- No Formal Coverage until the Canonical Function-ID denominator is Boss-frozen.
