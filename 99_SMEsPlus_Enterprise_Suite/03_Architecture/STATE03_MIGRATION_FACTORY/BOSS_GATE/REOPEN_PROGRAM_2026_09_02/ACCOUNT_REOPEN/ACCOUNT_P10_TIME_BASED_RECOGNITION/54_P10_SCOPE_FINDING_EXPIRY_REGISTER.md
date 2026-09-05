# P10 — SCOPE FINDING EXPIRY REGISTER

Session: `SMEPLUS-26-09-05-ACC-P10-TBR-DECISION-INTEGRITY-EVIDENCE-REPAIR-001` · Layer 1
Checkpoint `CP-P10D15`.

A scope determination taken against behaviour the programme is **obliged to change** is time-indexed, not a standing fact, and must record its expiry trigger. Thirteen determinations were revalidated; **three carry expiry triggers**. They are stated in full here.

---

## `SX-01` — The recognition event schema is PLATFORM

| Field | Content |
|-------|---------|
| Current determination | The **schema** of a recognition event is PLATFORM reference data; its **instances** are COMPANY |
| Why it is time-indexed | It is taken against a system in which **no accounting-event object exists**. P10 verified this within the declared reference root (`FACT VERIFIED`, one root); the peer's wider claim over 22 roots is carried at class `C` |
| **Expiry trigger** | **Boss decision `D-5`.** If a layer-3 accounting-event object is introduced, the schema passes to the ledger process and this determination is **superseded, not merely revised** |
| Future evidence that invalidates it | Publication of the object; or evidence that such an object already exists in a root P10 has not searched |
| Peer dependency | `PD-14` |
| Version dependency | None |
| Configuration dependency | None |

## `SX-02` — The allocation convention is a TENANT default and a COMPANY binding value

| Field | Content |
|-------|---------|
| Current determination | The tenant may **default** the convention; the **binding** value is the company's, because the amount it produces is company financial truth |
| Why it is time-indexed | The split rests on the Boss not yet having ruled whether a tenant may **bind** rather than default |
| **Expiry trigger** | **Boss decision `P10-D-04`.** A ruling that the tenant may bind converts this to a binding TENANT determination with COMPANY effect |
| Future evidence that invalidates it | None — this is normative, not factual |
| Peer dependency | None |
| Configuration dependency | **Yes, and it is currently masking the defect**: all 88 companies in the two multi-company databases hold **one identical configuration**, so the executing-scope defect cannot presently diverge. **That mitigation expires the first time any company's configuration differs** |

## `SX-03` — Recognition attribution is COMPANY-required and structurally scopeless

| Field | Content |
|-------|---------|
| Current determination | The attribution requirement is COMPANY-scoped; the structure carrying it has **no company field at all**, so under the absent-value rule its scope is **undefined** and the requirement may not be enforced through it |
| Why it is time-indexed | It is taken against a structure the programme is obliged to replace, and against a **cost object that does not yet exist as a first-class object** |
| **Expiry trigger** | **Authoring of the cost object** (peer `PD-15`), or replacement of the attribution structure. Either supersedes the determination |
| Future evidence that invalidates it | A company dimension added to the structure |
| Peer dependency | `PD-15` |
| Configuration dependency | None |

## Rules Recorded

1. **A determination taken against behaviour the programme must change is time-indexed.** It carries an expiry trigger or it will later be read as a permanent fact after it has ceased to be true.
2. **A mitigation that is a data state is not a control**, and its expiry is the first change to that data. Two of P10's exposure mitigations are data states — see `SX-02` and the chart-sharing state at `45`.
3. **Ten of thirteen determinations carry no trigger.** They are taken against facts the programme is not obliged to change — a convention definition, a fiscal calendar, a contract fact — and are standing determinations.
