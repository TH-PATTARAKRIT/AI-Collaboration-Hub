# P03 DEPLOYED-CODE IDENTITY DELTA

**LAYER 2 — AUDIT QUARANTINE.** `MD-01`, `MD-02`, `MD-04`, `MD-05`. The most consequential
file of this closure.

---

## 1. The defect

> **For four rounds P03 read series-18 source and reported it as the behaviour of a
> series-16 deployment.**

| Evidence | Value |
|---|---|
| P03's declared source root, rounds 1–4 | `/Volumes/iMacSys/CLAUDE AI/SMEsPlus18/odoo-18.0+e.20250608/odoo/addons` |
| The deployment carrying 9,807 MOs, 74,982 valuation rows, 447,384 GL lines | **`iSMEs`** |
| Its actual series — `ir_module_module.latest_version` | `base` **16.0.1.3** · `mrp` **16.0.2.0** · `mrp_account` **16.0.1.0** · `stock_account` **16.0.1.1** · `purchase_stock` **16.0.1.2** · `purchase_mrp` **16.0.1.0** |
| Series-16 source in P03's path set | **NONE** |

**P03 did not check the deployed version before reading source, in any of four rounds.** The
rule that would have caught it — `smeplus-version-basis-defect-rule` — was on file from P09's
identical failure.

## 2. The declared path set, now stated properly

| Root | Series present |
|---|---|
| `/Volumes/iMacSys` | 18, 19 |
| **`/Volumes/iMac`** — *a second mounted volume with its own `/Users/admin`, never declared in rounds 1–4* | 18, 19 |
| `/Volumes/ChatGPT Installer` | probed, none |
| `$HOME` excluding `~/Library` | 18, 19 |

**Positive control:** the probe (`-type d -name purchase_mrp`) fires **28 times**. It is a
working instrument returning a real zero for series 16.

**Instrument failure recorded:** an attempt to discriminate series by manifest `'version'`
returned `'1.0'` for **every** located copy. The manifest does not carry the series; the
server stamps it into `ir_module_module`. The instrument is reported as failed rather than
as a result (`MD-05`).

## 3. Version-sensitivity of P03's load-bearing findings

Measured across the two series available on this host. **Series 16 is older than both;
nothing here proves behaviour at 16.**

| Finding | Series 18 | Series 19 | Classification |
|---|---|---|---|
| **`DC-04`** standard-cost capitalisation skipped while relief posts | present | **FIXED** — v19 sets `price_unit = standard_price` and returns early | **VERSION-SPECIFIC, ≤18** |
| **`DC-07`** relief credits the product's expense/COGS account by default | `wo.workcenter_id.expense_account_id or product_accounts['expense']` | **byte-identical** | **STABLE 18–19** |
| **`DC-09`** relief dated `fields.Date.context_today` | present | **byte-identical** | **STABLE 18–19** |
| **`DC-03`** `extra_cost` capitalised, never relieved | present | still capitalised; **counterpart account changed** to the production location's valuation account | **CHANGED — re-derivation required** |
| `_cal_price` consumed-cost source | `−Σ stock_valuation_layer_ids.value` | `Σ move.value`, **not negated** | **CHANGED** |
| `_post_labour` entry gate | `valuation != 'real_time'` | **plus** `or not production_location.valuation_account_id` | **CHANGED — an extra guard** |
| `_post_labour` counterpart account | `move_finished_ids[0]._get_src_account(...)` | `production_location.valuation_account_id` | **CHANGED** |

**Both load-bearing files differ between 18 and 19.** The functions are demonstrably
version-sensitive, which is precisely why a v18 reading cannot be projected onto a v16
deployment.

## 4. What survives, and on what basis

| Class | Findings | Basis |
|---|---|---|
| **Stable across the two observable series** | `DC-07`, `DC-09` | Byte-identical in 18 and 19. **Evidence, not proof, of stability at 16** |
| **Version-specific to ≤18** | `DC-04` | Already dispositioned `UNREACHABLE` in round 4 on configuration grounds; now also **fixed upstream** |
| **Changed between observable series** | `DC-03`, and the `_cal_price` / `_post_labour` internals | **Cannot be asserted of the deployment** |
| **Version-independent** | The runtime measurements — 9,807 MOs, 0 work centres, 30 corrupt valuation rows, 25/25 GL mismatch, 0 of 60 company-less work centres | **Read from the databases themselves.** Unaffected by MD-01 |

> **The single most important consequence.** P03's **runtime** findings stand entirely.
> P03's **source** findings are bounded to the series they were read in and must not be
> stated as behaviour of the `iSMEs` deployment.

## 5. Corroboration that the chain shape is version-stable

`MD-03` found series 18's `_get_stock_valuation_layers` participants to be **exactly the
three P01 found in series 16** — `stock_account` (base), `stock_landed_costs`, `purchase_mrp`.

Two independent sessions, two series, the same three participants. **That is the strongest
version-stability evidence in the package** — and it holds for a chain in which no
manufacturing module participates at all.

By contrast, **series 19 has zero participants**: `purchase_mrp/models/account_move.py` does
not exist there. The mechanism is 16-and-18 behaviour that was removed by 19.

## 6. Disposition

> **`UNRESOLVED — SPECIFIC EVIDENCE UNAVAILABLE`** for the source-basis of P03's
> deployment-facing claims.

Not repairable by more searching: the evidence needed is a series-16 addons tree, and none
exists in a declared path set that has been enumerated with a working positive control.
Converting this into a hunt would breach §9's clamp.

**What P03 does instead:** every source claim in the package is re-labelled with the series
it was read in, and the four runtime claims — which do not depend on source — are marked as
unaffected. `P03_CLOSURE_QUESTION_REGISTER.md` carries the per-CQ effect.

**Routed:** `MD-06` — P01 read a series-16 core at a path that does not resolve here. P03
does not adjudicate it; if that root can be remounted, MD-01 becomes closable.
