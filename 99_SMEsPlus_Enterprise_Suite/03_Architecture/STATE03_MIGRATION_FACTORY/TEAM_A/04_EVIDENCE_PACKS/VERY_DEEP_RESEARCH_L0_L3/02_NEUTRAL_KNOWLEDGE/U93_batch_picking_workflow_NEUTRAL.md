# U93 Neutral Knowledge — Batch Picking Workflow
> NEUTRAL LAYER — no source paths, no class/method names, no file extensions, no snake_case, no backticks

| NR-ID | Statement |
|---|---|
| NR-U93-001 | A batch transfer record aggregates multiple warehouse transfer operations into a single managed unit; it supports messaging and activity tracking. |
| NR-U93-002 | The lifecycle of a batch transfer has four stages: Draft, In Progress, Done, and Cancelled; the current stage is computed automatically from the states of the included transfers. |
| NR-U93-003 | A batch transfer holds a list of individual transfer operations (pickings); this list is filtered to show only compatible, non-completed transfers. |
| NR-U93-004 | All stock movements belonging to transfers in a batch are accessible in aggregate through the batch record, enabling a single-screen overview. |
| NR-U93-005 | A Boolean flag on the batch record distinguishes regular batch transfers from wave transfers, which are a related but distinct concept used to group individual operation lines rather than whole transfers. |
| NR-U93-006 | Only transfers in the states Waiting, Confirmed, or Ready (assigned) may be added to a batch; Draft transfers are additionally allowed while the batch itself is still in Draft. |
| NR-U93-007 | The batch stage is recomputed whenever any included transfer changes its own state, so the batch automatically reflects the aggregate completion status. |
| NR-U93-008 | When every transfer inside a batch is individually cancelled, the batch itself transitions to Cancelled automatically. |
| NR-U93-009 | When every transfer in a batch is either Done or Cancelled (with at least one Done), the batch transitions to Done automatically. |
| NR-U93-010 | Confirming a batch calls confirmation on each included transfer and moves the batch to In Progress; a batch with no transfers cannot be confirmed. |
| NR-U93-011 | Attempting to confirm an empty batch raises a user-visible error. |
| NR-U93-012 | The batch validation action performs a collective sanity check across all included transfers before delegating actual validation to each individual transfer's own validate routine. |
| NR-U93-013 | Transfers that are waiting or confirmed with no processed quantities are silently detached from the batch instead of being cancelled when the batch is validated. |
| NR-U93-014 | The batch-level validation passes a context flag to individual transfers so they skip their own duplicate sanity check, avoiding redundant processing. |
| NR-U93-015 | Final validation of each transfer is performed by delegating to the standard individual transfer validation mechanism, not by a separate batch-specific action. |
| NR-U93-016 | When an individual transfer is validated independently while it belongs to a batch, the system checks for state consistency; if other transfers in the same batch are not yet done, the validated transfer is removed from the batch to prevent inconsistent batch state. |
| NR-U93-017 | Validating a single transfer independently inside a batch detaches it from the batch if the remaining transfers are not all done, preserving the integrity of the batch lifecycle. |
| NR-U93-018 | Any backorder transfers created during batch validation are collected and submitted to the automatic batch assignment mechanism so they can be grouped into a new or existing batch. |
| NR-U93-019 | When a backorder is created for a transfer that is being validated independently within a batch, the original transfer is removed from the batch before the backorder is produced. |
| NR-U93-020 | After a transfer is confirmed or after stock is reserved (assigned) for a transfer, the system attempts to automatically place the transfer into a matching batch if the operation type has automatic batching enabled. |
| NR-U93-021 | Automatic batch assignment is skipped when the operation type does not have automatic batching enabled, when the transfer already belongs to a batch, when the transfer has no movements, or when the transfer does not meet the batch eligibility criteria. |
| NR-U93-022 | Before adding a transfer to an existing automatic batch, the system checks that configured maximum-lines and maximum-transfer limits for that batch will not be exceeded. |
| NR-U93-023 | Adding operation lines to a wave may split an existing transfer into two parts: one part joins the wave, the other part remains in the original transfer. Splitting occurs only when a subset of lines is being wave-assigned. |
| NR-U93-024 | When all operation lines of a transfer are selected for a wave, the whole transfer is linked to the wave without splitting. |
| NR-U93-025 | After stock reservation is performed for movements, the system automatically attempts to group resulting operation lines into wave transfers based on the wave grouping criteria configured on the operation type. |
| NR-U93-026 | When an individual stock movement is cancelled and its parent transfer becomes cancelled, the transfer is removed from its batch if other transfers in that batch are still active. |
| NR-U93-027 | Confirming a transfer triggers the automatic batch assignment process, so transfers can be placed into batches at the moment they are confirmed. |
| NR-U93-028 | All warehouse staff users have full create, read, update, and delete rights on batch transfer records; there is no separate elevated group required for batch creation or validation at the access control list level. |
| NR-U93-029 | Access to batch transfer records is restricted by a multi-company rule so users can only see batch transfers belonging to their allowed companies. |
| NR-U93-030 | Cancelling a batch sets its stage to Cancelled and detaches all included transfers from the batch simultaneously. |
| NR-U93-031 | When a new warehouse is configured, its inbound and outbound operation types are created with automatic batching enabled and grouped by contact (partner) by default. |
| NR-U93-032 | A dedicated user-interface wizard allows operators to assign selected transfers to either a new batch or an existing in-progress or draft batch; the newly created batch is automatically confirmed unless the operator requests draft creation. |
