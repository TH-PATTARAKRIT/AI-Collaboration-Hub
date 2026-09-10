# SMES_CORE_CHALLENGE_CHECKLIST.md
# SMEs Core Independent Adversarial Challenge (Preparation Control 04)

Session: `[SMEPLUS-26-09-10-VDR-PREP-001-CORR1]`
Layer: **LAYER 1 — CLEAN-ROOM.**
Status: **FROZEN v1.0** (Pilot corrections incorporated; see `VDR_FRAMEWORK_PILOT_CORRECTION_REGISTER.md`)

---

## 1. Independence Rule

**The producing agent may not be the validating authority.** A research package is certified by a
party that did not produce it, working from the frozen package and from primary evidence — not from
the package's own summary.

Three controls exist and they are **not interchangeable**; each catches a different defect class and
scaling one harder does not substitute for the others:

| Control | Catches |
|---------|---------|
| **Self-challenge** | Internal inconsistency, arithmetic, unowned items |
| **Independent adversarial challenge** | Wrong predicates, wrong populations, unsupported claims |
| **Peer exchange** | Shared method assumptions invisible to both self and adversary |

The package must be **frozen** (commit SHA recorded) before challenge opens. A moving target cannot
be challenged.

---

## 2. Reading Rule for Challengers

- Cite the **corrections section** of a round, never its headline table. A round's summary is written
  by the party being challenged.
- Read a peer's **register row and status field**, never a peer's summary of it. An `UNRESOLVED`
  blocker is not a rule.
- A **secondary source may locate primary evidence; it may never be the evidence.**
- Verify before adopting. Refining a peer's route is a contribution; inheriting it is not.

---

## 3. The 25 Mandatory Challenge Questions

Each is answered per Learning Item or per bounded group of Learning Items, with a disposition and an
evidence pointer.

### A. Population & Discovery
1. **Missing menus?** Is the menu population derived by a rule over the whole evidence base, or listed?
2. **Missing functions?** Which functions exist with no menu at all (smart buttons, context actions,
   wizards, automation, API-only)?
3. **Missing configuration paths?** Which behaviours are reachable only from a settings screen?
4. **Missing feature toggles?** Is every toggle class covered — group activation, module installation,
   system parameter, pass-through, computed?
5. **Hidden automation?** Scheduled jobs, stored computed values, cascade/deletion behaviour,
   create/write/unlink overrides, sequence allocation.
6. **Hidden scheduler behaviour?** Interval, activation default, idempotency, failure and catch-up.

### B. Interpretation
7. **Wrong functional interpretation?** Does the described behaviour follow from the cited evidence?
8. **Alternative workflow?** Is there a second legitimate path to the same business outcome?
9. **State-transition exception?** Which transitions are absent, one-way, or reachable out of order?

### C. Consequence
10. **Cross-module dependency?** Which other domain owns part of this lifecycle?
11. **Accounting consequence?** What is posted, when, at what value, and what happens on reversal?
12. **Inventory consequence?** Quantity, ownership, valuation and reservation effects.

### D. SaaS / Security
13. **Security weakness?** Access rights, record rules, field-level gating, method-level guards.
14. **Tenant leakage?** Can a lower-level relationship weaken an upper-level boundary?
15. **Company boundary conflict?** Which records are company-scoped, which are shared, which are null-company?
16. **Approval bypass?** Any route to the controlled outcome that skips the control.

### E. Edge & Lifecycle
17. **Reverse / Cancel / Return gap?** Is every forward action reversible, and is the reversal itself audited?
18. **Migration / historical issue?** Legacy data, cutover, effective dating, historical immutability.
19. **Reconciliation gap?** Can the end-to-end result be proved from independent sources?

### F. Evidence Quality
20. **Weak evidence?** Is any claim carried by a summary, a memory, or a secondary source?
21. **Source contradiction?** Does the package contain a fact and its negation in two files?
22. **Clean-room contamination?** Vendor tokens on a Layer 1 surface — measured as a per-file count
    delta against baseline, not read by eye.
23. **Unsupported SMEsPlus design assumption?** Reference behaviour silently promoted to target design.
24. **Performance / scale issue?** Behaviour that is correct but not viable at tenant scale.
25. **Whole-system contradiction?** Does this finding contradict another domain's frozen finding?

### G. Mandatory additional classes (added by the Inventory Pilot — see CORR register)
26. **Instrument challenge.** For each published count: was the second-shape control run? the positive
    control? the coverage assertion? Was any zero re-tested?
27. **Denominator challenge.** Are D1–D5 declared *and executed*? Was the population instrument the
    same as the claim instrument?
28. **Decision-authority challenge.** Does any statement in this package settle a question reserved
    to Boss, or promote an unresolved peer blocker to a rule?
29. **Boundary challenge.** Is the domain boundary declared as a *set*, or described in prose? Is the
    complement published?
30. **Generation challenge.** Is every source finding labelled with the generation it was read from,
    and was that generation established by a content-based discriminator?

---

## 4. Dispositions

| Disposition | Meaning |
|-------------|---------|
| `PASS` | Challenged, no defect found, evidence sufficient |
| `QUESTION` | Clarification needed; does not block |
| `GAP` | Known missing knowledge with an owner and a trigger |
| `CONTRADICTION` | Two supported statements conflict; must be resolved before the Gate |
| `CRITICAL GAP` | A Critical Area is not at 100% |
| `SOURCE RESOLUTION REQUIRED` | Routed to LESA; general researchers must not free-search |

---

## 5. Recording Rule

A revision log is **not** a correction. Every accepted finding must be edited into the register text
itself, and the audit must be performed **by identifier over the whole population**, never by reading
the disposition column. A `CORRECTED` marker over an unrepaired register is a false assurance about
the entire review.

Pre-commit sweep (four checks, **disjoint units**, last step before every commit):

| # | Unit | Check |
|---|------|-------|
| 1 | identifier | every cited ID is defined; every defined ID is cited or explained |
| 2 | table row | every row of every table is structurally complete |
| 3 | file | manifest hash agreement |
| 4 | token | clean-room vendor-token count delta vs baseline, per file |

Three clean checks have previously shipped a broken integrity record. **A check whose unit does not
match the defect returns clean.**
