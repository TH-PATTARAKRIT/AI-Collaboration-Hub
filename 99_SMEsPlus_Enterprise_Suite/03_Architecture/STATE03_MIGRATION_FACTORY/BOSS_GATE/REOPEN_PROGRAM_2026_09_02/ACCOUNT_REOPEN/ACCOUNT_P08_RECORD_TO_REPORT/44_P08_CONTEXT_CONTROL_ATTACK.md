# P08_CONTEXT_CONTROL_ATTACK

Session `SMEPLUS-26-09-04-ACC-P08-R2R-TARGETED-FORENSIC-CLOSURE-001` · `CP-T07`

## 1. Population

**134 distinct context keys** read within the 42-module accounting population. Classified:

| Class | Count |
|---|---|
| Behaviour-altering — suppress or steer a check | **47** |
| Assessed and inert | 63 |
| Presentation and routing only | 24 |

This closes a standing programme residual: a prior round counted a bucket of roughly 48 generic tokens and never assessed it. **It resolves to 63 keys, of which 61 are genuinely inert and 2 were misclassified** — one steers the default monetary balance of a new line, the other defeats an explicit posting guard by arriving one layer beneath it.

## 2. Reachability — traced end to end, six hops, no filtering at any hop

`FACT VERIFIED`. The caller's context dictionary travels from the HTTP request body to the check itself with **no allowlist, no denylist, no key validation and no sanitisation**:

1. the request handler places the caller's parameters, including `context`, into the request — and its own documentation states that a caller may pass a context that **replaces** the session context;
2. the pre-dispatch hook mutates exactly one key (language) and never inspects the rest;
3. the controller gates the **method name** only — and create, write, unlink and post are all public;
4. the call helper does `context = kwargs.pop('context')` then applies it, with no statement between;
5. the context applier emits two advisory log warnings for two legacy keys and **drops nothing**;
6. the check reads the value straight from the caller's dictionary.

The remote-procedure entry point follows the identical path.

## 3. The keys that matter

| Key class | Effect | Default |
|---|---|---|
| **The balance switch** | disables the entire debit-equals-credit assertion | **fail open** |
| **The posted-record switch** | waives the readonly guard over nine header attributes of a posted entry | **fail open** |
| **The deletion switch** | waives the sequence-chain guard, the retention guard and the posted-item deletion guard | **fail open** |
| **The seal version selector** | chooses the tamper-seal field set **for both the write guard and the sealing algorithm** — the oldest version omits the entry number, stringifies amounts and writes no version marker, and the verifier accepts it | **fail open** |
| **The analytic validation switch** | the mandatory-analytic-distribution validation **never fires unless the client asks for it** | **fail open** |
| **The abnormal-amount switch** | inverted naming: the confirmation is **suppressed unless** a caller explicitly enables it | **fail open** |
| **A caller-supplied exchange rate** | replaces the computed rate in settlement and exchange computation — **it steers monetary amounts directly** | caller trust required |
| **The lock-date sentinel** | compared by object identity, therefore **not forgeable over the wire** | **secure by default** |
| **The audit-deletion sentinel** | same | **secure by default** |

**Nine keys that suppress a check have zero setters anywhere in the reference tree** — including two that remove rounding from tax computation. Every zero was re-run in a second, unfiltered form; two of the nine changed answer under the second form and were reclassified, which is why the second form was run.

## 4. The self-check that matters most

The primary pattern — a direct read of a literal key from the context — **does not fire on the single most important key in this deliverable**, because that key is resolved through a generic helper rather than read directly.

> **Any context-key register built on a direct-read pattern alone is incomplete by construction.**

A second pattern was required to find it. This is the same defect class this session has now recorded three times: a pattern that cannot fire on its target. It is recorded as `P08-M-09`.

## 5. Residual route to the two secure keys

The two sentinel-guarded controls — the period lock and audit-log deletion — cannot be reached from a remote caller. **Whether any server-side execution path can obtain and pass a sentinel** — a scheduled action's code, an automation rule, a server action, or an installed custom module — **was not enumerated**. `UNRESOLVED — EVIDENCE REQUIRED`. That is the residual route to the hard lock date, and it is the one worth closing next.

## 6. Classification

| Question | Answer |
|---|---|
| Secure by default? | **2 of 47** — both sentinels |
| Fail open? | **the majority**, including every control this package treats as material |
| Caller trust required? | 12 |
| Configuration dependent? | 4 |

**An accounting invariant must not be expressible as a request parameter.** In the version studied, the defining invariant of double-entry bookkeeping is exactly that.

## 7. Evidence-strength qualification on the register itself

The read-site column of the suppressor-key register was verified in **two independent query forms** — a per-key literal search across the source tree filtered to context-resolution sites, and a substring match over a pre-built `file:line:content` cache built by a different mechanism over a different I/O path.

| Segment | Keys | Query forms | Discrepancies |
|---|---|---|---|
| First alphabetical segment of the suppressor-shaped set | **30 of 51** | **2** | **0** — set difference empty across 107 references |
| Remainder, including the readonly-skip, invoice-sync-skip, matching-number-skip, rounding and analytic-validation keys | **21 of 51** | **1**, plus per-key unfiltered re-runs for the zero-setter claims only | not testable |

The 21-key remainder rests on a single query form for its read sites. The zero-setter claims inside that remainder were separately re-run unfiltered and are not affected. The read sites themselves were not cross-checked.

`UNRESOLVED — SECOND-FORM VERIFICATION OUTSTANDING FOR 21 OF 51 KEYS.` The gap is one of corroboration, not of a known error: no discrepancy was found in the 30 keys that were cross-checked, and the second form was run because the first had already been shown, twice in this session, to be capable of silent misses.
