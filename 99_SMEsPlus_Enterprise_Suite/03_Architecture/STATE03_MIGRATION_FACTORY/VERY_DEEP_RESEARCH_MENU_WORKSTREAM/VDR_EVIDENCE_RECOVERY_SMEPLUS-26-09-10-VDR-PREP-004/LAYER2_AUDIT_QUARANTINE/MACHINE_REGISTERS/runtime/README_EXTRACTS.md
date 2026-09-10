**LAYER 2 — AUDIT QUARANTINE.**

# Runtime extracts — what is here, what is not, and how to regenerate it

Every table below was produced by, per deployment and per table:

```
pg_restore --data-only -t <table> -f - <dump>
```

then parsed from the resulting COPY block. **No database server was started at any point.**
A current-generation client is required: an older client fails on the archive header, which is a loud
failure and was treated as a blocker, never as an absence.

## Retained here
`ir_ui_menu` · `res_groups` · `ir_module_module` · `ir_config_parameter` · `ir_cron` · `res_company` ·
`product_category` — the small tables that carry configuration and installation state.

## Deliberately omitted for size — a DECLARED EXCLUSION, not a gap
`ir_model_data` · `ir_model_fields` · `ir_model_constraint` · `ir_model_access` · `stock_move`

Together these exceed 190 MB. **`RUNTIME_EXTRACT_INDEX.json` records every one of them with its row
count and its SHA-256**, so a reviewer can regenerate each file with the command above and verify it
byte-for-byte against the hash this session used. Nothing is unverifiable; it is unbundled.

The element-level observation these tables produced is preserved in full, per item, in
`../runtime_observation.json` and in the `RUNTIME_CONDITION` column of the population register.
