# P09_EDGE_CASE_MATRIX

**Session:** SMEPLUS-26-09-04-ACC-P09-P2A-REV2-001 · **Process:** P09 Plan-to-Analyze
**Layer:** 1 — clean-room. Evidence identifiers resolve in the Layer 2 quarantine.

Each row states a condition, what the reference pattern does, the evidence class, and the SMEsPlus requirement it generates. Rows marked **CONFIRMED BY CHALLENGE** were adversarially verified by an independent reviewer against primary source; rows marked **PLAUSIBLE** are code-path inferences awaiting verification and must not be relied upon.

---

## A. CHANGE AFTER THE FACT

| ID | Condition | Reference-pattern behaviour | Class | SMEsPlus requirement |
|---|---|---|---|---|
| EC-01 | allocation is changed on a **posted** entry | old management records destroyed, new ones created; ledger untouched | A | change is an append-only event; originals retained |
| EC-02 | allocation is changed after the **lock date** | permitted — the allocation field is in none of the three protection lists the write guard consults | A | period close binds management truth |
| EC-03 | allocation is changed on a **hash-chained** entry | permitted — the field is in no integrity-hash field list for any hash version; the chain does not break | A | the integrity envelope shall include the allocation |
| EC-04 | allocation change on a posted entry is **audited** | it is not — the field is not in the tracked-field set, so no tracking value and no chatter entry is produced | A | every allocation change is audited with before/after |
| EC-05 | entry is **reset to draft** | all its management records are destroyed | A | reversal, not destruction |
| EC-06 | a dimension value is moved to another axis | historical management records are rewritten by a **direct statement outside the ordinary write path** — no tracking, no log, no confirmation | A | historical records are immutable; use an effective-dated mapping |
| EC-07 | the rewrite would collide with an occupied destination | a redirect warning is raised and the operation stops | A | keep the guard; extend it to *all* alteration, not only collision |
| EC-08 | an axis is deleted | the column is dropped with **`CASCADE`**, taking every dependent database object with it, unenumerated and unreported | A — **CONFIRMED BY CHALLENGE** | axes are retirable, never deletable once referenced |

## B. COMPLETENESS AND ARITHMETIC

| ID | Condition | Reference-pattern behaviour | Class | SMEsPlus requirement |
|---|---|---|---|---|
| EC-10 | allocation totals less than 100 % on an optional axis | accepted silently; the remainder has no management representation at all | A | named visible residual |
| EC-11 | allocation totals more than 100 % on an optional axis | accepted silently | A | rejected at the storage layer |
| EC-12 | allocation totals ≠ 100 % on a **mandatory** axis | rejected — **but only when the caller opts in by execution context** | A | enforced unconditionally at the storage layer |
| EC-13 | a split rounds to zero at the row's precision | the split is dropped; it still counts toward the 100 % total | A | recorded, or the total adjusted; never silent |
| EC-14 | rounding residue on an axis that completes exactly 100 % | absorbed by the completing split | A | acceptable pattern; retain, but make the absorbing split identifiable |
| EC-15 | rounding residue on an axis that never completes | unallocated and unrepresented | A | see EC-10 |
| EC-16 | percentages are stored at a configurable precision | default two digits; the allocated amount is a rounded percentage of a rounded base | A | allocate by exact rational shares |

## C. SCOPE AND OWNERSHIP

