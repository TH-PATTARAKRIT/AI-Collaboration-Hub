# Atomic Handoff Packet — U41

> **DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION.** Notification/traceability packet only: not a merge request, not Gate PASS, not a verification result. No V-level, Module/Function Complete, coverage figure or denominator freeze is asserted.

| Field | Value |
|---|---|
| Atomic Boundary ID | `U41` |
| Source revision | `19.0.post20260921` (Community only) |
| DB baseline | `iTest19C_2026-09-21` (zip sha256 `c49e022179ea6a64cbac8b5d1b138e428c31af414078049172351a16bd69966c`) |
| Content commit | `2438aec38c23ebb407697b3713e69d6546e15c59` on `claude/local-odoo-source-research` |
| Packet generated | 2026-10-02 |
| Mechanical gate | PASS-MECHANICAL (pointer+anchor+neutral-leak script; semantic verification pending) |
| Gate output | `claims=359 supported_pointer_and_anchor=359 unknown_class=10 neutral_ids=116` / `FAIL claim-checks=0 neutral-leak-tokens=0` |

## Files (restricted layer / neutral layer are separate)
| Layer | Path | sha256 |
|---|---|---|
| Restricted Technical Evidence | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/01_RESTRICTED_TECHNICAL_EVIDENCE/U41_html_http_iap_livechat_links.md` | `da624c34d6654af2052d86a99f8735d38dcbf715b5dd91dcbffd44c9bfaed886` |
| Neutral Knowledge | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/02_NEUTRAL_KNOWLEDGE/U41_html_http_iap_livechat_links_NEUTRAL.md` | `55eb83f348806caee365e417f2fde7437bc38c792a8024f08843651c579b4215` |

## Counts (derived from the claims table)
| Item | Count |
|---|---|
| Claims | 359 (FACT 309 · OBSERVATION 10 · INFERENCE 30 · UNKNOWN 10) |
| Neutral statements | 116 |
| Contradiction (CONTRA) claims | 0 |
| Runtime/AWT-required (RT) claims | 46 |
| Claims bound to an existing C1 Function-ID | 0 (distinct C1 IDs: none) |
| Claims with an existing Function-ID | 0; `FUNCTION MAPPING REQUIRED`: 359 |
| Existing Function-IDs referenced | none |

## Capabilities in scope
- CAP-U41-01 Paid external service accounts, credit handling and what leaves the system (iap, iap_mail, iap_crm)
- CAP-U41-02 Language-prefixed public addresses, language choice and redirects (http_routing)
- CAP-U41-03 Readable address segments, public translations and frontend error pages (http_routing)
- CAP-U41-04 Tracked short links, click counting and redirect, and link shortening in content (link_tracker)
- CAP-U41-05 Editor media, attachments, previews and outbound calls (html_editor controllers)
- CAP-U41-06 In-place editing save-back, snippets, field converters and revision history (html_editor models)
- CAP-U41-07 Live chat channel set-up, operators, rules and operator selection (im_livechat)
- CAP-U41-08 Visitor session creation, public and cross-origin surface, feedback, transcripts and session end (im_livechat)
- CAP-U41-09 Chatbot scripts, steps, visitor data capture and hand-over to a human (im_livechat, crm_livechat pointers)
- CAP-U41-10 Conversation handling after the first reply: status, escalation, history, tags, ratings and reporting (im_livechat)

## Contradiction claim ids
none

## Runtime-required claim ids
VDR-U41-C006, VDR-U41-C015, VDR-U41-C019, VDR-U41-C035, VDR-U41-C038, VDR-U41-C039, VDR-U41-C040, VDR-U41-C041, VDR-U41-C042, VDR-U41-C047, VDR-U41-C104, VDR-U41-C125, VDR-U41-C126, VDR-U41-C137, VDR-U41-C138, VDR-U41-C159, VDR-U41-C167, VDR-U41-C168, VDR-U41-C170, VDR-U41-C172, VDR-U41-C175, VDR-U41-C185, VDR-U41-C187, VDR-U41-C201, VDR-U41-C254, VDR-U41-C259, VDR-U41-C266, VDR-U41-C268, VDR-U41-C275, VDR-U41-C279, VDR-U41-C280, VDR-U41-C282, VDR-U41-C283, VDR-U41-C284, VDR-U41-C316, VDR-U41-C317, VDR-U41-C333, VDR-U41-C351, VDR-U41-C352, VDR-U41-C353, VDR-U41-C354, VDR-U41-C355, VDR-U41-C356, VDR-U41-C357, VDR-U41-C358, VDR-U41-C359

## Boundaries / limits
Source-static + configuration-only DB reconciliation of a near-empty restore; nothing was executed. Unknowns and runtime-required items are listed per capability in the restricted file; DISCOVERED SUPPORTING MODULES are listed in the unit report section of the restricted file or in the Handoff Round entry. Next: continue authorized batch plan (see `00_CONTROL/B00_CHECKPOINT_RECONCILIATION.md` §5).
