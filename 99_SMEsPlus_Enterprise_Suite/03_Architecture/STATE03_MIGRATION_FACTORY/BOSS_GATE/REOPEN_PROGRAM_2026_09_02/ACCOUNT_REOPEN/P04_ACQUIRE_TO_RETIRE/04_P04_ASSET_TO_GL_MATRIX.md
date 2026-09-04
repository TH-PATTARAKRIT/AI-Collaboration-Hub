# 04 — P04 ASSET TO GL MATRIX

Layer: **2 — audit quarantine**.

Event → journal entry → account, for every asset event that has an accounting
effect. Event IDs are those of `03_P04_ASSET_EVENT_REGISTER.md`.

---

## 1. The account-resolution chain

Five accounts participate. Their resolution differs, and the differences matter.

| Slot | How it resolves | Behaviour when blank |
|------|-----------------|----------------------|
| **Fixed-asset account** | **Computed and stored, editable.** Taken from the source journal items' account when they exist; otherwise falls back through an on-change to the accumulated-depreciation account | Field is blank. The corresponding entry leg is **silently dropped** |
| **Accumulated-depreciation account** | **No compute, no default.** Sourced only from the asset model, from an on-change, or manually | The entry line is written with **no account** |
| **Depreciation-expense account** | **No compute, no default.** Sourced only from the asset model or manually | as above |
| **Journal** | Computed: the **first general-type journal of the company**. Used by **every** asset entry | — |
| **Gain / loss on disposal** | **Company-level singletons**, read directly from the asset's company at disposal time | The leg is **silently dropped** |

### 1.1 Four findings from the chain itself

| ID | Finding | Class |
|----|---------|-------|
| **P04-F-20** | Gain and loss on disposal are **one account each per company**, for every asset class. Segregating disposal results by class, by administrative-versus-production use, or by any other dimension is **not possible without new behaviour** | FACT VERIFIED |
| **P04-F-21** | Every asset entry uses the **first general journal of the company**, resolved by ordering. Two companies, or a re-sequenced journal list, change where asset entries land without any asset-level configuration changing | FACT VERIFIED |
| **P04-F-22** | Neither depreciation account has a default or a compute. Only the asset model supplies them — and on the live population **no asset carries a model** | FACT VERIFIED |
| **P04-F-23** | A blank account does not raise; the leg is dropped. Combined with the draft disposal entry (P04-F-13), an **unbalanced entry can be created with no error surfaced** | FACT VERIFIED |

---

## 2. The matrix

Legend: **FA** fixed-asset account · **AD** accumulated depreciation ·
**DE** depreciation expense · **G/L** company gain or loss account.

| Event | Entry? | Debit | Credit | Accounting date | Posted? | Analytic |
|-------|--------|-------|--------|-----------------|---------|----------|
| **EV-03/05/06** create | **none** | — | — | — | — | asset-level distribution computed as a **balance-weighted average of the source bill lines** |
| **EV-04** create and confirm | yes | DE | AD | see below | **all posted at once** | inherited |
| **EV-10** compute schedule | draft lines only, unless running | DE | AD | **end of month** where the period is monthly; otherwise **end of fiscal year** | posted only when the asset is running; **future-dated entries are not posted — they are marked to auto-post at their date** | copied to **both** lines, only if the asset's distribution is non-empty |
| **EV-11** depreciation posting | yes | DE | AD | as above | yes | as above |
| **EV-12** reverse one entry | yes | AD | DE | **the original entry's date** | posted | copied |
| **EV-13** pause | yes — one catch-up | DE | AD | the pause date | **posted** | inherited |
| **EV-14** resume | normally none | — | — | — | — | — |
| **EV-15** re-evaluate, net decrease | yes | **DE** | AD | the wizard date | **posted** | inherited |
| **EV-07/15** re-evaluate, net increase | yes | **FA** | a counterpart account chosen in the wizard | **the wizard date plus one day** | **posted** | **NONE — neither line carries a distribution** |
| **EV-07** child asset schedule | yes | child DE | child AD | from the wizard date plus one day, clipped to the parent's remaining life | posted | **NONE — the child inherits none** |
| **EV-16** cancel asset | yes — reversals | AD | DE | **each original entry's own date** | posted | copied |
| **EV-19** sell | **two** | see `07` §2 | see `07` §2 | the wizard date | catch-up **posted**; **disposal entry LEFT IN DRAFT** | every line, including gain/loss |
| **EV-20** dispose | **two** | see `07` §2 | see `07` §2 | the wizard date | catch-up **posted**; **disposal entry LEFT IN DRAFT** | every line |
| **EV-18** re-open closed asset | possibly | as EV-15 | as EV-15 | today | as EV-15 | inherited |
| **EV-21/22** archive, delete | none | — | — | — | — | — |

