# P01 — PURCHASE ACCOUNTING TRUTH MODEL

Session: `SMEPLUS-26-09-05-…-TARGETED-CROSS-PROCESS-CLOSURE-001`
Layer: **1.**

Directive §24: for each fact, is it **ORIGINAL TRUTH**, **DERIVED TRUTH**, **REFERENCE**, or
**AGGREGATION** — and do not collapse receipt, bill, liability and journal into one event.

---

## 1. THE TRUTH LADDER

| # | Fact | Kind | Owning artefact | Deployed reality |
|---|---|---|---|---|
| 1 | A need to buy exists | ORIGINAL | purchase request | Custom module — installed in the **v18** deployment only |
| 2 | A commitment to buy exists | ORIGINAL | purchase order | Installed everywhere. **No ledger effect** |
| 3 | The commitment's money value | DERIVED | order lines | Not ledger-visible — P09 records this as an open question |
| 4 | Goods physically arrived | ORIGINAL | goods receipt movement | Installed everywhere |
| 5 | The arrived goods have a value | ORIGINAL | valuation event | **v18: layer + ledger. v19 deployments: computed and stored on the movement, never in the ledger** |
| 6 | The goods are inventory / expense | DERIVED | item configuration, applied at receipt | Configuration, not a business act |
| 7 | The purchase is a capital asset | **DERIVED — and from the wrong place** | the **ledger account** of the bill line | **No classification field exists on the order or the receipt.** Confirmed independently with P04 |
| 8 | An obligation to the vendor exists | ORIGINAL | vendor bill | The **only** universal accounting event |
| 9 | The obligation's amount | ORIGINAL | vendor bill lines | — |
| 10 | The obligation's counter-account | DERIVED | item and company configuration | Five patterns behind one document |
| 11 | Tax on the purchase | DERIVED | bill lines | Routed to P07 |
| 12 | Tax to be withheld | **CONTESTED ORIGINAL** | bill line or payment — **unresolved** | P07 reports the fact is created at payment but reported from the bill line |
| 13 | The journal entry | **DERIVED** | posting of the bill | Must never be treated as the original business truth |
| 14 | The journal item | DERIVED | posting | Some are **deleted** on reset-to-draft rather than reversed |
| 15 | The payable balance | **AGGREGATION** | ledger | — |
| 16 | Money left the company | ORIGINAL | payment | **No entry at all without an outstanding-payments account** |
| 17 | The obligation is settled | ORIGINAL | reconciliation | P06 owns it and **mutates** the bill's payment status |
| 18 | Exchange gain or loss | DERIVED | reconciliation | Arises at settlement, not at bill or receipt |
| 19 | Financial statement lines | AGGREGATION | reporting | P08 |
| 20 | The period is closed | REFERENCE | lock dates | **Re-dates rather than refuses** |

---

## 2. THE THREE COLLAPSES THAT THE EVIDENCE SHOWS

### 2.1 Receipt collapsed into the bill

In the v19 deployments, facts 4, 5 and 8 all first reach the ledger at the bill. Facts 4 and 5
have **no accounting representation of their own**. The receipt is an operational truth with no
financial counterpart.

### 2.2 Valuation collapsed into the journal entry

v18 keeps them separate: a valuation layer is the valuation truth, the entry is its accounting
expression, and the layer holds the link. **v19 removes the separate valuation record** — the
value lives on the movement and the entry is the only accounting artefact. Where no entry is
created, as in both deployments, the valuation truth exists **only** on the movement and is
therefore invisible to every accounting control.

### 2.3 Classification collapsed into the chart of accounts

Fact 7 — capital or expense — is expressed nowhere on the purchase documents. It is decided by
the account on the bill line, whose capitalization flag is computed from the account type. In
practice the decision is taken by whoever configures the chart, before any purchase exists.

**And that same field is contested**: for a storable, continuously-valued item under the v18
clearing model, the bill line's account is silently replaced by the clearing account before the
asset rule reads it. Two mechanisms write one field. Recorded as `CONTRA-P01-04`, now with
independent peer corroboration.

---

## 3. THE QUESTION §3.10 DEMANDS, ANSWERED

> *What business event created this financial fact?*

| Financial fact | Answerable from the data? |
|---|---|
| A payable line | **Yes** — the bill |
| A bill line's origin order | **Yes** — an explicit link, but that link is `ON DELETE SET NULL` in both deployed generations |
| The specific receipt a bill line settles | **v18: not from the documents alone** — the match is replayed using audit-log ordering. **v19 deployments: the question does not arise, because no receipt entry exists** |
| An order's accrual entry | **No** — no link is written, in either generation |
| An asset's originating purchase | **No** — confirmed with P04 |
| A cross-company generated document's origin | **Only via a chatter message** |
| The inventory value of goods received but not billed | **v19 deployments: nowhere in the ledger** |

**Six of seven are not fully answerable.** That is the finding, and it is the strongest single
argument in this package for an explicit event-identity spine in the target design.

---

## 4. WHAT THE TARGET DESIGN MUST NOT INHERIT

Stated as learning, **not** as a design decision — P01 makes no target-architecture decisions.

1. A valuation truth with no accounting representation.
2. A capital-versus-expense decision expressed only in the chart of accounts.
3. A field that two mechanisms both write.
4. A correction path that deletes derived journal items.
5. A period lock that re-dates instead of refusing.
6. A missing posting destination that produces silence rather than refusal.
7. A financial fact whose origin cannot be traced from the data.
