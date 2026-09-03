# 20 — EQUIPMENT WITHOUT AN ASSET
**LAYER 2 — AUDIT QUARANTINE**

Answers §34 part A.

## 1. Equipment as the reference product defines it

A maintenance-domain record. Its complete field set is operational and
administrative: name, category, owner, technician, vendor and vendor reference,
location, model, serial number, assigned date, warranty expiry, scrap date, notes,
colour, custom properties, plus computed reliability metrics (MTBF, MTTR, estimated
next failure, latest failure date) and a maintenance-request collection.

Financial content: **one plain `Cost` float.**

| What that field is not | |
|---|---|
| A monetary field | It has no currency |
| Linked to an account | No |
| Linked to an analytic account | No |
| Linked to a journal | No |
| Used in any computation | **No — it is written and displayed, never read by logic** |

`FACT VERIFIED` — field enumeration of the equipment model and search for its uses.

## 2. Is the acquisition cost of non-asset equipment expensed?

**The question does not arise in the equipment domain.** Equipment records carry no
accounting consequence at all. Creating one posts nothing; deleting one posts
nothing.

If a business buys a small machine and does not capitalise it, the expense is
recognised **through the vendor bill**, on whatever account the bill line uses, and
the equipment record is an independent operational artefact created separately.

`FACT VERIFIED`

## 3. Can analytic be used to track non-asset equipment cost?

**Not from the equipment record.** The equipment model has no analytic field.

Analytic attribution for such a purchase happens on the **bill line**, exactly as
for any other expense. Nothing associates that analytic line back to the equipment
record.

`FACT VERIFIED` — and this is a real limitation for the Boss's design: even for
equipment that is deliberately *not* capitalised, the system offers no way to
accumulate its cost against the machine.

## 4. How equipment records come into existence on this project

Three routes, and the third is the project's own:

| Route | Mechanism | Status |
|---|---|---|
| Manual | A user creates one | `NATIVE` |
| HR assignment | An employee/department bridge | `NATIVE` |
| **From stock** | A custom module creates equipment records from validated inventory and stock movements, keyed on **serial number**, driven by a flag on the product template | **`CUSTOM`** |

The custom route is the **Product → Equipment** path referred to in `08` §4. It is
serial-number driven, which means it works for serialised machinery and not for
anything tracked by lot or by quantity.

The custom equipment extension also adds: a category-derived group reference, an
internal reference generated from a configurable prefix/suffix/sequence scheme, and
the **status** field (*Equipment* / *To Assets*) that the asset link consumes.

`FACT VERIFIED`

## 5. The resulting operational picture

```
   Vendor bill line ──► Asset          (accountant, from the invoice)

   Goods receipt / serial ──► Equipment  (warehouse, from the delivery)

   Asset ──manual dropdown──► Equipment  (accountant, later, optional)
```

Two records, two documents, two departments, one machine, and an optional manual
join. `08` §4.

## 6. Equipment ↔ Work Center

The manufacturing bridge adds a `Work Center` field to equipment and the matching
collection to the work centre. This is the **only** native path from a machine
towards production, and it carries **capacity, not cost** (`08` §5).

`FACT VERIFIED`

## 7. Consolidated

| §34 question | Answer |
|---|---|
| Equipment without depreciation — does it exist? | Yes, and it is the **normal** case |
| Is its acquisition cost expensed? | Through the bill, not through the equipment record |
| Can analytic allocate it? | On the bill line only; **never associated back to the machine** |
| Does the equipment record carry any financial meaning? | **No** |
