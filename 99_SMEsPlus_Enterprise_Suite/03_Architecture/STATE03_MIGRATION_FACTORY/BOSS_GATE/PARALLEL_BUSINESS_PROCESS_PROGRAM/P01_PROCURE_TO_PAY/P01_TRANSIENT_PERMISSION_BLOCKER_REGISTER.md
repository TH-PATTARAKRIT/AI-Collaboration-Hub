# P01 — TRANSIENT PERMISSION / TOOL BLOCKER REGISTER

Session: `SMEPLUS-26-09-05-…-EVIDENCE-VERSION-DEPLOYMENT-INTEGRITY-001`
Layer: **1.**

Governing rule established by this programme:
**`PERMISSION FAILURE ≠ PERMANENT CAPABILITY ABSENCE`** and
**`ONE TOOL CANNOT READ AN ARTIFACT ≠ ARTIFACT IS UNREADABLE`.**

---

## 1. THE REGISTER

| ID | Operation | Timestamp | Error | Environment | Retry condition | Later outcome | Classification | Current status |
|---|---|---|---|---|---|---|---|---|
| `TB-01` | Push the research branch to the remote | round 2, 2026-09-04 | refused by the environment's permission classifier | interactive agent session | retry in a later turn | **Succeeded in round 3 with no change by the executor** | **TRANSIENT** | **CLOSED — published** |
| `TB-02` | Read the fourth database archive | rounds 2 and 3 | `unsupported version (1.16) in file header` | restore binary 16.15 | use a restore binary ≥ 18 | **Read successfully with the 18.6 binary already installed at a sibling path** | **TOOL FAILURE** — not an environment or permission failure | **CLOSED — read** |
| `TB-03` | Inter-agent messaging, to forward a mid-session constitution correction to running experts | round 2 | facility disabled in this environment | agent session | none found | Not retried; the correction was applied by the session instead, and the affected assignment was re-run **with** the correction in a later round | **PERSISTENT — in that environment** | **MITIGATED, not resolved** — see `DEP-P01-06` |
| `TB-04` | Authenticate the issue-tracker connector | rounds 3 and 4 | connector unauthenticated; OAuth cannot be run non-interactively | agent session | user authorises the connector | not retried | **AUTHORIZATION REQUIRED** | **OPEN — `JIRA — AUTHORITATIVE ISSUE NOT VERIFIED`** |

---

## 2. THE TWO STALE BLOCKERS THIS ROUND RETIRES

Both `TB-01` and `TB-02` were carried in the package as blockers **after the evidence had already
changed**. The directive's instruction — *do not keep a stale blocker after evidence changes* —
is what retires them.

| Blocker | How long it was stale | What it cost |
|---|---|---|
| `TB-01` publication blocked | one round | The package reported `PUBLICATION BLOCKED` in its own terminal statement while the operation was in fact available. It also contributed a false entry to a peer's cross-process dependency (`DEP-23`) |
| `TB-02` archive unreadable | **two rounds** | The most fully-installed deployment was excluded from the evidence base, producing **three false published claims** (`FAL-01`..`FAL-03`) |

---

## 3. THE PATTERN

Both were recorded honestly at the time — the error message was real, the operation genuinely
failed. Neither was re-tested when circumstances changed, because **a failure had been converted
into a property of the world**.

> A blocker is a **measurement**, not a **fact**. It carries a timestamp and a tool version, and
> it expires.

**Standing control adopted for P01:** every blocker in this register carries a *retry condition*
and a *later outcome* column, and no blocker may be cited in a terminal statement without both
being current.

---

## 4. CLASSIFICATION SUMMARY

| Classification | Count | IDs |
|---|---|---|
| TRANSIENT | 1 | `TB-01` |
| TOOL FAILURE | 1 | `TB-02` |
| PERSISTENT | 1 | `TB-03` |
| AUTHORIZATION REQUIRED | 1 | `TB-04` |
| ENVIRONMENT FAILURE | 0 | — |
| UNKNOWN | 0 | — |

**Two of four were retired this round.** Neither was retired by new capability — both were
retired by **re-testing an assumption**.
