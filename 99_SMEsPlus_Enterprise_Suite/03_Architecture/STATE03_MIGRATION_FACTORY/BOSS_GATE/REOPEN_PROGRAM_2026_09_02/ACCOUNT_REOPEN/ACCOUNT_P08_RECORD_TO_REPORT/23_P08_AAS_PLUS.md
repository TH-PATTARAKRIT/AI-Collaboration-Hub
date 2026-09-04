# P08_AAS_PLUS — Architecture assurance synthesis

Session `SMEPLUS-26-09-04-ACC-P08-R2R-REV2-001`
Status: **`PROVISIONAL / NON-CANONICAL`**. Parent Very Deep Research for the Account domain is not complete; no output here is implementation authority.

**AAS+ preserves contradictions.** Nothing below is smoothed. Where two positions conflict, both stand with their evidence.

## 1. The single architectural finding

Every accounting invariant in the benchmark is enforced in application code, and application code is reachable from callers that can decline to run it. Six database-level objects exist; five are per-item value checks and the sixth is a partial uniqueness index. **One** database object protects an accounting relationship. **No cross-record accounting invariant is enforced below the application layer — including the defining invariant of double-entry bookkeeping.**

Everything else in this package is a consequence of that, or a consequence of the four objects the benchmark does not have.

## 2. The four missing objects, in order of leverage

| Rank | Missing object | What its absence causes |
|---|---|---|
| 1 | **Accounting event** (`K2`) | duplicate postings undetectable; correction and edit collapse into one operation; no derived-versus-asserted distinction; `ONE FACT → ONE ACCOUNTING EFFECT` unenforceable because there is nothing to be *one* of |
| 2 | **Period as an object** (`K8`) | close is a date movement, reversible by writing an earlier one; no field answers "is this period closed"; each code path chooses independently whether to honour the date — which is why one control refuses an asset re-evaluation and relocates a posting |
| 3 | **Issued statement as a fact** (`K9`) | a past-period statement re-runs to a different number by eleven routes and nothing marks the earlier one superseded |
| 4 | **Posting instruction** (`K3`) | no provenance: two entries produced by different versions of the same rule are indistinguishable afterwards |

## 3. Positions this session takes, and what would disprove each

| ID | Position | Status | Disproved by |
|---|---|---|---|
| `AAS-01` | The kernel is nine objects, not four | `PROVISIONAL` | a benchmark-shaped design that delivers event identity and period state without them |
| `AAS-02` | `KRN-INV-00` (the accounting identity, at persistence level, in every currency frame) is the first invariant, not a remediation | `PROVISIONAL` | evidence that a persistence-layer invariant is not expressible in the target platform |
| `AAS-03` | Correction is by new fact only; the benchmark's own transfer routines are the pattern, and the destructive paths beside them are not | `PROVISIONAL` | a legitimate accounting operation that cannot be expressed additively |
| `AAS-04` | A tenant-scope mutation may never rewrite a company-scope posted fact **or silently change a company-scope issued statement** | `PROVISIONAL` | a tenant operation that must reach a posted fact and cannot be expressed as a new fact |
| `AAS-05` | Measurement splits three ways — platform observation, tenant policy, company-applied fact | `PROVISIONAL` | a jurisdiction requiring a tenant to source its own reference rates |
| `AAS-06` | Statutory statement layouts are platform reference data; management layouts are tenant-owned; a produced statement is company-owned | `PROVISIONAL` | `P08-BD-02` deciding otherwise |
| `AAS-07` | Consolidated financial statements are the consolidating parent's own artefact, with **posted** eliminations — **not** a pure derivation | `PROVISIONAL`; **this position reverses the session's own draft**, which had made consolidation derived-only and thereby made eliminations unrepresentable | a consolidation framework requiring no adjustment entries |
| `AAS-08` | Every subsidiary store with an independently maintained value carries a control-account relationship and a periodic proof, whose failure is itself an accounting event | `PROVISIONAL`; **produced by a peer session's correction, not by this session's own work** | — |
| `AAS-09` | The kernel supports more than one measurement basis over one set of events | `PROVISIONAL` | `P08-BD-11` |

## 4. Contradictions preserved, not resolved

| ID | Preserved contradiction |
|---|---|
| `P08-CONTRA-17` | Two governing instruments define the negative-claim class letters differently. P08 uses the ratified table and says so. Neither is overruled here. |
| `P08-CONTRA-18` | The class-`A` prohibition's closing condition is stated two ways in one parent package. P08 records both and takes neither silently. |
| `P08-CONTRA-15` | The Wave B stop-line versus P08's own commissioning. P08 executes as research only and does not adjudicate. |
| `P08-CONTRA-09` | A fiscal year is a company attribute in business semantics and a tree-root attribute in the benchmark. The semantic governs SMEsPlus; the behaviour is recorded as evidence, not adopted. |

## 5. What AAS+ will not say

It will not say the design is ready, safe, complete or converged. It will not say the reference behaviour is authority. It will not convert a `SUPPORTED INTERPRETATION` into a `FACT VERIFIED` because it is convenient, and it will not treat the absence of a veto as evidence.

Three positions in this file exist **only** because someone outside this session found the defect: `AAS-07` reverses the session's own draft, `AAS-08` came from a peer process, and `AAS-02` states an invariant the session had omitted while calling its absence the most severe finding it had. That is the honest record of how this synthesis was produced.
