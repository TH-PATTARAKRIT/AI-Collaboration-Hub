# T1 EVIDENCE EXTRACT — RETURN / CREDIT NOTE / REFUND / REVERSAL

`LAYER 2 — AUDIT QUARANTINE` · Parallel research track T1 · Session `SMEPLUS-26-09-04-ACC-P02-O2C-REV2-001`
Reference root: `/Volumes/iMacSys/CLAUDE AI/SMEsPlus18/odoo-18.0+e.20250608/odoo/addons` (`<ROOT>`)

Preserved as produced by the track, then independently spot-verified by the primary session
(verification record in `12_P02_CONTRADICTION_REGISTER.md` §5). Reference systems are benchmark
only; nothing here authorises copying.

## §0 DENOMINATOR

**POPULATION** — Python source files (models + wizards + controllers + reports, `tests/` excluded)
in the seven addons carrying O2C return / credit-note / reversal mechanics. Files in path set: **268**.
Files matching the declared pattern: **42**.

**PATTERN** (single ERE, `grep -rlE ... --include='*.py'`, then `grep -v '/tests/'`):
`origin_returned_move_id|returned_move_ids|_is_returned|to_refund|_reverse_moves|reversed_entry_id|move_reverse_cancel|out_refund|display_type *== *'cogs'|_stock_account_get_anglo_saxon_price_unit|backorder`

**PATH SET** — `account/`, `stock/`, `stock_account/`, `sale/`, `sale_stock/`, `purchase/`, `purchase_stock/`

**UNIT** — the *branch* (a specific predicate at a `path:line`). Files/methods are the addressing
scheme; the claim unit is the branch.

Read outside the denominator for dependency chase: `stock_account/models/stock_move_line.py`,
`account/models/company.py`, `sale_stock/tests/test_anglo_saxon_valuation.py` (corroboration only).

## §1 Physical customer return — creation, valuation layer, journal entry

- The only return wizard refuses non-completed pickings — `stock/wizard/stock_picking_return.py:104-105`,
  predicate `stock/models/stock_picking.py:2145-2147`. It copies the picking (`:159`), swaps source and
  destination (`:135-151`), and stamps each copied move with the originating move
  (`:35`). — `FACT VERIFIED`
- The return move is an inbound move (customer location → internal), so it routes to the inbound
  valuation-layer builder — `stock_account/models/stock_move.py:133-143`, `:365-369`. — `FACT VERIFIED`
- **Value at which returned stock re-enters — the branch.** `stock_account/models/stock_move.py:512-517`:
  - costing method **standard** → re-enters at the **current** standard price; the original outflow
    layer is never consulted. — `FACT VERIFIED`
  - costing method **FIFO / average** → `stock_account/models/stock_move.py:50` takes the
    originating-move branch and returns `sum(layer values) / sum(layer quantities)` (`:56`, `:65-67`),
    i.e. **the original outflow layer's realised unit cost**, including its correction layers. — `FACT VERIFIED`
  - Corroboration only (a test asserting the outcome, not the branch):
    `sale_stock/tests/test_anglo_saxon_valuation.py:1418-1444`. — `SUPPORTED INTERPRETATION`
- **Average-cost consequence.** The inbound return is weighted back into the moving average —
  `stock_account/models/stock_move.py:352`, body `:403-439`, write at `:434`. Returning old cheap stock
  **drags the moving average down**. — `FACT VERIFIED`
- **Journal entry.** `stock_account/models/stock_move.py:729-733`; the return predicate is
  `location_id.usage == 'customer'` (`:780-781`); destination account resolution `:534-536`.
  Net effect **Dr Inventory Valuation / Cr Outbound Stock (Delivered)** — the exact mirror of the
  delivery entry. The return context also sets the storno flag when the company enables it (`:685`). — `FACT VERIFIED`
