# SMEsPlus Community19 - G05-G08 RED TEAM A1 Static Delta R10

Date: 2026-09-25 Asia/Bangkok
State: G05/G06/G07/G08 = A1 ACTIVE -> WAIT QUESTION. No A2, Reconciliation, A3, MASTER or Formal Coverage.

Roster control: governed counts remain G05=14, G06=12, G07=9, G08=31. Controlled roster pointer remains GROUP_STRUCTURE_V2_CORE.tsv SHA-256 203ff43e7844a734de5e9aaebb91529e46dd7998423d4d5772999ed0db9ff5bf. Boss scope-rebase commit 3ede541ad8af7e5ec3c1c55902a3e052e6005a03 was re-read and still requires exact row-level reconstruction. GitHub exposes references/hash only; Drive search returned no accessible controlled roster; authorized desktop is currently offline. No inferred module membership is admitted.

Question Gate: current governed repository search returned no frozen/eligible G05-G08 question-bank package. Existing verified frozen GMVQ evidence is G01-specific. No QID was invented and no gate was bypassed.

G05 INVENTORY new A1 anchors:
- addons/stock/wizard/stock_backorder_confirmation.py blob 0cae055dd64c79576ddf2df65accbe009f3b9c67
- addons/stock/models/stock_move_line.py blob daf5027705acff05272af2ad0fdf64a101e71bb8
Findings: explicit per-transfer backorder decision; no-backorder path re-enters picking validation with skip_backorder control and logs short-picked quantities; move lines enforce company-aware product/location/package/lot links; negative quantity and lot/product mismatch guards; serial duplicate/location checks; serial quantity one-unit control; explicit putaway path. Source only, not runtime proof.

G06 MANUFACTURING new A1 anchors:
- addons/mrp/wizard/mrp_production_backorder.py blob cac73f6626a9b742c4ea548eccb438f36a8e59e0
- addons/mrp/wizard/mrp_consumption_warning.py blob 167878e026de5a1a541d77226726923c19279903
Findings: per-MO backorder decision; close/backorder paths re-enter button_mark_done with explicit context; consumption policy is flexible/warning/strict; correction can normalize raw-move quantities, mark picked, create missing additional raw moves, and rejects traceability gaps for tracked products. Source only, not runtime proof.

G07 PURCHASE new A1 anchors:
- addons/purchase/models/res_partner.py blob f2400a90b80e05994b6698fe3b9f7c9898218f34
- addons/purchase/models/account_invoice.py blob 47e2230f40b1864ce12e8d8c03446e879a14aa29
Findings: supplier currency and receipt-reminder controls are company-dependent; PO statistics are Purchase-user restricted; vendor-bill matching is company-scoped and ambiguity/time-out aware; it can reconcile PO/vendor references, totals, remaining PO-line amount, quantity, price and description; bill lines retain purchase-line/order lineage and analytic distribution. Source only, not runtime proof.

G08 SALES new A1 anchor:
- addons/sale/wizard/sale_make_invoice_advance.py blob 6bc18546e5adc65cc9ddd97f16c688c215edde24
Findings: invoice wizard distinguishes regular, percentage-down-payment and fixed-down-payment paths; down-payment amount must be positive; regular invoicing controls final deduction/grouping; down-payment path computes tax bases, creates down-payment SO lines and Accounting invoice values; account selection is company/fiscal-position aware. Source only, not runtime proof.

Integrity: A1_SOURCE_EVIDENCE_SHA256_20260925_R5.txt still points to G05_G08_RED_TEAM_A1_STATIC_DELTA_R5_20260925.md, but the detailed R5 file returns GitHub 404. Do not treat that pointer as complete evidence.

No Evidence = No Progress. Source Presence != Runtime Reachability.
