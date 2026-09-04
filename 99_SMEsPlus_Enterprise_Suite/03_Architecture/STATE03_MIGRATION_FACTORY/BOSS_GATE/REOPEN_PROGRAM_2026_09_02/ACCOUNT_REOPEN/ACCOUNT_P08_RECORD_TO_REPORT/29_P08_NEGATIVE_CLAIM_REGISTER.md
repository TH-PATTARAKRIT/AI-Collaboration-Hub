# P08_NEGATIVE_CLAIM_REGISTER

Session `SMEPLUS-26-09-04-ACC-P08-R2R-REV2-001`

**Class table used:** the ratified standard's — `A` verified absence within a stated scope · `B` not found in searched scope · `C` not yet searched · `D` unknown · `E` contradicted. A second governing instrument defines `B`, `D` and `E` differently; that conflict is `P08-CONTRA-17` and `P08-BD-15`.

## 1. Class `A` — re-run across the declared 22-root set

| ID | Claim | Pattern boundary that travels with it |
|---|---|---|
| `RS-A-01` | No accounting-event model exists | anchored model-name census per root, event token, deduplicated, event-management and framework namespaces excluded. **Independently reproduced by a reviewer.** |
| `RS-A-02` | No period object carrying state, closure or an entry link exists | anchored model-name census per root on two accounting-period name forms. **Re-worded after review** — the pattern never supported the broader sentence the draft published. |
| `RS-A-03` | No database-level object enforces per-entry balance | amended union of three patterns — check-constraint bodies aggregating debit/credit/balance, trigger creation, deferred/exclusion constructs. **Reproduced and strengthened by a reviewer**, who widened it to all file types: still zero. |

## 2. Class `A` scoped to **one root of 22**, and therefore **to be read as class `C`** pending re-run

An independent reviewer established that the root-set declaration does **not** cover these, and that the draft's blanket sentence claiming otherwise was false. They are listed rather than quietly left, because listing them is the only honest form of the closure:

`COA-17` · `AID-02` · `AID-08` · `JPM-11a` · `JPM-18` · `JPM-20` · `JPM-32` · `03`§2.1 accounting-event and subledger rows · `06`§2 zero-entries-in-configuration · `REC-11` · `REC-13` · `REC-24` · `FR-13` · `FR-20` · `FR-22` · `FX-10` · `FX-15` · `FX-16` · `E1-F10`'s merge-path negative.

**Nineteen.** Each carries a real, stated scope; none carries the root set. `P08-U-13`.

## 3. Class `B` — not found in searched scope

`JPM-10` (no context filtering at the dispatch layer) · `PC-14` (no screen listing derogations) · `PC-21`/`RS-B-01` (no year-end appropriation generator — **downgraded from `A` at every scope**) · `03`§2.1 posting instruction (**downgraded from `A`**) · `03`§2.1 subledger (**downgraded from `A`**) · `PC-27` (no override on the irrevocable lock) · `FR-24` (no countermeasure at the report layer) · `P08-PEER-03` (no reconciliation of a subsidiary store).

## 4. Class `C` — not yet searched

`P08-U-02`, `-09`, `-10`, `-12`, `-13`, `-14`, `-15`, `-16`, `-17`; the legacy custom tree; the deployed database; every runtime behaviour.

## 5. Class `D` — unknown

`P08-U-03`, `-05`, `-07`, `-08`; the reachability of the ledger-erase methods by a lower-privileged caller.

## 6. Class `E` — contradicted, with lineage preserved

| Claim | Contradicted by | Corrected form |
|---|---|---|
| "All 39 event-token models belong to the event-management domain" | reviewer, reproduced by the author | 36 do; 3 do not; none is accounting |
| "The general ledger is original truth" | this package's own `KRN-03` | the **journal item** is both original and derived; the ledger is uniformly derived |
| "334 is the upper bound of what can reach the ledger" | this package's own attack file | it is the dependency-graph denominator only |
| "An administrator can disable retention and erase the evidence" | a guard that refuses it once entries exist | the boundary survives on the default-off ground |
| "The journal item is the only durable accounting fact" (unqualified) | the P04 peer finding | true **within the ledger**; genuine separate subsidiary stores exist outside it |
| "The parity fallback is not version-specific" (`RS-P-01`) | reviewer, reproduced by the author | **inverted**: parity is 22/22; the earliest-rate-ever tier is 21/22 and **is** version-dependent |
| "No accounting-period entity exists" | this package's own close model | no period object **carrying state, closure or an entry link** |
| "Twenty-two attacks, none stopped outright" | this package's own body | one is stopped on the ordinary path and open on another |

## 7. Compliance scan result

Mechanical scan for the prohibited unqualified forms and the strength words, over all Layer 1 and Layer 2 files. Result recorded here as the standard requires.

- **B, C or D restated as A anywhere in the package, including summaries and the gate report: none found**, by the author and independently by a reviewer.
- **Upgrade by attrition, found by a reviewer and accepted:** four downstream restatements carried the class letter and the path set but **dropped the pattern**. Corrected — the pattern now travels with the claim in the kernel model, the event register, the attack file and the handoff pack.
- **Unqualified negatives with no class letter, found by a reviewer and accepted:** four (`SC-JE-07` provenance, `PC-17`'s "no field anywhere", `FR-24`'s "none sits at the report layer", and the handoff's restatement of the balance absence). Each now carries its class and boundary.
- **Clean-room scan:** Layer 1 free of vendor model names, paths and file extensions. One false positive noted in the scrub pattern itself — the token used to catch inventory vocabulary also matches ordinary English words.
