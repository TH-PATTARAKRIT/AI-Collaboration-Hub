# SA_CORR2_02 — BUSINESS NATURE ROUTING MATRIX (CORR2)
## CP-SA-C2-20 — DEMAND/SUPPLY ROUTING EVIDENCE COMPLETE OR BOUNDED

Session: `[SMEPLUS-26-09-08-PHASE-SA-CORR2-XMOD-001]`
Supersedes at claim level: `SA05` §3.1 status counts and the `SA05-F-01` root-cause statement.
**Scope of this register: the four `SA-D05`-dependent natures — BN-04, BN-05, BN-06, BN-07.** The
other four `HOLD` natures (BN-08, BN-10, BN-17, BN-18) are adjudicated in `SA_CORR2_03` §3 and
their statuses are set there, not here. *(Earlier drafts of §1, §4 and §5 variously said "six" and
"four"; corrected after adversarial challenge.)*
Does **not** supersede: `SA05` §2 (the routing principle) or `SA05` §2.2 (the alternatives),
which are re-verified and carried unchanged.
Evidence frame: `SA_CORR2_00` §2.

---

## 1. What changed, and why the change is large

`SA05` classified **7 of 18** business natures `HOLD` and attributed all seven to one root cause:
five `THIN` domains. `SA05-F-01` then asserted, untested, that *"closing SA-D05, D17, D18, D19 and
D20 closes all seven"* — a claim `SA20` §4 accepted as an uncorrected defect.

CORR2 tested the four `SA-D05`-dependent natures directly, in **both parties' path sets and both
parties' vocabularies**. The result is not marginal:

> **`C2-F-05`. Three of the four were not evidence gaps at all. They were reachability failures of
> the instrument that measured them.** The evidence existed, in the Account programme, under
> vocabulary the `SA-D05` token count could not carry.

`SA-D05`'s 81-blob figure is a real measurement of one **token set**. It was read as a measurement of
a **domain**. Those are different things, and the difference is four business natures.

---

## 2. Authoritative Business Natures — enumerated from evidence, not invented

Master prompt §4 requires the Business Natures to be enumerated from existing Phase SA evidence
rather than invented. `SA05` §3 defines eighteen (`BN-01`…`BN-18`). That enumeration is **adopted
unchanged**; no nature is added or removed by this round. Only the status of the four named above changes here; four more change in `SA_CORR2_03` §3.

---

## 3. Re-adjudicated natures

Legend for evidence class, used throughout and never conflated:
`DESIGN` = reference behaviour read at source · `DEPLOY` = counted in a deployed database ·
`TARGET` = SMEsPlus clean-room design text · `DECISION` = nobody has decided.

### 3.1 `BN-04` — RM shortage during manufacture → purchase

| Prior `SA05` ground | `HOLD` — *"the shortage→purchase trigger is a supply-routing decision; SA-D05 evidence is 81 blobs. Trigger, ownership and reservation interaction not evidenced."* |
|---|---|
| **What is actually evidenced** | **The trigger mechanism is `DESIGN`-determined.** Two independent, evidenced trigger paths converge on a **single dispatch choke point in the replenishment rule engine**, which selects a fulfilment action (buy / manufacture / pull / push) per demand. The manufacturing order **never raises the purchase itself** — the raiser is always the rule engine acting on a demand-or-forecast deficit. |
| | **Ownership is `FACT VERIFIED` in the accounting programme.** P03's cross-process ownership register assigns raw-material *purchase* cost to P01 and raw-material *consumption* valuation to the Inventory track; P03's business-event register `BE-01` puts the demand owner outside manufacturing entirely — *"Demand source (sales order, reorder rule, forecast)"*, `FACT VERIFIED`. |
| | **Reservation interaction is evidenced** — see `BN-06` below; it is the same chained-replenishment mechanism. |
| **Instrument note** | `shortage` returns **18 unique paths (U2)** corpus-wide and **0** in the P01/P02/P03 path set, with two positive controls firing in that same path set (`procurement` 10 paths, `raw.?material` 18 paths). **The accounting programme genuinely has no shortage vocabulary** — that is a real, controlled absence in that path set, and it is *why* `SA05` found nothing: it searched for the word, and the answer is filed under ownership and demand. |
| **New status** | **`PARTIAL`** |
| **Residual, restated on its true ground** | **`DECISION`, and it is a target-design decision, not research.** The SMEsPlus target fact-ownership matrix binds the fulfiller **softly** — *"Hard trigger, soft binding (Inventory does not know who will respond)"* — and the target manufacturing state machine's shortage state exits **only on reservation completing, never on procurement being raised.** A shortage can therefore be entered and never left by supply. Raised as `C2-D-01` |

### 3.2 `BN-05` — Dropship

Adjudicated in full at `SA_CORR2_01` §4. **New status `PARTIAL`.** Additions from this round:

