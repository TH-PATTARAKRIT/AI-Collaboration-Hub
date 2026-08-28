> DOMAIN_01 — Accounting Core | Team A PART 2 (Sonnet) | Input: committed Part 1 evidence | No SMEsPlus design

# 09 — EXCEPTION & FAILURE ANALYSIS

For each scenario: Expected Business Principle / Reference-System Behaviour / Independent
Evidence / Risk / Unknown. Scenarios not evidenced are marked UNKNOWN rather than guessed.

| Scenario | Expected principle | Reference-system behaviour (evidenced) | Independent evidence | Risk | Unknown |
|---|---|---|---|---|---|
| Unbalanced entry | Must be refused (GR-01) | Refused by application code, UNLESS the check is suppressed (`_disable_recursion`); no DB backstop | AP-01 | An unbalanced entry can reach storage if the suppression path is exercised | Whether it has, in this snapshot (GAP-D01-11) |
| Closed period | Must be refused without override (GR-05) | Refused by six independent lock checks, UNLESS `BYPASS_LOCK_CHECK` context is set | AP-06 | Six controls can disagree; bypass is a code-level escape hatch | Whether the six controls have ever disagreed in practice |
| Invalid account | Line must reference a real account | DB CHECK `check_accountable_required_fields` refuses null account on financial lines | — | Low — DB-enforced | none material |
| Inactive/deprecated account | Should not accept new postings | Deprecation is guarded, but **only against tax-repartition usage**, not general posting usage | — | An account could be deprecated while still in other active use | Whether posting to a deprecated account is separately blocked (not evidenced) |
| Wrong company | A transaction must not cross company boundaries | `company_id` FK present on core tables; no cross-company posting path was evidenced as blocked or permitted | — | UNKNOWN in either direction — absence of an observed cross-company posting is not proof it is blocked | Whether company-boundary enforcement exists beyond FK typing |
| Currency mismatch | Currency amount and company amount must be consistent | DB CHECK enforces sign agreement; rate validity checked at header (BR-06) | AP-07 | Per-line remeasurement over time (IAS 21) not evidenced | Whether periodic remeasurement exists at all |
| Rounding discrepancy | Rounding policy must be defined and applied consistently | `decimal_precision.py` exists, unread | — | Cannot be assessed | Entire rounding policy — GAP-D01-04, genuinely UNKNOWN |
| Duplicate accounting event | Should not double-post the same fact | `_fetch_duplicate_reference` exists (SE evidence in Part 1, matching_states draft/posted) suggests a duplicate-detection path exists | — | Mechanism exists; effectiveness/coverage not evidenced | Whether it catches all duplicate classes |
| Backdated posting | Should be subject to the same period controls as any other date | No evidence of a *separate* rule for backdating beyond ordinary lock-date checks | — | If a backdated entry falls inside an OPEN period, it is permitted — this is not necessarily wrong, but was not specifically evidenced as a distinct control point | Whether any additional scrutiny applies to backdated entries |
| Future posting | UNKNOWN whether restricted | No evidence either way was found in this pass | — | UNKNOWN | Genuinely unresearched this pass |
| Unauthorized posting | Only authorized users/roles should be able to post | Not analysed this domain pass (security domain, deferred per scope) | — | Deferred, not zero | Full security/permission model unread |
| Unauthorized reset/reopen | Only authorized users should reopen posted entries | `button_draft`'s guard is status-based, not evidenced as role-gated at the core-model level | — | If reopening is available to the same role that can post, this compounds CF-06's weakness | Whether a permission layer restricts this beyond the core guard |
| Reversal | Correct pattern; should always be available | Confirmed present and auto-reconciling (CF-04) | AP-05 | Low — genuine strength | none material |
| Repeated reversal | A reversal of a reversal — should be well-defined | Not specifically traced; `reversed_entry_id` is a simple FK, so a reversal-of-a-reversal is structurally possible but its semantics were not traced | — | Could create ambiguous chains if not constrained | Whether the model prevents or defines double-reversal |
| Missing reference | An entry should be traceable to its originating business event where applicable | Not analysed this pass (would require tracing `ref`/origin fields, deferred) | — | Deferred | Not researched this pass |
| Imported invalid history | Migrated data may already violate GR-01/GR-05/etc. | This is precisely CF-01/CF-03's consequence — the source system does not guarantee these hold historically | AP-01, AP-06 | **Direct migration risk** — cannot assume source history is internally valid | Extent of actual violation — data-level, unproven |
| Migration imbalance | A migrated entry might not balance even if it appeared to in the source | Same root cause as above | — | Must independently re-validate GR-01 on every migrated entry | Same as CF-01 |
| Concurrent changes | Two users editing related records simultaneously should not corrupt state | Not analysed this pass — would require tracing ORM-level locking, out of scope for a read-only forensic pass | — | Deferred | Not researched; concurrency control entirely unevidenced |

## PATTERN ACROSS ALL SCENARIOS
Every scenario where the reference system shows a **weakness** traces back to one of three
root causes already identified as critical findings: **CF-01** (suppressible balance check),
**CF-03** (bypassable lock check), or **CF-06** (mutable posted history). No new root cause was
discovered by this exception sweep — it confirms the critical-finding set is complete for the
scenarios that evidence could reach, and surfaces several genuinely new UNKNOWNs (future
posting, concurrency, unauthorized reopen, repeated reversal) that were not previously
registered as gaps in Part 1.
