# ACCOUNT WAVE A — `MCU-04` FINAL DISPOSITION

Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-FC-001` · Layer 1 clean-room
Parent `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-MCC-001` · Programme `SMEPLUS-26-09-04-ACCOUNT-FULL-DEEP-001`

> **Recommendation only. Boss is the sole Final Approver. No AI may declare Final Approval.**
> This file re-verifies `MCU-04` from primary source. It does **not** inherit the parent disposition.

---

## 1. Why this file exists

The round instruction §4 states that the evidence *"indicates `MCU-04` may now be closable as a
verified defect rather than a deferred tenant question"*, and then instructs: **do not accept that
statement automatically.**

Two parent artefacts disagree, and the disagreement is live:

| Artefact | `MCU-04` disposition |
|---|---|
| `MCC_D_GATING_UNKNOWN_EXHAUSTION_REGISTER.md` §2 | **`REMAINS GATING — HOLD`** |
| `ACCOUNT_WAVE_A_MCC_FINAL_GATE_REPORT.md` §7 item 4 | *"`MCU-04` **is closable** now"* — i.e. **not yet closed** |
| `MCC_00_CANONICAL_FIGURES_REGISTER.md` §2 | **`CLOSED — VERIFIED DEFECT`** — and `MCC_00` governs |

So the governing register already carries the closure, one artefact carries the opposite, and a third
carries a state between the two. **This file settles it on evidence rather than on precedence.**

---

## 2. The exact claim under test

> `account.report` — the accounting **report-definition** model — carries **no company dimension**, is
> targeted by **no record rule anywhere**, and is fully writable, creatable and deletable by the
> accounting-manager role; two `state=code` server actions are bound to it, one of them granted to the
> ordinary accounting-**user** role.

Source of the claim: `MCC_J_FRESH_EXPERT_AND_AUDIT_CHALLENGE.md` `J-11`, evidence tag `MCCX-5`.

---

## 3. Declared search parameters

Per the Denominator Completeness Rule (`POPULATION` + `PATTERN` + `PATH SET` + `UNIT`, none
author-chosen):

| Element | Declared value |
|---|---|
| **POPULATION** | Every declaration that could give `account.report` a company dimension or a record rule: model field declarations, model extensions, ACL rows, XML `ir.rule` records, Python `ir.rule` creations |
| **PATTERN** | `_name = ['"]account\.report['"]` · `_inherit = ['"]account\.report['"]` · `ref="(account\.)?model_account_report"` · `model_account_report,` in `*.csv` · `model="ir\.rule"` in `*.xml` · `env\['ir\.rule'\]` in `*.py` |
| **PATH SET** | **Six reference roots**, listed in §4. Not one tree. This is the correction `GB-07` demands |
| **UNIT** | One **declaration site** (one field declaration, one ACL row, one `<record>` element) |

**Every root was enumerated. No root was sampled.**

---

## 4. Path set actually searched

| # | Root | Exists |
|---|---|---|
| 1 | `/Volumes/iMacSys/ODOO/ODOO-COMMUNITY/ODOO19` | yes |
| 2 | `/Volumes/iMacSys/ODOO/ODOO-COMMUNITY/SMEsPlus19` | yes |
| 3 | `/Volumes/iMacSys/ODOO/ODOO-COMMUNITY/Odoo18` | yes |
| 4 | `/Volumes/iMacSys/ODOO/ODOO-COMMUNITY/Odoo16` | yes |
| 5 | `/Volumes/iMacSys/ODOO/ODOO-COMMUNITY/Odoo14` | yes |
| 6 | `/Volumes/iMacSys/ODOO/SOURCE CODE/ODOO 18/odoo-18.0.post20260605` | yes |

---

## 5. Findings — element by element

### 5.1 No company dimension · `VERIFIED FACT`

`ODOO19/addons/account/models/account_report.py:45` declares `_name = 'account.report'`. The complete
field list of that class contains **`country_id`** and **no `company_id`**.

`filter_multi_company` (line 120) is **not** a scoping field. The source carries an explicit comment
immediately above it:

> `# Those fields control the display of menus on the report`

It selects between *"Use Company Selector"* and *"Use Tax Units"* — a **rendering option**, not an
access control. Treating it as a defence would be a reader's error; the source forecloses it.

**Cross-version:** identical in v18 (`_name = "account.report"`, `account_report.py:25`) and in both
v19 trees.

### 5.2 No extension adds one · `VERIFIED FACT`, bounded negative

Ten-plus modules declare `_inherit = 'account.report'` (localisations, `account_reports`,
`documents_account`, cash-basis, analytic, executive summary). **Every one was opened and tested for a
`company_id = fields.` declaration. Zero declare one.**

> This is a **bounded** negative claim, class `A`: the population is the complete set of
> `_inherit = 'account.report'` sites in the path set, the pattern is declared, and every member was
> tested. It is **not** "no evidence found".

### 5.3 Full manager CRUD · `VERIFIED FACT`

`ODOO19/addons/account/security/ir.model.access.csv`:

| line | rule | group | R | W | C | U |
|---|---|---|---|---|---|---|
| 129 | `access_account_report_basic` | `account.group_account_basic` | 1 | 0 | 0 | 0 |
| 130 | `access_account_report_readonly` | `account.group_account_readonly` | 1 | 0 | 0 | 0 |
| **131** | **`access_account_report_ac_user`** | **`account.group_account_manager`** | **1** | **1** | **1** | **1** |

**Identical in v18** (same file, lines 136–138) and **identical in all three SMEsPlus19 copies.**
Read, write, create and **unlink** — an accounting manager can *delete* a financial-statement
definition.

### 5.4 No record rule anywhere · `VERIFIED FACT`, bounded negative

| Route | Result |
|---|---|
| XML `ir.rule` records referencing `model_account_report` or `account.model_account_report` | **0 across all six roots** |
| Python-created `ir.rule` naming `account.report` | **0**. The only textual hits are a *comment* in `account_reports/models/account_return.py:833` |

The four XML sites that *do* reference `model_account_report` are **a cron, two server actions and
their two bindings** — no rule among them. This reproduces `J-11`'s enumeration exactly.

> **Contrast that settles it.** The same security file `account/security/account_security.xml`
> contains ~25 company rules, including `report_external_value_comp_rule` on
> **`account.report.external.value`** (line 313–315). **The sibling model in the same file is
> company-scoped. `account.report` is not.** The absence is a divergence inside one module, not an
> oversight of the whole security layer.

### 5.5 The two bound server actions — **claim partially corrected**

| Action | File | `group_ids` | What its code actually does |
|---|---|---|---|
| `action_create_report_menu` | `account_reports/data/account_report_actions.xml:133` | **none declared** | calls `records._create_menu_item_for_report()` |
| `action_create_composite_report` | `account_reports/views/account_report_view.xml:371` | **`account.group_account_user`** | calls `records.action_create_composite_report()` |

**Correction 1 — `FC-C1`.** `J-11` describes these as *"carrying arbitrary server-side code"*. The
shipped `code` bodies are **two single named-method calls**, not caller-supplied code. The "arbitrary"
property belongs to the `ir.actions.server` model's **own** ACL, not to `account.report`. The wording
overstates; the finding does not depend on it.

**Correction 2 — `FC-C2`.** `action_create_composite_report` is granted to the ordinary accounting-user
role, but its body (`account_report.py:7417`) only **returns an `act_window` with a default context**.
It creates nothing. The subsequent create is ACL-gated, and `group_account_user` holds no create right
on `account.report`. **The ordinary-user grant is therefore not itself an escalation.** `J-11`'s
severity on this point is overstated.

**Amplification — `FC-A1`, and it is worse than the claim.** `_create_menu_item_for_report`
(`account_report.py:242–262`) creates an `ir.actions.client` **and an `ir.ui.menu`** parented to
`account.menu_finance_reports`. Verified this round: **`ir.ui.menu` has no company field and no record
rule** — its only visibility control is `group_ids`. So a report menu created by one company's
accounting manager is **visible to every user holding the group, in every company in the database.**

---

## 6. The six tests the instruction requires

| Test | Result |
|---|---|
| **Exact claim** | §2 — stated verbatim, tested element by element |
| **Exact source evidence** | §5 — file, line and content for every element; six roots |
| **Tenant / company scope** | The model has **no** company dimension, so there is **no** tenant scope to be conditional on. A shared-database, multi-company deployment shares one `account.report` population |
| **Reproducibility** | **Reproduced independently this round** from primary source, on a declared pattern, across six roots, and **cross-version stable** on v18 and v19 |
| **Failure path** | Accounting manager of company A → opens *Accounting Reports* → edits or deletes the Balance Sheet / P&L definition, **or** adds a menu item → the change is applied to the **single shared definition** and the menu is **globally visible**. No record rule intervenes at any step |
| **Accounting consequence** | The **structure** of the statutory financial statements of every company in the database is a **shared, unversioned, manager-writable object**. A deleted or re-formulated line changes what every company reports, retroactively, with no journal trace |
| **Control consequence** | **Defence in depth is absent, not weak.** Three layers — field, rule, ACL — and the first two do not exist while the third grants full CRUD. There is no second barrier to fail back to |
| **Tolerance classification** | **`T0-04` tenant isolation** — the boundary the class already occupies. Also touches `T0-09` declared-but-inert control, because `filter_multi_company` **reads** to a reviewer as a company control and is not one |
| **Contradiction history** | Carried as `medium open unknown` → recovered to `GATING` by the parent round's routing-abuse test → merged with `MCU-11` as a two-member class → third member found (`J-10`, Thai VAT export) → `MCC_D` held it `REMAINS GATING` on a tenant-question ground → `MCC_J` `J-11` rejected that ground → `MCC_00` closed it. **This file is the first re-verification from source rather than from a prior register.** |

---

## 7. The disposition question that actually mattered

`MCC_D` held `MCU-04` open because it is *"a tenant question"*. That ground **fails**, and the reason
is precise:

> A tenant question is one whose **answer** depends on how tenants are mapped to companies.
> `MCU-04`'s **mechanism** — no field, no rule, full manager CRUD, global menu — is **fully determined
> by source and is invariant under every tenant mapping.** Only the *blast radius* varies.
>
> An unknown is closed when its **mechanism** is determined. `MCU-04`'s mechanism is determined.
> **What remains is not an unknown; it is a design decision about an established defect** — and that
> decision belongs to `GB-01`, where it is already carried.

Holding a determined mechanism open as an unknown *because its consequence is policy-dependent* is the
mirror image of the routing abuse the programme forbids: it keeps a closable item open and inflates the
unknown count, exactly as routing a blocker forward deflates it.

---

## 8. Final disposition

> # `VERIFIED DEFECT`

Scope of the closure, stated so it cannot be over-read:

| Closed | Not closed |
|---|---|
| **`MCU-04`** — the `account.report` mechanism | **`MCU-11`** — the caller-supplied company parameter on the client-callable conversion endpoint. **Different mechanism. Remains `GATING — HOLD`.** The merge of the two into one class was an aggregation of *symptom*, not of mechanism |
| The mechanism, cross-version, on six roots | The **tenant-mapping decision** about it — carried in `GB-01`, unchanged |
| — | **`T0-04`** — the tolerance-zero boundary is **UNRESOLVED**. Closing the unknown does not resolve the boundary |

**Why the disposition changed from `REMAINS GATING — HOLD`:** not because new evidence appeared, but
because the **ground** for holding it was tested and failed. The mechanism was already fully evidenced
in `MCC_J`; `MCC_D` declined to close it on a criterion — *"it is a tenant question"* — that this file
shows does not apply. The change is a **correction of a disposition rule**, not a change of fact.

**Lineage preserved:** `MCC_D` §2 (`REMAINS GATING`) and `MCC_J` `J-11` (`closable`) both stand in
their original wording per `DR-NC-06`. This file supersedes neither text; it supplies the
re-verification that `MCC_00`'s closure was asserted without.

---

## 9. Arithmetic consequence — and a defect in the governing register

Closing `MCU-04` changes the closure count. Recomputed from `MCC_D` §3 and `MCC_00` §2:

| Step | Ids | Running total closed |
|---|---|---|
| `MCC_D` §3 closures | `MCU-05`, `MCU-06`, `MCU-07`, `MCU-08`, `MCU-09`, `MCU-10`, `MCU-13`, `MCU-14` | **8** |
| `MCC_00` §2 closes `MCU-15` | `MCU-15` | **9** |
| `MCC_00` §2 closes `MCU-04` | `MCU-04` | **10** |

`MCC_00` §1 publishes **`9`** closed and **`9 of 17 (52.9%)`**.

> # `FC-F1` — the canonical figures register is internally inconsistent.
>
> **`MCC_00` §2 closes ten ids. `MCC_00` §1 counts nine.** The two sections of the single file that
> exists to make figures consistent disagree by one, and the id they disagree about is `MCU-04`.
>
> **This is `GB-06` again, and it is now three deep:** the correction channel failed in the round that
> specified it (`J-16`), the mechanism built to stop that (`MCC_00`) failed on its own first use, and
> **neither failure was detected by the round that shipped them.**
>
> Correct value on the evidence: **10 of 17 closed (58.8%), 7 inherited unknowns remaining.**
> `MCC_00` governs by rule and this file does not overwrite it. **The register requires a Boss-visible
> correction; it is carried as an open item in the Final Gate Report.**

---

## 10. Bound on this file's negative claims — quantified

After this file's searches were run, a mechanical root discovery (declared pattern: every directory
containing `addons/base/models/res_currency.py`) returned **22 reference core roots** on the evidence
volume. **This file searched 6 of them.**

