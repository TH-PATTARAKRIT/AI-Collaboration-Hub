# VDR_FUNCTIONAL_OWNERSHIP_RECONCILIATION_REPORT.md
# Functional Ownership — reconciliation and recommendation

Session `[SMEPLUS-26-09-10-VDR-PREP-002]` · Layer: **LAYER 1 — CLEAN-ROOM.**

---

## 1. What was reconciled

The prior Pilot derived a **mechanical** boundary of 149 modules and 96 objects and refused to trim it
by hand, routing the question to Boss as `BOSS-DEC-02` with the derived set attached. That refusal was
correct. **This workstream supplies the evidence the decision was missing.**

## 2. The reconciliation

| | Mechanical boundary | By functional ownership |
|---|---|---|
| Unit | module extension | object declaration, resolved through the dependency graph |
| Size | 149 modules · 96 objects | **60 objects owned by Inventory** |
| Largest contributor | **point-of-sale — 34 modules** | **Inventory — 60 objects** |
| Point-of-sale contribution | 34 modules (23%) | **1 object (1%)** |
| Objects owned elsewhere | not distinguished | **36 across 8 clusters** |

**The two boundaries disagree by a factor of 34 on the point-of-sale cluster alone.**

## 3. Ownership classes assigned

| Class | Objects |
|-------|--------:|
| PRIMARY OWNER | **60** |
| DEPENDENT MODULE | 13 |
| CONSUMING MODULE | 10 |
| TRIGGERING MODULE | 7 |
| OPTIONAL MODULE | 5 |
| **CROSS-MODULE CO-OWNER** | **1** |
| UNRESOLVED OWNERSHIP | **0** |

## 4. Recommendation to Boss on `BOSS-DEC-02`

**This is a recommendation with its evidence attached. The decision is Boss's and remains open.**

| Cluster | Recommended treatment | Why |
|---------|----------------------|-----|
| **Inventory** (60 objects) | **IN — this is the subject** | primary ownership |
| **Manufacturing** (13) | **the production order IN as a joint subject with a named owner per fact; the other 12 as handoff targets** | one object is displayed inside Inventory, carries stock quantity and carries financial fields; the rest trigger without being displayed |
| **Product / unit-of-measure** (5) | **OUT — they are the master-data subjects** `VDR-MD-03` / `VDR-MD-04` | consuming only; researching them here would duplicate an upstream subject |
| **Localisation** (5) | **OUT of the baseline; re-admit per tenant** | installed on no observed deployment |
| **Point-of-sale** (1) | **OUT** | one object, no quantity, no display |
| **Sales channel, delivery, repair, quality, field service, barcode** (**11**) | **OUT as subjects, IN as handoff targets** | they trigger or consume; none owns Inventory behaviour |
| **Platform** (1) | **BOUNDARY object** | extended by everyone |

**Net effect if adopted:** the Inventory VDR population contracts from 96 objects to **61** — the 60
owned plus the jointly-owned production order — and **35 objects become cross-module handoff targets
with named owners** rather than research subjects. (The cluster rows sum to 35: 13 manufacturing minus
the co-owner, 5 product, 5 localisation, 1 point-of-sale, 11 across the six trigger/consume clusters,
1 platform boundary object. The first version's row labels summed to 36 — an off-by-one in the
labelling, not in the derivation.)

## 5. What this does **not** decide

- It does not decide that the 35 handoff targets need no research — it decides **whose** research
  they are.
- It does not alter `P-07` (*Inventory emits facts; Accounting decides postings*). That prior ruling
  is **independently corroborated** and stands.
- It does not resolve `BOSS-DEC-12` — whether domain eligibility follows the **binding object** or
  **functional ownership**. The valuation-closing job is the live counter-example: it is inventory
  valuation, it runs, and the binding-object rule puts it outside the domain.

## 6. Status

| Control | Status |
|---------|--------|
| Ownership class assigned to every applicable item | **COMPLETE — 96 of 96, 0 unresolved** |
| Derivation reproducible by a second party | **yes for the primary-owner derivation** — independently re-derived with **0 disagreements on all 96 objects**. **No for the two supporting axes**: neither the quantity token set nor its module scope was published, and executing the published wording literally disagrees on 11 of 96 rows (`CORR-F-41`) |
| Material items resolved | **COMPLETE** for ownership class; **the deployment column was withdrawn and recomputed** after re-challenge found 10 rows had never been tested (`FO-F-07`) |
| `BOSS-DEC-02` | **OPEN — recommendation supplied** |
| `BOSS-DEC-12` | **OPEN — live counter-example supplied** |
