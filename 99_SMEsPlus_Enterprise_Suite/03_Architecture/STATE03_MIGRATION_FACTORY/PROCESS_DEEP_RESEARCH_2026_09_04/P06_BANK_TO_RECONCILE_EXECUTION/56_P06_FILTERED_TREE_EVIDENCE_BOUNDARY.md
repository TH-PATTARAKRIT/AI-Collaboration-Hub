# P06_FILTERED_TREE_EVIDENCE_BOUNDARY.md

**Session:** P06 — SUPPLEMENTAL CRITICAL-RISK CLOSURE (CP-P06S10)
**Classification:** LAYER 2 — AUDIT QUARANTINE

---

## 1. The two trees, measured

| | **V18E** (research target) | **V19E** (discovered this round) |
|---|---|---|
| Path | `CLAUDE AI/SMEsPlus18/odoo-18.0+e.20250608` | `ODOO/ODOO-COMMUNITY/SMEsPlus19/odoo-19.0+e.20260312` |
| `version_info` | `(18, 0, 0, FINAL, 0, '')` | `(19, 0, 0, FINAL, 0, '')` |
| **Addon directories** | **791** | **1422** |
| **`l10n_*` packs** | **2** — `l10n_th`, `l10n_th_reports` | **514** |

Commands: `ls -d <tree>/odoo/addons/*/ | wc -l` · `ls -d <tree>/odoo/addons/l10n_* | wc -l` · `grep -n "version_info = " <tree>/odoo/release.py`.

> **SUBSTANTIALLY CORRECTED — REV-E-16.** The counts are right; the inference was wrong. **The localisations were not removed, they were RELOCATED.**
> `$V18E/../addons_archive/` holds **961 directories, 904 of them `l10n_*`**, and the project's own `odoo.conf:14` states that `addons_archive` must not be on the `addons_path`. **`l10n_th` and `l10n_th_reports` are NOT in the archive** — the Thai packs were deliberately promoted to the live path and the rest archived.
> **The population therefore splits, and both halves matter:**
> - **Loadable population = 791.** Every negative scoped to what actually runs stands unchanged.
> - **Full v18 distribution = 791 + 961 = 1752.** Any claim phrased as "in Odoo 18" must use this, and **904 localisation packs were reachable on disk and unsearched at round 3.**
> **They have now been searched** — see §4a.

**FTB-F-01 — The v18 tree's live `addons_path` is Thai-only by deliberate configuration, not by a lossy build.** 791 loadable addons with 2 localisation packs, alongside 961 archived directories excluded by config. The v19 tree, by contrast, carries 1422 addons and 514 localisation packs on one path.

---

## 2. Filter rule — inferred, and declared as inferred

**FTB-F-02 — The filter rule is NOT documented anywhere on the workstation.** No manifest, README or build script stating the inclusion criteria was found.

What the evidence supports: the v18 tree retains **the Thai localisation only**, which is consistent with a build filtered to the deployment jurisdiction. **Classification: `SUPPORTED INTERPRETATION`, not `FACT VERIFIED`.** The rule is inferred from what survived, not read from a specification.

**Consequence, and it is the uncomfortable one:** because the rule is unknown, **it is not possible to state which non-`l10n_` modules were removed.** The 631-directory difference is not all localisation — 514 of it is, leaving **117 other directories present in v19 and absent from v18**. Some of that is genuine v19 addition; some may be v18 modules the filter dropped. **This session did not enumerate the difference.** Recorded as `P06-OQ-110`.

---

## 3. Population classification

| Class | Count | Basis |
|---|---|---|
| **INCLUDED — verified present in V18E** | **791** | executed directory count |
| **EXCLUDED — verified absent from V18E, present in V19E** | **≥ 512** localisation packs | 514 − 2 |
| **UNKNOWN population** | **117 non-`l10n_` directories** in V19E and not in V18E, of which an unknown share are v19 additions and an unknown share are filter removals | not enumerated — `P06-OQ-110` |

---

