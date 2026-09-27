# ROSTER RECONCILIATION FOR LANE A READINESS — G02, G03, G04, G06, G07, G11
Owner: GMVQ / Question Factory Control Desk · Opened 2026-09-27 · Status: PREPARED ONLY / READY FOR MASTER + LANE A CROSS-CHECK
Authorization: Boss directive "ROSTER RECONCILIATION FOR LANE A READINESS", 2026-09-27, addressed to MASTER + GMVQ.
Execution Mode: A (device-bash, live read/write against connected root, this session).

## R3 — restating the question
MASTER's `01_G_READINESS_REGISTER.tsv` marks G01,G02,G03,G04,G06,G07,G11 = CONDITIONAL READY.
Lane A reports G02,G03,G04,G06,G07,G11 = EVIDENCE POINTER NOT VERIFIED because the canonical
roster artifact `GROUP_STRUCTURE_V2_CORE.tsv` (expected sha256
203ff43e7844a734de5e9aaebb91529e46dd7998423d4d5772999ed0db9ff5bf) could not be verified. Boss
asks MASTER+GMVQ to reconcile, per G: canonical artifact, hash result, exact roster, evidence
pointer, authority, CURRENT/SUPERSEDED/CANDIDATE status, and one disposition from the closed
vocabulary — without rerunning completed GMVQ work and without stopping G01 Lane A work.

## 0. Canonical artifact search result — GMVQ, this session
`GROUP_STRUCTURE_V2_CORE.tsv` was searched for by exact and case-insensitive name across the
following locations on the connected device and NOT FOUND in any of them:
- `00_CONTROL/` and all `02_REGISTERS/` under this GMVQ workspace
- `01_ACTIVE/ROOM_A_MASTER_CANONICALIZATION_20260921_REV001/` (all `.tsv` there enumerated by name)
- `01_ACTIVE/ROOM_A_MASTER_LANE_A_ENTRY_READINESS_GATE_20260927_REV001/`
- `01_ACTIVE/ROOM_A_MASTER_LANE_RESPONSIBILITY_MODEL_20260927_REV001/`
- `01_ACTIVE/ROOM_A_MASTER_READINESS_FLOW_PLAN_20260927_REV001/`
- `01_ACTIVE/ROOM_A_MASTER_ROLLING_6SLOT_EXECUTION_PLAN_20260927_REV001/`
- `01_ACTIVE/ROOM_A_MASTER_FLOW_SYNC_20260927_REV001/`
- `AI-Collaboration-Hub/99_SMEsPlus_Enterprise_Suite/` (top level — the Primary Project Path per
  Project Instructions §"Primary Project Path") including its `00_Architecture_Office/`,
  `00_PROJECT_STANDARD/`, and `V2.0/` subtrees
- `03_Architecture/`, `03_ARCHITECTURE_STATE03/`, `90_AI_DOCS/`, `91_AI_EVIDENCE/`, `_ARCHIVED/`,
  `outputs/`, `Claude outputs/` (top level of the connected root)

`02_SOURCE_CODE/` was searched but the search was cut off by a 15-second per-directory bound
before completing (large tree) — INCONCLUSIVE, not a clean negative, flagged below as G-09b.

**Result: GROUP_STRUCTURE_V2_CORE.tsv NOT LOCATED. Its stated sha256
(203ff43e7844a734de5e9aaebb91529e46dd7998423d4d5772999ed0db9ff5bf, confirmed 64 hex chars —
well-formed) CANNOT BE VERIFIED because GMVQ has no file to hash. This is reported as fact, not
fabricated, per §20 — GMVQ will not invent a location or a match.**

## 1. Delta-first analysis (§4 of Boss directive)
Per the five candidate causes:
- **(A) evidence exists but was not exposed to Lane A — MOST LIKELY, partial**: GMVQ holds real,
  on-disk, hashable roster evidence for all six groups (bank files + per-group validator reports,
  §2 below) that was never published under the specific name `GROUP_STRUCTURE_V2_CORE.tsv`, and
  Lane A's check is keyed to that exact artifact. The roster fact is real; the pointer Lane A was
  told to check does not exist under that name/location.
