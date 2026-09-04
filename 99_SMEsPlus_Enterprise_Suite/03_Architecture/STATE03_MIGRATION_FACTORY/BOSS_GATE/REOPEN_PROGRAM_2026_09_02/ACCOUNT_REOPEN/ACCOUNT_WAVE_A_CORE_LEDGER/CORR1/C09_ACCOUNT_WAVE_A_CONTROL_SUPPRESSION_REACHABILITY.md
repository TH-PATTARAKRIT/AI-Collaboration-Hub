# C09 — CONTROL-SUPPRESSION REACHABILITY — `GAP-C04` CLOSED

Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-CORR1-001` · Layer 2 / audit quarantine

> The parent package named `GAP-C04` — whether the control-suppression context flags are reachable
> from an external interface — as **"the single most valuable open test in the programme"**, and
> classified it as requiring an executed test rather than source reading.
>
> This session establishes the answer **from the dispatch layer's source**, which the parent had not
> examined. An executed confirmation is still recommended, and the classification below is stated
> with that limit attached.

---

## 1. The question

Six named context flags disable accounting controls in the reference model:

| Flag | Control it disables | Parent ref |
|---|---|---|
| `check_move_validity` | **the debit = credit invariant** | `COR-07` / `SF-02` |
| `skip_readonly_check` | the posted-entry field freeze | `COR-15` |
| `force_delete` | deletion protection on a posted entry | `EV-011` |
| `skip_account_deprecation_check` | the block on posting to a retired account | `COR-03` |
| `defer_account_code_checks` | account code uniqueness | `EV-002` / `COR-05` |
| `skip_matching_number_check` | matching-number validation | `COR-09` context |

The parent could not determine whether these are an **internal engineering convenience** — reachable
only from server-side code — or an **externally reachable control bypass**. The distinction changes
the severity of four findings.

---

## 2. The dispatch chain, traced

**`VERIFIED FACT`** — three links, all read this session.

### Link 1 — the HTTP endpoint

`addons/web/controllers/dataset.py:33-36` — the route `/web/dataset/call_kw` is declared
`type='json'`, `auth="user"`. It resolves the model, calls `get_public_method(Model, method)` as a
gate, and then hands the **client-supplied `kwargs` verbatim** to `call_kw`.

An equivalent path exists at `:38-45` for `/web/dataset/call_button`.

### Link 2 — the method gate

`service/model.py:28-45` — `get_public_method` refuses a method **only** when its name begins with an
underscore, or when it carries the private-API marker. It performs **no inspection of arguments and
no inspection of context whatsoever.**

Therefore `create`, `write`, `unlink`, `action_post`, `button_draft` and every other public method
remain remotely callable. Only internals such as `_post` are refused.

### Link 3 — context application

`api.py:512-535` — `call_kw` performs:

```
kwargs  = dict(kwargs)
context = kwargs.pop('context', None) or {}
recs    = recs.with_context(context)
```

**There is no allowlist, no denylist, no key validation, no type check and no filtering of any kind.**
The dictionary the client sent becomes the environment context for the call.

---

## 3. Result

> **`VERIFIED FACT`** — the framework's remote-call dispatch applies a client-supplied context
> dictionary to the ORM call **without filtering**, gated only by the method name not being private.
>
> **`INFERENCE`** — therefore any authenticated user who can call `write` on an entry can call it
> with `context = {'check_move_validity': False}`, and the debit = credit invariant is not enforced
> for that call. The same reasoning applies to the other five flags.

The inference is short and the chain is fully read, but it **is** an inference: this session did not
execute the call. Per the negative-claim standard's discipline on evidence classes, it is not promoted
to a verified fact.

**Classification of `GAP-C04`: substantially closed. `VERIFIED FACT` as to unfiltered context
dispatch; `INFERENCE` as to end-to-end exploitability. An executed test remains recommended and is
now cheap — it is a single call.**

---

## 4. Consequences

### `SF-02` severity — **ESCALATED**

The parent's own words were that this "changes the severity of four findings" and that it decides
"whether the suppression pattern is an internal engineering convenience or an externally reachable
control bypass". On the evidence above, it is the second.

| Finding | Parent severity | Revised |
|---|---|---|
| `SF-02` entry balance invariant suppressible | severe, reachability unknown | **severe, and reachable by any authenticated user with write access to entries** |
| `COR-15` posted freeze bypass | owned by the calling module | **also settable by the caller over RPC** |
| `EV-011` deletion protection bypass | a context flag used internally | **also settable over RPC** |
| `COR-03` deprecated-account block | two of three guards have a bypass | **those two are externally suppressible; the item-write guard at `account_move_line.py:1550-1552` has no bypass and remains effective** |

### The architectural point

This is not a defect unique to the accounting module. It is a property of the **framework's**
call convention: context is an open channel from client to ORM, and the accounting module chose to
express control decisions as context keys travelling on that channel.

`INFERENCE:` the two choices are individually defensible and jointly unsound. An open context channel
is reasonable for presentation concerns — language, active company, display preferences. Expressing
**accounting invariants** on the same channel means the client can address them.

### SMEsPlus requirement — reinforces `ST-28`

`ST-28` already classified control suppression by caller-supplied flags as `REJECT` as a pattern.
This evidence raises it from a design-hygiene objection to a **security and integrity requirement**:

> An accounting invariant must not be expressible as a request parameter. Where a legitimate need
> exists to defer a check during multi-step construction, the deferral must be **server-side,
> scoped to a transaction, and must re-assert the invariant before commit** — never a flag the caller
> supplies.

`RECOMMENDATION:` this strengthens the case for proposed `Tolerance = 0` candidate `T0-01`, and adds
a fourth blocker-class consideration for the gate.

---

## 5. Residual limits of this finding

| # | Limit | Class |
|---|---|---|
| `RCH-01` | No call was executed; end-to-end exploitability is inferred from the read chain | `INFERENCE` — executed test recommended |
| `RCH-02` | Whether record rules or field-level access would independently refuse the write for a given user was not assessed | `NOT YET SEARCHED` |
| `RCH-03` | Whether any deployment-layer proxy filters context keys | `NOT YET SEARCHED` |
| `RCH-04` | Whether other transport paths (scheduled actions, external APIs, import) apply the same convention | `NOT YET SEARCHED` |

`RCH-02` matters and is named explicitly: an authenticated user still needs write access to the
entry. The finding is that **a user who may legitimately write an entry may also, on the same call,
switch off the invariant that makes it an accounting entry** — not that an unauthorised user gains
access.
