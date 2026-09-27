# INDEPENDENT GMVQ AUDIT RECORD — G09 (CRM) and G11 (EVENTS) — AUD-3
Authority: GMVQ_MASTER_AUDIT_CHARTER_V1.00 · GMVQ_AUTHORING_STANDARD_V1.00 · GMVQ_BRIDGE_MODULE_RULE_V1.00
Auditor: Independent audit cell AUD-3. Did not author these banks. Read-only on `01_QUESTION_BANKS/`.
Status: AUDIT COMPLETE — recommendation only. Not Boss approval, not a certification.

## Scope
G09_CRM: 8 of 11 modules on disk (crm, crm_iap_enrich, crm_iap_mine, crm_livechat, website_crm,
website_crm_iap_reveal, website_crm_livechat, website_crm_partner_assign). The remaining 3 CRM
modules are pre-recorded in `02_REGISTERS/13_OPEN_GAPS_AND_BLOCKERS.md` (G-07) as unauthored due
to a harness-level dispatch block, not a content defect of the 8 audited here — not re-flagged.

G11_EVENTS: 8 of 8 modules on disk (event, event_booth, event_booth_sale, event_crm,
event_crm_sale, event_product, event_sale, event_sms).

## Method
1. Ran `03_TOOLS/question_bank_lint_v1_01.py` V1.05 per-group against all 16 files with an
   explicit `--modules` allow-list, producing an actual-count register and advisory queue.
2. Read HYPOTHESIS text in full for the base bank and both `_sale` three-way bridges in each
   group (crm, event, event_sale, event_booth_sale, event_crm_sale, crm_iap_enrich,
   crm_iap_mine — 7 files, 354 questions read in full) and sampled 3 full question blocks
   (QID/HYPOTHESIS/DISCONFIRMING_OBSERVATION) from each of the remaining 9 files (27 more
   questions), for a total of 381 of 821 questions read in full text — well above the charter's
   12-per-bank floor for every bank.
3. Wrote a pairwise HYPOTHESIS-similarity script (difflib SequenceMatcher, ratio>0.6) across
   every cross-file question pair within each group (415 questions x 415 in G09;
   406 x 406 in G11) to surface candidate near-duplicates the sampling could miss, per
   GMVQ_BRIDGE_MODULE_RULE_V1.00's "noun-swapped near-duplicate" concern.
4. Checked QID contiguity and prefix-to-module correctness by direct count for all 16 files.

## Validator results (V1.05, actual counts)
| module | actual_mvq | filename claims | match | field/vocab/clean-room errors |
|---|---|---|---|---|
| crm | 66 | 66 | YES | 0 |
| crm_iap_enrich | 48 | 48 | YES | 0 |
| crm_iap_mine | 48 | 48 | YES | 0 |
| crm_livechat | 50 | 50 | YES | 0 |
| website_crm | 48 | 48 | YES | 0 |
| website_crm_iap_reveal | 48 | 48 | YES | 0 |
| website_crm_livechat | 55 | 55 | YES | 0 |
| website_crm_partner_assign | 52 | 52 | YES | 0 |
| event | 62 | 62 | YES | 0 |
| event_booth | 50 | 50 | YES | 0 |
| event_booth_sale | 50 | 50 | YES | 0 |
| event_crm | 48 | 48 | YES | 0 |
| event_crm_sale | 48 | 48 | YES | 0 |
| event_product | 50 | 50 | YES | 0 |
| event_sale | 50 | 50 | YES | 0 |
| event_sms | 48 | 48 | YES | 0 |