- **(B) artifact moved**: no evidence of a move — no historical copy, alias, or superseded-stamp
  referencing this filename was found anywhere searched.
- **(C) artifact superseded**: no superseding document declares itself the successor to
  `GROUP_STRUCTURE_V2_CORE.tsv` by that name; not established.
- **(D) MASTER used another current controlled roster**: NOT CONFIRMED. MASTER's own two
  same-day documents disagree with each other on these same six groups —
  `01_G_READINESS_REGISTER.tsv` records validator_status=PASS and bank_evidence for G02/G03/G04
  (module counts matching GMVQ's live files), while `01_CANONICAL_G_REGISTER.tsv` (rolling-6-slot,
  also dated 2026-09-27) records `entry_status: NO MVQ BANK` / `LOCAL NOT READY` for the identical
  groups. GMVQ cannot determine from these two documents alone which roster source, if any,
  MASTER's CONDITIONAL READY declaration actually cites — this is a question back to MASTER, not
  an assumption GMVQ will fill in.
- **(E) readiness declared without verifiable roster evidence — LIKELY, contributing**: given the
  internal contradiction in MASTER's own registers above, GMVQ cannot rule out that CONDITIONAL
  READY was recorded before a roster artifact was pinned down.
No rerun of completed GMVQ authoring/audit work is proposed. This is a pointer/evidence-exposure
problem, not a content problem.

## 2. Per-G roster — GMVQ primary evidence (live files, this device, hashed just now)
Module lists below are read directly from GMVQ's own live bank filenames and confirmed against
QID-bearing file counts. Each row is independently reproducible: `sha256sum` on the exact path.

### G02 — IDENTITY_ACCESS — 11/11 modules banked
| # | Module | File | SHA-256 |
|---|---|---|---|
| 1 | auth_ldap | G02_AUTH_LDAP_GMVQ_MVQ_48_V1.00_DRAFT.md | 95777a7c1f906ff2ada8282b442e02dfbe10f4b1fcb80f61ded17dbb1b46e969 |
| 2 | auth_oauth | G02_AUTH_OAUTH_GMVQ_MVQ_48_V1.00_DRAFT.md | f5890be3d39b233adcbbb1a86da718c3fb42a6aeb36229ad62f87e14b65b4071 |
| 3 | auth_passkey | G02_AUTH_PASSKEY_GMVQ_MVQ_48_V1.00_DRAFT.md | 48a0e8bd26a8819da16eacc0765f1c5103b1f85218b66ec24d3d2cbbb3624704 |
| 4 | auth_passkey_portal | G02_AUTH_PASSKEY_PORTAL_GMVQ_MVQ_48_V1.00_DRAFT.md | f18105c4399c8843663b27e7e965ef5513a83481eb0a7be81f0b8a3e25fdd93a |
| 5 | auth_password_policy | G02_AUTH_PASSWORD_POLICY_GMVQ_MVQ_48_V1.00_DRAFT.md | 23f2e9b3625a2e921237044a6390a254e412847fd168c7396fc0a161a3a72e61 |
| 6 | auth_password_policy_portal | G02_AUTH_PASSWORD_POLICY_PORTAL_GMVQ_MVQ_48_V1.00_DRAFT.md | 2b83e83fac9adb5134974798388a4bfbd41fd79b8e0d68b00b666fac099b191f |
| 7 | auth_password_policy_signup | G02_AUTH_PASSWORD_POLICY_SIGNUP_GMVQ_MVQ_48_V1.00_DRAFT.md | 5cfe819aa8f08446b6b8c02893c1fe55fb57e8a2195faf06c05aff1cc236403b |
| 8 | auth_timeout | G02_AUTH_TIMEOUT_GMVQ_MVQ_48_V1.00_DRAFT.md | e201259d64fe0afbc50eabb9f61acf26d386676c3e64912ee2b224e86ffe4b66 |
| 9 | auth_totp | G02_AUTH_TOTP_GMVQ_MVQ_48_V1.00_DRAFT.md | 534f3d0a9648db10f97d3e39e6c4f5b2af29999599acb57dd8280fd88c4a3e32 |
| 10 | auth_totp_mail | G02_AUTH_TOTP_MAIL_GMVQ_MVQ_48_V1.00_DRAFT.md | b72ec8b0bd8762ccfb409b8e8ecdf08cf1d81ca48c794c95ef4cd921a7ae3dc0 |
| 11 | auth_totp_portal | G02_AUTH_TOTP_PORTAL_GMVQ_MVQ_48_V1.00_DRAFT.md | ac0be0f6b8b05163b47c9f069c23de4af963839b7b6c22da6ba673d3d9395e81 |
Evidence pointer: `01_QUESTION_BANKS/G02_IDENTITY_ACCESS/` (this workspace). Cross-corroborated by
MASTER `01_G_READINESS_REGISTER.tsv` row G02 (modules_in_scope=11, validator PASS) AND by
MASTER `01_CANONICAL_G_REGISTER.tsv` row G02 (modules=11) — the two MASTER documents agree on
COUNT even though they disagree on READINESS STATE for this group.
DISPOSITION: **ROSTER_PARTIALLY_VERIFIED** (module identity/count verified via GMVQ primary
evidence + double MASTER corroboration; the named canonical artifact and its hash are not
verified because the artifact was not found).

