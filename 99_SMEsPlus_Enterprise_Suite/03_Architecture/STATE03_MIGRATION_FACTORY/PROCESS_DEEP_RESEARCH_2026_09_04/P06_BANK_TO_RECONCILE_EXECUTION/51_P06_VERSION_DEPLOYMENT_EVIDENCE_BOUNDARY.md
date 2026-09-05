# P06_VERSION_DEPLOYMENT_EVIDENCE_BOUNDARY.md

**Session:** P06 — SUPPLEMENTAL CRITICAL-RISK CLOSURE (CP-P06S08)
**Classification:** LAYER 2 — AUDIT QUARANTINE

> **THIS FILE OVERTURNS A PRIOR P06 CONCLUSION.** Round 3 recorded `P06-B-44` as a *"generation gap"* on the premise that only v19 **deployment** evidence existed while the research target was v18, and that no v19 **source** was available. **A complete Odoo 19 Enterprise tree named `SMEsPlus19` is present on this workstation.** Round 3 did not search for it. §5 records the author error.

---

## 1. What is actually on the workstation

| Ref | Tree | `version_info` | Addon dirs | `l10n_*` packs |
|---|---|---|---|---|
| **V18E** | `/Volumes/iMacSys/CLAUDE AI/SMEsPlus18/odoo-18.0+e.20250608` | `(18, 0, 0, FINAL, 0, '')` | **791** | **2** |
| **V19E** | `/Volumes/iMacSys/ODOO/ODOO-COMMUNITY/SMEsPlus19/odoo-19.0+e.20260312` | `(19, 0, 0, FINAL, 0, '')` | **1422** | **514** |

Commands executed: `grep -n "version_info = " <tree>/odoo/release.py` · `ls -d <tree>/odoo/addons/*/ | wc -l` · `ls -d <tree>/odoo/addons/l10n_* | wc -l`.

Also present, not analysed here: `/Volumes/iMacSys/CLAUDE AI/SMEsPlus/SMEsPlus_19.0.20260418`.

**VER-F-01 — The v18 tree is a filtered subset; the v19 tree is a complete distribution.**
791 versus 1422 addons, and **2 versus 514 localisation packs**. The v18 tree was filtered to the Thai deployment. **This retroactively confirms `P06-B-55` and supplies the comparison that proves it**, which round 3 inferred from the l10n count alone.

**VER-F-02 — The tree is named `SMEsPlus19`.** The directory naming is the same convention as `SMEsPlus18`. **A v19 line exists for this project.** Classification: **FACT VERIFIED** as to the tree's existence and naming. It is **NOT** evidence of what is deployed — naming is not a deployment record.

---

## 2. Cross-version invariance — every core P06 finding re-tested against v19

This is the material work of this file. Each check was run against `V19E` and compared with the recorded v18 finding.

| # | P06 finding | v18 | v19 | Classification |
|---|---|---|---|---|
| 1 | **`is_matched` is true without a bank statement** (`B-06`, `C-01`) | 3 config branches at `account_payment.py:436-455` | **same branches** — `:479` `pay.is_matched = pay.state == 'paid'`; `:485`/`:491` `= True` | **CROSS-VERSION INVARIANT VERIFIED** |
| 2 | **`root_id` is a fiscal hierarchy, `vat` not delegated** (`B-27`) | base returns `['currency_id']`; account adds 4 | **identical** — base `return ['currency_id']`; account adds `fiscalyear_last_day`, `fiscalyear_last_month`, `account_storno`, `tax_exigibility` | **CROSS-VERSION INVARIANT VERIFIED** |
| 3 | **Reconcile/un-reconcile outside the close regime** (`A6`) | lock-date hits: `account_full_reconcile` 0, `account_bank_statement_line` 0, `account_partial_reconcile` 2 (date relocation) | **same distribution** — 0, 0, 2 | **CROSS-VERSION INVARIANT VERIFIED** |
| 4 | **`remove_move_reconcile` is a bare unlink with no checks** | 3-line body | **identical 3-line body** | **CROSS-VERSION INVARIANT VERIFIED** |
| 5 | **No bank fee / interest / commission concept** (`B-17`) | 0 definitions over 6 modules | 2 files hit over `account`+`account_accountant`+`payment`: `chart_template.py` (the CoA row) and a **test**. **No model or field definition** | **CROSS-VERSION INVARIANT VERIFIED**, bounded as before |
| 6 | **No server-side authorisation on the RPC dispatch chain** (`B-50`) | `auth="user"`; `get_public_method` blocks only private/`@api.private`; `call_kw` has no access check; ACL row is `base.group_system` | **same chain**; `get_public_method` additionally blocks `_UNSAFE_ATTRIBUTES` and classmethod/staticmethod — **neither excludes `remove_all`**; ACL row identical at `:131` | **CROSS-VERSION INVARIANT VERIFIED** |

**VER-F-03 — All six core findings hold in v19. Not one is version-dependent.**

**This is the most consequential result of the supplemental round, and it cuts against the package's own prior anxiety.** Round 3 wrote that *"if the target generation has moved, a material fraction of this package is scoped to a superseded line."* **That fear is now measured and largely disproved:** the findings that carry the CRITICAL and HIGH severity survive the generation change intact, because they are properties of a design that v19 did not alter.

