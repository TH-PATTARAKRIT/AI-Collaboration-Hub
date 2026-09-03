# 25 — ASSET SALE AND DISPOSAL RESEARCH
**LAYER 2 — AUDIT QUARANTINE**

Answers §31.

## 1. The two paths

| | Dispose | Sell |
|---|---|---|
| Proceeds | none | from a **posted customer invoice**, line-selected |
| Entry type | *disposal* | *sale* |
| Precondition | not before the lock date | as dispose, **plus** no running child value increase |
| Result | `close` | `close` |

The requirement of a **posted customer invoice** is worth noting: an asset cannot be
recorded as sold on the strength of a price alone. The revenue document must exist
first. `FACT VERIFIED`

## 2. What happens, in order

1. **Catch up** — a depreciation entry is posted covering the part-period up to the
   disposal date, and all future entries are destroyed or reversed.
2. The asset **and all its children** are set to `close`.
3. The disposal entry is built (§3).
4. A chatter message records *Asset sold* or *Asset disposed* with the user's note.
5. `net_gain_on_sale` is stored as `proceeds − book_value`.

**Step 2 happens before step 5**, and closing the asset changes how book value is
computed (`18` §6). This ordering is the source of `CTR-05`.

`FACT VERIFIED`

## 3. The disposal entry

```
Cr   Fixed asset account            original value            (gross cost, in full)
Dr   Accumulated depreciation       depreciation to date       (incl. imported amount)
Dr   proceeds account(s)            sale proceeds              (sale only)
Dr/Cr Gain or Loss account          the balancing difference
```

with:

```
difference = − original value − depreciated amount − invoice amount
account    = the company's gain account if the difference is positive,
             otherwise the company's loss account
```

Every line carries the **asset's analytic distribution**. The fixed-asset account
used is the source bill's account where there is exactly one, otherwise the asset's
own.

`FACT VERIFIED`

### Validation of §31's expected identity

> Gain/Loss on disposal = proceeds − financial carrying amount

The entry satisfies this, because the carrying amount is
`original − accumulated depreciation` and the difference line is the plug that
balances gross cost, accumulated depreciation and proceeds. **The identity holds.**

**But**: the *carrying amount* implied by the entry **includes the residual**,
because the residual is simply the undepreciated part of the gross cost. Whereas the
`book_value` field, read at step 5 after closure, **excludes** it.

**Therefore the posted gain/loss and the stored gain/loss can differ by exactly the
not-depreciable value.** `CTR-05`, `FAIL-R08`.

`FACT VERIFIED` — the entry construction and the closure ordering.

## 4. Parent and child

Selling a parent that has a **running** value increase is blocked: the user is told
to dispose of the increase first. Disposing (rather than selling) closes the parent
and all its children together, with one entry per record.

`FACT VERIFIED`

## 5. Equipment consequence

**Intended:** deactivate the linked equipment on sale.
**Actual:** the override is in a file the module never imports. **It does not run.**

So after selling a machine, its equipment record remains **active** and still
flagged *To Assets* — the status the asset confirm set. Nothing resets it.

`CONTRADICTED` — `19` `EQ-DEF-01`.

## 6. Tax

No tax-specific disposal treatment exists (`12` §7 `FAIL-T06`). Thai tax gain or loss
on disposal is computed on the **tax** written-down value, which this system does not
hold. The reconciliation is external.

`VERIFIED GAP`

## 7. Reversal

`close` is not terminal. Reset-to-running re-opens the asset and, if the last line is
non-zero, runs a modify to rebuild the board. The stored gain is reset to zero. The
disposal entry itself is **not automatically reversed** by that action.

`FACT VERIFIED` — and worth flagging: re-opening a closed asset leaves the disposal
entry in the ledger unless someone reverses it manually.

## 8. Consolidated answers to §31

| Item | Answer |
|---|---|
| Sale proceeds | From a posted customer invoice, line-selected |
| Book value | Not used in the entry; used only for the stored gain figure |
| Accumulated depreciation | Written out in full, including any imported amount |
| Remaining depreciation | Caught up to the disposal date first |
| Tax | Not handled |
| Gain/Loss | The balancing difference, to a company-level gain or loss account |
| Journal entries | One multi-line entry per asset, plus the catch-up entry |
| Asset status | `close`, together with all children |
| Equipment status | **Unchanged — the intended behaviour is dead code** |
| Analytic | Carried on every disposal line |
| Audit trail | Chatter message; the stored gain figure is **not visible in the form** |