### G03 — MASTER_DATA — 11/11 modules banked
| # | Module | File | SHA-256 |
|---|---|---|---|
| 1 | analytic | G03_ANALYTIC_GMVQ_MVQ_48_V1.00_DRAFT.md | 21ba423f82c881cdb35df5c46d9f3fc04f40b520e520edb907d16b74e51ccbff |
| 2 | base_address_extended | G03_BASE_ADDRESS_EXTENDED_GMVQ_MVQ_48_V1.00_DRAFT.md | e7fb4a167527ed0fd80f6bef3d80b2ee5efe52e02b36ed5f3ebb74cf640ef776 |
| 3 | base_geolocalize | G03_BASE_GEOLOCALIZE_GMVQ_MVQ_48_V1.00_DRAFT.md | 61107d5b5c04c9901ab3f2b8ccca814f01210cdf049f7d3ce65abe06e0bc90c4 |
| 4 | contacts | G03_CONTACTS_GMVQ_MVQ_48_V1.00_DRAFT.md | 2b1616fb1217ae8862df41b4845cdb9371adcb6bfb9635ecc311c363d0343fd1 |
| 5 | partnership | G03_PARTNERSHIP_GMVQ_MVQ_48_V1.00_DRAFT.md | 0bdef79ab8de8efe7d3c1f914908877949b2f3aecdf79b2c7a3248aef78281b1 |
| 6 | partner_autocomplete | G03_PARTNER_AUTOCOMPLETE_GMVQ_MVQ_48_V1.00_DRAFT.md | 3190acce6ba3170d1d43b1a4af9fc0c8a6cc58b7e6f758a10f0965f510630a5a |
| 7 | product_email_template | G03_PRODUCT_EMAIL_TEMPLATE_GMVQ_MVQ_48_V1.00_DRAFT.md | 879235e9bd0c6178d53ed2e4ed421e52f4af536b25b7eea2bf53c8a6ec7d228e |
| 8 | product | G03_PRODUCT_GMVQ_MVQ_48_V1.00_DRAFT.md | 3479409233c5e822fae2073f140ebb0efb187f7fd7b9f3bbcafedd95a81a4732 |
| 9 | product_margin | G03_PRODUCT_MARGIN_GMVQ_MVQ_48_V1.00_DRAFT.md | e83eb7dee09a37661fa44f6dcc847dd7e9da429473a2ee4bfa00ad6cb36fe4b1 |
| 10 | product_matrix | G03_PRODUCT_MATRIX_GMVQ_MVQ_48_V1.00_DRAFT.md | e3257e339361275174cc063f490536cf1b3b6269495c557d2c4e197dbf0dc2f2 |
| 11 | uom | G03_UOM_GMVQ_MVQ_50_V1.00_DRAFT.md | 9b8f4fd0ab82194fcdb662a2b7b8dd748c277e715bea5591f6df3299216ac6b0 |
Evidence pointer: `01_QUESTION_BANKS/G03_MASTER_DATA/`. Corroborated by both MASTER documents on
COUNT (11); readiness state again disagrees between the two (PASS vs LOCAL NOT READY).
DISPOSITION: **ROSTER_PARTIALLY_VERIFIED** (same basis as G02).