- **Journal entry date.** `stock_account/models/stock_move.py:670-675` — forced-period date, else the
  layer's own accounting line date, else **today**. The forced-period path is written only by inventory
  adjustments (`stock_account/models/stock_quant.py:71`), never by a picking. **The return's valuation
  entry is dated today, not the picking date.** — `FACT VERIFIED`

## §2 Credit note — reversal date and full-reversal mode

- Reversal date defaults to today — `account/wizard/account_move_reversal.py:17` — and is written to the
  accounting date, the due date and the document date — `:90-104`, `:97-99`. — `FACT VERIFIED`
- A future reversal date sets deferred auto-posting instead of posting now — `:103`. — `FACT VERIFIED`
- **Full-reversal flag computation** — `:134-136`:
  `is_cancel_needed = not is_auto_post and (is_modify or move_type == 'entry')`.
  - plain credit note (`:181-182`) → **not** a cancelling reversal;
  - reverse-and-modify (`:184-185`) → cancelling reversal, **unless the date is in the future**, in
    which case it silently degrades to the plain path. — `FACT VERIFIED`
- What the cancelling mode changes — `account/models/account_move.py:4760-4803`: existing
  reconciliations on the original are torn down first (`:4771-4775`); the cancel flag is put into the
  copy context (`:4784-4788`); the reversal is posted hard (`:4801`).
  It does **not** control reversal↔original reconciliation — that happens on the reversal link alone
  (`:4955`, `:4962`); the flag only switches tax-cash-basis handling (`:4739-4742`, `:4756`). — `FACT VERIFIED`
- **Sign flip is selective** — `account/models/account_move.py:4790-4797` negates balances only for
  general entries and for **cost-of-sales** lines. Invoice product / tax / receivable lines are not
  negated here; their sign comes from the document-type map (`:58-66`). Cost-of-sales lines are the
  explicit exception. — `FACT VERIFIED`
- **A locked period does not block a reversal; it relocates it** — `account/models/account_move.py:4932-4936`,
  `:5655-5692` (`:5674`, `:5675-5680`). The user-chosen reversal date is discarded, the document date is
  left unchanged, and the two diverge. The only warning is advisory and pre-post (`:5703-5719`). — `FACT VERIFIED`

## §3 Cost of sales on a credit note

- Cost lines are created for credit notes with **no reference to any stock movement**. The only filters
  are sale-document, company split-recognition flag (`stock_account/models/account_move.py:111`) and
  product eligibility (`:119`, `:276-278`). — `FACT VERIFIED`
- Sign handling — `:130`, `:132`, `:146`, `:162` — yields **Dr Outbound Stock (Delivered) / Cr Expense**. — `FACT VERIFIED`
- **Three branches decide whether the credit note uses the ORIGINAL cost or a re-derived one:**
  - **(a) cancelling reversal** — `stock_account/models/account_move.py:42-43` returns before creating
    any cost lines, and `copy_data` (`:31-35`) strips cost lines **only when the flag is absent**. So the
    original document's cost lines are copied verbatim and sign-flipped by
    `account/models/account_move.py:4796`. **Exact original cost, no re-derivation.** — `FACT VERIFIED`
  - **(b) plain credit note, line NOT linked to an order line** — `:305-314` looks up the reversed
    document's own cost line for the same product and unit, and returns its unit price; falling back to
    the product's current standard price (`stock_account/models/product.py:859-863`). — `FACT VERIFIED`
  - **(c) plain credit note, line LINKED to an order line** — `sale_stock/models/account_move.py:151-202`.
    Line `:153` computes branch (b), then `:161`/`:201` **overwrite it entirely**. The re-derivation
    (`:162-164`, `:168`, `:170-184`, `:185-197`, `:200`) restricts the candidate layers via
    `stock_account/models/product.py:883` to **physical returns with a net-positive layer only**.
    If a return exists, the answer coincides with the original cost. **If no return exists the candidate
    set is empty and `stock_account/models/product.py:901-907` values the whole credit note at the
    product's CURRENT standard price on the day it is posted.** — `FACT VERIFIED`