| ID | Condition | Reference-pattern behaviour | Class | SMEsPlus requirement |
|---|---|---|---|---|
| EC-20 | a costed row of company A is allocated to a dimension value of company B **through the privileged axis** | blocked — that axis is a conventional relational field carrying the platform's company check | A | retain |
| EC-21 | the same, **through any other axis** | **not blocked.** Two independent structural reasons: a runtime-created relational field cannot carry a company check through that mechanism at all, and the write path does not even invoke the company check unless a checked field or the company field itself is written | A — **CONFIRMED BY CHALLENGE** (both mechanisms read in the platform source) | uniform enforcement across all axes at the storage layer |
| EC-22 | the same, through the **allocation payload** | structurally unattachable — a company check is a relational-field mechanism and the payload is a schemaless value; no substitute check found | A / B | allocation shall be relationally integral so that the check can attach |
| EC-23 | a dimension value carries **no** company | it is visible to every company | A | ownership and availability shall be separately represented (see `P09_SCOPE_OWNERSHIP_MATRIX`) |
| EC-24 | a management record carries **no** company | it is admitted into **every** company's dimension balance | A | aggregation within a declared scope only |
| EC-25 | an allocation **rule** carries no selectors at all | it matches every transaction in the database | A | prohibited, or an explicit "applies to all" declaration |
| EC-26 | the dimension **axis** is scoped | it is not — the object carries no company field and no tenant concept, and materialises as shared physical schema | A | axes are tenant-owned data |
| EC-27 | a rule's company is changed | the company-consistency check fires | A | retain |
| EC-28 | only a rule's **allocation payload** is changed | the check **does not fire** — the constraint's declared trigger is the company field alone, and the platform's validation is driven strictly by the written field names | A — **CONFIRMED BY CHALLENGE** (platform validation path read directly) | constraints shall declare every field whose change can invalidate them |

## D. ALLOCATION BECOMING A POSTING

| ID | Condition | Reference-pattern behaviour | Class | SMEsPlus requirement |
|---|---|---|---|---|
| EC-30 | a periodic reallocation rule runs | it creates **real journal entries** | A | allocation-to-ledger is a named accounting event with approval and reversal |
| EC-31 | the generated entry is still in draft when the rule runs again | its rows are **deleted and rewritten**; the source states entries are recomputed daily until posted | A | a generated document is immutable once created; re-runs create a new version |
| EC-32 | new postings arrive in a period whose generated entry is already **posted** | the next run starts after the last posted entry, and the regeneration path can only find a **draft** entry, so that period is permanently outside it | A — **CONFIRMED BY CHALLENGE** (full module read; the only escape is a manual reset to draft, which is a human act, not part of the mechanism) | late postings shall be detected and allocated by an explicit catch-up event |
| EC-33 | a rule filters by dimension value and a row is only **partially** allocated to it | the filter compiles to an **array-overlap test on the allocation's keys**; the associated percentage never enters the query. The aggregation then takes the **full balance**. The complementary unfiltered bucket excludes the same rows in full, so the unallocated remainder is not picked up anywhere either. | A — **CONFIRMED BY CHALLENGE**; every step read in full, no percentage-aware alternative path exists in the module. **This is a misallocation, not a duplication** | a dimension filter shall move the allocated share, never the whole balance |
| EC-34 | the generated entry's own dimension | **none is written**; the causing dimension survives only inside a description string | A | the causing dimension is carried as data |
| EC-35 | the rule's percentages total exactly 100 % | the last row absorbs the remainder | A | acceptable; make the absorbing row identifiable |
| EC-36 | the rule's percentages total near-but-not-exactly 100 % | the remainder stays on the source account; the remainder rule is an exact-equality test against 100.0 | A | tolerance shall be declared, not implied by a float comparison |
| EC-37 | two rows of one rule target the same destination account | prevented by a uniqueness constraint | A | acceptable, but it also prevents splitting one destination by two dimension filters |

## E. REPORTING