| Measure | Value |
|---|---|
| Reference core roots discovered | **22** |
| Roots searched by this file | **6** |
| Roots **not** searched | **16** |

**What this does and does not do to the disposition.**

| Element | Affected? |
|---|---|
| `account.report` has no `company_id` | **No.** Verified in the model's own definition, and cross-version stable on v18 and v19. A root cannot remove a field |
| Manager ACL is `1,1,1,1` | **No.** Verified identically in four separate copies across three roots |
| No `_inherit` extension adds a company field | **Bounded to 6 roots.** An unsearched root could contain one — though it would have to be *installed* to matter |
| **No record rule targets the model anywhere** | **BOUNDED TO 6 ROOTS, and this is the load-bearing negative.** A record rule in one of the 16 unsearched roots is **not excluded** |

**Disposition impact: none.** The defect is established by the **presence** of a full-CRUD ACL on a
model with **no company field of its own** — two positive facts. The record-rule negative *widens* the
finding; it is not what creates it. A record rule found later in an unsearched root would reduce the
blast radius of `MCU-04`, not overturn `VERIFIED DEFECT`.

**Recorded as a residual:** `FC-R1` — *complete the record-rule negative over the remaining 16 roots.*
Class `C — NOT YET SEARCHED`, boundary declared. Cheap and mechanical.

---

> ### NEGATIVE-CLAIM NOTICE
> Two negative claims are made here — "no extension adds a company field" and "no record rule targets
> the model anywhere". **Both are class `A` (bounded, complete enumeration over a declared pattern and
> a declared path set), not class `E` (no evidence found).** Their bound is the six roots in §4, out of **22** that exist — quantified in §10. A
> record rule created at runtime by a database administrator, or in a module outside those six roots,
> is **outside the bound and is not excluded by this file.**
