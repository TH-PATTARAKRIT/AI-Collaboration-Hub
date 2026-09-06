# P04 — FOUR AAS-03 INDEPENDENT CHALLENGES (G01 CLOSURE)

**LAYER 2 — AUDIT QUARANTINE.** Prompt §9, Constitution §10.
**Challenge output is evidence pressure, not a verdict.** Dissent is preserved.

---

## C-1 · Leader Functional Design

**Supported.** Asset lifecycle `draft→open→(paused)→close` is coherent and dated. Disposal
distinguishes *sold* from *disposed*. The end-of-life clamp is correct — the board cannot
overshoot the residual.

**Missing.** No lifecycle event for *"fully depreciated but still in use"*, which is the exact
state the Boss policy is about. No release of the equipment on disposal.

**Risky.** `DF-02`'s mixture — ten snapshot fields and one live field on the same object — will
be read by an accountant as one behaviour. **Whichever design is chosen, the current mixture
must not survive into SMEsPlus by default.**

**Challenged — and this challenge succeeded.** *"The Asset Model supplies policy only in a
form"* was the headline of `CQ-P04-01`. **It was false.** `_auto_create_asset` calls
`_onchange_model_id` explicitly. The finding was withdrawn and reissued as *"policy is an
action three call sites perform, not a property of the record"* — a narrower claim that
survives. **This is the most consequential conclusion of the closure and it was disproved by
its own author's mandated disproof pass, not by a reviewer.**

**Evidence needed next.** Whether any *deployed* custom module creates assets programmatically
with `model_id` — that turns `P04-F-145`'s failure mode from latent to live. Bounded and
registered as **`P04-B-55`**; **not** run here, because it needs the runtime population and
this run's surface is source.

## C-2 · Leadership Database Design

**Supported.** Per-identity version keying is applied throughout; runtime and source claims are
separated (`MD-P04-01`).

**Missing.** **Cardinality on `name_asset`.** No unique index, no constraint, no `@api.constrains`.
Several assets may reference one equipment, and no rule apportions between them.

**Risky.** `write()` addresses depreciation lines **positionally** — `move.line_ids[::2]` — on
the assumption that every even-indexed line is the depreciation-account line. **Any entry that
is not exactly two lines in that order silently re-accounts the wrong line.** Not proven to
occur; recorded as a structural risk with the code cited.

**Challenged.** *"The analytic route nets to zero."* Attempted disproof: the distribution is
written by one statement to `move.line_ids` — **all** of them. The claim **survives**, and now
has its source cause (`P04-F-153`) rather than only a measurement.

**Evidence needed next.** A runtime count of equipment referenced by more than one asset —
**`P04-B-53`**, registered, not measured here.

## C-3 · Lead Integration & Localization

**Supported.** The P03 boundary is consumed and not re-researched; `CQ-P04-07` attributes every
manufacturing-side claim. Statutory questions are routed to P07 without inference.

**Missing.** The record-rule half of the company-scope question. Field domains were examined;
`ir.rule` was not.

**Risky.** **`P04-F-156`** — `model_id` carries a company domain and `name_asset` carries none,
in the same custom module. Publishing that as a cross-company hole on field evidence alone
would repeat a mistake this package has already made twice. **Registered as `P04-B-54`, stated
as a question.**

**Challenged.** *"The estate runs `daily_computation`."* Attempted disproof by generation: the
claim rests on `iSMEs` (**v16**) and `idemo18_uat` (**v18**) — two generations, two independent
populations, same result. **Survives**, and the source implementation traced is **v18 only**;
the v16 implementation is unobtainable (`MD-P04-01`).

**Evidence needed next.** P07's statutory position on day convention. **P07-owned; not P04's to
close.**

## C-4 · Lead Code & UI Architect

**Supported.** Module identity is established from the installed set, not from manifests — the
manifest of `account_asset` reads `'version': '1.3'`, which **independently corroborates P03's
`MD-05`**: the manifest does not carry the series.

**Missing.** Reachability of `name_asset` in the UI. The field exists on the model; whether the
inherited view exposes it in every relevant form was **not** verified.

**Risky.** Three of eight model files in `equipment_sequence` are never imported, and one of the
three inherits a model that does not exist. **A maintainer reading the directory sees an
asset↔equipment design that is not the one running.** The dead file is also the one whose name
(`om_asset_asset`) suggests it is the real one.

**Challenged — this challenge also succeeded.** *"`equipment_sequence` cannot install."* That
was the natural reading of an `_inherit` on an undefined model. **Disproved by the installed
set:** it is recorded installed at `18.0.1.6`. The resolution — the file is never imported —
is what produced `P04-F-148`. **`Source present ≠ installed` was not enough here; the needed
rule was `source present ≠ registered`.**

**Evidence needed next.** Whether the view actually renders `name_asset`, and whether
`name_get`'s removal leaves a visibly degraded label. Both are UI-reachability questions,
**bounded**, and neither changes an accounting conclusion — **Class E, recorded, not opened.**

---

## Convergence

| Challenge | Outcome |
|---|---|
| C-1 | **Author's headline disproved and reissued narrower** |
| C-2 | Analytic net-to-zero **survives**, now with source cause; one structural risk recorded |
| C-3 | Day-convention usage **survives** two generations; one boundary downgraded to a question |
| C-4 | *"Cannot install"* **disproved** by the installed set; produced `P04-F-148` |

**Two of four challenges falsified a claim this run had already written down.** Both were
author-side overstatements, and both were caught by the mandated disproof rather than by
re-reading.
