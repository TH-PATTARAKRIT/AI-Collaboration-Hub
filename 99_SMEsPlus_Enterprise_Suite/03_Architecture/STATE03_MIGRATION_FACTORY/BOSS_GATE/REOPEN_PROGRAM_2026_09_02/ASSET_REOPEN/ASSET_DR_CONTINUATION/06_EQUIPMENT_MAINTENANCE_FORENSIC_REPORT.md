# 06 — EQUIPMENT / MAINTENANCE FORENSIC REPORT (LEVEL 9)

**LAYER 2 — AUDIT QUARANTINE.**

The prompt forbids assuming a one-to-one mapping between asset and equipment. This
report determines the cardinalities from source, and states which of them are
*enforced*, which are *conventional*, and which are simply *unconstrained*.

---

## 1. The two records and what each knows

| | **Financial record** (asset) | **Operational record** (equipment) |
|---|---|---|
| Created from | A vendor bill line, by Accounting | By hand, by Maintenance |
| Knows | Cost, method, life, residual, accounts, analytic tag, company | Name, category, vendor, serial, location, model, warranty, owner, assigned date, scrap date, work centre |
| Knows about the other | Nothing, natively | Nothing, natively |
| Company | **Required** | **Optional** — may be empty |
| Lifecycle | Six states with guarded transitions | An `active` flag and a `scrap_date`. **No state machine** |

The two halves of one machine are created by two people, from two documents, on two
days, and the reference product joins them nowhere.

## 2. Cardinality — determined, not assumed

| Relation | Cardinality in source | Enforcement |
|---|---|---|
| Equipment → Work centre | **Many-to-one** | A single reference field on equipment. A work centre may hold many machines; a machine belongs to at most one work centre at a time |
| Operation → Work centre | **Many-to-one** | Required reference. See `07` |
| Operation → Equipment | **Does not exist** | — |
| Asset → Equipment (custom) | **Many-to-one, structurally** | An optional single reference on the asset. **Nothing prevents many assets pointing at one machine** |
| Equipment → Asset | **No inverse exists** | A machine cannot be asked which asset owns it |

### The answer to the prompt's question

**All three of the prompt's hypotheses are structurally possible, and the product
distinguishes none of them:**

- *1 asset = 1 equipment* — the intended case, achieved only by convention.
- *1 asset = many equipment* — **not expressible.** The link is single-valued on the
  asset side. A machine bought as one capitalised unit but operated as three stations
  cannot be modelled. This is the same gap TAS 16 exposes from the other direction:
  **component depreciation is required** (`18` §3), and the product supports neither
  components nor a one-to-many operational split.
- *many assets = 1 operational resource* — **expressible and unconstrained**, and it
  is the dangerous one. Two capitalised assets pointing at one machine give that
  machine's cost pool double the depreciation. Nothing prevents, warns or reports it.
  This is `BLK-02`.

Legitimate business circumstances for each, and what SMEsPlus must therefore support,
are in `19` §3.

## 3. Equipment lifecycle — thinner than it appears

There is no commissioning, no installation, no standby, no decommissioned state. The
product offers:

- `active` — a boolean, used for archiving,
- `scrap_date` — a date, informational,
- category, location, assigned date, warranty date — descriptive,
- and, through the custom module, a two-valued `status` (equipment / to-assets) which
  is **not** a lifecycle: it records whether the machine has been claimed by an asset.

**Consequence for the Boss's toll-gate model.** Every state the design needs —
commissioned, in production, under maintenance, broken down, standby, disposed,
reassigned — must be built. Only two exist today, and neither means what the design
needs. `19` §3 specifies the state set.

**Reassignment is silently destructive.** Moving equipment to another work centre is a
single field write with no history. Any historical cost attribution that read
"this machine belonged to that work centre" is retrospectively falsified with no trace.
`19` §3 makes the assignment a **dated record**, not a field.

## 4. Maintenance — what it records and what it costs

| Question | Answer | Class |
|---|---|---|
| Does a maintenance request carry a monetary field? | **No — none of any kind.** Re-verified by exhaustive field scan | `FACT VERIFIED` |
| Does it distinguish planned from unplanned work? | **Yes** — a maintenance type of *preventive* or *corrective* | `FACT VERIFIED` |
| Can it be tied to a manufacturing order or a work order? | **Yes** — both references exist | `FACT VERIFIED` |
| Does it affect production? | Yes, and only in one way: it **blocks capacity** by creating calendar leaves on the work centre's resource | `FACT VERIFIED` |
| Does equipment maintenance block the work centre? | **Yes** — the work centre's unavailability computation reads scheduled equipment maintenance directly, by database query | `FACT VERIFIED` |

