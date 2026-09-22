# WIP Policy

- Maximum active worker processes: 4.
- Each module/role/attempt has a unique context, PID, log and output directory.
- Launch order follows `01_MODULE_QUEUE.tsv`.
- No duplicate writer key.
- If a worker ends without a valid answer manifest, mark correction required; do not treat it as complete.
- If no A2 profile exists, do not invent runtime evidence and do not stop unaffected A1 work.
