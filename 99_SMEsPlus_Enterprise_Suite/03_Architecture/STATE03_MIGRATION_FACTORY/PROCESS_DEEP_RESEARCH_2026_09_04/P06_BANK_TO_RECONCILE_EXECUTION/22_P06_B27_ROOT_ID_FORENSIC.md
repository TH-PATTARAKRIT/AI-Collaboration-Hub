# P06_B27_ROOT_ID_FORENSIC.md

**Session:** P06 Bank-to-Reconcile — TARGETED CONTINUATION
**Blocker:** `P06-B-27` — **CLOSED — SOURCE EVIDENCE VERIFIED**
**Classification:** LAYER 2 — AUDIT QUARANTINE
**Evidence root `$V18E`:** `/Volumes/iMacSys/CLAUDE AI/SMEsPlus18/odoo-18.0+e.20250608/odoo/addons`

---

## 1. The authoritative blocker wording

Retrieved verbatim from `19_P06_SCOPE_OWNERSHIP_MATRIX.md` (SCOPE-F-04) and `17_P06_PMO.md` §6, not from memory:

> *"Does `root_id` denote one legal entity or several?"* — **HOLD — SCOPE EVIDENCE REQUIRED**, gating attack A4a, requirement RM-R-10 and SCOPE-R-02.

The prior round could not answer it and correctly refused to guess. This continuation answers it from the model definition itself.

---

## 2. What `root_id` actually is

**B27-F-01 — `root_id` is a computed, non-stored field derived from the materialised ancestor path.**
`$V18E/base/models/res_company.py:36-42`:
```
parent_id = fields.Many2one('res.company', string='Parent Company', index=True, ondelete='restrict')
child_ids = fields.One2many('res.company', 'parent_id', string='Branches')
parent_path = fields.Char(index=True)
parent_ids = fields.Many2many('res.company', compute='_compute_parent_ids', compute_sudo=True)
root_id = fields.Many2one('res.company', compute='_compute_parent_ids', compute_sudo=True)
```
`:114-118`:
```
@api.depends('parent_path')
def _compute_parent_ids(self):
    company.parent_ids = self.browse(int(id) for id in company.parent_path.split('/') if id) if company.parent_path else company
    company.root_id = company.parent_ids[0]
```
So `root_id` is simply **the topmost ancestor in the `parent_id` chain**. It is not stored, not indexed, and carries no semantics of its own beyond "top of this tree".
**Classification: FACT VERIFIED.**

**B27-F-02 — The relation's own label is "Branches", not "Subsidiaries".**
`$V18E/base/models/res_company.py:38` — `child_ids = fields.One2many('res.company', 'parent_id', string='Branches')`.
**This is a label, and a label is not evidence of semantics.** Per §3.3 of the governing constitution a UI label may not be converted into FACT VERIFIED. It is recorded as **SUPPORTED INTERPRETATION of intent only**, and the decisive test is what the model *constrains*, which follows.

---

## 3. The decisive test — what the model forces to be identical

If `root_id` denoted one legal entity, the model would force the attributes of legal identity to be shared. It does not.

**B27-F-03 — Exactly five fields are delegated from root to branch and constrained equal.**
`$V18E/base/models/res_company.py:95-103`:
```
def _get_company_root_delegated_field_names(self):
    """Get the set of fields delegated to the root company.
    Some fields need to be identical on all branches of the company...
    return ['currency_id']
```
extended once, by accounting — `$V18E/account/models/company.py:281-287`:
```
def _get_company_root_delegated_field_names(self):
    return super()._get_company_root_delegated_field_names() + [
        'fiscalyear_last_day',
        'fiscalyear_last_month',
        'account_storno',
        'tax_exigibility',
    ]
```
Enforced by `$V18E/base/models/res_company.py:416-424`:
```
@api.constrains(lambda self: self._get_company_root_delegated_field_names() +['parent_id'])
def _check_root_delegated_fields(self):
    if company.parent_id:
        if company[fname] != company.parent_id[fname]:
            raise ValidationError(_("The %s of a subsidiary must be the same as it's root company.", description))
```
and propagated downward on write (`:379-387`).

**DENOMINATOR:** POPULATION: all definitions and extensions of `_get_company_root_delegated_field_names` in `$V18E`. PATTERN: that method name, `--include="*.py"`. UNIT: definition site. **RESULT: 9 occurrences, of which 2 are definitions** (base and account) and 7 are call sites. **The delegated set is therefore exactly 5 fields: `currency_id`, `fiscalyear_last_day`, `fiscalyear_last_month`, `account_storno`, `tax_exigibility`.**
**Classification: FACT VERIFIED.**

**B27-F-04 — Tax ID and company registration number are NOT delegated, and nothing constrains them to match.**
`$V18E/base/models/res_company.py:71-72`:
```
vat = fields.Char(related='partner_id.vat', string="Tax ID", readonly=False)
company_registry = fields.Char(related='partner_id.company_registry', string="Company ID", readonly=False)
```
Both are ordinary writable related fields. Neither appears in the delegated set (B27-F-03). PATTERN `vat` over `$V18E/base/models/res_company.py`: 3 hits — a mixin declaration at `:21`, the field at `:71`, and a create-vals copy at `:298`. **No constraint requiring a branch's `vat` to equal its parent's was found.**
**Class A within the declared scope** of `$V18E/base/models/res_company.py` and `$V18E/account/models/company.py`.
`country_id` is likewise not delegated (`:64`, computed from the address).