### 2.1 Negative assets (credit notes)

The automatic creation path fires on vendor **credit notes** as well as bills.
The resulting asset carries a **negative** original value and the entry sides
invert — Dr accumulated depreciation / Cr depreciation expense — with the sign
carried through to disposal. **FACT VERIFIED.**

Whether a vendor credit note reliably satisfies the positive-total eligibility
test is **UNRESOLVED**: the sign behaviour is produced by the tax engine and was
not traced. The account's own help text asserts the intent ("a vendor bill or a
refund"), so intent is clear and the code path is not. Registered **P04-B-16**.

---

## 3. Multi-currency

**There is no genuine multi-currency behaviour on the asset.** The asset's
currency is a related field pointing at the company's currency, so every
conversion in the depreciation and disposal paths is an identity operation.
Sale proceeds enter as the customer invoice's **company-currency** amount at the
invoice's own rate.

> Any exchange movement between the invoice date and the disposal date is
> **absorbed into the gain or loss line**, with no separate exchange account.
> Classification: **FACT VERIFIED.**

Two write paths set a currency value into the asset's creation values, targeting
a stored related field whose inverse writes back to the **company's** currency.
This is harmless only because the two values are always identical — it is a
latent defect that becomes live the moment a genuine asset currency is
introduced. Registered **P04-F-24**.

This connects to the Account Wave A finding on silent one-to-one exchange
fallback: the asset domain does not merely fall back to one-to-one, it has
**no currency dimension to fall back from**.

---

## 4. Period control (P08 boundary)

| Control | Present? | Class |
|---------|----------|-------|
| Lock-date check on **disposal** | **Yes** — disposal is refused at or before the user fiscal lock date for the asset's journal | FACT VERIFIED |
| Lock-date check on **entry creation** during pause and cancellation | Yes — reversal dates are bumped to lock date plus one where the original date is at or before the lock | FACT VERIFIED |
| Lock-date check on **confirm** | **Not found.** Confirm posts the whole life in one action | PRIOR EVIDENCE, re-confirmed |
| An asset-specific period or year-close step | **Not found** under the asset module | FACT VERIFIED (scoped negative) |
| Sub-ledger to general-ledger reconciliation | **Not found anywhere in the reference product** | PRIOR EVIDENCE (P2 fit/gap item 27) |

---

## 5. The reconciliation gap — the structural finding of this file

The asset sub-ledger and the general ledger are joined by a **many-to-many
relation table**, not by a balancing entry. Nothing in the estate proves that

```
Σ asset original value  =  balance of the fixed-asset account
Σ asset accumulated depreciation  =  balance of the accumulated-depreciation account
```

Six mechanisms can break that agreement, all verified this session or in prior
packages:

1. Creation from a bill **does not touch** the source journal item — the asset is
   an unbalanced addition to a sub-ledger (P04-F-05).
2. The migration field for previously-recognised depreciation is a **sanctioned
   way** to introduce an asset whose accumulated depreciation has no
   corresponding ledger balance.
3. A blank account causes a leg to be **dropped** (P04-F-23).
4. Writing to the asset rewrites accounts **on posted entries by line ordinal**,
   including on the disposal entry (P04-F-17).
5. The derecognition entry is **left in draft**, so a closed asset's cost and
   accumulated depreciation remain in the ledger indefinitely (P04-F-13).
6. Duplication **detaches** the copy from its source journal items (`01` §2,
   mechanism 8e), so cost appears in the sub-ledger with no ledger counterpart.

> **P04-F-25.** There is no mechanism in the estate that would detect any of the
> six. A design that reconciles the asset sub-ledger to the ledger must be
> originated by SMEsPlus; it cannot be adapted.
> Class: **FACT VERIFIED.** Registered as blocker **P04-B-17**.
