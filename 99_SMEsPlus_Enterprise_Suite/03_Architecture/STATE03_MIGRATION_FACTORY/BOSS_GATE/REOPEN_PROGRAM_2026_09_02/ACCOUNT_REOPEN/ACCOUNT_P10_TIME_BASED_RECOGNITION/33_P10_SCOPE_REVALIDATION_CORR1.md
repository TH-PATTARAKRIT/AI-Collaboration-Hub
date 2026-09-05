# P10 — SCOPE-AWARE REVALIDATION (REV2-CORR1)

Session: `SMEPLUS-26-09-04-ACC-P10-TBR-CROSS-PROCESS-RECON-001` · Layer 1

Revalidation of P10's scope determinations against `SMEPLUS-26-09-04-ACC-REV2-CORR1` and against three programme positions adopted since the parent round. **Scope-aware everywhere. Tenant and Company are not imposed on every object.**

Per the continuation directive, each material recognition object is determined on **six** separate axes, not one.

---

## 1. Positions Adopted Since the Parent Round

| Position | Origin | Effect on P10 |
|----------|--------|---------------|
| `SCP-08` — the semantics of an absent scope value must be defined; **"unset" may never mean "all"** | `P11` | P10 had no rule for absent scope. Adopted; applied in §3 |
| `SCP-09` — a scope determination taken against behaviour the programme is **obliged to change** must record its **expiry trigger** | `P11`, raised by `P04` | **P10's parent scope matrix recorded no expiry triggers at all.** Corrected in §2 |
| `MA-11` — a company-scoped attribution requirement shall never be enforced through a tenant-scoped structure | `P09` | Adopted as a P10 design constraint; applied in §3 |

## 2. Six-Axis Determination, With Expiry Triggers

| Object | Ownership | Configuration | Execution | Recognition | Financial effect | Reference | Expiry trigger (`SCP-09`) |
|--------|-----------|---------------|-----------|-------------|------------------|-----------|---------------------------|
| Day-count convention **definition** | PLATFORM | PLATFORM | PLATFORM | n/a | none | any | **None** — a convention definition is not behaviour the programme must change |
| Period-grid **algorithm** | PLATFORM | PLATFORM | PLATFORM | n/a | none | any | **None** |
| Recognition **event schema** | PLATFORM | PLATFORM | PLATFORM | n/a | none | any | **EXPIRES** on Boss decision `D-5`. If `P08` authors the accounting-event object, this determination is superseded and the schema is `P08`'s, not a P10 PLATFORM item |
| Service / benefit **window** | TENANT | TENANT | TENANT | referenced by COMPANY | none directly | COMPANY | **None** — a contract fact does not change scope when the programme fixes the ledger |
| Allocation convention **tenant standard** | TENANT | TENANT | TENANT | n/a | none directly | COMPANY | **EXPIRES** on Boss decision `P10-D-04` — if the Boss rules a tenant may *bind* rather than default, this becomes a binding TENANT determination with COMPANY effect |
| Fiscal calendar / period-grid **instance** | COMPANY | COMPANY | COMPANY | COMPANY | none directly | COMPANY | **None** |
| Allocation convention **binding value** | COMPANY | COMPANY | **currently the ACTIVE company — defect `P10-S-01`** | COMPANY | yes, indirectly | COMPANY | n/a — this is a defect, not a determination |
| Deferral / accrual control accounts and journals | COMPANY | COMPANY | COMPANY | COMPANY | yes | COMPANY | **None** |
| **Recognition base** | COMPANY | COMPANY | COMPANY | COMPANY | yes | COMPANY | **None** |
| **Recognition event** | COMPANY | COMPANY | COMPANY | COMPANY | yes | COMPANY | **EXPIRES** on `D-5` — the *instance* stays COMPANY, but the *object* passes to `P08` |
| **Posting act** | COMPANY | COMPANY | COMPANY | COMPANY | yes | COMPANY | **None** |
| **Recognition attribution** (economic effect) | COMPANY *required* | **structure has no company field at all** | COMPANY | COMPANY | yes | COMPANY | **EXPIRES** when the cost object is authored (`P09` `AD-5`) |
| Recognition **report** | COMPANY data | COMPANY | **must be COMPANY; currently derived — defect `P10-S-02`** | COMPANY | yes when it generates | COMPANY | n/a — defect |

Three determinations now carry expiry triggers. The parent matrix carried none, and would have presented a time-indexed judgement as a standing fact — the defect `SCP-09` was written to prevent.

## 3. Three Applications of the New Positions

### `SCP-08` applied — the attribution structure

The structure carrying recognition attribution has **no company field at all**. Under the superseded reading that would be "available to all companies". Under `SCP-08` it is **undefined**, and `MISSING REQUIRED SCOPE = DENY` applies.

P10's determination: **recognition attribution may not be enforced, relied upon, or reported as company truth through the present structure.** This is a constraint P10 places on its own design; it is not a demand on `P09`, which found and published the defect.

### `MA-11` applied

A recognition event's economic effect is a COMPANY-scoped attribution requirement. It is currently carried on a structure with no company scope. That is precisely the arrangement `MA-11` prohibits. P10 adopts `MA-11` and records that **no P10 design may satisfy its attribution requirement through the present structure**, independently of whether the structure is later fixed.

### `SCP-09` applied to P10's own defects

`P10-S-01` and `P10-S-02` are defects, not determinations, and therefore take no expiry trigger. But their **severity** is time-indexed: deployed evidence shows all 44 companies identically configured and the chart almost unshared, so realised exposure is nil **today**. P10 records the expiry of that mitigation explicitly:

> The mitigation on `P10-S-01` expires the first time any company's allocation configuration diverges from the estate default. The mitigation on `P10-S-02` expires the first time a second account is shared across companies.

Neither is a control. Both are current states of data.

## 4. What Remains Deliberately Not COMPANY-Scoped

Restated because the superseded blanket reading would have got all four wrong, and because the reconciliation confirmed rather than weakened them:

1. Day-count convention **definitions** — PLATFORM reference data. A company owns the *choice*, not the definition.
2. The period-grid **algorithm** — PLATFORM. The company owns its fiscal calendar, not the arithmetic.
3. The recognition **event schema** — PLATFORM today, `P08`'s after `D-5`. The *instances* are COMPANY.
4. The service **window** — a TENANT fact. One contract billed by two companies of one tenant has **one** window. Forcing it to COMPANY would duplicate a customer fact per legal entity and make inter-company recharge incoherent.

`P08`'s and `P04`'s scope matrices were not read in full by this round — the peer-extraction agents that would have compared them line by line did not complete. **Agreement between P10's assignments and the peers' is therefore class `C` — NOT COMPARED**, not class `A`. Recorded as `P10-U-21` and returned to `P11`, which owns cross-process scope reconciliation.

## 5. Revalidation Result

| Item | Result |
|------|--------|
| Determinations revalidated | 13 |
| Changed by revalidation | 0 |
| **Gaining an expiry trigger** | **3** |
| New constraints adopted from peers | 3 (`SCP-08`, `SCP-09`, `MA-11`) |
| Determinations found over-constrained | 0 — the four PLATFORM/TENANT assignments survived |
| Determinations found under-constrained | 1 — attribution, now explicitly denied rather than assumed available |
| Cross-process scope comparison | **Class `C` — not performed.** Routed to `P11` |