**B27-F-05 — Lock dates are not delegated either; they are inherited, and the strictest ancestor wins.**
`$V18E/account/models/company.py:397-401`:
```
def _compute_user_hard_lock_date(self):
    company.user_hard_lock_date = max(
        ...
        for c in company.with_context(active_test=False).sudo().parent_ids
```
and `:530-540` — `_get_user_lock_date` iterates `self.sudo().parent_ids`, its docstring stating: *"We consider the field and exceptions … for it in this company and the parent companies."*
So a parent's lock date binds every branch beneath it, and the **maximum** across the ancestor chain applies.
**Classification: FACT VERIFIED.**

---

## 4. Conclusion — the answer to B-27

**B27-CONCLUSION — `root_id` denotes a FISCAL AND CURRENCY HIERARCHY. It does not denote one legal entity, and it cannot be relied upon as a legal-entity boundary.**

What the hierarchy guarantees is shared **accounting calendar and currency**: one currency, one fiscal year end, one storno convention, one tax-exigibility basis, and a cascading period lock.
What it does **not** guarantee is shared **legal identity**: two companies under the same `root_id` may hold **different Tax IDs, different company registration numbers and different countries**, because none of those is delegated or constrained.

**Therefore, neither reading offered by the blocker is correct as stated.** `root_id` is not "one legal entity" and it is not "several legal entities" — **it is a boundary of a different kind entirely**, and the model permits either legal arrangement beneath it.

**Classification: FACT VERIFIED** (from the delegated-field set, its constraint, and the absence of any VAT constraint). **This conclusion is independent of deployment data** — it is a statement about what the model is capable of enforcing, not about how any database is configured.

---

## 5. What this settles, and what it does not

**Settles:** the guard at `$V18E/account/models/account_move_line.py:2336-2340` —
```
if len(self.company_id.root_id) > 1:
    raise UserError(_("Entries don't belong to the same company: %s",
```
— **is structurally incapable of enforcing a legal-entity boundary.** It tests a fiscal hierarchy. Whatever legal arrangement sits beneath a root, the guard permits reconciliation across all of it. Its own error message says *"don't belong to the same company"*, which is **not what it tests**: this is a Type II contradiction between the code and its own user-facing text, newly raised as **C-29**.

**Does not settle:** whether any *particular* SMEsPlus deployment places distinct legal entities under one root. That remains a data question — but it is now a **materially smaller** question, because the control is defective regardless of the answer. If all branches under a root happen to be one legal entity today, the guard still cannot prevent tomorrow's configuration from breaking that assumption.

**The prior HOLD is therefore lifted, and A4a's downgrade is reversed** — see §6 and the dependency closure graph.

---

## 6. Cross-references

| Item | Prior status | New status |
|---|---|---|
| `P06-B-27` | HOLD — SCOPE EVIDENCE REQUIRED | **CLOSED — SOURCE EVIDENCE VERIFIED** |
| Attack A4a | HOLD — SCOPE EVIDENCE REQUIRED | **CONFIRMED DEFECT** (control cannot enforce the boundary it names) |
| RM-R-10 | conditional, restated as SCOPE-R-02 | **REINSTATED, with a corrected rationale** |
| SCOPE-R-02 | "declare the boundary once" | **strengthened** — see the dependency graph |
| SCOPE-F-04 | contradiction, defect severity HOLD | **defect severity restored to HIGH** |
| C-13 | Type I contradiction, defect classification HOLD | **defect classification restored** |
| C-29 | — | **newly raised** — the guard's message names a boundary it does not test |

---

## 7. Scope determination for `res.company` hierarchy objects (CORR1)

| Object | Ownership | Operational | Financial | Reference | Verdict |
|---|---|---|---|---|---|
| `res.company` | COMPANY | COMPANY | COMPANY | TENANT | the legal/accounting boundary |
| `parent_id` / `root_id` hierarchy | TENANT | TENANT | — | TENANT | **a tenant-level grouping of companies, not itself a financial boundary** |
| Delegated set (currency, fiscal year, storno, tax exigibility) | TENANT-propagated, COMPANY-applied | COMPANY | COMPANY | — | shared calendar, applied per company |
| Lock dates | COMPANY, inherited from ancestors | COMPANY | COMPANY | — | strictest ancestor wins |
| `vat` / `company_registry` | **COMPANY, unconstrained by the hierarchy** | COMPANY | COMPANY | — | legal identity is per-company |

**Reading:** the hierarchy is a **TENANT-scoped grouping**; the legal and financial boundary remains **COMPANY**. This is precisely the CORR1 distinction — ownership scope ≠ operational scope ≠ financial scope — and it is why a guard written at the grouping level cannot protect a boundary that lives one level down.

---

# End