### G04 — ACCOUNT_BASE — 9/9 modules banked
| # | Module | File | SHA-256 |
|---|---|---|---|
| 1 | account_add_gln | G04_ACCOUNT_ADD_GLN_GMVQ_MVQ_48_V1.00_DRAFT.md | 0f8a0c77911a38f33db301d43679f279ce5cfe4970395452fb56db71becef915 |
| 2 | account | G04_ACCOUNT_GMVQ_MVQ_62_V1.00_DRAFT.md | 21bb2dcc472a8a10a95962408b3067837d71ffcc77e12ccb7f3119ebf533cc17 |
| 3 | account_tax_python | G04_ACCOUNT_TAX_PYTHON_GMVQ_MVQ_48_V1.00_DRAFT.md | 794182e3c459fbb11e3a92427d2f202b4a2a9ea85fde1cdc1b38b31716c44f20 |
| 4 | account_test | G04_ACCOUNT_TEST_GMVQ_MVQ_48_V1.00_DRAFT.md | dc24303c486ad8dc630ee6d3a0f8c27427dcaaeaf02789dc5620a00143285f5e |
| 5 | account_update_tax_tags | G04_ACCOUNT_UPDATE_TAX_TAGS_GMVQ_MVQ_48_V1.00_DRAFT.md | b43d509346f672ec4e5968544a463cad3272aa53cf8c9af43fa9054b89ff476e |
| 6 | base_iban | G04_BASE_IBAN_GMVQ_MVQ_48_V1.00_DRAFT.md | 2656c0fc76f48bb030d45ed97729698c870dd47c571df9b176a64e839a67a0ab |
| 7 | base_vat | G04_BASE_VAT_GMVQ_MVQ_48_V1.00_DRAFT.md | c7c16b0767a0a77970935819cc87b112fa14c213f85b5f5038bafd6fd44b9802 |
| 8 | l10n_account_withholding_tax | G04_L10N_ACCOUNT_WITHHOLDING_TAX_GMVQ_MVQ_48_V1.00_DRAFT.md | 0f24d4e65bc54237f5084e84584d3e6b2eb18a3040a47a1ef25405247d551cc6 |
| 9 | l10n_th | G04_L10N_TH_GMVQ_MVQ_50_V1.00_DRAFT.md | fbf79b7faf77f9dcd60981a5bcea0b8510199ecff376cc7a77a63189db5d3fbe |
Evidence pointer: `01_QUESTION_BANKS/G04_ACCOUNT_BASE/`. NOTE — NP-01 (open, separate register)
records that Boss has additional ACCOUNT material authored outside this sweep; that is ADDITIONAL
scope, not a contradiction of this 9-module G04 roster (see `30_NEXT_PHASE_CARRY_FORWARD.md`).
DISPOSITION: **ROSTER_PARTIALLY_VERIFIED**.

