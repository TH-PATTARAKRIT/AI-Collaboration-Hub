# P11 — `CO-F-02` STALE INBOUND NEGATIVE REPAIR

**Session** `[SMEPLUS-26-09-07-ACC-PHASE-S-REMEDIATION-002]`
**Authority** Boss ruling `Q-BOSS-03` §3.A @ closeout `2e2b8de`
**Base** `corr/p11-phase-s-final-2026-09-07-001` @ `002748d` — **read-only, never rewritten**
**Peer evidence** read at its immutable SHA; **P08 was not edited and will not be.**

> Owner repair, not verification. **`RC-02` must test it.** No disposition, no PASS.

---

## 1. The two stale assertions, exactly as they stood

| # | Carrier | Line | Text as published |
|---|---|---|---|
| 1 | `P11_OWNER_BOUNDED_CORRECTION_2026_09_07.md` | `112–113` | *"**`P08` owes P11 this notification in writing under `Q-P08-01`. Not yet received; recorded as outstanding.**"* |
| 2 | `P11_AUTO_RESUME_STATE.md` | `101` | *"**OUTSTANDING INBOUND:** `P08` owes P11 the `Q-P08-01` notification in writing. Not received."* |

**Claim class:** *a P08 inbound owed under `Q-P08-01` has not arrived.* **Both are now struck in place
with the superseded text preserved.**

## 2. The notification, at its immutable SHA

`64_P08_NOTIFICATION_TO_P11_Q_P08_01.md`, added by **`c7cfd8a`** on
`research/account-p08-record-to-report-2026-09-04-001` — the same commit that is `RC-05`'s frozen
surface. **Read at that SHA, not from any summary of it.**

| Event | Commit | Timestamp |
|---|---|---|
| **P08 publishes the notification** | `c7cfd8a` | **`2026-09-07 09:05:24 +0700`** |
| P11's first owner-correction commit | `ce0cc2b` | `2026-09-07 09:07:25 +0700` — **+2 min 01 s** |
| P11's final correction commit | `002748d` | `2026-09-07 09:09:56 +0700` — **+4 min 32 s** |

**Both negatives were false when written, and false again when carried forward into the resume state.**

## 3. What the notification actually says — the replacement text's only basis

- The figure *"at `1e-7` the answer is 3"* in `58_` §1 item 1 **has no referent** and has been
  **deleted, not re-scoped** — `P08-CONTRA-75`.
- Re-derived in **exact decimal, no floating point at any step**: **0 unbalanced** on `DB-SM`
  (169,143 posted), `DB-BK` (16) and `DB-EV` (6), on **both** the computed and the stored balance
  column, at **exact equality** and at `1e-7`, `1e-4`, `0.005`. **Tolerance-independent.**
- P08 **expressly declines to adjudicate** P11's disposition of `F-02` or of the derived method rule:
  *"Whether to retain, re-ground or withdraw the rule is P11's decision."*
- P08 draws a distinction P11 needs: the **settlement** reconstruction **is** tolerance-dependent —
  **2,354 lines at exact equality, 0 at ≥ `1e-6`, worst residual `2.1 × 10⁻⁹`** — while the **balance**
  measurement needs no tolerance. **P08 marks this `SUPPORTED INTERPRETATION`, not fact:** *"the
  mechanism was not traced and the round that published the figure is closed."*
- P08 records `RC-05` as **REQUIRED and NOT SATISFIED** and `AAS+-PS-VETO-01` `C-6` as
  **NOT DISCHARGED**.

**P11 adopts the first three as the basis for the receipt correction. P11 adopts none of the
interpretive limbs as verified**, and neither discharges nor comments on P08's veto.

## 4. What this does and does not change

| | |
|---|---|
| The **receipt record** | **CORRECTED — the negatives are withdrawn as false** |
| `Q-P11-04`'s **substantive disposition** | **UNCHANGED and NOT re-opened.** `F-02` withdrawn, method rule withdrawn — exactly what the notification supports |
| `AAS+-PS-VETO-01` `C-6` | **NOT DISCHARGED** — P08's, not P11's, to discharge |
| `RC-05` / `RC-06` | **UNAFFECTED.** `RC-06` remains blocked on `RC-05` |

**The narrow, and uncomfortable, statement of the defect:** P11 reached the **right conclusion** on
`Q-P11-04` while simultaneously asserting it had never been told. The **conclusion** was sound; the
**provenance record attached to it** was false. A reader auditing P11's disposition would have found
it unsupported by anything P11 admitted holding.

> **`P11-G-14`: an inbound is received when the producer publishes it at a resolvable ref, not when the
> consumer notices. Re-read every "not received" against the producer's ref immediately before
> publishing** — a receipt negative decays faster than any other claim in a live multi-party round, and
> it decays silently.

## 5. Package-wide sweep for the same claim class

**Required by the remit: report every occurrence, not only the two named.** Swept with **five
independent patterns** over **every `*.md` in the P11 package** — `owes P11` · `not (yet) received` ·
`awaiting|await` · `outstanding` · `no notification|never notified|not notified|absent|has not
been sent/delivered/arrived/provided`.

| Result | |
|---|---|
| Occurrences **in this claim class** | **2 — both named in §1, both repaired** |
| Further occurrences | **0** |

**Inspected and excluded, with the reason stated rather than left silent:**

| Hit | Why it is not in this class |
|---|---|
| `P11_BLOCKER_REGISTER_CORR2.md` `B-29` — *"P08's `AAS+-VETO-01` … is absent from the package"* | A **CORR2-era** claim about a **veto artefact**, not about the `Q-P08-01` notification. **Different claim, different producer artefact, not tested here** — flagged to `RC-02` as adjacent and **unverified by this session** |
| `B-25`, `B-28`, `EC-08`, `D-10`, `DEP-14` | *"outstanding"* / *"absent"* about decisions, producer cells and monetary positions — **not inbound-receipt claims** |
| ~60 `absent` hits in the domain registers | Absent **accounting events, fields and mechanisms** — the domain sense of the word, unrelated to inbound receipt |

**The `absent` pattern is deliberately over-broad and its false positives are reported rather than
filtered away**, so a reader can see the sweep could have caught more and did not miss quietly.

## 6. A genuinely unconsumed inbound — recorded, not repaired

`P06_TO_P11_COUNT_CORRECTION_NOTICE.md` was added by **`b5f5a21`** at
**`2026-09-07 09:11:29 +0700` — 1 min 33 s *after* P11's final commit `002748d`.**

**P11 makes no assertion about it, so no P11 negative concerning it is stale.** It is an **unconsumed
inbound**, not a defect in the published package. **Not consumed here** — it lands on the `RC-04`
surface and consuming it would widen this bounded remit. **Routed to `RC-02`/`RC-04` as a dependency.**

## 7. Standing

| | |
|---|---|
| `CO-F-02` | **REPAIRED — UNVERIFIED** |
| Verification | **`RC-02`** |
| P08 package | **NOT MUTATED** |
| Terminal | **`TERMINAL B` — unchanged** |

**No Evidence = No Progress. Never Skip Gate. Boss is the sole Final Approver.**
