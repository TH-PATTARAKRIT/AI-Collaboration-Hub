# 02 — P04 ASSET LIFECYCLE MAP

Layer: **2 — audit quarantine**. Classification vocabulary per `00_README_LAYER_AND_METHOD.md`.

The governing prompt names 17 lifecycle stages. Each is mapped below to what the
reference estate actually provides, and to which SMEsPlus process owns it.

---

## 1. The lifecycle as the estate implements it

```
 P01  Purchase requisition ─┐
 P01  Purchase order        │   NO ASSET CONSEQUENCE
 P01  Goods receipt        ─┘   (three-way match, valuation entry — no asset)
                    │
                    ▼
 P01  VENDOR BILL  ── posted ──►  ★ THE ONLY AUTOMATIC CAPITALIZATION TRIGGER ★
                    │                 (account-level flag decides)
                    ▼
 P04  ASSET RECORD  (draft)
                    │  confirm
                    ▼
 P04  ASSET RECORD  (running) ──► depreciation schedule generated and posted
                    │
     ┌──────────────┼───────────────┬──────────────┬─────────────┐
     ▼              ▼               ▼              ▼             ▼
  pause /        modify /        increase /     cancel        (transfer)
  resume         re-evaluate     child asset                   ABSENT
     │              │               │              │
     └──────────────┴───────────────┴──────────────┘
                    │
                    ▼
 P04  CLOSED  ◄── sell ── or ── dispose ──►  derecognition entry LEFT IN DRAFT
                    │
                    ▼
              archive (only from closed)
```

## 2. Stage-by-stage map

| # | Stage named in the prompt | Present in the estate? | Owning process | Class |
|---|---------------------------|------------------------|----------------|-------|
| 1 | **Purchase** | Yes, but with **no asset consequence whatsoever** | P01 | FACT VERIFIED |
| 2 | **Receipt / Vendor Bill** | Receipt: no asset consequence. **Vendor bill: the sole automatic trigger** | P01 → P04 | FACT VERIFIED |
| 3 | **Capitalization decision** | **ABSENT as a decision.** Nothing in the estate distinguishes a repair from an improvement. The decision is pre-committed once, per account, by an accountant configuring a flag — never per transaction, never per item | **unowned** | FACT VERIFIED |
| 4 | **Asset creation** | Yes — one automatic path, three manual, one system-generated (revaluation child), one import | P04 | FACT VERIFIED |
| 5 | **Asset model** | Yes, but it **governs nothing after creation**; on the live population it governs nothing at all (280 assets, zero models attached) | P04 | FACT VERIFIED |
| 6 | **Depreciation** | Yes — deeply covered by prior packages, imported not re-derived | P04 / P10 | PRIOR EVIDENCE |
| 7 | **Analytic / cost allocation** | Yes at the asset level; **broken at the revaluation-child level** (P04-F-07) | P09 | FACT VERIFIED |
| 8 | **Equipment relationship** | Custom link only; three of four intended behaviours inert | P04 / P03 | PRIOR EVIDENCE, re-verified this session |
| 9 | **Production relationship** | Exists via work-centre rate and analytic distribution — **two live mechanisms** | P03 | PRIOR EVIDENCE |
| 10 | **Transfer** | **ABSENT.** Not found under the asset module using case-insensitive `transfer`. No state, no field, no wizard action | **unowned** | FACT VERIFIED (scoped negative) |
| 11 | **Modification** | Yes — one wizard covering duration, rate, value and pause/resume | P04 | FACT VERIFIED |
| 12 | **Revaluation** | Upward → child asset. Downward → a single entry posted to **depreciation expense**. **No revaluation surplus, no other-comprehensive-income treatment** | P04 | FACT VERIFIED |
| 13 | **Impairment** | **ABSENT.** Not found under the asset module using case-insensitive `impair`. The nearest behaviour records an impairment as accelerated depreciation | **unowned** | FACT VERIFIED (scoped negative) |
| 14 | **Sale** | Yes. Requires a **posted customer invoice** whose lines supply the proceeds | P02 → P04 | FACT VERIFIED |
| 15 | **Disposal** | Yes — the same path as sale, with no proceeds lines | P04 | FACT VERIFIED |
| 16 | **Scrap** | **ABSENT as an asset event.** Not found under the asset module using case-insensitive `scrap`. Scrapping must be recorded as a disposal | **unowned** | FACT VERIFIED (scoped negative) |
| 17 | **Derecognition** | **Not a distinct event.** Derecognition *is* the disposal entry — and that entry is **created in draft and never posted by the system** | P04 → P08 | FACT VERIFIED |