### G06 — MANUFACTURING — 12/12 modules banked
| # | Module | File | SHA-256 |
|---|---|---|---|
| 1 | maintenance | G06_MAINTENANCE_GMVQ_MVQ_48_V1.00_DRAFT.md | 5ee4e0c863a60e183e32ac92396964fddb885fe2a969eaa22aac206b4a0ad898 |
| 2 | mrp_account | G06_MRP_ACCOUNT_GMVQ_MVQ_48_V1.00_DRAFT.md | b691c4d3c9ec78d289e0cea7416ae334c46631ad0c42fa006aec3b2fe7aba602 |
| 3 | mrp | G06_MRP_GMVQ_MVQ_67_V1.00_DRAFT.md | 0c370c5e091e603bf59b8c493f5e233ca72d946195657b3d35c36e2e9670ae07 |
| 4 | mrp_landed_costs | G06_MRP_LANDED_COSTS_GMVQ_MVQ_48_V1.00_DRAFT.md | a2bcd2619361dc4cd9ed13411fe9559e1427ee3f1fadcf785101513b4b84ae27 |
| 5 | mrp_product_expiry | G06_MRP_PRODUCT_EXPIRY_GMVQ_MVQ_48_V1.00_DRAFT.md | 78454bd42b9e37f8ecc0b4e57a31a1ac48f3a4c978a21a0153dcf07ba8639637 |
| 6 | mrp_repair | G06_MRP_REPAIR_GMVQ_MVQ_48_V1.00_DRAFT.md | 64df7baf80f4450a9b220a83d27c1bbc89d803ce535189ef3f4a9ce6b6ce4d7f |
| 7 | mrp_subcontracting_account | G06_MRP_SUBCONTRACTING_ACCOUNT_GMVQ_MVQ_48_V1.00_DRAFT.md | 8d896dc62b4085411ff9f02ad4d8a14efd2eb485b9e88e195bed8fb9defa07e7 |
| 8 | mrp_subcontracting_dropshipping | G06_MRP_SUBCONTRACTING_DROPSHIPPING_GMVQ_MVQ_48_V1.00_DRAFT.md | 34e40ae95a3541121ed13c5dc7dc6aa1f856db1465727b43a413d5284739fa32 |
| 9 | mrp_subcontracting | G06_MRP_SUBCONTRACTING_GMVQ_MVQ_61_V1.00_DRAFT.md | 0787bab979220fe5b82e79671e761b41a1caa84e81b3f1613c672601f3752f16 |
| 10 | mrp_subcontracting_landed_costs | G06_MRP_SUBCONTRACTING_LANDED_COSTS_GMVQ_MVQ_48_V1.00_DRAFT.md | 13dbc965371ccffc7827d73655f36c4022022eabdbd00b58256486953766b195 |
| 11 | mrp_subcontracting_purchase | G06_MRP_SUBCONTRACTING_PURCHASE_GMVQ_MVQ_48_V1.00_DRAFT.md | e3e29ad62d01da054222fa927ea4467b74c8b86d97919cabe6980f0d8c110e44 |
| 12 | mrp_subcontracting_repair | G06_MRP_SUBCONTRACTING_REPAIR_GMVQ_MVQ_48_V1.00_DRAFT.md | baa28fd6c8be398167f018140f292a4a984b16e9b1fdd4ab58c83821a3312aba |
Evidence pointer: `01_QUESTION_BANKS/G06_MANUFACTURING/`. Both MASTER documents agree count=12.
DISPOSITION: **ROSTER_PARTIALLY_VERIFIED**.

