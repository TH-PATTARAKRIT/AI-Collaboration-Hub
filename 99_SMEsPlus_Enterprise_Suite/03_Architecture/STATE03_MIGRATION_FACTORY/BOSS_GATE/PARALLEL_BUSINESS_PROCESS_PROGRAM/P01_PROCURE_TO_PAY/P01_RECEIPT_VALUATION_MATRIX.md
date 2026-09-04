# P01 — RECEIPT VALUATION MATRIX

Session: `SMEPLUS-26-09-04-ACC-P01-P2P-REV2-001`
Layer: **1 — Clean-room business learning.**

The question this matrix answers: **when goods or services are received, what is created?**

## 1. THE MATRIX

| Item shape | Valuation mode | Operational record | Valuation layer | Journal entry | Value carried into the bill |
|---|---|---|---|---|---|
| Storable | Continuous | Receipt | Yes | **Yes** — Inventory / Clearing | Clearing balance |
| Storable | Periodic | Receipt | Yes | **No** | Nothing; expense arises at the bill |
| Consumable | any | Receipt | **No** | **No** | Nothing |
| Service | — | **No receipt document** | No | No | Nothing |
| Asset-destined | depends on item shape above | as above | as above | as above | Asset decided at the bill, not here |

Evidence: `EV-P01-04` (storable guard), `EV-P01-05` (valuation-mode guard).
Classification: **FACT VERIFIED**, scope `R1`.

## 2. UNIT COST AT RECEIPT

For an item under a moving/actual cost method, the unit cost written at receipt is taken from
the receiving movement's own price, which for a purchase receipt derives from the order line.
For an item under a standard cost method, the unit cost is the item's standing standard cost
and the order price is **ignored at this point**; the difference surfaces later as a price
difference at the bill.

Classification: **SUPPORTED INTERPRETATION**, scope `R1`, read from the incoming-layer value
routine. Runtime confirmation required.

## 3. ACCOUNT SELECTION AT RECEIPT

| Leg | Account chosen | Override surface |
|---|---|---|
| Debit | Item's inventory valuation account, from the item category | none observed at receipt |
| Credit | **Storage-location override if set**, otherwise the item category's goods-received clearing account | per-location override `EV-P01-07` |

The per-location override is a quiet configuration surface: two receipts of the same item into
two locations can credit two different accounts, with no document-level indication.

Classification: **FACT VERIFIED**, scope `R1`.

## 4. FAILURE BEHAVIOUR

A missing valuation journal, missing clearing account, or missing valuation account raises a
**blocking error at the moment of receiving goods**. `EV-P01-08`.

Design consequence: configuration completeness is enforced at the warehouse, by a warehouse
user, at the least appropriate moment. A clean-room design should validate at configuration
time and at order time, not at goods-movement time.

## 5. THE DATE

The date on the receipt's journal entry is **not** the date of the goods movement. It is:

1. a context override, where the caller supplies one;
2. otherwise the date of a bill line linked to the valuation layer;
3. otherwise **the system's current date, resolved in the acting user's timezone**.

`EV-P01-06`. Classification: **FACT VERIFIED**, scope `R1`.

Two consequences:

- a receipt entered on Monday for goods that arrived the previous Friday, in the previous
  period, posts in the current period;
- the user's timezone participates in period assignment, so two users completing the same
  receipt at the same instant can post it to two different dates.

This was independently re-examined by the Code & UI Architect expert, whose challenge is
recorded in `P01_AAS03_EXPERT_CHALLENGE.md`.

## 6. CROSS-GENERATION WARNING

Everything in this matrix is read from `R1`. The later generation `R3` **does not implement
the clearing-account model at all**: the clearing-account resolution keys have no runtime
definition anywhere in that root, and a different two-account model is used instead.
`EV-P01-24`, `EV-P01-25`.

**Therefore no row of this matrix may be carried into design as "how the reference system
works" without naming the generation it came from.**