## 3. The six lifecycle states, and the transitions that do not exist

**States (6):** model · draft · running · on-hold · closed · cancelled.
Plus an orthogonal archive flag.

**Transitions that were tested for and not found**, under the asset module using
the state-comparison pattern declared in `13_P04_SOURCE_LINK_REGISTER.md`:

| Missing transition | Consequence |
|--------------------|-------------|
| closed → cancelled | A wrongly closed asset cannot be cancelled; it must be re-opened first |
| on-hold → cancelled | The cancel control is visible only in the running state |
| cancelled → running | Recovery from cancellation is possible only via draft, and the draft control is gated on there being **no** depreciation entries — which cancellation satisfies only if the entries were unlinked rather than reversed |
| model → draft | A model cannot become a real asset |
| **any → transferred** | No such state — see stage 10 |
| **any → under construction / not yet in service** | No such state. This is the assets-under-construction gap; it was named in a prior fit/gap register and has never been designed |

## 3A. Two arcs this map originally omitted

Added after independent challenge.

| Arc | Behaviour | Consequence |
|-----|-----------|-------------|
| **Any operation → the pending-entry clearing routine → deletion** | The routine that clears pending entries before pause, re-evaluation, re-opening and disposal filters *draft* **or** *(posted and dated after the operation date)*. **The draft branch carries no date test.** Every pending entry on the asset is removed whatever its date | The draft derecognition entry left by a disposal is **silently deleted** by any of those later operations. `P04-B-40` |
| **Any state → archive, via cancellation of the source document** | Cancelling the source accounting document attempts to archive **every** asset created from its lines, with no state filter, while the archive guard raises unless the asset is closed or a model | Every automatically created asset is draft or running, so **the guard always raises**. The arc drawn in §1 as "archive (only from closed)" is the *guard's* rule; this arc is the *attempt*, and the two disagree. Corrected in `03` `EV-23` |

A third interaction is registered but not traced: re-evaluating an asset that
already carries gross-increase children writes method and period to those
children unconditionally and re-posts their schedules. The interaction with an
existing child's own schedule is **untested in the estate and unresolved here**.
Registered `P04-B-42`.

## 4. What P04 owns that is not in the estate at all

These are lifecycle stages the SMEsPlus design must originate rather than adapt.
None is a configuration gap; each requires new behaviour.

| Stage | Why it cannot be configured | Registered as |
|-------|----------------------------|---------------|
| Capitalization-vs-expense decision, with a threshold policy | There is no decision point; the flag is on the account, evaluated per posted line | P04-B-06 |
| Assets under construction / capitalization stage | No state exists between "does not exist" and "draft asset with a full cost" | P04-B-07 |
| Acquisition cost composition (freight, installation, import duty, non-recoverable input VAT, testing, dismantling provision) | The cost is taken as the bill line balance. Nothing assembles a cost from several documents | P04-B-08 |
| Transfer | No state, no field, no action | P04-B-09 |
| Impairment (TAS 36) | No concept anywhere | P04-B-10 |
| Revaluation model accounting (surplus in equity, transfer to retained earnings on derecognition) | Downward revaluation posts to depreciation expense; no equity component exists | P04-B-11 |
| Asset scrap as an event distinct from disposal | Not found; and the Thai evidence requirement differs between the two — see `07` §5 | P04-B-12 |
| Tax book / tax written-down value | Named in a prior package as "the largest single functional gap for a Thai deployment" and then **dropped from every later register** — see `08` §5 | P04-B-13 |
| Asset numbering, tagging and physical verification | Not covered by any package and not found in the estate | P04-B-14 |
| Component depreciation | Required by the TAS 16 explanatory manual; the estate has no component concept and a single-valued asset-to-machine link | P04-B-15 |

## 5. The structural statement this map produces

> Buying a machine creates **two** records, by two people, from two documents —
> an accounting asset from the vendor bill, and an operational equipment record
> from the goods receipt. **The estate joins them nowhere in standard code**, and
> the project's own custom join is three-quarters inert.

That statement was reached by a prior package. This session re-verified the
custom join's import chain directly and confirms it: the module's package
initialiser imports only its model package, so the wizard override that would
retire the equipment when its asset is sold **is present and not live**. Of the
module's eight model files, five are imported; three are not.

Consequence for P04: **retiring an asset does not retire its equipment.** The
operational register and the accounting register diverge silently at the retire
end, exactly as they diverge at the acquire end.
