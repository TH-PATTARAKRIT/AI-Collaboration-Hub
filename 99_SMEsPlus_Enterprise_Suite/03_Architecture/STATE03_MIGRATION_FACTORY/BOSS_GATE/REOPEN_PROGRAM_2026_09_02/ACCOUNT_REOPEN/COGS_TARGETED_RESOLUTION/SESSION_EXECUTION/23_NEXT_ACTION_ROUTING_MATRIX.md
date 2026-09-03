# 23 — Next Action Routing Matrix

Every concrete next action named anywhere in this package, consolidated into one routing table. Ordered by the mandated priority sequence.

| # | Action | Owner | Parallelizable With | Blocks | Effort (qualitative, no invented estimate) |
|---|---|---|---|---|---|
| 1 | Answer `SME-Q-03` (invoice/delivery sequencing) | Business SME | #2, #3, #4 | `JT-04`, Model A/B/D selection (file 11) | Low — single stakeholder conversation |
| 2 | Research `TH-NEW-01` (TAS 2 trigger-event constraint) | Thai Accounting-Tax track | #1, #3, #4 | `JT-04` | Medium — primary-source research pass |
| 3 | Re-fetch `CGS-U20`/`CGS-U31` (invoicing-policy/timing interaction) | Docs/Research owner | #1, #2, #4 | `JT-04` | Low — bounded page fetch(es) |
| 4 | Answer `SME-Q-02` (return cost-basis preference) | Business SME | #1, #2, #3, #5, #6 | `JT-05` | Low — single stakeholder conversation |
| 5 | Research `TH-NEW-02` (TAS 2 costing-consistency vs. returns) | Thai Accounting-Tax track | #1–#4, #6 | `JT-05` | Medium — primary-source research pass |
| 6 | Live-instance FIFO-return test, or stronger primary source | Research owner (needs live-instance access) | #1–#5 | `JT-05` FIFO sub-case | Medium-High — requires live-instance access this session lacked |
| 7 | Answer `SME-Q-01` (non-sale value-decrease classification practice) | Business SME | All above | `JT-01` (secondary), `JT-06` design | Low — single stakeholder conversation |
| 8 | Re-fetch six `JT-01` sub-items (`CGS-U06,U09,U11,U12,U13,U42` partial) | Docs/Research owner | All above | `JT-01` | Low-Medium — six bounded page fetches |
| 9 | Live-instance test for `CGS-U07`/`CGS-U08` | Research owner (blocked) | All above | `JT-01` | Medium-High — requires live-instance access |
| 10 | Re-fetch `CGS-U03` scope conflict (Price Difference vs. Variation Account) | Docs/Research owner | All above | `JT-02` | Low |
| 11 | Re-fetch `CGS-U34`/`CGS-U36` A-vs-B version pinning | Docs/Research owner | All above | `JT-08` (documentation sub-part only) | Low |
| 12 | Boss ruling: landed-cost-after-sale control design (independent of #11's outcome) | Boss | All above | `JT-08`, Audit VETO closure | n/a — decision, not research |
| 13 | Re-read the already-approved 16-field handoff contract for `CGS-U41` | Docs owner | All above | none named (cheap, do anytime) | Very low — no new research needed |
| 14 | Create `GAP-FS-08` artifact, prerequisite to `CGS-U45` | Design/Docs owner | All above | Migration duplicate-posting design | Low — artifact creation, not research |

## Notes

- Actions #1–#9 cover the full evidence path for the three priority Joint Decisions and are the recommended focus of the next targeted-resolution session.
- Actions #10–#14 are lower-priority (P1/P2-tier) and can be deferred without blocking the priority path.
- No action in this table requires this session's unavailable tools to *plan* — only to *execute*. This table is itself executable without further research; it is a routing artifact, not a research output.