## 4. The qualifier every tree-scope negative must carry

**Permitted form:**
> *"NO DEFINITION FOUND IN THE FILTERED 791-ADDON v18 TREE, PATTERN `<x>`, PATH SET `<y>`."*

**Not permitted:**
> *"No definition exists."* — unless the whole relevant population has been verified.

### Negatives in this package, re-qualified

| Negative | Prior scope | **Re-qualified** | Cross-version status |
|---|---|---|---|
| No bank fee / interest / commission concept (`B-17`) | 6 modules + 2 l10n packs | **791-addon filtered v18 tree, 6 declared modules, 13 tokens** | **also tested on V19E — 2 hits, both a CoA row and a test. CROSS-VERSION INVARIANT VERIFIED** |
| No returned/bounced/PDC concept (`B-34`, `B-35`) | 6 modules + 2 l10n packs | same | **not re-tested on V19E — `P06-OQ-111`** |
| `is_internal_transfer` field NOT FOUND | whole v18 tree | **filtered 791-addon tree** | not re-tested |
| `destination_journal_id` NOT FOUND | whole v18 tree | **filtered 791-addon tree** | not re-tested |
| `paired_internal_transfer` never written | whole v18 tree | **filtered 791-addon tree** | not re-tested |
| `provider_reference` uniqueness NOT FOUND | whole v18 tree | **filtered 791-addon tree** | not re-tested |
| `chargeback|dispute` NOT FOUND | 3 modules | **loadable set (791 addons), 3 declared modules** [REV-E-23, 2026-09-06] | not re-tested |