- **The two generations answer oppositely, both `FACT VERIFIED`.** The prior generation had a
  purpose-built dropship valuation entry — two offsetting valuation layers, with the invoice adding
  a cost line and the two netting through an interim account. The current generation has **no cost
  entry anywhere in the sell-side leg**, excluded on three independent paths.
- **`DEPLOY`: dropship is not a live state in the measured estate** — the enabling module is not
  among the installed set, and the sell-side linkage columns are null on all 10,490 purchase lines,
  **with a positive control confirming the columns exist**. So the exposure is latent, not firing.
- **An undischarged peer handover.** The sell-side package formally routed to the buy-side package:
  *"Determine the account, the date, and whether anything links it to the originating sale."* No
  artefact discharging it was found in the declared path set. Raised as `C2-D-02`.

### 3.3 `BN-06` — Buy-to-order / MTO

| Prior `SA05` ground | `PARTIAL` — *"The order-to-purchase linkage and its reservation semantics are not [evidenced]."* |
|---|---|
| **Adjudication** | **FALSIFIED as a statement about the corpus.** A database-confirmed link from a purchase line to a sales line exists; the declaring capability was resolved **twice, independently**, by two different parties; reservation semantics are evidenced as a two-way link between the purchase line and the physical movement, plus a many-to-many carrying chained auto-created lines, backed at database level by a junction table with cascade delete; and the re-trigger site on confirmation was located, then **independently re-performed by a second party and reproduced "character-for-character"**. |
| **New status** | **`EVIDENCED — DESIGN; NOT LIVE`** |
| **Residual** | **`DEPLOY`: zero live rows.** The linkage is structurally present and measured empty. And **no accounting-programme package restates it** — the make-to-order vocabulary returns **0 paths** in the P01/P02/P03 path set with a firing control. The design is known; the accounting consequence of the linkage has never been written down by the party that owns accounting |

### 3.4 `BN-07` — Kit / bundle

| Prior `SA05` ground | `HOLD` — *"Component resolution point (order entry vs delivery), and whether the kit or its components carry the cost, are undetermined."* |
|---|---|
| **Half one — resolution point** | **DETERMINED, `DESIGN`.** A kit is a **structure-level flag, not a product classification**. When a sale line carries one, the fulfilment flow is redirected to create physical movements **for the components, not for the parent**, at rule-dispatch time on the sell side. **The parent never moves.** The prior wording — *"order entry vs delivery, undetermined"* — is wrong as stated. |
| | A second, distinct mechanism exists and must not be conflated with it: a **selector** construct that lets a customer choose one item per category and resolves to constituent products each carrying its own storability. `DEPLOY`: **0 of 83,753** product templates use it. |
| **Half two — which level carries cost** | **PARTLY DETERMINED, and the finding is worse than "undetermined".** For purchase price-difference correction, the filter that decides which valuation layers a bill line may correct **contains no kit predicate at all** — it compares the **bill line's own product**, unconditionally. Where the bill line's product differs from the ordering line's product, the layer set empties and **the correction is silently skipped**. |
| | `DEPLOY`, with controls: 14,335 bill lines carrying an order-line link (*positive control*); 14,312 product-matched; **23 mismatched; 18 valid posted; 13 where the filter actively drops at least one layer.** A synthetic injection control flips the measure 0 → 1, proving the predicate can fire. Independently carried in a second package with the same numbers. |
| **Reachability of the kit branch specifically** | **`DEPLOY`: unreachable in the measured estate.** Movements carrying both the structure-line fingerprint and a purchase-line link: **0**, against a positive control of **34,492** movements carrying the structure-line fingerprint. **No kit has ever been purchased in the deployment.** An earlier census that rested on a *mutable* structure-type field was **withdrawn as insufficient** by its own author and replaced by this fingerprint control — a correction CORR2 adopts rather than re-deriving |
| **New status** | **`PARTIAL`** |
| **Residual** | **`DECISION`** — the `SA05` product-category ambiguity survives intact and is the real open item: `BD-ACC-03A/03B` set valuation and costing at Product Category, **and a kit and its components may sit in different categories**, so a kit's costing policy is ambiguous by construction. Raised as `C2-D-03`. Plus one **evidence-lineage** item: a planned artefact on kit cost correction is named in a deliverables list and **is absent from the declared path set** (verified by filename listing — a different command shape from content search — with 93 sibling filenames enumerating normally) |

### 3.5 `BN-01`, `BN-02`, `BN-03` — carried, with one narrowing

Unchanged at `PARTIAL`. `BN-01`'s open element narrows: `SA_CORR2_01` §3 replaces *"cancellation-gate
symmetry open"* with **two decisions and one delivery**, plus the durability precondition `C2-F-01`.

### 3.6 `BN-08`, `BN-10`, `BN-17`, `BN-18` — held pending the functional-domain extraction

These four depend on `SA-D17` (Service), `SA-D18` (Project), `SA-D19` (Quality) and `SA-D20`
(Equipment/Maintenance). They are adjudicated in `SA_CORR2_03` §3 on the same discipline applied
above, and their statuses are set there.