- Cost lines are excluded from the currency set that drives settlement state
  (`stock_account/models/account_move.py:23-25` → `account/models/account_move.py:1180`), so they cannot
  influence payment state. — `FACT VERIFIED`
- Reset-to-draft and cancel unlink cost lines (`:56-71`); the reset button is hidden when the document
  carries valuation layers (`:13-17`). — `FACT VERIFIED`

## §4 THE CENTRAL QUESTION — is a credit note coupled to a physical return?

**Answer: No. They are structurally independent. No field, constraint or guard in the path set ties one
to the other. The only relationship is opportunistic matching of a shared clearing account.**

### 4a. Credit note with NO stock return

1. Nothing gates credit-note creation on stock — `account/wizard/account_move_reversal.py:74-75`;
   the file contains no inventory import. — `FACT VERIFIED`
2. Nothing gates posting on stock — `account/models/account_move.py:4832-4993`; the inventory-accounting
   override (`stock_account/models/account_move.py:38-54`) adds lines, it does not block. — `FACT VERIFIED`
3. Cost of sales is reversed regardless — eligibility is product-property-only
   (`stock_account/models/account_move.py:276-278`); the generation loop (`:116-134`) never inspects the
   order line's movements. — `FACT VERIFIED`
4. No valuation layer and no inventory change — layers are created only from movement completion
   (`stock_account/models/stock_move.py:365-369`) and quantity correction
   (`stock_account/models/stock_move_line.py:95-113`). Posting an accounting document reaches neither. — `FACT VERIFIED`
5. The clearing account is left one-legged — `stock_account/models/account_move.py:183-247`; the credit-note
   branch (`sale_stock/models/account_move.py:26-28`) only picks up movements **out of** the customer
   location, i.e. returns. With no return, `:199-200` skips and **nothing is matched**. The debit sits
   open in the outbound stock account indefinitely. — `FACT VERIFIED`
6. And it is valued at today's standard price — `stock_account/models/product.py:906-907`. — `FACT VERIFIED`

**Net effect of a credit note with no return:** revenue reversed, receivable reversed, **expense credited
at current standard cost**, outbound stock account debited and left unmatched, **inventory quantity and
valuation unchanged**. The margin reversal in the profit and loss is computed from a cost that may bear no
relation to what was shipped. — `SUPPORTED INTERPRETATION` (each leg above is `FACT VERIFIED`)

### 4b. Physical return with NO credit note

1. The return wizard creates a picking and opens it — `stock/wizard/stock_picking_return.py:193-203`.
   It never touches an accounting document. The only accounting artefact is the valuation entry
   (`stock_account/models/stock_valuation_layer.py:96-100`). — `FACT VERIFIED`
2. The strongest coupling that exists is a **quantity** signal, not a document trigger. The
   refund-intent flag defaults on in the wizard (`stock_account/wizard/stock_picking_return.py:10`,
   written at `:13-17`); its entire effect is `sale_stock/models/sale_order_line.py:318-326` —
   `:321` excludes a return from delivered quantity unless the flag is set, `:323` counts it as inbound
   only if the flag is set. **With the flag off, a return restores inventory and does not even reduce the
   delivered quantity.** — `FACT VERIFIED`
3. The flag is hidden from ordinary users — `stock_account/views/stock_account_views.xml:49` renders it
   behind the developer-mode group. — `FACT VERIFIED`
4. Even with the flag on, the credit note is **opt-in and manual**: delivered quantity drops, billable
   quantity goes negative (`sale/models/sale_order_line.py:969`), and a negative line is picked up **only**
   when the user passes the final-invoice option — `sale/models/sale_order.py:1493`. The resulting draft is
   flipped to a credit note after creation (`sale/models/sale_order.py:1633-1635` via
   `account/models/account_move.py:5129-5151`). Nothing calls this from the return. — `FACT VERIFIED`

