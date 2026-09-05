# P06_OM_DATA_REMOVE_FORENSIC.md

**Session:** P06 Bank-to-Reconcile — **SUPPLEMENTAL CRITICAL-RISK CLOSURE** (CP-P06S03)
**Prompt:** `[SMEPLUS-26-09-05-ACC-P06-B2R-CRITICAL-RISK-SUPPLEMENT-001]`
**Baseline:** `ebf24a05dba5e9cad6b611b42b561cf46a96bfb8`
**Classification:** LAYER 2 — AUDIT QUARANTINE
**Method:** the whole module was read **first-hand by this session**, not delegated. 368 lines of `models/model.py`, the manifest, both `__init__.py`, and `views/view.xml` in full.

> **NO DESTRUCTIVE PATH WAS EXECUTED.** Nothing in this file was obtained by running the module. All findings are source and call-graph analysis.

---

## 1. Module identity, verified per copy

**DENOMINATOR:** POPULATION: the four declared custom roots. PATTERN: existence of `<root>/om_data_remove/__manifest__.py`. UNIT: copy. **RESULT: present in 4 of 4.** The prior round's claim is **CONFIRMED**.

| Copy | Manifest version | `model.py` lines | `__pycache__` |
|---|---|---|---|
| CUST18 (`smeplus-custom`) | `1.0.0` | 368 | `cpython-313` |
| T8MASTER | `1.0.0` | 368 | none |
| CUST14 | `1.0.0` | 430 | `cpython-37`, `cpython-38` |
| MIGR18 (`18.0.4_smeplus_v2`) | **`18.0.1.1`** | **387** | `cpython-310` |

**OMD-F-01 — There are THREE DISTINCT VARIANTS across the four examined copies.** *(Narrowed by AAS-03 E4-S-03: two of the four ARE byte-identical; the earlier wording "the four copies are NOT identical" overstated it.)*
`20_` Appendix A implied one behaviour across all four. In fact:
- **CUST18 ≡ T8MASTER** — byte-identical `model.py` (`diff -q` reports no difference).
- **MIGR18 differs**: 387 lines, version `18.0.1.1`.
- **CUST14 differs**: 430 lines, adds `remove_assets`, and **raises `ValidationError` where the v18 copies swallow the exception**.

**OMD-F-02 — The MIGR18 copy has been locally customised for THIS project, and that is the most important fact about it.**
`$MIGR18/om_data_remove/models/model.py:178-190` adds, inside `remove_account`:
```
# Unlink related withholding tax certificates first (for account.payment)
payments = self.env['account.payment'].search([('company_id', '=', self.env.company.id)])
for payment in payments:
    withholding_tax_cert = self.env['withholding.tax.cert'].search([('payment_id', '=', payment.id)])
    withholding_tax_cert.unlink()  # Unlink or delete related withholding tax certs
```
`withholding.tax.cert` is a **Thai localisation model** from the project's own custom estate (`l10n_th_withholding_tax_cert`). **A third party's generic database-cleanup module has been edited to handle this project's Thai withholding-tax certificates.**
**Classification: FACT VERIFIED.** Someone in this programme opened this module, understood it, and extended it for the Thai deployment. That removes any reading in which the module is incidental vendor baggage nobody touched.
And note the shape of the edit: the WHT-certificate cleanup **is** company-filtered (`self.env.company.id`), while the deletes it precedes are not.

**OMD-F-03 — The vendor is a third party, and the licence is LGPL-3.**
`__manifest__.py`: `'author': 'Odoo Mates, Sunpop.cn'`, `'category': 'Tools'`, `'license': 'LGPL-3'`, `'depends': ['base']`, `'data': ['views/view.xml']`.
**`data` lists exactly one file. There is no security file in the manifest.**

---

## 2. The destructive primitive

`$CUST18/om_data_remove/models/model.py:7-40` — the whole engine:
```
class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    def remove_data(self, o, s=[]):
        for line in o:
            ...
            obj = self.pool.get(obj_name)
            if not obj:
                t_name = obj_name.replace('.', '_')
            else:
                t_name = obj._table
            sql = "delete from %s" % t_name
            try:
                self._cr.execute(sql)
                self._cr.commit()
            except Exception as e:
                _logger.warning('remove data error: %s,%s', line, e)
```

