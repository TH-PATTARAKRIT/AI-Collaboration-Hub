# P01 — DATABASE FALSIFICATION REGISTER

Session: `SMEPLUS-26-09-05-…-EVIDENCE-VERSION-DEPLOYMENT-INTEGRITY-001`
Layer: **1.**

The claims below were **retrieved verbatim** from the published package, not inferred. The
package records **three FALSE claims and one WRONG COUNT** — four entries, of which three are
falsifications proper.

---

## `FAL-01` — three-way matching

| Field | Content |
|---|---|
| **Original finding, verbatim** | *"Three-way matching is **not installed in any readable deployment**"* |
| **Original evidence base** | The installed-module registries of three databases — `D1`, `D2`, `D3` |
| **Why the evidence base was incomplete** | The fourth archive was classified unreadable after a single failed invocation of one restore binary, while a newer binary capable of reading it was installed on the same machine. The bound *"any readable deployment"* was stated honestly and was **itself the error** |
| **New database evidence** | The three-way-match module is **installed** in `D4` |
| **Corrected finding** | **Installed in one of the five distinct database identities (`E-3`; see `ERR-P01-22`).** The separate finding that it is *advisory rather than a control* is **unaffected** and stands |
| **Affected severity** | Raised from *not present anywhere* to *present but, on the evidence, unexercised* — `E-3` holds 10 journal entries in total |
| **Affected process** | P01 |
| **Affected handoff** | The three-way-match position in the P11 handoff |
| **Architecture implication** | A design decision on three-way matching cannot be justified by *"the benchmark does not have it"* |

## `FAL-02` — subcontract purchase

| Field | Content |
|---|---|
| **Original finding, verbatim** | *"Subcontract purchase is in scope by dependency but **installed nowhere** — latent"* |
| **Original evidence base** | As `FAL-01` |
| **Why incomplete** | As `FAL-01` |
| **New database evidence** | The subcontracting family is **installed** in `D4` |
| **Corrected finding** | **`INSTALLED BUT NOT EXERCISED`** — installed in `E-3`, with zero subcontract transactions reported. That zero is under independent disproof challenge this round |
| **Affected severity** | *Latent* → *installed and unexercised*. **These are different risk classes**: latent means unreachable without an install; installed-unexercised means one transaction away |
| **Affected process** | P01, **P03** |
| **Affected handoff** | The correction owed to P03 is unchanged in substance and now carries the installed status |
| **Architecture implication** | Subcontract valuation must be designed for, not deferred as absent |

## `FAL-03` — the requisition family

| Field | Content |
|---|---|
| **Original finding, verbatim** | *"`purchase_requisition` is **not installed anywhere**; two requisition mechanisms are live in the v16 deployment and none in v19"* |
| **Original evidence base** | As `FAL-01` |
| **Why incomplete** | As `FAL-01`. **The second clause carries an additional, independent defect**: it says *"none in v19"*, but `E-3` **is** a series-19 deployment and **does** have the family installed. The clause was wrong even about the databases that had been read, once `D4` is admitted |
| **New database evidence** | The base requisition family is **installed** in `D4` |
| **Corrected finding** | Requisition mechanisms are live in the series-16 deployment **and** in one series-19 deployment |
| **Affected severity** | Moderate. It changes the count of coexisting requisition mechanisms, which bears on the *"three requisition mechanisms coexist"* business-fit observation |
| **Affected process** | P01 |
| **Architecture implication** | The demand-origination surface is broader than P01 recorded |

## `FAL-04` — a count error, not a falsified claim

| Field | Content |
|---|---|
| **Original finding, verbatim** | *"47 of 65 members are source-capability only"* |
| **Corrected** | **28 of 65** |
| **Nature** | This is a **denominator-scope error**, not a falsified behavioural claim. Recorded separately so the falsification count is not inflated: **three claims falsified, one count corrected** |

---

## 2. WHAT ALL THREE FALSIFICATIONS HAVE IN COMMON

Every one was a **class-A-shaped statement bounded to a scope that wrongly excluded the decisive
database**. In each case:

- the negative-claim discipline was followed — a bound was declared;
- the bound was **honest** — it said *"readable deployment"*, not *"anywhere"*;
- and the bound was **wrong**, because *readable* had been decided by a single tool invocation.

> **The negative-claim standard protects against over-scoping a claim. It offers no protection
> against under-scoping the evidence.** That is the lesson, and it is now a standing rule
> (`ERR-P01-15`, §7.2 of the governing directive).

---

## 3. FALSIFICATIONS THIS ROUND ADDS

Beyond the three above, this round's identity repair falsifies two further statements made by
the research about its own evidence base:

| ID | Statement | Correction |
|---|---|---|
| `FAL-05` | *"`D4` is the most relevant database in the estate"* | **Half right.** Highest module coverage; **10 journal entries in total.** Decisive for *what is installed*, near-useless for *what happens* (`ERR-P01-16`) |
| `FAL-06` | Treating `D1` and `D2` as two independent deployments, and aggregating *"90 company rows"* | **They are one deployment observed twice** — identical 44-company identifier sets. Distinct companies in the estate: **46**, not 90. Their agreement is **not** independent corroboration (`ERR-P01-17`) |

---

## 4. WHAT IS **NOT** FALSIFIED

Stated explicitly, so the repair is not read as broader than it is:

- The **three-way match is advisory, not a control** — unaffected.
- The **receipt-to-bill bridge classification** — unaffected; it rests on source design intent
  and on configuration counts, not on the installed-module scope.
- The **period-lock and bill-correction** findings — unaffected by the identity repair, and
  separately under disproof challenge this round.
- The **withholding corrections** made last round — unaffected.