### G07 — PURCHASE — 9/9 modules banked (+1 backup file, not a module)
| # | Module | File | SHA-256 |
|---|---|---|---|
| 1 | purchase_edi_ubl_bis3 | G07_PURCHASE_EDI_UBL_BIS3_GMVQ_MVQ_50_V1.00_DRAFT.md | e3ebe5bf6b2b6350f83063f7e68afeb637ef37b81aa83c7f45c30ca95bdc63c8 |
| 2 | purchase | G07_PURCHASE_GMVQ_MVQ_62_V1.00_DRAFT.md | ff33abda2b8af43d67f1541ec4806eb5c4b9ebc9cb9f7df6b942f750c9d26df8 |
| 3 | purchase_mrp | G07_PURCHASE_MRP_GMVQ_MVQ_48_V1.00_DRAFT.md | 3f290d7731eecea1e5a95cfd79717d1f3e66ab8277e11f0353144c68651b0026 |
| 4 | purchase_product_matrix | G07_PURCHASE_PRODUCT_MATRIX_GMVQ_MVQ_48_V1.00_DRAFT.md | 861e55f46b392583ddf26098f7de447c05fcf7d045366b6f9c2074d1ea23ee43 |
| 5 | purchase_repair | G07_PURCHASE_REPAIR_GMVQ_MVQ_48_V1.00_DRAFT.md | 02e9078a68113f3e73ac0023d9382f6067dbb79e7635e72aacd695c0705a86d2 |
| 6 | purchase_requisition | G07_PURCHASE_REQUISITION_GMVQ_MVQ_50_V1.00_DRAFT.md | ffc982a3918f428ba9cf53e338e93f42c93a31f202dd70f112e42e2d6f1c9720 |
| 7 | purchase_requisition_sale | G07_PURCHASE_REQUISITION_SALE_GMVQ_MVQ_48_V1.00_DRAFT.md | 72eff4f11d265735a6e08ffe962fc7ab3d60e7e0ecb12adc992a659478786619 |
| 8 | purchase_requisition_stock | G07_PURCHASE_REQUISITION_STOCK_GMVQ_MVQ_48_V1.00_DRAFT.md | 81aad9b5a89ed7b306081689b27a517d799b978a9cb622e1a7b9f61676c75404 |
| 9 | purchase_stock | G07_PURCHASE_STOCK_GMVQ_MVQ_48_V1.00_DRAFT.md | b0cee6b658962e790b0a3e0ef31883e728fad045fb7ec2947819662d888d1277 |
Evidence-hygiene note: the folder also contains `G07_PURCHASE_GMVQ_MVQ_62_V1.00_DRAFT.md.bak_preverify`
(sha256 541dd42bc3d240f56f816af41f17c74fe92ef2b0b8c0b02c5b67e07f072db84a) — a pre-verify backup of
module #2, not a 10th module. Flagged here so Lane A's automated count check does not misread the
folder as 10 modules.
Evidence pointer: `01_QUESTION_BANKS/G07_PURCHASE/`. Both MASTER documents agree count=9.
DISPOSITION: **ROSTER_PARTIALLY_VERIFIED**.

### G11 — EVENTS — 8/8 modules banked
| # | Module | File | SHA-256 |
|---|---|---|---|
| 1 | event_booth | G11_EVENT_BOOTH_GMVQ_MVQ_50_V1.00_DRAFT.md | 8a4b247a2e97d35468ae51f32d93ca8b2c3d44ee6b74128724e0adf0958450ea |
| 2 | event_booth_sale | G11_EVENT_BOOTH_SALE_GMVQ_MVQ_50_V1.00_DRAFT.md | bcc9b19db4886255aa05a603094101977a85c6395eb963bb93b09c7e26496955 |
| 3 | event_crm | G11_EVENT_CRM_GMVQ_MVQ_48_V1.00_DRAFT.md | ef18942290009f0a263b07277ebcd1af1c858553c276e40d98c375c44d872527 |
| 4 | event_crm_sale | G11_EVENT_CRM_SALE_GMVQ_MVQ_48_V1.00_DRAFT.md | 66e24df13c030f984c89d3353c91b0cc18cdf30cd2ac49f176b3a1b552daf465 |
| 5 | event | G11_EVENT_GMVQ_MVQ_62_V1.00_DRAFT.md | 8e6ff6cfa2b69786ea3d11feae8ed80053f3750f504444110a384b287e3c0d80 |
| 6 | event_product | G11_EVENT_PRODUCT_GMVQ_MVQ_50_V1.00_DRAFT.md | 763c3d818d3223323ada6c3d0c1a80c25e6c5c3600d4ff73f821c53e155b68f7 |
| 7 | event_sale | G11_EVENT_SALE_GMVQ_MVQ_50_V1.00_DRAFT.md | bc28b43c73841f1cdbcbc72ac292ef23c52d2c7b23434b2b5f3a2de59b35aa39 |
| 8 | event_sms | G11_EVENT_SMS_GMVQ_MVQ_48_V1.00_DRAFT.md | 5bc62407818dc296f0e76e18173a6bc99790af3396f70698184ce3bb51f8b650 |
Evidence pointer: `01_QUESTION_BANKS/G11_EVENTS/`. Both MASTER documents agree count=8; AUD-3
independent audit already ACCEPTed all 8 (see W2/G09/G11 audit record).
DISPOSITION: **ROSTER_PARTIALLY_VERIFIED**.

