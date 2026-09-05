# P06_PAYMENT_TOKEN_SCOPE_REVALIDATION.md

**Session:** P06 Bank-to-Reconcile — TARGETED CONTINUATION (CP-C10)
**Classification:** LAYER 2 — AUDIT QUARANTINE
**Subject:** `P06-B-28` / contradiction `C-11` / attack `A4c` — the payment-token scope contradiction raised by CORR1.
**Governing constraint from the prompt:** *"Do not resolve by simply adding Company everywhere."*

---

## 1. Why this finding is being revalidated

`C-11` was **produced by** the CORR1 correction — it was invisible under the superseded "tenant and company everywhere" wording, because that wording collapses the ownership/availability distinction that makes it visible. A finding created by a correction deserves a harder look than one that merely survived it.

---

## 2. The six scopes of a payment token

Per CORR1 §4, determined from business semantics first and then tested against source.

| Scope question | Determination | Basis |
|---|---|---|
| **Ownership** — whose object is it? | **COMPANY**, derived | `$V18E/payment/models/payment_token.py:17-19` — `company_id = fields.Many2one(related='provider_id.company_id', store=True, index=True)` |
| **Operational** — who executes with it? | **COMPANY** | a transaction using it is company-scoped and derives its own `company_id` from the same provider |
| **Financial** — who owns the money effect? | **COMPANY** | the settlement lands in one company's bank journal |
| **Reference** — who may point at it? | **the owning COMPANY only** | a payment instrument is not shared reference data |
| **Access** — who may see it? | **wider than the owner** | `$V18E/payment/security/payment_security.xml:31-35` — `[('company_id', 'parent_of', company_ids)]` |
| **Mutation** — who may change it? | not separately constrained | no distinct write rule found in that file |

**PTS-F-01 — Access scope exceeds ownership scope, and the same file proves the narrower rule was available.**
Token rule (`:31-35`): `parent_of`. Transaction rule, immediately above it (`:14-18`): `[('company_id', 'in', company_ids)]`.
**Two rules, two boundaries, one file.** The narrower form was not merely possible — it is used ten lines earlier for the object that *records* what the token did.

**PTS-F-02 — `parent_of` is an ancestor test, and it admits an unowned record.**
The ORM contract (`/Volumes/iMacSys/CLAUDE AI/SMEsPlus18/odoo-18.0+e.20250608/odoo/models.py:188-194`) documents the analogous domain helper as permitting a record whose `company_id` is **`False`** *or* a **parent** of the given companies. Applied to a credential-bearing object, a token owned by an ancestor company is visible to every descendant.

**PTS-F-03 — And for validation operations the search widens again, past the provider.**
`$V18E/payment/models/payment_token.py:137-143`, with its own in-code comment:
```
# Get all the tokens of the partner and of their commercial partner, regardless of
[('partner_id', 'in', [partner.id, partner.commercial_partner_id.id])]
```
The commercial-partner rollup is a **partner-hierarchy** widening on top of the **company-hierarchy** widening of PTS-F-01.

---

## 3. Is the finding correct? — the adversarial test

The obligation here is to try to *break* the finding, not to confirm it.

**Counter-argument 1: "`parent_of` is deliberate — a parent company administering its branches' payment methods is a legitimate operating model."**
**Assessed: partially valid, and it does not rescue the finding's target.** A shared administration model may justify a wider *administrative* view. It does not justify the **same** rule governing *use*. The file draws no distinction between seeing a token and transacting with it, and no separate rule for either was found — PATTERN `payment_token` over `$V18E/payment/security/payment_security.xml`: the token rule at `:31-35` is the only company rule for that model. **The contradiction survives, but its correct statement is narrower:** *one rule governs both visibility and usability, where two different scopes are required.*

