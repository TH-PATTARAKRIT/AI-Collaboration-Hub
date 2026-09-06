# 78 — P05 AAS-03 DOMAIN-PURE CLOSURE CHALLENGE

`LAYER 2 — AUDIT QUARANTINE` · four bounded independent challenges · PHASE S

Each expert was given a **bounded** brief: named files, named source roots, one named dump, and an
explicit instruction to report any domain-boundary violation **in their own conduct**. None was given
the author's conclusions as a starting position.

**Every finding below was re-verified by the author against source or data before adoption.** The
standing rule is *Independent Review ≠ Truth*. Two experts' reports contained no claim that failed
re-verification; the verification commands and their outputs are recorded in `81` and `83`.

## 1. Attribution

| Expert | Seat | Status | Findings adopted | Findings rejected |
|---|---|---|---|---|
| **1** | Financial-Domain Expert | reported | 4 | 0 |
| **2** | Leadership Database Design | reported | 6 | 0 |
| **3** | Integration Architect | reported | 4 | 0 |
| **4** | Lead Code & UI Architect | reported | 4 | 0 |
| | | | **18** | **0** |

**Zero rejections is itself reported, not celebrated.** It means the author's re-verification found
no expert overreach — and it also means every expert challenge that landed, landed on the author.
The author self-corrected **0** of these 18 before review opened.

## 2. Expert 1 — Financial Domain

| # | Challenge | Verified | Disposition |
|---|---|---|---|
| 1.1 | `CI-01` cites 993 rows for a class whose true population is 2 | author re-extracted: `own_account`=2 · `company_account`=357 · `petty_cash`=634 | **ADOPTED** → `RE-31` |
| 1.2 | `CI-07` is not an input class but a cross-cutting property | schema non-conformance visible on the page | **ADOPTED** → `RE-32`; count 7→6 |
| 1.3 | `69 §B`'s blanket posting rule silently decides capitalisation, which is not P05's | contradicts `67 §4` in the same package | **ADOPTED** → `RE-33`; carve-out added |
| 1.4 | The state model has no post-recording mutation state though the fields stay writable | confirmed against the model | **ADOPTED** → `SR-02` |

## 3. Expert 2 — Leadership Database Design

Re-extracted independently from the dump; every count reproduced by the author a second time.

| # | Challenge | Author re-verification | Disposition |
|---|---|---|---|
| 2.1 | The two `own_account` rows both have **no claim** (`sheet_id` null) | `own_account rows: 2 · sheet_id: [NULL, NULL]` | **ADOPTED** → `RE-40` |
| 2.2 | **26 rows carry a float-holder link while typed `company_account`** — the two fields that define `CI-02`/`CI-03` disagree | `('company_account', petty_cash_id set) = 26` · `('company_account', unset) = 331` · `('petty_cash', set) = 634` | **ADOPTED** → `RE-39` |
| 2.3 | Every sheet has exactly one line, so the reimbursement-vs-business cardinality asymmetry is **not data-testable** | `lines-per-sheet = {1: 979}`, no exceptions | **ADOPTED** → `RE-41` |
| 2.4 | 11 duplicate `(description, employee, amount, date)` groups / 23 rows, covered by no existing finding | reproduced exactly: 11 groups, 23 rows | **ADOPTED** → `DUP-07`, disposition **`C — NOT DECIDABLE`** |
| 2.5 | *"Payable lineage is severed"* is true at the line grain but **overstated**: the sheet-level key survives and, at one line per sheet, reconstructs the link | `expense_sheet_id` set on **712 of 712** linked entries; amount reconciles on **711 of 712** | **ADOPTED** → `RE-42`; claim narrowed |
| 2.6 | `CO-05`/`CO-06`/`ORPH-02`/`ORPH-03` are negative claims carrying **no A–E class letter**, unlike `ORPH-01a` two rows away | confirmed by reading the file | **ADOPTED** → `RE-43` |
| 2.7 | The pack runs two classification vocabularies with no mapping between them | confirmed | **ADOPTED** → `RE-44` |

