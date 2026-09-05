# P06_BLOCKER_LEVERAGE_GRAPH.md

**Session:** P06 — SUPPLEMENTAL CRITICAL-RISK CLOSURE (CP-P06S19)
**Classification:** LAYER 2 — AUDIT QUARANTINE
**Rule observed:** *"Do NOT estimate time. Time is not evidence."* Cost below is **evidence cost** — how much evidence must be obtained — not duration.

---

## 1. The graph

```
        ┌──────────────────────────────────────────────────────────────┐
        │  L1  TARGET MODULE REGISTRY EXPORT          cost: LOW        │
        │      one ir.module.module export from the target database    │
        └───────────────┬──────────────────────────────────────────────┘
                        │ closes or materially bounds
          ┌─────────────┼─────────────┬─────────────┬──────────────┐
          ▼             ▼             ▼             ▼              ▼
       B-44          B-50          B-31          B-19          F02 evidence
    generation   is the module   v14 provider   voided        class upgraded
       gap        installed?      deployed?     cheques       from source-only
                                                              to deployed
        risk reduction: CRITICAL

        ┌──────────────────────────────────────────────────────────────┐
        │  L2  COMPANY-HIERARCHY QUERY                cost: LOW        │
        │      SELECT id, parent_id, vat, company_registry             │
        │      FROM res_company                                        │
        └───────────────┬──────────────────────────────────────────────┘
                        │ bounds the EXPOSURE of (control defect already closed)
              ┌─────────┴─────────┬──────────────┐
              ▼                   ▼              ▼
           B-45               B-26 exposure   B-43 exposure
       lock inheritance     unowned banks    2nd root-scope site
        risk reduction: HIGH

        ┌──────────────────────────────────────────────────────────────┐
        │  L3  P08 PACKAGE  — NOW PUBLISHED           cost: LOW        │
        └───────────────┬──────────────────────────────────────────────┘
                        │
          ┌─────────────┼─────────────┬──────────────┐
          ▼             ▼             ▼              ▼
        B-46          F-06          F-15           F-17
      relocate    posting-state   GL balance    close status
        risk reduction: HIGH  ·  see 52_ for the intake

        ┌──────────────────────────────────────────────────────────────┐
        │  L4  BOSS DECISION ON THE DESIGN POPULATION cost: n/a        │
        │      26 HOLD — DESIGN DECISION REQUIRED                      │
        └───────────────┬──────────────────────────────────────────────┘
                        │ these cannot be closed by evidence at all
          ┌─────────────┼─────────────┬──────────────┐
          ▼             ▼             ▼              ▼
        B-06          B-10          A6/B-46        B-13
        risk reduction: CRITICAL, but not by research
```

---

## 2. High-leverage parents

| Parent | Dependents | Evidence needed | Cost | Risk reduction |
|---|---|---|---|---|
| **L1 — target module registry** | `B-44`, `B-50`, `B-31`, `B-19`, plus the evidence class of headline finding F02 | one `ir.module.module` export from the **target** database: `name`, `state`, `latest_version` | **LOW** | **CRITICAL** |
| **L2 — company hierarchy** | `B-45`, and the *exposure* half of `B-26` and `B-43` | one read-only `SELECT` on `res_company` | **LOW** | **HIGH** |
| **L3 — P08 intake** | `B-46`, `F-06`, `F-15`, `F-17` | read the published branch | **LOW** | **HIGH** |
| **L5 — second-pass negatives** | the five single-pass tree-scope negatives that keep `AASP-VETO-01` partly in force | five greps with independently-worded patterns | **LOW** | **MEDIUM** |
| **L6 — P01 publication** | `F-02`, part of `B-04` | peer publishes | **n/a — not P06's to obtain** | MEDIUM |
| **L7 — statutory sources** | `B-08`, `B-09`, `B-21`, `B-13` statutory half | Thai Revenue Code / TFRS | **HIGH** | MEDIUM |
| **L8 — Boss design decisions** | 26 items incl. 4 of the 6 CRITICAL | none — a decision, not evidence | **n/a** | **CRITICAL** |

---

## 3. The single most valuable action

**LEV-F-01 — One artefact moves more risk than any other: the target module registry.**

It is the only item in the package that:
- closes an **evidence-boundary** blocker (`B-44`, the v18/v19 generation gap);
- **bounds the package's highest-impact finding** (`B-50` — if the module is not installed on the target, a CRITICAL becomes a latent supply-chain risk rather than a live one);
- resolves two MEDIUM deployment questions (`B-31`, `B-19`);
- upgrades the evidence class of a headline negative that is currently source-bounded.

**It is a read-only export. It requires no privilege beyond reading a list of installed modules, and it is the same artefact the previous round already identified and did not obtain.**

**LEV-F-02 — And it is the only place where "more evidence" changes a CRITICAL.**
The other five CRITICALs — `B-06`, `B-10`, `A6/B-46`, `B-26`, `B-13` — are **design decisions**. No amount of further research will close them, because the finding is not *"we do not know"*; the finding is *"the system does not do this"*. Continuing to research them would be work that cannot change its own conclusion.

---

## 4. Leverage that is now discharged

| Parent | Status |
|---|---|
| **`B-27` `root_id`** | **DISCHARGED at round 3.** It gated attack A4a, `RM-R-10` and `SCOPE-R-02`; two closed on their own merits, one reclassified to a design decision. **P11 may strike it from its decision `D-3`.** |
| **`B-03` peers unread** | **DISCHARGED to 8 of 9** — P08 published this round; only P01 remains. |
| **`B-40` unverified negatives** | **DISCHARGED for the two principal negatives**; five single-pass items remain (L5). |
| **`B-41` no severity model** | **DISCHARGED by `46_` and `47_`.** |

---

## 5. Anti-leverage — items that look connected and are not

Recorded so a reader does not infer a cascade that does not exist.

| Apparent parent | Apparent child | Why there is no leverage |
|---|---|---|
| `B-50` unauthorised deletion | `B-12` deletability is a toggle | **Different paths.** `B-12` is the ORM `unlink` path governed by a company setting; `B-50` bypasses the ORM entirely. Fixing one does nothing for the other. |
| `B-44` generation gap | the v18 source findings | **No.** The source findings are true of the v18 tree regardless of what is deployed. The generation gap changes *relevance*, not *correctness*. |
| `B-10` ingestion identity | `B-29` identity scope | Related, not dependent. `B-10` is about doors with no identity; `B-29` is about the enforcement scope of the identity that does exist. Both must be designed. |
| `B-06` no confirmation fact | everything else | Tempting and wrong. `B-06` is the deepest finding but closing it would not close `B-10`, `A6` or `B-50`, each of which fails for its own reason. |

**LEV-F-03 — There is no single design decision that closes the CRITICAL band.** Four separate decisions are required: create a confirmation fact; make bank-event identity mandatory; bring the reconciliation relation inside the close regime; and make destructive operations self-authorising. **A design that addresses three of the four leaves a CRITICAL open.**