## §5 Invoiced-quantity counter and how a credit note gets its order-line link

- The counter — `sale/models/sale_order_line.py:908-924` — adds invoices (`:920-921`) and subtracts credit
  notes (`:922-923`), iterating only lines that carry the order-line link. **A credit-note line with no link
  is not in the iteration and cannot decrease the counter.** The docstring at `:911-914` states this is
  deliberate. — `FACT VERIFIED`
- The link field — `sale/models/account_move_line.py:12-16` — is not copied and is read-only in the UI. — `FACT VERIFIED`
- **Complete enumeration of writers** (denominator: pattern `sale_line_ids` over `sale/` and `sale_stock/`):

| path | mechanism | link set? |
|---|---|---|
| Reversal wizard (both modes) | business-field copy context (`account/models/account_move.py:4786`) → `account/models/account_move_line.py:1769-1770` → `sale/models/account_move_line.py:18-21` | **yes** |
| Order-driven final invoicing on a negative line | `sale/models/sale_order_line.py:1395`, `:1408`, then document-type flip `sale/models/sale_order.py:1633-1635` | **yes** |
| Credit note created by hand in Accounting | no compute, no default, not copied, read-only | **no** — the counter is not decreased; the order still reads as fully invoiced |
| An arbitrary copy of an invoice | field not copied; the business-field guard is false | **no** |

— `FACT VERIFIED` for all four rows.

- **Side effect** — because the reversal wizard *does* set the link, it also activates the re-derivation
  branch (§3c) and thereby **discards** the original-cost lookup performed one layer below
  (`stock_account/models/account_move.py:309-314`). Linking a credit note to its order line makes its cost
  **less** anchored to the original invoice, not more. — `SUPPORTED INTERPRETATION`
- The reversal link is separate and weaker — always set by the reversal path
  (`account/models/account_move.py:4781`), set by the order-driven path only when a localisation hook
  demands it (`:6255-6266`, false in base). An order-generated credit note therefore normally has the
  order-line link but **no** reversal link. — `FACT VERIFIED`

## §6 Reversal of a delivery; corrected / backdated completed pickings; return-of-a-return

- **A completed delivery cannot be cancelled or reversed** — `stock/models/stock_move.py:1971-1973` raises
  and directs the user to create a return. The inventory-accounting cancel override
  (`stock_account/models/stock_move.py:235-237`) never runs on a completed move.
  **A return is the only reversal mechanism for delivered goods.** — `FACT VERIFIED`
- **Correcting the quantity of a completed move** — `stock_account/models/stock_move_line.py:44-47` →
  `:76-84`, `:95-113`; branches at `:99-111`; entries validated at `:113`. Corrections are **new layers plus a
  new entry**; nothing is amended in place. The layer is stamped as a correction of a past move
  (`stock_account/models/stock_move.py:262`, `:301`, `:527`). — `FACT VERIFIED`
- **Backdating is not honoured by the correction entry** — the entry takes today's date
  (`stock_account/models/stock_move.py:670-675`). — `FACT VERIFIED`
- Locations of a completed move cannot be re-pointed across the valuation boundary —
  `stock_account/models/stock_move_line.py:48-60` raises. — `FACT VERIFIED`
- **Return-of-a-return** — the wizard re-wires the movement graph so it links to the original chain
  (`stock/wizard/stock_picking_return.py:57-74`, comment at `:65-69`); the originating-move link is always
  the immediate parent (`:35`), so a return-of-a-return is valued at the **return layer's** cost. Since the
  return layer was itself valued at the delivery cost, the chain is cost-stable through one hop.
  Exchange creation is an explicit return-of-the-return (`:222-247`). — `FACT VERIFIED` for the wiring;
  `SUPPORTED INTERPRETATION` for cost stability.