**FTB-F-03 — Five tree-scope negatives remain single-pass AND bounded to the LOADABLE SET.** ~~*"filtered-tree-bounded"*~~ [REV-E-23, 2026-09-06] — the tree is **RELOCATED** (loadable 791 of a full v18 population of 1752; 961 dirs / 904 l10n in `addons_archive`, excluded by the project's own `odoo.conf` and since searched), not filtered (`REV-E-16`). They are the residue keeping `AASP-VETO-01` partly in force, and the v19 tree now makes a second pass cheap: the same patterns can be run against a complete distribution.

---

## 5. What the boundary does NOT invalidate

**FTB-F-04 — No positive finding is affected.** Every CONFIRMED DEFECT rests on quoted code that is present in the tree. A filtered tree can make a negative unsafe; it cannot make a quotation false.

**FTB-F-05 — And six core findings were re-tested against the complete v19 tree and survived** (`51_` §2). **The loadable-set boundary risk** ~~*"filtered-build risk"*~~ [REV-E-23, 2026-09-06] **is therefore measured for the findings that carry the severity, and it is small.** What remains exposed is the five single-pass negatives in §4.

---

## 6. Requirement

| ID | Requirement |
|---|---|
| `FTB-R-01` | Every negative claim states the population it was searched over, by count, not by name alone. "The tree" is not a population. |
| `FTB-R-02` | Where a filtered build is the evidence base, the filter rule is documented or declared unknown. |
| `FTB-R-03` | P11 records the evidence-base boundary alongside each P06 negative, or confirms peers used the same build. **This is `AASP-VETO-03`.** |

---

## 4a. The archive, searched (added at the supplemental round)

**DENOMINATOR:** POPULATION `$V18E/../addons_archive` — **961 directories, 904 `l10n_*`**. UNIT: matching file / field definition.

| Pattern | Result |
|---|---|
| `bank_fee\|bank_charge\|transaction_fee\|merchant_fee\|processing_fee\|commission_amount` | **5 files.** Two are chart-of-account *rows* (`l10n_fr`, `l10n_lu` templates). One is `sale_amazon`, carrying **`commission_amount = fields.Monetary()`** ×2 |
| ~~`payment_return\|bounce\|dishonou?r\|post_dated\|postdated`~~ **— WITHDRAWN, THE PATTERN COULD NOT FIRE** **[Q-P06-04 / XRD-004, 2026-09-07]** | ~~*"hits are email-bounce and SMS tracking plus one NZ EFT test. **No bank-return concept**"*~~ → **the search was published with no command, no `-E`/`-F` flag and no path expression.** Under **ERE** the whole alternation matches **0 of 5** (`\|` is a literal pipe); under **BRE** the `dishonou?r` branch matches only the literal string `dishonou?r`, because `?` is not a metacharacter there. **RE-RUN — `/usr/bin/grep -rlE 'payment_return\|bounce\|dishonou?r\|post_dated\|postdated'` over the same 961 directories → 76 files.** Positive control **inside the population**: `bounce` → 66 files. Negative control: impossible token → 0. Per branch: `payment_return` 0 · `bounce` 66 · **`dishonou?r` 10** · `post_dated` 0 · `postdated` 0. Widened spellings, same population: **`post-dated` (hyphenated) → 2 files** — a spelling the original pattern could not match either |

**FTB-F-06 — One real field hit, and it narrows the wording rather than overturning the finding.**
`commission_amount` exists as a `fields.Monetary()` in an **archived marketplace connector** (`sale_amazon`), which is **not on the live addons path**. A marketplace commission is not a bank fee, a bank interest or a payment-provider settlement commission.
**`B-17` survives.** Its permitted wording is now: *"no bank fee, bank interest or provider-commission concept exists in the loadable v18 population (791 addons) or in the 961-module archive"* — **not** *"no commission field exists in Odoo 18"*.

**FTB-F-07 — WITHDRAWN AS PUBLISHED. THE NEGATIVE WAS UNEVIDENCED, AND ON RE-EXECUTION IT IS FALSE.** **[Q-P06-04 / XRD-004, 2026-09-07]**

~~*"`B-34` / `B-35` survive the enlarged population intact. No returned-item, bounced-cheque or post-dated-cheque concept was found across 1752 v18 directories."*~~

**Re-run with a pattern proved to fire, over the same declared 961-directory archive, finds the concept — twice for returns and once for post-dating:**

| Concept | Archived artefact | What it is |
|---|---|---|
| **Dishonoured payment** | `l10n_nz_eft/models/account_batch_payment.py` — `l10n_nz_dishonour_account_id = fields.Many2one(...)`, help *"Used by ANZ as a fallback account in case of dishonored payment"* | **a real ORM field on `account.batch.payment`**, with a form view (`views/account_batch_payment_views.xml`) and a test |
| **Dishonoured instrument** | `l10n_kr/data/template/account.account-kr.csv` — account `121504` *"dishonored bills and checks"*, `asset_non_current` | **a chart-of-accounts row** |
| **Post-dated cheque** | `l10n_latam_check/__manifest__.py` — *"add an optional 'Check Cash-In Date' for **post-dated checks** (deferred payments)"* | **a module feature** |

**Restated, with the boundary the evidence actually supports:**

> **A returned-item / dishonoured-payment concept and a post-dated-cheque concept BOTH EXIST in the v18 distribution — in `addons_archive` only.** Neither is on the live `addons_path`: `odoo.conf:67` excludes `addons_archive`, and `l10n_nz_eft` is absent from the 791 loadable addons. **The concept is not missing from Odoo 18; it is missing from this deployment's loadable set.**

**Consequence for `P06-B-34` and `P06-B-35`, flagged and NOT disposed here:** their surviving basis is now *"absent from the loadable set"*, **not** *"absent from the v18 distribution"*. **That is a materially weaker claim and a different remedy** — a module exists that could be loaded, rather than a capability that must be built. **Their disposition is the owner's, and is routed, not decided by this correction** (`Q-P06-04` authorises re-stating `FTB-F-07`, not re-adjudicating the blockers it feeds).

*Same shape as `FTB-F-06`: an archived module carries the capability, and the archive is excluded by the project's own config.*

**FTB-F-08 — And the round-3 gap was real but smaller than feared.** Searching 904 additional localisation packs changed **one word** in one finding. That is the correct outcome of a boundary check: it is run to find out, not to confirm.