**OMD-F-04 — `delete from <table>` with no `WHERE` clause. FACT VERIFIED.**
No company predicate. No date predicate. No state predicate. No lock-date consultation. No ORM. The table name is derived from the model name, falling back to `model_name.replace('.', '_')` when the model is not in the registry.

**OMD-F-05 — Each delete is committed immediately, so a partial run is durable.**
`self._cr.commit()` inside the loop. A failure on table *n* leaves tables 1…*n−1* **committed and unrecoverable by rollback**.

**OMD-F-06 — Every exception is swallowed to a WARNING in the v18 copies.**
`except Exception as e: _logger.warning(...)`. **The CUST14 copy instead raises `ValidationError`** (`$CUST14/.../model.py:33,44`). So the older copy fails loudly and the newer ones fail silently — a regression in the direction that matters.

**OMD-F-07 — The sequence reset is a separate mechanism and IS `sudo()`-ed.**
Same method, `:29-38`:
```
seqs = self.env['ir.sequence'].sudo().search(domain)
if seqs.exists():
    seqs.write({'number_next': 1})
```
`.sudo()` here **defeats the `ir.sequence` ACL** for the generic path.

---

## 3. Method inventory

**DENOMINATOR:** POPULATION: `def` statements at class level in `$CUST18/om_data_remove/models/model.py`. PATTERN: `^    def `. UNIT: method. **RESULT: 19 methods + 1 class.**

| Line | Method | Financial? |
|---|---|---|
| 10 | `remove_data` | the primitive |
| 42 | `remove_sales` | partly |
| 52 | `remove_product` | no |
| 62 | `remove_product_attribute` | no |
| 70 | `remove_pos` | partly |
| 89 | `remove_purchase` | partly |
| 101 | `remove_expense` | partly |
| 113 | `remove_mrp` | no |
| 131 | `remove_mrp_bom` | no |
| 139 | `remove_inventory` | partly |
| **165** | **`remove_account`** | **YES** |
| **199** | **`remove_account_chart`** | **YES** |
| 276 | `remove_project` | no |
| 286 | `remove_quality` | no |
| 297 | `remove_quality_setting` | no |
| 308 | `remove_website` | no |
| **325** | **`remove_message`** | **audit trail** |
| **334** | **`remove_all`** | **calls 13 of the above** |
| 350 | `reset_cat_loc_name` | no |

---

## 4. What `remove_account` actually deletes — corrected list

`$CUST18/om_data_remove/models/model.py:165-177`:
```
'payment.transaction', 'account.bank.statement.line', 'account.payment',
'account.analytic.line', 'account.analytic.account', 'account.partial.reconcile',
'account.move.line', 'hr.expense.sheet', 'account.move',
```
**Nine models.** Note what this list contains that the prior round did not name: **`account.analytic.line` and `account.analytic.account`** — which is P09's entire domain — and **`hr.expense.sheet`**, which is P05's.

`remove_account_chart` (`:199-215`) deletes a further eleven, including **`account.bank.statement`**, **`res.partner.bank`**, **`account.journal`** and **`account.account`**.

**OMD-F-08 — `account.full.reconcile` is NOT in either list.**
PATTERN `full.reconcile` over the whole file: no hit. Its consequence is examined in the destructive-data-path graph — deleting `account_partial_reconcile` rows by raw SQL leaves `account_full_reconcile` rows whose members no longer exist.

---

## 5. THE CORRECTION — scoping is mixed, not uniformly absent

**OMD-F-09 — The prior round overstated this, and the correction matters.**

`20_` Appendix A wrote: *"No `WHERE` clause. Therefore no company filter, no date filter, no state filter and no lock-date check."* That is true **of the table deletes**. It is **not** true of the whole method.

Three parts of `remove_account` and `remove_account_chart` **are** company-scoped:

1. **The sequence reset in `remove_account` carries a company predicate** — `:178-188`:
```
domain = [
    ('company_id', '=', self.env.company.id),
    '|', ('code', '=ilike', 'account.%'),
    '|', ('prefix', '=ilike', 'BNK1/%'),
    ...
```
2. **`remove_account_chart` sets a company context** — `:200`: `self = self.with_context(force_company=company_id, company_id=company_id)`.
3. **Two auxiliary SQL statements in `remove_account_chart` carry `company_id=%d`** — `:216-220`, on `ir_default` and `account_journal`.

