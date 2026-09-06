# P08_HANDOFF_PROPAGATION_AUDIT

Prompt `[SMEPLUS-26-09-06-P08-R2R-INDEPENDENT-EXTERNAL-CORRECTION-VERIFICATION-003]` · frozen surface `00ccd66`

**Scope discipline:** this audit judges **only whether P08's own outbound wording matches P08's own evidence**. **No peer package was opened and no peer internals were researched.**

---

## 1. The governing result

**The corrections were written into the registers and not into the wording that leaves the process.**

| | |
|---|---|
| Outbound handoff rows in `54` §4 | **14** |
| Rows whose wording matches the package's current evidence | **4** |
| Rows carrying **superseded** wording | **4** |
| Rows **under-qualified** (true but missing a scope, version or reachability qualifier the package itself established) | **5** |
| Rows whose **evidence reference does not support them** | **1** |
| Rows carrying a **version marker** | **1 of 14** — and it is the row *about* version markers |
| Rows that are **structurally malformed** | **1** (`HO-02`, to P11) |

## 2. Per-handoff verdicts — independently re-checked by this verifier

| ID | To | Verdict | Verifier's basis |
|---|---|---|---|
| `HO-01` | P11 | **EVIDENCE REFERENCE DOES NOT SUPPORT IT** | The row cites `58`. **`58` contains zero occurrences of "contract".** Re-derived by the verifier |
| `HO-02` | P11 | **SUPERSEDED + MALFORMED** | Rests on `58` §2 row 2, whose *"the asset register and the inventory valuation record **are** separate stores"* is the text `55` §5.2 records as contamination `K-3`. **And the row carries 7 cells against an 8-cell header** — verified by cell count; the Scope column is lost and every later value shifts |
| `HO-03` | P07 | **SUPERSEDED** | *"reaches **no** entry's full item set"* is the pre-`P08-CONTRA-58` unit, withdrawn 40 lines below in the same file |
| `HO-04` | P09, P10 | **UNDER-QUALIFIED** | Says *"per channel"*; `48` §2.2 says **one** channel, and adds that the register row is *"re-opened, not closed"* — neither clause is carried |
| `HO-05` | P04, P06, P10 | **SUPERSEDED — the most serious row** | *"the default for **every non-sale document**"* is verbatim the wording `56` §1 row 8 records as **withdrawn**. **Verified live in 6 further locations** — `54` `PR-02`, `52` §4, `46` (twice), `17` `P08-CONTRA-31`, `13` `AE-02` |
| `HO-06` | P05 | **MATCHES EVIDENCE** | Independently confirmed |
| `HO-07` | P06 | **UNDER-QUALIFIED** | Publishes reachability — the best-qualified row — but fuses a three-database install state with single-line mechanism evidence |
| `HO-08` | all | **MATCHES EVIDENCE** | The only row of 14 carrying a version marker |
| `HO-09` | all | **UNDER-QUALIFIED** | The capability predicate behind `7 of 89` / `75 of 109` **is published nowhere**; two independent challengers could not re-derive it from the artefact |
| `HO-10` | P09, P10, P11 | **MATCHES EVIDENCE** | |
| `HO-11` | Boss | **MATCHES EVIDENCE** | 19 decision identifiers, contiguous, verified |
| `HO-12` | Boss, PMO | **SUPERSEDED — and it understates the gate to the Boss** | Says *"`AAS+-VETO-01` — **two conditions**"*. At the frozen SHA **nine distinct veto identifiers** exist and `61` §5 records **5 standing with 25 lifting conditions**. **The row that tells the Boss what is blocking understates it by roughly an order of magnitude** |
| `HO-13` | P11, P06 | **UNDER-QUALIFIED** | Install state confirmed on all three; **the mechanism was read on one build only**, and the build deployed on the two 19.0 databases is not on this host |
| `HO-14` | P07 | **UNDER-QUALIFIED** | Substance confirmed. **The module is installed on one of three databases** — unstated — and the enumeration carries no POPULATION / PATTERN / PATH SET / UNIT |

## 3. `IVR-F-13` · MATERIAL · The handoff identifier namespace is collided across two live artefacts

**Found by this verifier; raised by no challenger.**

**ENUMERATION.** POPULATION: every artefact at `00ccd66`. PATTERN: `HO-\d+` with its containing file. UNIT: one identifier. CONTROL: `HO-07` … `HO-12` resolve to a single file, so the detector distinguishes collided from clean identifiers.

| Identifier | Defined in |
|---|---|
| `HO-01` … `HO-06` | **`25` AND `54`** |
| `HO-07` … `HO-12` | `54` only |
| `HO-13`, `HO-14` | `54` and `58` |

**The two definitions are different handoffs with different consumers.** Verified:

| | `25` `HO-01` | `54` `HO-01` |
|---|---|---|
| Consumers | **P01–P07, P09** | **P11** |
| Content | *"the recognition point of every business event"* | *"The ledger contract every process must satisfy to post"* |

**A peer citing "P08 `HO-03`" cannot determine which handoff is meant.** `52` supersedes `25`, but `25` remains in the package, remains readable, and its identifiers were re-used rather than retired. This compounds `HO-01`'s broken reference: the row points at a file that does not contain its subject, **and** its identifier resolves to two different subjects.

## 4. `IVR-F-14` · MATERIAL · A correction that asserts a scope of application it did not perform

`47` `P08-CONTRA-26` closes with: **"Corrected to 0 of 109 wherever it appears."**

**It was not.** Enumerated at the frozen SHA:

| | |
|---|---|
| Files still carrying the superseded **"0 of 64 journals"** | **`35`, `36`, `39`, `40` (×2), `46`, `48`** |
| Files carrying the corrected "0 of 109" | 4 occurrences |
| Files the correction **named** as carriers | `35`, `36`, **`38`**, `40` |
| **`38`'s actual occurrences of the superseded form** | **0 — named but not a carrier** |
| Carriers the correction **did not name** | **`39`, `46`, `48`** |

**The target list is wrong in both directions and the edit was never made.** `48` is the AAS-03 challenge record — so a **veto** is scoped over a denominator the package had already condemned.

> **`IVR-M-05`. A correction that names its own scope of application must be audited against the text, not against its own disposition line.** This one claimed *"wherever it appears"*, named a file that never carried the defect, missed three that did, and left every carrier unedited.

## 5. What this means for the outbound surface

**No control in this package is scoped at the outbound surface.** The registers were corrected; the rows that leave were not. Ten of fourteen handoffs are superseded, under-qualified, mis-referenced or malformed; one identifier family is collided; and the row that reports the blocking gate to the Boss understates it by roughly an order of magnitude.

**Bounded repair requirement — routed to P08 and the Boss, not performed here.** Every outbound row must be re-issued against the corrected evidence, carrying a version marker and a reachability qualifier, with the `HO-` namespace either retired in `25` or re-numbered in `54`.