| ID | Condition | Reference-pattern behaviour | Class | SMEsPlus requirement |
|---|---|---|---|---|
| EC-40 | a financial report is given a dimension column | the ledger table is **replaced** by a temporary view built from management records for the rest of that report's queries | A | management figures are never sourced through the ledger's own query surface |
| EC-41 | a management record has no ledger counterpart | it still appears, admitted by an outer join, and is stamped with the **literal posting state "posted"** | A | provenance marker on every figure |
| EC-42 | the user enables the inclusion switch | the journal filter and the audit drill-down are widened to admit rows with no journal at all; the visible caption offers this as including analytic simulations | A | prohibited on any statement presented as accounting information |
| EC-43 | the report's sign | the management amount is negated to fit the ledger's convention | A | declare the convention once; state it on every equation |
| EC-44 | a management record populates two axes | the view construction expands **every** management record into one row per **root axis defined anywhere in the database**, repeating the full amount on each. An independent challenge enumerated every caller and found **exactly one** call site, which always attaches the restricting filter in the same construction — so the duplicates are always collapsed. | **DISPROVED as an exposure claim** — mechanism CONFIRMED, exposure not reachable in the scope enumerated | the row multiplication remains a latent hazard: correctness depends on one filter that one call site happens always to attach. **An aggregation shall be duplicate-free by construction, not by a co-located filter.** |
| EC-44b | a **new** exposure surfaced while disproving EC-44: two budget lines with overlapping windows and complementary blank axis filters both match the same management record, each counting its **full** amount | a blank axis column on a budget line is a **wildcard**, not "does not apply"; the matching join has no exclusivity guard and no uniqueness constraint across budget lines | CONFIRMED as a mechanism by independent challenge; whether any live configuration triggers it is a data question | budget scope shall be a declared filter set, and a blank dimension shall mean *not applicable*, never *any* |
| EC-45 | a dimension balance is read on two different days | it differs — conversion is at today's rate | A | as-at date is an input, never the reading date |
| EC-46 | a dimension balance is read by two different users | it differs — conversion targets the reader's active company currency | A | presentation currency is an input |

## F. STORAGE AND LIFECYCLE

| ID | Condition | Reference-pattern behaviour | Class | SMEsPlus requirement |
|---|---|---|---|---|
| EC-50 | a dimension value referenced inside an allocation payload is deleted | no foreign key exists on that path; dangling references are an expected state and are filtered out on read | A | referential integrity |
| EC-51 | a dimension value referenced by a management record's axis column is deleted | blocked by a delete rule on that column | A | retain |
| EC-52 | the same, on a database upgraded from an earlier version | before the current module version the delete rule was **set-to-null**, and the shipped migration converts it only for the management-record table — other carriers of the same columns are not named by it | B — boundary declared (one migration directory, fully enumerated) | migration completeness shall be proven per carrier, not per table |
| EC-53 | any database-level check constraint on the analytic or budget surface | **none found** — every integrity control is an application constraint or a foreign key | A within the two surfaces searched | the completeness and scope rules shall be enforced at the storage layer |
| EC-54 | a query filters by allocation **percentage** rather than by dimension value | no index supports it; it is a full scan by construction | A | index the allocation shape the business actually queries |
| EC-55 | the upgrade script runs on a database where the privileged-axis parameter is unset | it unpacks a query result without an existence guard and aborts — although the module's own runtime code treats that same state as expected and handles it | A | upgrade paths shall handle every state the runtime declares possible |

## G. OPEN — NOT SEARCHED, NEVER TO BE RESTATED AS ABSENCE

| ID | Item | Class |
|---|---|---|
| EC-U-01 | budget control implemented outside the two budget modules | C |
| EC-U-02 | alternative reporting aggregation for the seven non-groupable allocation carriers | C |
| EC-U-03 | producers reached through a variable-held model name | C |
| EC-U-04 | a compensating migration for non-management-record plan-column carriers, in other modules' migration directories | C |
| EC-U-05 | which of the three tenant custom copies is deployed, and therefore whether the department dimension exists at all | D |

## TERMINAL STATE

**MATRIX ISSUED. 6 ROWS CONFIRMED BY INDEPENDENT CHALLENGE, 1 ROW DISPROVED AS AN EXPOSURE CLAIM, 1 NEW ROW ADDED BY THE CHALLENGE THAT DISPROVED IT, 5 ITEMS OPEN. NO GATE MOVED.**