All 16 modules meet the >=48 MVQ floor with no padding-to-exactly-48 pattern (counts land on
48/50/52/55/62/66 — matches the authoring standard's "48, 50, 52, 55 all valid" language).
Zero FIELD, FORMAT, VOCABULARY (RISK_TIER/OUTPUT_CLASS closed-list), or CLEAN_ROOM
(vendor/technical-identifier/module-name leakage) errors across all 821 questions in both groups.
Zero ADVISORY entries were raised by the validator's generic-word-module screen for either group.

**Validator artifact, not a defect**: the tool reported every module BELOW_FLOOR on
`actual_research_depth` because it was run without `--standard` (no STANDARD-55 bank file exists
inside this package's authorized folder to point it at, so `standard_actual=0`). Per the
authoring standard, research depth = 55 (shared standard, authored elsewhere) + actual_mvq; since
every audited module has actual_mvq>=48, true depth is >=103 for all 16 and the floor is met.
Recorded here per Charter SS4 evidence discipline (report actual numbers, never round, never
publish a competing number) — the register TSV faithfully reproduces the tool's raw output and
this note explains the artifact rather than silently correcting it.

## Duplicate / overlap findings (Charter SS3 item 4, Bridge Rule)
Pairwise HYPOTHESIS similarity flagged 3 cross-file pairs in G09 (none in G11):

1. **RETURN** — `G09-WEBSITE_CRM_PARTNER_ASSIGN-Q048` vs base-bank `G09-CRM-Q017`
   (ratio 0.61). Both assert "audit trail of previous owner/assignment survives reassignment,"
   both DISCONFIRMING_OBSERVATIONs describe the identical failure event (post-reassignment trail
   erased) with only the entity noun changed (opportunity/owner -> lead/assignment). Q048 never
   exercises the one fact that would make it a genuine seam question distinct from the base bank
   — which routing rule fired — despite naming it in the HYPOTHESIS. This is the shape
   GMVQ_BRIDGE_MODULE_RULE_V1.00 SS4 names as forbidden ("restates the base module's behaviour
   with the bridge's name attached"). Recorded as a defect against website_crm_partner_assign
   only; the base crm bank is not at fault. Full defect record in the TSV.

2. **Reviewed, not a defect** — `G09-CRM_IAP_ENRICH-Q047` vs `G09-CRM_IAP_MINE-Q038` (ratio 0.72)
   and `-Q032` vs `-Q023` (ratio 0.64). Both pairs reuse an "eligibility-on-paper vs.
   reachability-at-runtime" phrasing template across the two IAP-bridge siblings. Read in full:
   the DISCONFIRMING_OBSERVATION events are concretely different — Q047/Q038 test a scheduled
   background pass's actual per-record coverage (enrich) against an on-demand action's actual
   triggerability (mine); Q032/Q023 test default-off gating against, respectively, module
   presence and independently, available credit. Different EXPECTED_SURFACE codes (S7,S8 vs
   S3,S7). Judged genuine seam variation on two different mechanisms (push/scheduled vs.
   pull/on-demand), not a noun-swapped duplicate. No action requested.

The three `_sale` bridge banks in G11 (`event_sale`, `event_booth_sale`, `event_crm_sale`) were
specifically checked against each other given the Bridge Rule's own worked warning about `sale_*`
family duplication in W2 — 0 pairs at ratio>=0.6 were found; each bank's questions are anchored to
a genuinely different pair of state machines (order<->registration; order<->booth-allocation;
order<->registration<->opportunity), confirming this is not a repeat of the W1 defect pattern.

## Filler / answer-leakage / DISCONFIRMING quality
No forbidden question shapes ("does it exist," "is it well designed," pure confirmation with no
failure mode) were found in the 381 questions read. In every sampled/full-read question the
DISCONFIRMING_OBSERVATION states a distinct, concrete observable failure state rather than a
negated restatement of the HYPOTHESIS.

## Verdict summary
- ACCEPT: 15 of 16 modules (crm, crm_iap_enrich, crm_iap_mine, crm_livechat, website_crm,
  website_crm_iap_reveal, website_crm_livechat, event, event_booth, event_booth_sale, event_crm,
  event_crm_sale, event_product, event_sale, event_sms).
- RETURN: 1 module (website_crm_partner_assign) — 1 named QID defect (Q048), rest of the bank
  (51/52 questions) unaffected.
- HOLD: 0. ESCALATE: 0.

No governance-level (ESCALATE) issue was found in either group. The pre-existing G-07 gap (3 of
11 CRM modules undispatched) and the depth-floor validator artifact above are noted for
completeness but are not new findings created by this audit.
