# 14 — ASSET MODEL FUNCTION FORENSIC
**LAYER 2 — AUDIT QUARANTINE**

Answers §22 in full.

## 1. What an Asset Model actually is

**The same model, with `state = 'model'`.** Not a separate entity, not a separate
table, not a separate set of fields. `FACT VERIFIED`

Consequences, all confirmed from source:

- A model carries every field a live asset carries, including value fields that
  have no meaning on a template.
- A model can be created **from an account's configuration screen**, and when it is,
  the fixed-asset account field is hidden — the account is implied by where you
  created it.
- A live asset can be **saved back as a model** by an action on the form.
- Models are excluded from asset lists by domain, not by type.

## 2. Fields a model governs

| Field | Copied to the asset? | Notes |
|---|---|---|
| Method | Yes | |
| Duration (number of periods) | Yes | |
| Period length (1 or 12 months) | Yes | |
| Declining factor | Yes | |
| **Computation mode** (prorata type) | Yes | The critical one — `16` §3 |
| Prorata date | **No** | Recomputed from the asset's own acquisition date |
| Fixed asset account | Yes | |
| Depreciation account | Yes | |
| Expense account | Yes | |
| Journal | Yes | |
| Analytic distribution | Yes, **as a default only** | Overwritten if the source bill carries its own — §4 |
| **Not-depreciable percentage** | Yes, **as a rule** | See §3 — this one behaves differently |
| Model properties definition | Yes, as the definition for the asset's properties | |
| Original value, salvage amount, dates | **No** | |

## 3. The salvage percentage is the one live rule

Every other model field is a one-time copy. The not-depreciable **percentage** is
different: the asset's salvage amount is a **computed field that depends on the
model's percentage and the asset's own original value**.

```
salvage_value = original_value × model.salvage_value_pct        (when the pct is non-zero)
```

So changing the original value on an asset that has a model re-derives its salvage
amount. This is the only place where the model exerts continuing influence.

`FACT VERIFIED`

## 4. Analytic: the model loses to the bill

The model supplies an analytic distribution as a default. But the asset's
distribution is **computed from its source bill lines** and only falls back to the
existing value when the bill supplies none.

**Where an asset is auto-created from a vendor bill — the primary route — the
bill's analytic distribution wins over the model's.** `FACT VERIFIED`

## 5. What happens if the model changes after the asset was created — §22 core question

**Nothing.** `FACT VERIFIED`, and independently corroborated by runtime evidence.

- Historical schedule: unchanged.
- Future schedule: unchanged.
- Existing journal entries: unchanged.
- The asset's own field values: unchanged.

The only exception is the salvage percentage rule in §3, and that fires on a
recompute of the asset's own value, not on a change to the model.

There is **no re-apply action, no propagate-to-assets function, and no warning**
that assets created from a model have diverged from it.

### Runtime corroboration — and a surprise

`EV-RT` shows something stronger than "models do not propagate":

> **All 280 real assets on the UAT have no model linked at all.**
> `byModel: {"false": 280}`

Combined with the project's own migration handoff, which states *"Before this step,
current C1 assets have model_id unset"* and defines a 16-model controlled list as
the target, the picture is unambiguous: the models exist as a **standardisation
target for a migration step**, and at the time of capture no live asset was linked
to one.

So on this deployment the Asset Model is not, today, a configuration mechanism at
all. Whatever governs the 280 assets' depreciation is on the asset rows themselves.

**This is the direct route to `UNR-02`.** The question "which computation mode are
the 217 running assets using?" cannot be answered by inspecting the 16 models. It
must be read off the assets.

## 6. Can an asset override its model?

Yes, freely and silently, on every field. There is no lock, no warning and no
divergence report. `FACT VERIFIED` — `FAIL-X02`.

## 7. What this means for SMEsPlus

1. **A template that stops governing after creation is a weak control.** If SMEsPlus
   wants asset classes to mean something, the class must either keep governing or
   the divergence must be reported. The reference product does neither.
2. **The account triple is the real classification.** The runtime shows six distinct
   account triples in use across 280 assets, and 16 templates governing none of
   them. The accounts, not the template, are what actually differentiates the
   population.
3. **Do not model "Asset Model" as an entity** without deciding first whether it is a
   template (copy once) or a policy (keeps governing). The reference product says
   template, and its own users' behaviour — 280 assets, zero links — suggests even
   that is not being used.