### The preventive/corrective distinction is worth more than it looks

`BLK-08` requires the design to separate **planned** maintenance — which TAS 2 ¶13
places *inside* normal capacity, and which is therefore absorbed into product cost —
from **unplanned** breakdown, which is not and must be expensed.

The reference product already carries exactly that axis, on the maintenance request,
as a first-class field. SMEsPlus does not need to invent it; it needs to **give it a
costing consequence**, which the reference product does not.

### The equipment `cost` field — a second source of truth, inert

The equipment record carries a **cost** amount. It is referenced **nowhere** in the
maintenance module's own logic: nothing computes from it, nothing posts it, nothing
reconciles it to the asset's acquisition value.

So the same machine can carry two different costs — one that drives depreciation and
one that drives nothing — with no constraint that they agree and no report when they
do not. It is a trap for anyone building a machine cost pool who reaches for the
nearest field named "cost".

**SMEsPlus ruling:** a machine's cost has exactly one source, the financial record.
The operational record holds no monetary field at all. That is a deliberate omission,
and `19` §3 states it as a rule so it is not later "fixed" by someone adding a field.

## 5. The custom link — re-verified, with one refinement

Four intended behaviours. Re-derived independently from primary source this session:

| Behaviour | Intended | Actual | Basis |
|---|---|---|---|
| Confirming an asset marks the linked machine as claimed | Yes | **Executes** | The confirm override is in an imported file |
| Selling or disposing of an asset retires the linked machine | Yes | **Never executes** | The file defining it lives in a package the module's initialiser does not import |
| The link is editable only while the asset is draft | Yes | **Never applies** | Expressed with a field attribute that **does not exist in this platform generation** — searched the platform's field engine and found no such attribute anywhere |
| The asset's display name shows the machine's group reference | Yes | **Never fires** | Expressed by overriding a method the platform **removed** in this generation |

**Three of four are inert. None reports an error.**

### The refinement to "no uniqueness rule"

The baseline recorded that nothing prevents several assets claiming one machine. That
remains true and `BLK-02` remains open. But the mechanism is more interesting than
"no constraint":

- The link's selection list is filtered to machines whose status is *unclaimed*.
- Confirming an asset flips its machine's status to *claimed*.
- So after confirmation, that machine **disappears from the picker** for other assets.

This is a **soft guard**: it materially reduces duplicates created through the screen.
It does **not** stop duplicates arising from data import, from a direct write, from two
draft assets picking the same machine before either is confirmed, or from the status
being set back. And it is not a constraint, so nothing detects a duplicate that exists.

The refinement lowers the *expected* number of duplicates on the pilot data. It does
not lower the *consequence* of one, which is a doubled cost pool. `BLK-02` therefore
stays open at unchanged severity, and `19` §3 requires a real uniqueness constraint.

### And a fifth defect, not previously recorded

The claim is **one-way**. Confirming an asset marks the machine claimed; nothing ever
marks it unclaimed. Cancelling the asset does not. Deleting the link does not. Disposal
does not — that is the behaviour that never executes. So the soft guard is also a
**one-way ratchet**: a machine wrongly claimed by a cancelled asset is invisible to
every future asset, permanently, with no user-facing way back.

## 6. Company scoping — the leakage vector

| Record | Company | Visibility rule |
|---|---|---|
| Asset | **Required** | Assets of the company **and of its parents** |
| Equipment | **Optional** | Company in the allowed set **or empty** |
| Work centre | **Optional** | Company in the allowed set **or empty** |
| Work order | Required | Company in the allowed set — strict |
| Time log | Required | Company in the allowed set — strict |

An equipment record with no company is visible to, and usable by, **every** company on
the system. An asset, which must have a company, can be linked to it. Full analysis and
the SaaS consequences are in `14`.

## 7. Level 9 conclusions

1. Asset and equipment are two records with **no native relationship**, joined only by
   a custom optional pointer whose maintenance behaviours largely do not run.
2. The cardinality that matters is **many assets to one machine**, and it is
   unconstrained. This is a correctness precondition for costing, not hygiene.
3. **One asset to many machines is not expressible**, which collides with the component
   depreciation that TAS 16 requires.
4. Equipment has no lifecycle worth the name and no history on its work-centre
   assignment; both must be built.
5. Maintenance carries **no cost** but does carry the **planned/unplanned** axis the
   statutory allocation model needs.
6. The equipment `cost` field is a second, inert source of truth and must not be used.
