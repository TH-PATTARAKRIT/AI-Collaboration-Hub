# G05-G08 R28 Verified Material Delta

Date: 2026-09-26

Verified static A1 closures: G05 stock Job/Config; G05 stock Cross-Module via stock_account; G08 sale Cross-Module via sale_stock. Additional static handoffs verified: G07 Purchase to Inventory via purchase_stock; G06 Manufacturing to Accounting via mrp_account. Bridge-module membership remains unassigned pending the exact governed roster.

Roster recovery blocker RT-G05G08-ROSTER-BRANCHSWEEP-016 is closed as a recovery path after deduplicated recursive-tree checks across the distinct G05-G08 evidence branches found no GROUP_STRUCTURE_V2_CORE.tsv. Exact membership remains OPEN.

Evidence-integrity contradiction RT-G05G08-PERSIST-PROV-017 is corrected: R27 branch contains an orphan sidecar explicitly marked PERSISTENCE_INCOMPLETE. R27 remains non-canonical.

G05-G08 remain A1 ACTIVE / WAIT QUESTION. A2, Reconciliation, A3 and MASTER are not started. Source Presence != Runtime Reachability. No Formal Coverage. Zero incremental cost.
