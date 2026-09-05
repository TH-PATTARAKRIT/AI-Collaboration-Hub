# P01 — DEPLOYED SCHEMA EVIDENCE

Session: `SMEPLUS-26-09-04-ACC-P01-P2P-REV2-001`
Layer: **1 — business conclusions.** Column and table identifiers appear here only where the
finding *is* the presence or absence of the structure; the reference-system file paths that
would make this Layer 2 are not present.
Added: **late in the session**, after an independent expert established that readable dumps of
live databases exist. This supersedes several earlier statements in this package that no
database evidence was available.

---

## 1. WHY THIS DOCUMENT EXISTS, AND WHAT IT CHANGES

Every other finding in this package is read from source. **A deployed schema is a stronger
class of evidence than source**, because it states what a running system actually has, not
what a source tree would build.

The dumps were **not** in this session's declared evidence base. They were found by the
Database Design expert, whose brief listed a different set of runtime artefacts and instructed
it to report the list as wrong if it was. It was wrong. This is the second time in this
session that the "challenge the brief" instruction produced the most valuable result
(`ERR-P01-05` was the first).

**Method.** Four database dumps are present. Three restore with the locally-installed tooling;
one does not. Schema-only definitions were extracted for the three and probed by structural
search. **No data was read by this session** — only the schema. Configuration-value findings
attributed to the Database Design expert below are its own and are marked as not
re-verified here.

**A false result was produced and caught in this step.** The first extraction wrote empty
files, and the probe consequently reported every structure as absent. Had the output not been
line-counted, this package would have published a set of fabricated class-A absences. Recorded
as `ERR-P01-06`.

---

## 2. THE DATABASES

| Tag | Generation | Schema size (DDL lines) | Restorable |
|---|---|---|---|
| `D1` | **v19 line** | 150,677 | yes |
| `D2` | **v19 line** | 148,090 | yes |
| `D3` | **v16 line** | 106,836 | yes |
| `D4` | unknown | — | **no** — not readable by the available tooling |

Generation was determined structurally, not from the file name: the two v19 databases carry a
stock-variation account structure and a restrictive audit-trail flag that the v18 one does not,
and the v18 one carries valuation-layer tables that the v19 ones do not.

---

## 3. THE DECISIVE FINDING

> **The deployed v19 databases have no goods-received clearing account and no inventory
> valuation-layer table.**

| Structure | `D1` (v19) | `D2` (v19) | `D3` (v16) |
|---|---|---|---|
| Goods-received clearing account on the item category | **absent** | **absent** | see §4 |
| Goods-received *output* account on the item category | **absent** | **absent** | see §4 |
| Inventory valuation account on the item category | present | present | see §4 |
| **Price-difference account on the item category** | **present** | **present** | see §4 |
| Production-cost account on the item category | present | present | see §4 |
| Valuation journal on the item category | present | present | see §4 |
| **Inventory valuation layer table** | **absent** | **absent** | **present** |
| Valuation-layer revaluation table | absent | absent | present |
| Stock variation account structure | present | present | absent |

**Classification: FACT VERIFIED — class A within `D1` and `D2`.** The absence is meaningful in
these two databases specifically because the *sibling* properties on the same table are
present, so it is not a storage-mechanism artefact (see §4).

### What this means for P01

The entire receipt-to-bill bridge that this package traced in the v18 source — goods received
into a clearing account, the bill debiting that clearing account, a price-difference engine
reconciling valuation layers — **has no physical structure to run on in the deployed v19
databases.** There is no clearing account column and no valuation-layer table.

This raises `CONTRA-P01-03` from a **source-level** cross-version divergence to a
**deployed-level** one, and correspondingly raises `DEP-P01-01` from a documentation question
to a structural one. Any P01 design taken from the v18 pattern would be modelled on a bridge
two of the three readable live databases do not have.

---

## 4. A NEGATIVE THIS SESSION DECLINED TO MAKE

The same probe reported that the v18 database's item-category table carries **no accounting
property columns at all**. That looked like an even stronger finding. It is not one, and it is
recorded here as a negative that was **deliberately not published**:

The v18 database **has** the generic property-storage table that older generations use for
company-dependent values; the two v19 databases **do not**. So in the v18 database those values
are expected to live as rows in that table rather than as columns, and a column probe cannot
see them. The correct classification for the v18 row is **class D — unknown from this probe**,
not class A.

The same reasoning is what *licenses* the v19 finding in §3: there, the sibling properties are
columns on the same table, so a column probe is the right instrument and the absence is real.

---

## 5. REFERENTIAL INTEGRITY OF THE P2P CHAIN

Verified directly in the extracted schemas of both generations:

| Link | Deployed behaviour on deletion of the purchase order line |
|---|---|
| Bill line → order line | **SET NULL** in v18 and v19 |
| Receipt movement → order line | **SET NULL** in v18 and v19 |
| Generated-movement → order line | SET NULL in v18; CASCADE in v19 |
| Custom request allocation → order line | CASCADE, present in the v18 database |

**Classification: FACT VERIFIED** in the deployed schemas of both generations.

Deleting a purchase order line therefore **silently erases the bill's record of where it came
from and the receipt's record of what it was fulfilling, in the same operation**, leaving both
documents in place and internally valid. No error, no cascade, no orphan marker.

This corroborates the Database Design expert's finding that the chain has almost no
database-level integrity, and it is the physical counterpart of this package's `§2.12` finding
that a payable cannot always be traced back to its business event.

The presence of the custom purchase-request link in the v18 database is also direct evidence
that **the project's own custom purchase-request capability is deployed** there — a fact no
amount of source reading could establish.

---

## 6. WHAT THIS DOCUMENT DOES NOT ESTABLISH

- It does not read data. Configuration values, company counts and per-journal settings
  reported by the Database Design expert are **its** evidence and are **not** re-verified here.
- It does not establish which database corresponds to which deployment, customer, or tenant.
- It does not establish behaviour. A schema shows what can be stored, not what happens.
- The fourth dump is unreadable with the available tooling and is **class C — not searched**.
- Class A claims here are bounded to the specific databases named. They are not claims about
  any other deployment.