- Matching is return-aware — `stock_account/models/stock_valuation_layer.py:107`;
  `stock_account/models/account_move.py:196-197`. — `FACT VERIFIED`

## §7 Backorders and order-line consistency

- Creation — `stock/models/stock_picking.py:1421-1428`; the ask-mode confirmation predicate
  `:1488-1491`, `:1528-1541`. — `FACT VERIFIED`
- Split — `stock/models/stock_move.py:2072-2073`, `:2080-2096` (`:2087`, `:2089`); split values carry the
  originating-move link and price (`:2108-2117`) and, via inventory accounting, the refund-intent flag
  (`stock_account/models/stock_move.py:660-663`). The picking copy clears the picked marker on the moved
  remainder — `stock/models/stock_picking.py:1571-1597` (`:1585`). — `FACT VERIFIED`
- **Consistency holds by construction:** delivered quantity sums only completed movements
  (`sale_stock/models/sale_order_line.py:201-208`); the split preserves total quantity; the procurement
  quantity helper prevents re-procurement of the remainder
  (`sale_stock/models/sale_order_line.py:284-294`, `:359-361`). — `FACT VERIFIED`
- **One hazard verified:** the never-backorder branch (`stock/models/stock_picking.py:1421`, `:1427`)
  cancels the undelivered remainder outright. Delivered quantity then permanently reports the short
  quantity while the ordered quantity still shows the full order, leaving billable quantity short with no
  document trail beyond the cancelled movements. — `SUPPORTED INTERPRETATION`

## §8 CONTRADICTIONS / SURPRISES

- **T1-C1 — Two mutually inconsistent definitions of "this movement is a return."** Valuation uses the
  originating-move link (`stock_account/models/stock_move.py:50`); accounting uses the customer-location
  test (`:780-781`). A manually created inbound picking from the customer location with no originating-move
  link is booked with the **return** account pair and the storno flag (`:731`, `:685`) while being **valued
  at current standard price** (`:512-515`, since `:50` is false). The entry says "return"; the layer says
  "receipt". — `CONTRADICTED` (of the obvious reading that one predicate governs both)
- **T1-C2 — A future reversal date silently downgrades a full reversal to a plain credit note.**
  `account/wizard/account_move_reversal.py:103` then `:134-136`. Reverse-and-modify dated tomorrow takes the
  plain path: cost of sales is **stripped and re-derived at tomorrow's standard price** instead of copied at
  the original cost. The cost basis of a "full reversal" depends on whether the user picked today or
  tomorrow. — `FACT VERIFIED`
- **T1-C3 — Linking a credit note to its order line makes its cost LESS accurate.**
  `sale_stock/models/account_move.py:153` computes the original-cost answer, then `:161`/`:201` throws it
  away whenever an order line is present. The base lookup at
  `stock_account/models/account_move.py:309-314` is dead code for every order-originated credit note. — `FACT VERIFIED`
- **T1-C4 — The refund-intent flag defaults on but is invisible.**
  `stock_account/wizard/stock_picking_return.py:10` vs `stock_account/views/stock_account_views.xml:49`.
  Every ordinary return silently reduces delivered quantity and flips the order back to "to invoice" — but a
  user without developer mode cannot see or change this, and no credit note is produced. — `FACT VERIFIED`
- **T1-C5 — Locked periods do not block a reversal; they relocate it.**
  `account/models/account_move.py:4934-4936`. The only hard stop nearby (`:4805-4809`) merely routes deletion
  to reversal. — `FACT VERIFIED`
- **T1-C6 — The cancelling mode is not what causes reversal↔original matching.**
  `account/models/account_move.py:4955`, `:4962` match on the reversal link alone. — `FACT VERIFIED`
- **T1-C7 — A customer return moves the average cost.** `stock_account/models/stock_move.py:352` → `:403-439`
  (`:434`). Returning old cheap stock re-weights the average downward, which then becomes the fallback cost
  for any **subsequent** credit note posted with no return (§3c). The two failure modes compound. — `SUPPORTED INTERPRETATION`