**Counter-argument 2: "Ownership is enforced elsewhere — `_check_company_auto = True` at `:13`, and the transaction's token domain is restricted to the same provider (`payment_transaction.py:57`)."**
**Assessed: valid, and it materially reduces the impact.** A transaction cannot use a token from a different provider, and the provider carries the company. So the realistic exposure is **not** "company B charges company A's saved card" but **"company B can see, and select in a UI, an instrument it does not own."**
**The finding is therefore downgraded in severity: HIGH → MEDIUM.** Recorded as a downgrade rather than defended, because that is what the evidence supports.

**Counter-argument 3: "`company_id` is stored and indexed, so this is a record-rule choice, not a model defect."**
**Assessed: valid, and it changes the classification, not the existence.** This is a **configuration-level** scope defect, not a structural one. It is cheap to fix in the reference and cheap to get wrong in the target — which is exactly why it belongs in the handoff.

---

## 4. Revalidation record (CORR1 §6 shape)

| Field | Content |
|---|---|
| **Original finding** | C-11 / `P06-B-28`: a payment token is visible to a wider scope than the transactions made with it. Severity HIGH. |
| **Old scope assumption** | pre-CORR1: tenant+company mandatory everywhere, which collapsed ownership into availability and hid the finding entirely. |
| **Ownership scope** | COMPANY (derived from provider) |
| **Operational scope** | COMPANY |
| **Financial scope** | COMPANY |
| **Reference scope** | owning COMPANY only |
| **Access scope** | **ancestor chain — wider than ownership** |
| **Corrected finding** | **One record rule governs both visibility and usability of a credential-bearing object, at a boundary wider than the object's owner. The realistic exposure is cross-company visibility and selection, not cross-company charging** — provider binding blocks the latter. |
| **Evidence** | `payment_token.py:13,17-19,137-143`; `payment_security.xml:14-18,31-35`; `payment_transaction.py:36-38,57`; ORM `models.py:188-194` |
| **Updated classification** | **CONFIRMED DEFECT, severity MEDIUM** (downgraded from HIGH) |
| **Architecture impact** | availability may never exceed ownership; visibility and usability need separate scopes for credential-bearing objects |
| **Cross-process impact** | P02 (customer receipts via saved instruments); P07 if provider data carries tax-relevant identifiers |
| **Evidence still required** | none for the finding. Whether any deployment uses a company hierarchy with providers is data — but the rule is defective independent of that. |

---

## 5. What the target must do — without "adding Company everywhere"

The prompt's constraint is the right one, and the correct answer is **not** to bolt a company filter onto the existing rule.

| Requirement | Rationale |
|---|---|
| **PTS-R-01** | Split the scope: an **access** scope for administration and a **usability** scope for transacting. They are different questions and must not share a rule. |
| **PTS-R-02** | Usability is **COMPANY**, and it is the owning company — not an ancestor, not a descendant. |
| **PTS-R-03** | A credential-bearing object may not be admitted by a hierarchy test, and may never be admitted on a null owner. |
| **PTS-R-04** | The partner-hierarchy widening for validation (PTS-F-03) must be an explicit, separately-authorised path, not a silent widening of the same search. |
| **PTS-R-05** | Ownership must be **asserted**, not derived through two hops (`token → provider → company`). A derived owner cannot be independently verified. |

**PTS-R-05 is the general lesson.** The token's company is real, stored and indexed — but it is a `related` field two hops from the object. The same pattern appears in `res.partner.bank.company_id` (`related='partner_id.company_id'`, attack A4b) where it produces a worse outcome: an owner that can be empty. **Derived ownership is the shared root cause of both A4b and A4c**, and that connection was not visible until this revalidation. Raised as **`P06-B-47`**.

---

## 6. Status

| Item | Prior | New |
|---|---|---|
| `P06-B-28` | open, HIGH | **CLOSED — SOURCE EVIDENCE VERIFIED**, as a finding; severity **MEDIUM**; requirement carried to handoff |
| C-11 | Type I contradiction, HIGH | **retained, severity MEDIUM** |
| Attack A4c | CONFIRMED DEFECT | **retained, severity MEDIUM**, exposure restated as visibility/selection |
| `P06-B-47` | — | **NEW** — derived ownership as the common root of A4b and A4c |

---

# End
