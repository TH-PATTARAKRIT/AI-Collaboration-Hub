# G05-G08 A1 Static Delta R3 - 2026-09-25

Control: four stations ACTIVE in A1. Governed counts remain G05=14, G06=12, G07=9, G08=31. Exact technical rosters remain open. The authorized desktop source device is offline, so local Community19 package and row-level GROUP_STRUCTURE_V2_CORE.tsv cannot be re-read. Historical roster pointer is carried forward only: 203ff43e7844a734de5e9aaebb91529e46dd7998423d4d5772999ed0db9ff5bf.

Question gate re-check: current COMMUNITY19/GMVQ tree still has no governed/frozen G05, G06, G07 or G08 question-bank directory. All four stations remain A1 -> WAIT QUESTION. No A2/Reconciliation/A3/MASTER.

G05 verified source delta: stock_location.py 51bd3117fec1eb09ebf5d48564c7fc7048c10b5c; stock_orderpoint.py cc1b7e551e186145cc7f6f3a6477f332267183e1; stock_warehouse.py 9eef52627b615ad7ee5507e037517cd258fe81d7. Static evidence covers company/shared locations, guarded location changes, cyclic inventory, putaway/removal controls, 1/2/3-step receipt and delivery configuration, Auto/Manual replenishment triggers, and company-scoped orderpoint identity.

G06 verified source delta: mrp_workcenter.py e751fbedc7724e67665bcb8263988dda07303ee7; mrp stock_rule.py 4e6d16abcea85b0ea4145c1a14d87b52ecf406dd. Static evidence covers workcenter state/OEE/capacity and company-grouped manufacture-order creation from stock-rule procurement.

G07 verified source delta: purchase_order_line.py 813d171324d3ab05ddb55b4d2f2550b4364877f2. Static evidence covers company-derived PO lines, received/billed/to-invoice quantities, a base manual received-quantity path with stock-move extension seam, and invoice-line preparation.

G08 verified source delta: sale_order_line.py c959c38550d834cb89dbbea58bc74f7522083ff7. Static evidence covers ordered/invoiced/to-invoice quantities, company-filtered taxes, invoice-line preparation and an empty base procurement-values extension seam.

Control correction: A1_SOURCE_STUDY_INDEX_20260924.md was corrected from QUEUED to ACTIVE / ROSTER RECONCILIATION / WAIT QUESTION for G05-G08.

Source Presence != Runtime Reachability. No Evidence = No Progress. Formal Coverage remains prohibited.