- **T1-C8 — Valuation entries are always dated today.** `stock_account/models/stock_move.py:675`. A picking
  validated on the 3rd for goods that moved on the 1st books valuation on the 3rd; a quantity correction made
  on the 30th books on the 30th, in a different period from the movement it corrects. — `FACT VERIFIED`
- **T1-C9 — The invoiced-quantity counter is documented as intentionally lossy.**
  `sale/models/sale_order_line.py:911-914`. Design, not defect — but it means the order's "fully invoiced"
  status is silent about any credit note raised outside the wizard. — `FACT VERIFIED`

## §9 NEGATIVE CLAIMS (each with search scope)

- **T1-N1.** No code creating, drafting or scheduling a credit note as a consequence of validating a return
  picking was found in `stock/`, `stock_account/`, `sale/`, `sale_stock/` (`*.py`, `tests/` excluded) under
  the patterns `out_refund`, `_reverse_moves`, `action_reverse`, `_create_invoices`, `account.move` within
  the return and movement-completion call paths. The return wizard contains no accounting reference.
  `NOT FOUND IN SEARCHED SCOPE` — localisation and enterprise addons outside the path set were not searched.
- **T1-N2.** No constraint or guard blocking the posting of a credit note when the related order line has no
  returned movement was found in the four accounting-document files of the path set under
  `raise UserError`, `raise ValidationError`, `_check_`, `constrains` within the post routine and its
  overrides. `NOT FOUND IN SEARCHED SCOPE`
- **T1-N3.** No mechanism back-dating a picking's valuation entry to the picking's completion date was found
  in `stock_account/` under the forced-period-date pattern. The only writer is the inventory-adjustment path
  (`stock_account/models/stock_quant.py:71`). `NOT FOUND IN SEARCHED SCOPE`
- **T1-N4.** No override of the return predicate outside `stock_account/models/stock_move.py:778` was found in
  the full path set. `VERIFIED ABSENCE` within the path set.
- **T1-N5.** No writer of the invoice-line→order-line link other than `sale/models/sale_order_line.py:1395`,
  `:1408` and `sale/models/account_move_line.py:21` was found in `sale/` and `sale_stock/`.
  `NOT FOUND IN SEARCHED SCOPE` — modules outside the path set were not searched.
- **T1-N6.** No default on the movement-level refund-intent flag was found at its declaration
  (`stock_account/models/stock_move.py:17`); the on-default exists only on the wizard line
  (`stock_account/wizard/stock_picking_return.py:10`) and on negative-quantity procurements
  (`stock/models/stock_rule.py:347-348`). `VERIFIED ABSENCE` at the declaration.
- **T1-N7 — `UNRESOLVED — EVIDENCE REQUIRED`.** Whether the no-exchange-difference matching branch
  (`stock_account/models/account_move.py:235-247`) leaves a residual in the outbound stock account when a
  credit note's re-derived cost differs from the return layer's value. Settling this requires either reading
  the reconciliation plan and partial write-off logic end to end, or executing: deliver at 10 → invoice →
  change standard price to 50 → return → credit note, and dumping the account's lines.
- **T1-N8 — `UNRESOLVED — EVIDENCE REQUIRED`.** Whether the two layer-consumption strategies
  (`stock_account/models/stock_valuation_layer.py:197-229` vs `:161-195`) can diverge for the same credit
  note. The selector is a context key (`stock_account/models/product.py:894`) always injected by
  `sale_stock/models/account_move.py:199`, but other callers exist outside the path set
  (manufacturing-accounting layers). Settling this requires extending the path set.
- **T1-N9 — `UNRESOLVED — EVIDENCE REQUIRED`.** The purchase-side mirror matched the denominator pattern but
  was not read; it is out of scope for a customer-side track. Whether the vendor-return path exhibits the same
  independence is P01's question.