**Expert 2 also independently reproduced** the version-basis table cell by cell, the 0-mismatch
company consistency checks, the float-holder isolation, the table-wide null on the line-level expense
link, and every state and payment-mode count. Those reproductions **support** the package.

## 4. Expert 3 — Integration Architect

| # | Challenge | Disposition |
|---|---|---|
| 3.1 | Company absent from attribution and re-invoice payloads | **ADOPTED** → `RE-34`; `company` added to `CO-03`/`CH-02`/`CH-06` |
| 3.2 | Withheld-tax payload omits income-type/form, certificate identity, branch and currency basis — all four already in this package's evidence | **ADOPTED** → `RE-35`; added, with the freeze question routed out as `CH-04a` |
| 3.3 | The correction gap is understated: for a completed certificate there is **no correction mechanism at all** | **ADOPTED** → `RE-36`; `ORPH-01a`; orphan count 4→5 |
| 3.4 | The withholding-module ownership boundary was applied but never written down | **ADOPTED** → `RE-37`; `DP-12` |

Expert 3 confirmed **zero statutory leaks** and **zero domain-boundary violations** in the package.

## 5. Expert 4 — Lead Code & UI Architect

| # | Challenge | Author re-verification | Disposition |
|---|---|---|---|
| 4.1 | **`PSC-01` is contradicted by the table immediately above it.** Approval and entry creation collapse; **posting does not** — it is a separate method, on a different state gate, behind a different permission group | source read: `_do_approve` creates entries in draft and writes the approval fields; `action_sheet_move_post` is a distinct method that posts. The table already said *"a separate posting act."* | **ADOPTED** → `RE-45`; headline corrected to **two of three** |
| 4.2 | The custom override is **unreachable by construction**, not merely unused: it calls a parent hook that **does not exist** in this generation | grep across the whole core module returns **nothing** for the called hook; the current hook has a different name and a different shape | **ADOPTED** → `RE-46`; strengthened from *"non-executing"* |
| 4.3 | The core version normalisation is **asserted, not sourced** | confirmed | **ADOPTED** → `RE-47` |
| 4.4 | **The declared path set was never tested against its own deployment.** Expert 4 ran one listing of the declared root's parent and found a sibling family of installed same-vendor modules | author executed the full test Expert 4 named: **170 of 361 installed modules (47.1%) are outside the declared path set**, including three that inherit the P05 core models, one of which **overrides both methods `PSC-01` turns on** | **ADOPTED** → `RE-48`, and see `81` |

### Expert 4's self-disclosure

Expert 4 reported, unprompted, that it briefly opened one adjacent-domain file before finding the
answer inside P05's own source, and stopped. **It also disclosed the one directory listing that
produced 4.4.** Both disclosures are recorded here rather than filtered out: the second is the single
most consequential finding of this round, and it was produced by an expert testing a boundary the
author had declared and never checked.

## 6. The Author's Follow-Through on 4.4

Expert 4 stopped at *"the boundary was not tested."* The author ran the test and it inverted the
framing of a published claim — see `81`. One result of that follow-through cuts **against** the
severity of the new finding and is stated plainly: the bypass route `81 §4` uncovers is **latent, not
live** — zero qualifying rows exist on the deployment. The route is real; it has not fired here.

## 7. What No Expert Challenged

Recorded because silence is not endorsement, and because a shared blind spot has bitten this
programme before:

- **`TX-01`** (100.00%, 358 of 358 at v18) was not challenged by any of the four.
- **`EC-01`'s** NOT-SATISFIED disposition was not challenged — and `81` now shows it was closer to the
  truth than the author's own confidence elsewhere.
- **No expert questioned the choice of `idemo18_uat` as the target deployment.** The ranking of the
  candidate population was not re-examined by anyone this round.

## 8. Boundary Conduct

| Check | Result |
|---|---|
| Adjacent-domain internals researched by any expert | **one, self-disclosed by Expert 4, stopped on resolution** |
| Whole-estate / whole-volume / CloudStorage sweeps | **none** |
| Statutory determinations made | **none** |
| Writes, restores, mutations | **none** |
| Named-locator reads outside the declared root | **one**, by the author, bounded to the three modules `PS-02` names |
