# 10 — Remediation Action Register

Session: `SMEPLUS-26-09-02-INV-CLEANROOM-REAUDIT-001` | Control Level: `/L999.999`

Every action below traces to a specific finding in `02`–`09`. No action here is self-executed by this session — prompt §2 prohibits modifying source evidence except as a "separately proposed remediation list," which is what this register is.

---

| # | Finding | Source | Action | Owner | Priority | Blocking? |
|---|---|---|---|---|---|---|
| R-01 | Original leaked vendor code (commits `ac9e1e40`, `0eb78c68`) remains reachable via `git show <SHA>:<path>` by any repository reader | `02` §4, §6 | Boss decision required: either (a) restrict read access to these specific historical objects at the hosting/repository-permission level, or (b) accept policy-only quarantine as sufficient and document that acceptance explicitly, or (c) commission a coordinated history rewrite (all clones invalidated) if the risk is judged unacceptable | Boss | **Highest** | **Yes — blocks any `C-05 CLOSED` determination** |
| R-02 | File `10_WAREHOUSE_LOCATION_ROUTE_RULE_MAP.md` reproduces a near-verbatim benchmark location-path scaffold (`WH/Stock`, `WH/Input`, `WH/Quality`, `WH/Output`, `WH/Packing`) | `03` §4, `05` §4 | Rewrite §2 as prose location-role descriptions; re-derive the location *set* (not just relabel it) from Thai warehouse practice once TBRAC evidence exists, rather than carrying the benchmark's five-node structure forward | Package maintainers (menu-deep-challenge branch) | Medium | No — narrow, correctable, does not block Boss review of the package as a whole |
| R-03 | Doc `21`'s "Convergence" section cites `25 §6` for required-evidence content that does not exist there (it exists in `24 §4` instead) | `04` §2 | Correct the citation in doc `21` to reference `24 §4` only | Package maintainers | Low | No |
| R-04 | The `R:` external-citation convention (reference into the separate reopen package) is used consistently but never documented inside the 29-file package | `04` §2, `09` E3 | Add one explanatory line defining `R:NN §X` as "external citation into the Inventory Full Reopen package, commit `170af9ea`" near the top of any file that uses it, or in a shared glossary file | Package maintainers | Low | No |
| R-05 | Product Category is framed (in `08`, `15`) as the natural owner of both storage/putaway grouping and valuation policy — a benchmark architectural coupling, not a demonstrated Thai requirement | `05` §2 | Resolve at the Account × Inventory Joint Session (doc `26` action #5) or a direct Boss ruling — decide whether valuation policy belongs on Product Category, a separate object, or a jointly-owned object | Boss / Joint Session | Medium | No — correctly deferred already, not newly blocking |
| R-06 | Systemic: behavioral/process claims in `06` and the operational maps read as confident declarative prose without a per-claim Thai-fitness hedge, even though file headers carry the hedge | `05` §1 | On next revision, add inline hedging at the paragraph or table-row level for behavior-defining claims, not only in file status lines; alternatively, any prompt that hands this package to a future reading session should restate the hedge explicitly in that prompt | Package maintainers / future prompt author | Medium | No |
| R-07 | SHA-256 manifest verification in this re-audit covered only 5 of 29 package files (sample, not exhaustive) | `04` §4, `07` Track 04 | If full manifest assurance is required before any stronger reliance classification, run a complete 29-file recomputation rather than relying on this session's 5-file sample | Whoever performs the next audit pass | Low | No |
| R-08 | Delegated evidence-gathering passes in this session were spot-verified, not exhaustively independently re-derived | `07` Track 09 | Disclosed as a limitation here; no action required unless Boss wants full independent re-derivation for a higher-assurance re-audit | Boss (if desired) | Low | No |

---

## Priority Summary

**Blocking action:** R-01 only. Everything else is correctable at the package-maintenance level or is a deferred design/governance question already correctly routed to Boss or a Joint Session, not a new blocker this re-audit introduces.

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
