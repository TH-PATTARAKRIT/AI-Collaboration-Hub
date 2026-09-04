# G05 — B-05 TARGETED CLOSURE — DOES AN APPROVAL ENGINE EXIST, AND IS IT BYPASSABLE?

Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-GAPCLOSE-001` · Layer 2 / audit quarantine
Prior classification: `NOT PROVEN`

---

## 1. Original claim

Raised by fresh Reviewer B (`N10`): a generic approval engine exists which patches public methods,
special-cases the journal-entry model by name, and is **skipped under privilege elevation** — which
would contradict the parent finding that no maker-checker exists, and would interact with `GAP-C04`.

## 2. Exact search scope

Module listing of `addons/` for approval-related modules; then
`addons/approvals/models/`, and `addons/web_studio/models/studio_approval.py` in full for the
relevant methods. Method: targeted grep plus direct read. Other modules not searched — stated per
`DR-NC-02`.

## 3. Source evidence

### 3.1 Two distinct mechanisms exist, and only one is relevant

| Module | Nature | Relevant? |
|---|---|---|
| `approvals` (plus `approvals_purchase`, `approvals_purchase_stock`, `documents_approvals`) | a **standalone** approval-request workflow with its own model | **No** — it does not gate journal-entry posting. No reference to the journal-entry model found in its models or data |
| `web_studio` — `models/studio_approval.py` | a **generic engine that patches methods on arbitrary models** | **Yes** |

### 3.2 The engine — `VERIFIED FACT`

`web_studio/models/studio_approval.py:378-393` — `_register_hook` defines
`_patch(model, method_name, function)`, which replaces a method on the model class via `setattr`,
preserving the original as `studio_approval_rule_origin`. Applied at `:459`.

**Its own guards:**
- `:383-384` — private methods cannot be patched;
- `:385-386` — **`create`, `write` and `unlink` cannot be patched.**

### 3.3 The journal entry is special-cased by name — `VERIFIED FACT`

`web_studio/models/studio_approval.py:267-268`:
```
if model_name == "account.move":
    state_field = self.env["ir.model.fields"]._get("account.move", "state")
```

### 3.4 The elevation bypass — `VERIFIED FACT`, and self-documented

`web_studio/models/studio_approval.py:395-404`, inside the patched wrapper:
```
if self.env.su:
    # in a sudoed environment, approvals are skipped
    # otherwise we risk breaking some important flows
    # (e.g. ecommerce order confirmations, invoice posting because
    # online payment succeeeded, etc.)
    _logger.info("Skipping approval checks in a sudoed environment: ...")
    return method.studio_approval_rule_origin(self, *args, **kwargs)
```

> The bypass is deliberate, documented, and its own comment **names invoice posting** as a reason it
> exists. The skip is written to the application log, **not** to an accounting record.

## 4. Analysis

**The reviewer's claim is correct in all three particulars.** But its consequence for the parent
finding is narrower than "maker-checker exists":

| Property | Finding |
|---|---|
| Is it part of the accounting module? | **No.** It is a Studio customisation facility |
| Does it ship configured for accounting? | **No evidence found** that any rule is shipped — `B — NOT FOUND IN SEARCHED SCOPE` |
| Can it gate posting? | **Yes** — `action_post` is public and patchable |
| Can it gate the underlying write? | **No** — `create`, `write` and `unlink` are explicitly excluded |
| Is it bypassable? | **Yes**, under any elevated-privilege execution, silently as far as the ledger is concerned |

### Interaction with `GAP-C04` / `C09`

`C09` established that the remote-call dispatch applies a client-supplied context to the ORM
unfiltered. The two findings compose:

- an approval rule can gate `action_post`;
- it cannot gate `write`;
- and control-suppression context keys ride on the same unfiltered channel.

`INFERENCE:` an approval control implemented at this layer constrains the **button**, not the
**fact**. That is the substantive point for SMEsPlus, and it holds whether or not the elevation
bypass is ever exercised.

## 5. Final narrow claim

> A generic approval engine exists in `addons/web_studio`. It patches public methods on arbitrary
> models, explicitly cannot patch `create`, `write` or `unlink`, special-cases the journal-entry model
> by name for its state field, and **skips all approval checks under elevated privilege**, logging
> the skip to the application log. No shipped approval rule for accounting was found in the searched
> scope. It is a user-configurable customisation facility, not an accounting control.

## 6. Disposition

> ## `VERIFIED` — the engine exists and is bypassable
> ## The parent finding stands, **rescoped**

**Parent claim, corrected wording:**

> "No approval step distinct from the posting permission was found **in `addons/account`**. A generic,
> user-configurable approval engine exists in `addons/web_studio` which can gate the posting action;
> it cannot gate the underlying write, and it is skipped under elevated privilege."

This replaces the parent's `NC-15` wording and closes it as **`E — CONTRADICTED` at domain scope,
`A — VERIFIED ABSENCE` within `addons/account`**.

## 7. SMEsPlus position

**`EXTEND`, and the requirement is sharpened by this evidence:**

1. Authorisation to create an accounting fact belongs to the **fact**, not to a UI action, so it
   cannot be circumvented by writing rather than posting.
2. It must not be suppressible by execution context. Where automated flows must post without human
   approval — the reference's stated reason for the bypass — that is a **named automated actor with
   its own authority**, recorded on the event, not an absence of control.
3. Every bypass must produce an **accounting record**, inside the tenant's data.

## 8. Residual

| # | Item | Class |
|---|---|---|
| `B05-R1` | Whether any shipped data or localization configures an approval rule for accounting | `B — NOT FOUND IN SEARCHED SCOPE` |
| `B05-R2` | Whether `web_studio` is present in the intended SMEsPlus reference baseline | `C — NOT YET SEARCHED` |
| `B05-R3` | Whether other elevation paths reach `action_post` in normal operation | `C — NOT YET SEARCHED` |
