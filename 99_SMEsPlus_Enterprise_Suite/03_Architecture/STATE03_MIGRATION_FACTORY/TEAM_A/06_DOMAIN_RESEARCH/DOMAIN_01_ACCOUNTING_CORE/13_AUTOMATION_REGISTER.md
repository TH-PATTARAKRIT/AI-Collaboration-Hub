> DOMAIN_01 — Accounting Core | Team A (Maker) | READ ONLY | No target design | Boss sole Final Approver

# 13 — AUTOMATION REGISTER

| ID | Automation | Trigger | Observed effect | Evidence |
|---|---|---|---|---|
| AU-01 | Auto-post | `auto_post` on the entry, with a required date | Entry posts without manual action | SE-06 |
| AU-02 | Balance assertion | create / write | Raises UserError naming unbalanced entries | SE-03 |
| AU-03 | Balance assertion suspension | context flag | Silently skips AU-02 for a block of work | SE-04 |
| AU-04 | Name computation | post / state change | Assigns entry number from journal sequence | SE-13 |
| AU-05 | Secure sequence advance | post on hash-protected journal | Gapless counter increments | SE-13 |
| AU-06 | Reversal auto-reconciliation | posting a draft reversal of a posted original | Reversal reconciled to the original automatically | SE-09 |
| AU-07 | parent_state propagation | header state change | State copied down to all lines | DB relationship register |
| AU-08 | Dynamic line synchronisation | create/write (`_sync_dynamic_lines`) | System-generated lines maintained alongside user lines | SE-05 context |

**AU-08 caution.** The core maintains *system-generated* lines (tax lines, payment terms lines,
rounding) alongside user-entered lines within the same entry. A migration that treats every
line as user-authored will double-count. Detail deferred to the Tax/AR/AP domains.
