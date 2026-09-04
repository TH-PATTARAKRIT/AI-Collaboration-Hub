# P08_SOURCE_TO_GL_TRACE

Session `SMEPLUS-26-09-04-ACC-P08-R2R-REV2-001` · Layer 1

## 1. The trace as the benchmark actually implements it

`Business source` → *(no object)* → *(no object)* → **Journal entry** → **Journal item** → *(projection)* → *(reading)* → **Report (derived, plus three independent stores)**

Two nodes of the mandated eight-node chain have no carrier, one is a projection and one is a reading. Only two nodes are durable objects.

## 2. Who posts — the reproducible denominator

| Element | Value |
|---|---|
| POPULATION | every module directory in the target root containing a manifest |
| PATTERN | manifest census, then a creation-site sweep over non-test Python: model-reference within a 15-line window of a creation call, plus the reversal-builder symbols, plus verified copy-based creation; every hit read before inclusion |
| PATH SET | the target root's addon tree (root 13 of the declared 22) |
| UNIT | one module |
| DENOMINATOR | **790** modules present · **334** in the accounting dependency closure · **18** actually create journal entries |

**18 of 790.** Business-document posting **11**, accounting-internal posting **7**, infrastructure/test **0**.

Declared pattern-boundedness: the tight regex under-counts — two verified creators bind the model to a local name or call through the model itself and are invisible to it. The 15-line window catches them. **The figure is a floor, not a ceiling**, and it is stated as such rather than as a closed set.

Adjacent populations, recorded so 18 is not misread: **5** modules append items to an existing entry without creating one; **7** modules orchestrate another module's creator; **2** modules extend the reversal builder without creating; **43** non-test files extend the entry object and may therefore alter any semantic in this package.

**Zero** journal entries are declared in static configuration data. `A VERIFIED ABSENCE`, scope = every configuration file of the target root.

## 3. What survives the trace, and what does not

| Trace element | Survives to the posted fact? |
|---|---|
| Which business document caused it | Yes for document-generated entries, via a writable reference |
| Which **event** within that document | **No** — no carrier |
| Which posting rule, and which version of it | **No** — no carrier |
| Who caused it | Only as a record-creation stamp, and elevated paths overwrite the acting identity with a system identity |
| The measurement context (rate, rate date, rate source, rate type) | **No** — not persisted on the item; a bare rate number is persisted on invoice-family headers only |
| Which tenant and company own it | Company yes; tenant has no carrier at all |

## 4. Where the trace breaks, ranked

| ID | Break | Consequence |
|---|---|---|
| `TR-01` | The provenance reference on an entry is an ordinary writable field with no validation | A manual entry can claim a source it never had; a generated entry can be stripped of its source |
| `TR-02` | Returning an entry to unposted destroys its settlement matches and cost allocations silently | The trace downstream of the entry is destroyed by an operation whose stated purpose is correction |
| `TR-03` | A custom re-dating utility discards the entry number and re-posts under a new one | The identity the trace is keyed on is replaced, and the old number becomes an unexplained gap |
| `TR-04` | A bulk import creates entries with an operator-supplied number, an operator-supplied date and no company resolution | Entries enter the ledger with externally chosen identity and no derivable origin |
| `TR-05` | The change-log that would preserve provenance is a company-level option that is **off by default** | On a fresh installation the trace has no retention guarantee at all |
| `TR-06` | Thirteen subsystem integrations create entries with the permission layer switched off, and two post them with the posting-rights assertion switched off | The acting identity recorded on those entries is not the identity that caused them |

## 5. The trace P08 requires

`Business fact` → `Accounting event (identity, recognition point, rule version, actor)` → `Posting instruction (as evaluated, retained)` → `Journal entry` → `Journal item (with its measurement context)` → `Settlement fact (with its own event date)` → `Period (as an object with state)` → `Issued statement (as a fact)`

Each arrow is a stored, immutable link. `KRN-INV-01` (`ONE FACT → ONE ACCOUNTING EFFECT`) is enforced at the second node and nowhere else, because that is the only node at which "one" is countable.
