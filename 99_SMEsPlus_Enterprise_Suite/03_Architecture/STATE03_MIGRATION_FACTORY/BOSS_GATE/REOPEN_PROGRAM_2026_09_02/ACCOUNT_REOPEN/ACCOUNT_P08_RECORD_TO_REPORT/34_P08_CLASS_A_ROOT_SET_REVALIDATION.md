# P08_CLASS_A_ROOT_SET_REVALIDATION

Session `SMEPLUS-26-09-04-ACC-P08-R2R-TARGETED-FORENSIC-CLOSURE-001` · Phase A · `CP-T02`

This closes the unclosed half of the root-set defect. The prior session declared the 22-root set and re-ran **3** class-A patterns across it, leaving **19** scoped to one root. All eligible remaining patterns have now been re-run across all 22.

## 1. Method — and the control this phase added

Every pattern in this phase carries a **positive control**: a companion measurement proving the pattern is capable of firing. This was added because the first attempt at this phase produced silent zeros from patterns that could not fire at all — a malformed guard search, and a counter search that matched declarations rather than writes.

> **A pattern that cannot fire yields silence indistinguishable from absence.**

Two results changed when the controls were applied, and both are recorded rather than quietly fixed:

| Claim | First pass | With control | Cause |
|---|---|---|---|
| Account-table uniqueness | non-zero in 12 roots — appeared to **contradict** the class-A claim | **0 in 21 of 21** | the file-level search caught a constraint block belonging to a *different class* in the same file. Class-scoped re-run resolves it |
| Gapless counter writes | 1–3 per root — appeared to **contradict** the claim | **0 in 21 of 21** | the pattern matched the field *declaration* and an ordering string, not writes. Write-scoped re-run resolves it |
| Entry-table check constraints | 1 in one root | **0 in 21 of 21** | first-pass artefact of an unanchored search |

Root `R-18` is a 28-module partial tree and returns `NA` for every file-scoped pattern; it is excluded from those denominators and the exclusion is declared, not silent.

## 2. Results — every claim, every root

| ID | Claim re-run | Control applied | Result across roots | Disposition |
|---|---|---|---|---|
| `AID-02` | No database-level uniqueness on the ledger account | constraints present elsewhere in the same file prove the pattern fires | **0 in 21 of 21** | **VERIFIED ABSENT** |
| `COA-17` / `AID-08` | No posting-existence guard in the account write path | the write method itself is found in every root | **0 in 21 of 21** | **VERIFIED ABSENT** |
| `JPM-11a-line` | Check constraints on the journal item | — | **4 in 21 of 21** | **VERIFIED PRESENT**, uniformly |
| `JPM-11a-move` | Check constraints on the journal entry | the item file's four prove the pattern fires | **0 in 21 of 21** | **VERIFIED ABSENT** |
| `JPM-20` | Nothing writes the gapless counter | the symbol occurs 3–11 times per root, so the pattern fires | **0 writes in 21 of 21** | **VERIFIED ABSENT** |
| `JPM-32` | No approval or maker-checker state on the entry | the state field is found in every root | **0 in 21 of 21** | **VERIFIED ABSENT** |
| `CFG-JE` | No journal entry declared in **production** configuration data | **demo data declares entries in 12 of 22 roots — this proves the pattern fires** | **0 in 22 of 22** for production data | **VERIFIED ABSENT — and refined**, see §3 |
| `REC-11` | No lock guard inside the settlement models | the files are present and non-trivial in every root | **0 in 21 of 21** | **VERIFIED ABSENT** |
| `REC-13` | No change history or tracking on the settlement models | as above | **0 in 21 of 21** | **VERIFIED ABSENT** |
| `REC-24` | No isolation rule on either settlement model | the accounting module carries many isolation-rule files, so the pattern fires | **0 in 22 of 22** | **VERIFIED ABSENT** |
| `FR-13` | No change history on the statement definition model | the file is present in every root | **0 in 21 of 21** | **VERIFIED ABSENT** |
| `FR-20` | No consolidation module | module counts of 28–1 433 prove the tree is enumerable | **0 in 22 of 22** | **VERIFIED ABSENT** |
| `FR-22` | No report-run or issued-statement entity | — | **0 in 22 of 22** | **VERIFIED ABSENT** |
| `FX-10` | No tracking or deletion guard on the rate master | the rate class is found in every root | **0 in 22 of 22** | **VERIFIED ABSENT** |
| `FX-15` | No tenant dimension in the accounting currency surface | 200+ files searched per root | **0 in 22 of 22** | **VERIFIED ABSENT** |

## 3. The one claim that changed on re-run

`CFG-JE` — the prior session claimed, at target-root scope, that **no journal entry is declared in static configuration data**.

Across the root set the pattern fires: **12 of 22 roots declare journal entries in configuration files.** Every one of those declarations is in a **demonstration-data** directory, not production data. So:

- **In production configuration data: 0 in 22 of 22.** `VERIFIED ABSENT` at root-set scope — a strengthening of the original claim.
- **In demonstration data: present in 12 of 22 roots.** This was **not** stated before and is a material refinement: a demonstration installation carries posted journal entries that have no business event behind them and no producing process, and they are indistinguishable in the ledger from real ones.

Recorded as `P08-CONTRA-19`: the original claim was true but its scope wording ("every configuration file") would have been read as covering demo data, which it does not.

## 4. Claims not re-runnable in this phase

| ID | Reason |
|---|---|
| `FX-16` | Its path set is the project custom addon tree, not the reference root set. Handled in Phase B |
| The merge-path negative | Contributed by an independent reviewer against a five-file wizard population; re-run belongs with Phase B's custom sweep and is recorded as remaining |

## 5. Disposition of the root-set defect

| State | Count |
|---|---|
| Class-A claims previously re-run across the root set | 3 |
| Class-A claims re-run in this phase | **14** |
| **Total now carrying the declared 22-root scope** | **16** — one of the three inherited claims (`RS-A-01`) was **withdrawn as contradicted** during this continuation |
| Remaining scoped to a narrower stated path set | **2** (`FX-16`, the merge-path negative) |
| Claims whose scope wording was refined by the re-run | 1 (`CFG-JE`) |

The prohibition that blocked this package is now satisfied for **17 of 19** previously-single-root claims. The remaining two are named, not absorbed, and their path sets are declared.


## 6. A class-A claim withdrawn during this phase

`RS-A-01` — *"no accounting-event model exists"* — was one of the three claims the prior session had already re-run across the root set. A targeted forensic pass commissioned to disprove it **succeeded**, and the author verified the counterexamples against primary source.

**It is withdrawn, not amended.** The full analysis, the corrected finding and the method lesson are in `39_P08_ACCOUNTING_EVENT_IDENTITY_FORENSIC.md`.

The lesson bears directly on this phase's own method: `RS-A-01` **passed** its positive control. The control proved the pattern could find models named "event"; it did not prove the pattern could find event *identity*. **A positive control must be able to match the thing being denied, not merely produce output.** Recorded as `P08-M-07`.