---

## 3. What IS version-dependent

**VER-F-04 — v19 ships a native withholding-tax capability that v18 does not.**
`$V19E/addons/l10n_account_withholding_tax` and `l10n_account_withholding_tax_pos` exist. **NOT FOUND** in `$V18E` (which has no such directory in its 791).
This corroborates the DM-B registry, which showed `Withholding Tax on Payment` **Installed** on a `saas~19.1` database.
**Consequence:** the project's two custom Thai WHT subsystems — which P05, P06 and P07 all found mutating the settled amount — would, on v19, sit alongside a **platform-native** capability covering the same ground. **That is a P07 question and P06 does not adjudicate it.** Routed as `P06→P07` note.

**VER-F-05 — The localisation surface differs by two orders of magnitude** (2 vs 514). Any negative claimed at "localisation scope" on v18 is a claim about a Thai-only filter; the same claim on v19 would be a claim about 514 packs. **They are not the same negative and must not be merged at P11.**

---

## 4. Classification per the required vocabulary

| Question | Classification |
|---|---|
| **V18 research target** | **V18 SOURCE VERIFIED** — `version_info = (18,0,0,FINAL,0)`; 791 addons, filtered |
| **V18 deployment** | **NOT VERIFIED** — no target registry exists |
| **V19 source** | **V19 SOURCE VERIFIED** — `version_info = (19,0,0,FINAL,0)`; 1422 addons, complete; tree named `SMEsPlus19` |
| **V19 deployment** | **V19 DEPLOYMENT EVIDENCE ONLY** — two `ir.module.module` exports, one attributable to the BHPRO client, one unattributable. **Neither is the SMEsPlus target.** |
| **Cross-version conclusion** | **CROSS-VERSION INVARIANT VERIFIED** for all six core P06 findings; **VERSION-DEPENDENT** for the native WHT capability and the localisation surface |
| **Which generation is the SMEsPlus target?** | **UNRESOLVED — DEPLOYMENT EVIDENCE REQUIRED.** Both a `SMEsPlus18` and a `SMEsPlus19` tree exist. Directory naming is not a deployment record. |

---

## 5. Author error — REV-E-10

**Original statement (round 3, `24_` DME-F-03 and `40_` `B-44`):**
> *"The only deployment evidence available is from **Odoo 19** databases, while the entire P06 research target is the **v18** line. If the programme's target generation has moved, a material fraction of this package is scoped to a superseded line."*

**What was wrong:** not the observation, but the **search boundary behind it**. Round 3 searched `~/Downloads` for registries and the v18 tree for source. **It did not search the workstation for a v19 source tree**, and therefore framed the generation gap as unanswerable without a database export.

**The command that exposed it:** `find /Volumes/iMacSys -maxdepth 4 -type d \( -iname "*odoo-19*" -o -iname "*19.0*" \)` — run in this round, returning five hits including a complete v19 Enterprise tree named `SMEsPlus19`.

**Corrected result:** the generation question is **still open as to deployment**, but the **research risk it implied is now measured and largely retired** — six of six core findings are cross-version invariant.

**Affected items:** `B-44` re-worded (§6); `B-55` confirmed and strengthened with a real comparison; `AASP-VETO-02`'s first ground materially weakened (`66_`).

**Significance.** This is the **third** time in the P06 programme that a conclusion rested on an unsearched evidence base — after *"no source/DB access exists"* in an earlier session and the filtered-build discovery in round 3. **The recurring defect is not a wrong answer; it is a search boundary drawn without being declared.** The lesson already exists in the programme's standing rules; it was not applied.

---

## 6. `P06-B-44`, restated

**Prior wording:** *"GENERATION GAP — the only deployment evidence is Odoo 19 while the research target is v18; a material fraction of this package may be scoped to a superseded line."*

**Restated:**
> **`P06-B-44` — The SMEsPlus target generation is undeclared. Both a filtered v18 tree and a complete v19 tree exist on the workstation, and the only module registries available are v19 databases that are not the SMEsPlus target. The six core P06 findings have been re-tested and are cross-version invariant, so the research risk is retired; what remains is that no artefact states which generation the target runs.**
> **Status: HOLD — DEPLOYMENT REGISTRY EVIDENCE REQUIRED. Severity: HIGH → MEDIUM** (the finding-invalidation risk is measured and disproved; the remaining risk is relevance, not correctness).

---

## 7. Open items

| ID | Item | Class |
|---|---|---|
| `P06-OQ-103` | Which generation the SMEsPlus target runs. One `ir.module.module` export settles it. | **HOLD — DEPLOYMENT REGISTRY EVIDENCE REQUIRED** |
| `P06-OQ-104` | The v19 native `l10n_account_withholding_tax` overlaps two custom Thai WHT subsystems. **Routed to P07.** | C |
| `P06-OQ-105` | `SMEsPlus_19.0.20260418` was not analysed. | C |
| `P06-OQ-106` | Whether the custom addon set has a v19 line. Not searched this round. | C |
