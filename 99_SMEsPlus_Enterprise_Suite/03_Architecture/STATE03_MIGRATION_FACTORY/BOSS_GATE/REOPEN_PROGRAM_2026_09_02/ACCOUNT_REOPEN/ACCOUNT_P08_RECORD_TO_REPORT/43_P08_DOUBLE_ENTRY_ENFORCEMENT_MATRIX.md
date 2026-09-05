# P08_DOUBLE_ENTRY_ENFORCEMENT_MATRIX

Session `SMEPLUS-26-09-04-ACC-P08-R2R-TARGETED-FORENSIC-CLOSURE-001` · `CP-T06`

Invariant under test: **for one journal entry, the sum of its items' reporting-currency balances is zero.**

## 1. The stack, layer by layer

| # | Layer | Present | What enforces it | What defeats it |
|---|---|---|---|---|
| 1 | Client interface | **absent** | nothing — the form only *displays* totals | n/a |
| 2 | **The posting method** | **absent** | **the posting method contains no balance assertion at all.** It runs fourteen other validations and relies entirely on its own status write re-entering layer 3 | any path reaching the posted status without passing through the object-layer write |
| 3 | **Object layer** | **present — the sole real enforcement** | one query wrapped around create, write, unlink and the settlement plan: group by entry, reject a non-zero rounded sum | the context switch at layer 4 |
| 4 | **Context** | present **as a switch, not a control** | a single caller-supplied key returns the check before the query runs | supplying the key |
| 5 | Caller parameter | present, and **asymmetric** | the check inspects only the record set the caller passed in | a line moved between entries has its **destination** unchecked; the pre-seeding covers only two of the three command forms |
| 6 | Declared model constraints | **absent** | zero of the eight declared constraints on the two models concerns entry balance | n/a |
| 7 | **Database** | **absent** | one uniqueness constraint on the entry, four **per-row** checks on the item. No aggregate check, no trigger, no deferred constraint | any write reaching the database |
| 8 | Transaction boundary | **absent** | nothing runs at commit | n/a |
| 9 | Background job | **absent as a check** | no scheduled job re-verifies the balance of a posted entry | an entry written unbalanced stays unbalanced |
| 10 | **External control** | present, optional, **and not deployed** | a separate installable consistency-test module | see §3 |

**Verified by the author:** the posting method contains no balance assertion; the raw-database state flip of §4 exists; the analytic validation defaults to off.

## 2. What this means

The invariant has **exactly one line of defence**, at the object layer, and that line is switched off by a value the caller supplies. Everything else in the stack is either absent or downstream of it.

**Auto-repair is not enforcement.** An automatic balancing line exists, but only for plain journal entries, only before posting, and **only when taxes are involved** — and it lives inside a synchronisation block that another caller-supplied key disables.

## 3. The external control, and its deployment status

The only balance check outside application code is a separate consistency-test module. Verified:

- It is **not installed by default**, has **no scheduled run**, and produces a report on demand.
- Its first test sums debits and credits **across the whole table with no company and no currency filter** — in any database with more than one company currency it returns non-zero by construction and is uninterpretable.
- Several of its eight seeded tests reference schema removed long before the version under study and would raise on execution.
- **It is `uninstalled` in all three deployed databases.**

`FACT VERIFIED`. **The only control that could detect an unbalanced entry after the fact is absent from every deployment examined, and would be scope-blind if present.**

## 4. A posting-control bypass that needs no context key

Writing an ordinary configuration threshold on a company executes **four raw database statements** that set entries to posted or cancelled and update their items' mirrored status to match — with **no posting method, no number assignment, no seal, no period check, no balance check and no audit entry**. `FACT VERIFIED`, read by the author.

This is not an imbalance route. It is a **posting-status route that bypasses the entire stack above**, and it is reachable by writing one field on a company record.

## 5. Indirect imbalance

Tested and **not found**: exchange-difference generation, cash-basis tax generation, cash rounding, and the settlement path all emit mirrored pairs and remain inside the object-layer check. The raw database statements in the settlement code touch matching fields only — never debit, credit or balance.

**Two caller-supplied levers remove rounding from tax computation**, and **neither has a single setter anywhere in the reference tree**. Whether either can drive an entry past the rounding tolerance is `UNRESOLVED — EVIDENCE REQUIRED`.

The overall negative — *no mechanism produces an unbalanced posted entry without a context key* — is **class C**, bounded by the declared population and patterns. It is not a statement that none exists.

## 6. Reconciliation with the deployed data

Phase C measured **0 unbalanced posted entries in the reporting currency** across 169,143 posted entries, and **1,851 unbalanced in transaction currency** of which 53 have multiple non-offsetting foreign-currency lines.

Both results are consistent with this matrix. The reporting-currency invariant has one line of defence and it evidently held in that database. **The transaction-currency invariant has no line of defence at any layer** — the check sums one currency frame only — and that is precisely the frame in which 53 posted entries are unbalanced.