**And the MIGR18 WHT-certificate cleanup is company-filtered too** (OMD-F-02).

**So the accurate statement is:** *the author of this module was aware of company scoping and applied it to the sequence reset, to two auxiliary updates and to the Thai WHT extension — and did not apply it to the table deletes themselves.*

**That is worse than uniform carelessness, not better.** It is a module whose author demonstrably understood multi-company scoping and left the destructive primitive unscoped. Recorded as a **correction to the prior round's wording** and as the sharpest available statement of the finding.

---

## 6. UI gating — exactly what exists

`$CUST18/om_data_remove/views/view.xml`:
- `:104-111` — `ir.actions.act_window` on `res_model = res.config.settings`, `target = inline`. **No `groups` field on the action.**
- `:113-119` — `menuitem … parent="base.menu_administration" sequence="1" groups="base.group_system"`.
- Every button is `type="object"` with a `confirm="…"` string, e.g. `:20`:
```
<button string="Delete All Transactions Except Master Data" type="object" name="remove_all" confirm="Please confirm to delete the data?" class="oe_highlight"/>
```

**OMD-F-10 — Both gates are client-side.**
A `groups=` attribute on a **menuitem** governs whether the menu is rendered. A `confirm=` attribute governs whether the web client shows a dialog before issuing the RPC. **Neither is consulted by the server when the method is invoked.** This is the `UI NOT VISIBLE` versus `SERVER-SIDE NOT AUTHORIZED` distinction the directive requires, and here it is decisive.

**OMD-F-11 — The `ir.actions.act_window` itself carries no group restriction**, so the action is resolvable by any user who can read `ir.actions.act_window`.

---

## 7. Cross-copy behavioural delta table

| Behaviour | CUST18 / T8 | CUST14 | MIGR18 |
|---|---|---|---|
| `delete from <table>` unfiltered | yes | yes | yes |
| commit inside the loop | yes | yes | yes |
| exception handling | **swallowed to WARNING** | **raises `ValidationError`** | swallowed |
| Thai WHT-cert cleanup | no | no | **yes, company-filtered** |
| `remove_assets` | no | **yes** | no |
| extra logging on sequence reset | no | no | **yes** |
| version string | `1.0.0` | `1.0.0` | **`18.0.1.1`** |

**OMD-F-12 — Version `1.0.0` on a module sitting in an Odoo-18 addons path is not a v18-conformant version string.** Only the MIGR18 copy carries a generation-prefixed version. This is the same defect class as `P06-B-39` (a module version-stamped without a migration) seen from the other direction: three copies are **not** version-stamped at all.

---

## 8. Classification

| Question | Classification |
|---|---|
| **OM_DATA_REMOVE destructive path** | **DESTRUCTIVE PATH VERIFIED** — `delete from <table>` with no `WHERE`, committed per table, on nine accounting models in `remove_account` and eleven more in `remove_account_chart` |
| Present in all four custom roots | **FACT VERIFIED** — 4 of 4 |
| Copies identical | **CONTRADICTED** — the prior round implied uniformity; CUST18 ≡ T8 only, MIGR18 and CUST14 differ |
| Locally customised for this project | **FACT VERIFIED** — MIGR18 handles `withholding.tax.cert` |
| Scoping uniformly absent | **CONTRADICTED** — deletes unscoped, sequence reset and two auxiliary updates company-scoped |
| Executed against any system by this session | **NO. Not attempted, not authorised, not required.** |

---

## 9. Open items

| ID | Item | Class |
|---|---|---|
| `P06-OQ-98` | Which of the four copies, if any, is on a deployed `addons_path`. **HOLD — DEPLOYMENT REGISTRY EVIDENCE REQUIRED** | D |
| `P06-OQ-99` | Whether `withholding.tax.cert` exists in the deployed estate (its presence in MIGR18's edit implies the editor believed it did) | D |
| `P06-OQ-100` | `__pycache__` presence proves the module was **imported** by a Python interpreter in three copies. Import is not installation. Timestamps are filesystem metadata, not audit evidence. | D |