---

## 4. Status summary — before and after

| Status | `SA05` (before) | CORR2 (after, for the six re-adjudicated) |
|---|---|---|
| `DETERMINED` / `EVIDENCED — DESIGN` | 0 | **1** — BN-06 |
| `PARTIAL` | 11 | **13** — the eleven **less BN-06**, which moves up, plus BN-04, BN-05, BN-07 |
| `HOLD` | 7 | **4** — BN-08, BN-10, BN-17, BN-18, pending `SA_CORR2_03` §3; see §3.6 |

1 + 13 + 4 = 18. *(**Corrected after adversarial challenge.** First published `1 / 14 / 3`: the
`HOLD` row **listed four identifiers and said three**, and `BN-06` was double-counted — left in
`PARTIAL` while also being promoted. Neither error changed the total, which is why both survived.)*

The final count is set in `SA_CORR2_03` §4 once the functional-domain extraction is adjudicated.
**It is not asserted here**, because asserting a total before its constituents are decided is how a
count becomes a claim nobody can audit.

---

## 5. `C2-F-06` — what `SA05-F-01` got wrong, and it matters for the research decision

`SA05-F-01` asserted **one root cause with seven symptoms**, and `SA16` consolidated six research
triggers into one programme on that basis. `SA19` Decision 4 asks Boss to authorize it.

**Tested. The single-root-cause claim is false for the four natures tested here.**

| Nature | Alleged root cause | Actual cause found |
|---|---|---|
| BN-04 | SA-D05 thin | **A target-design decision** — soft fulfiller binding, and a shortage state with no supply exit |
| BN-05 | SA-D05 thin | **A SMEsPlus determination**, plus an **undischarged peer handover**. Reference behaviour is `FACT VERIFIED` in two generations |
| BN-06 | SA-D05 thin | **Nothing — it was evidenced.** The instrument could not reach it |
| BN-07 | SA-D05 thin | **A Boss-ruling ambiguity** (`BD-ACC-03A/03B` at category level vs a kit spanning categories), plus a live, measured defect in an unrelated mechanism |

**Four different causes, of four different kinds, only one of which research can close.**

This is the consequence for Boss Decision 4, and it is favourable: **the consolidated research
programme is smaller than `SA16` scoped it.** Research is the right instrument for the domains that
are genuinely unstudied. It is the *wrong* instrument for BN-04 (decide), BN-05 (decide + chase a
handover), BN-06 (nothing to research), and half of BN-07 (a ruling to clarify).

`SA16`'s consolidation was reached honestly from the evidence available to it. It rested on a
count that was read as a domain measure, and it was never tested — `SA20` §4 recorded exactly that.
**Tested now, it does not hold.**

---

## 6. Decisions raised by this register

| ID | Decision | Authority | Why it is not research |
|---|---|---|---|
| `C2-D-01` | Does an SMEsPlus manufacturing shortage **raise supply**, and if so who is bound to answer it — a named fulfiller, or a soft-bound registry? | SMEs Core design position → Boss confirm | The reference mechanism is known. The target design deliberately left the binding soft; that is a choice to make, not a fact to find |
| `C2-D-02` | Where does dropship cost recognition land in SMEsPlus, and what identity binds it to the sale? | SMEs Core → Boss | Both reference generations are `FACT VERIFIED` and they disagree. Choosing between them is a determination |
| `C2-D-03` | When a kit and its components sit in different Product Categories, **which category's valuation and costing policy governs?** | **Boss** — `BD-ACC-03A`/`BD-ACC-03B` are Boss rulings and this is an ambiguity inside them | No amount of research resolves an ambiguity in a ruling |
| `C2-D-04` | Is the undischarged peer handover on dropship cost recognition commissioned, or closed as a determination under `C2-D-02`? | PMO / Boss | — |

---

## 7. Two instrument traps recorded for the next round

Published because an uncorrected false friend becomes a published count.

| Trap | Effect | Correction |
|---|---|---|
| The token used for a kit-structure flag **also names a cost defect class** in the Order-to-Cash package (`phantom cost`, a double-valuation finding). A naive search returns roughly half false friends in that path set | Would have reported kit evidence in a package that has none | Print what the pattern matched before counting it |
| A four-character token identical to the make-to-order abbreviation is used as a **migration identifier prefix** (`MTO-01`…`MTO-07`) in an unrelated register | Would have reported make-to-order coverage in the accounting programme where there is none | Word-bound, then inspect the hits |

Both are the `SA00-I-01` class — a false positive that looks like coverage — recurring under new tokens.

---

`CP-SA-C2-20 — DEMAND/SUPPLY ROUTING EVIDENCE COMPLETE OR BOUNDED (execution status)`, for the four
`SA-D05`-dependent natures. The remaining four are bounded in `SA_CORR2_03`.

Checkpoint completion is **not** Boss approval.

Boss remains the sole Final Approver. No Evidence = No Progress. Never Skip Gate.