## 3. G01 — not part of the reconciliation set, status only (per directive §1, continue, do not stop)
G01 PLATFORM_BASE: 23 modules in scope per both MASTER documents; W1-B01 slice (base, mail, web)
recorded READY - WAITING SHARED CONTROLS with open item B-01 (19 legacy banks pending Boss
Option A/B/C). No new disposition requested by this directive for G01; GMVQ takes no action here
that would interrupt Lane A's G01 AUTO PROCESS.

## 4. MASTER readiness record — correction required (directive §8)
`01_CANONICAL_G_REGISTER.tsv` (ROOM_A_MASTER_ROLLING_6SLOT_EXECUTION_PLAN_20260927_REV001),
same date as the readiness register, states `entry_status: NO MVQ BANK` for G02/G03/G04 and
`no bank` bank_evidence for G05 through G16 inclusive. This is factually superseded by on-disk
evidence: real, hashed bank files exist for G02,G03,G04,G05,G06,G07,G08(partial),G09(partial),
G11,G12,G15 as of this session. GMVQ recommends MASTER reclassify the affected rows in that
specific document as **READINESS_EVIDENCE_GAP** (stale, not authoritative) rather than treat it as
a current roster source — this is a MASTER-owned document; GMVQ does not edit it. This is the
same staleness class already open as gap G-06 (`29_BACKLOG_ROLLUP_BY_G.tsv`) — a second MASTER/
control artifact found stale on the same day. Recommend MASTER audit all rolling-plan TSVs for the
same drift before any is cited as a roster source again.

## 5. New gap filed (at time of discovery, per the B-03 filing-gap lesson)
**G-09 — canonical roster artifact `GROUP_STRUCTURE_V2_CORE.tsv` not locatable on connected
device.** Filed in `13_OPEN_GAPS_AND_BLOCKERS.md` this session. Owner: MASTER / Governance
Controller (GMVQ cannot create an artifact it has no source content for — inventing one would
violate §20). Boss/MASTER to state where this artifact is meant to live, or to formally designate
GMVQ's per-G evidence tables above (§2) as the current governed roster pointer for these six
groups pending that artifact's recovery.

## 6. Lane A release recommendation (directive §6, §7)
For all six groups, GMVQ recommends: release as **PARTIAL_READY** on the strength of §2's
per-module evidence (module identity, count, and content hash all independently reproducible),
while the specific `GROUP_STRUCTURE_V2_CORE.tsv` pointer/hash check itself remains
HOLD-LOCAL pending MASTER's answer in §4-§5. No module within G02,G03,G04,G06,G07,G11 is held for
a content reason — only the named-artifact pointer is unresolved. Boss manual routing not required
for this release per directive §6/§10, once MASTER confirms or corrects §4.
