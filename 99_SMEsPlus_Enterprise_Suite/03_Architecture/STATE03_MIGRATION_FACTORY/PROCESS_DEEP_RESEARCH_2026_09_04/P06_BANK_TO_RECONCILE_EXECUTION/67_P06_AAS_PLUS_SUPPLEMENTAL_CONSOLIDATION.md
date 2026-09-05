# P06_AAS_PLUS_SUPPLEMENTAL_CONSOLIDATION.md

**Session:** P06 — SUPPLEMENTAL CRITICAL-RISK CLOSURE
**Classification:** LAYER 2 — AUDIT QUARANTINE

---

## 1. Consolidation across the eleven required dimensions

| Dimension | Assessment |
|---|---|
| **Security control** | **FAILED.** No server-side authorisation on the destructive dispatch chain; the only gates are a menu attribute and a client-side confirm. Corroborated by P08 `AT-21`, whose open question P06 has now answered. |
| **Financial integrity** | **FAILED.** Posted entries, payments, statements and reconciliations deletable by unfiltered SQL; balance survives, truth does not; the ledger is left in a state the ORM rejects. |
| **Accounting provenance** | **FAILED.** The audit trail is a deletion target and a cascade victim; `mail_tracking_value` goes with `mail_message`; on a default installation a forced deletion leaves no record at all (P08 `JPM-28`). |
| **Auditability** | **FAILED.** Failure states carry no payload; the one durable trace of a rejection is a chatter entry that the same tool deletes. |
| **Scope** | **FAILED, and instructively.** The operation is PLATFORM-scoped and its targets are COMPANY-scoped; the author applied company filtering to the sequence reset and the auxiliary updates and **not** to the deletes. |
| **Version boundary** | **IMPROVED.** Six core findings cross-version invariant. Target generation still undeclared; the FK, sequence and numbering analyses remain v18-only while the installation evidence is v19. |
| **Deployment boundary** | **IMPROVED and WORSENED.** Registry evidence obtained — the module is **installed** on a v19 database. It is **not** the SMEsPlus target, so the target question is unchanged; but the module is no longer hypothetical. |
| **Banking semantics** | **UNCHANGED.** No bank-confirmation fact, no fee/interest/commission concept, no returned-item lifecycle. All survive an enlarged population. |
| **Period close** | **RESOLVED IN OWNERSHIP, UNRESOLVED IN SUBSTANCE.** P08 claims it and supplies the answer P06 needed: *"no field anywhere answers 'is month M closed?'"* The reconciliation relation remains outside the regime. |
| **Cross-process contradictions** | **ONE, RECONCILED AND ROUTED.** `P06-XC-01` classified `BOTH PARTIAL / CONFIGURATION-DEPENDENT`, routed to P11 as `P11-C-08`. Zero contradictions with P08 across six convergences. |
| **Blocker severity** | **BUILT.** 6 CRITICAL · 17 HIGH · 20 MEDIUM · 3 LOW · 7 INFORMATIONAL · 2 UNRANKED. Two axes, two different first actions. |
| **Recovery** | **NONE.** No reversal, no log, no rollback; per-table commit makes partial destruction durable. |

---

## 2. The consolidated position

**Three things now stand together that did not before:**

1. **The bank half of P06 runs on unmodified reference behaviour** — 0 of 12 custom modules touch `account.bank.statement`.
2. **That reference behaviour has no bank-confirmation fact, no bank-event identity on 4 of 7 doors, and no period-close discipline over reconciliation** — each independently corroborated by at least one peer.
3. **And the estate contains an installed module that can delete the entire ledger, its reconciliations and its audit trail by unauthorised SQL** — corroborated by P08, evidenced by a database dump, and with first-party evidence that it has already been run once.

**AAS+ consolidated view: the third fact changes what the first two mean.** Weak foundations are a design problem. **Weak foundations plus an installed, unauthorised, irreversible deletion path is a control environment problem, and it is not solved by better design of the settlement model.**

---

## 3. Dissent preserved — 16 items

Carried forward: `DIS-01` … `DIS-11` (rounds 2–3), plus this round's:

| ID | Position | Counter | Status |
|---|---|---|---|
| `DIS-12` | Rebranding indicates programme adoption | may be vendor white-labelling | **both stand** |
| `DIS-13` | `B-13` is CRITICAL | identity fields are not the audit trail | **retained, marked weakest** |
| `DIS-14` | `B-50` is CRITICAL | conditional on target installation | **retained, marked conditional** |
| `DIS-15` | v19 evidence transfers | only for the six re-tested findings | **refined** |
| `DIS-16` | Self-correction is a strength | indistinguishable from unreliability from inside | **unresolved — `P06-B-58`** |

**No dissent was resolved by majority. Two were resolved by evidence; three stand.**
