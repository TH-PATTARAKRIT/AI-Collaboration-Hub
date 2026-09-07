# 02 — `CO-F-02` STALE INBOUND NEGATIVE REPAIR (controller record)

**Repair published on** `corr/p11-phase-s-remediation-2026-09-07-001` @ **`9d4ecdc`**
**Full owner record** `P11_CENTRAL_CORE_RECONCILIATION/P11_CO_F_02_STALE_INBOUND_REPAIR.md`
**P08 was read at its immutable SHA and was not edited.**

---

## 1. The two assertions and their timing

| # | Carrier | Line | Text |
|---|---|---|---|
| 1 | `P11_OWNER_BOUNDED_CORRECTION_2026_09_07.md` | 112–113 | *"`P08` owes P11 this notification in writing under `Q-P08-01`. **Not yet received**; recorded as outstanding."* |
| 2 | `P11_AUTO_RESUME_STATE.md` | 101 | *"**OUTSTANDING INBOUND:** `P08` owes P11 the `Q-P08-01` notification in writing. **Not received**."* |

| Event | Commit | Timestamp |
|---|---|---|
| P08 publishes `64_P08_NOTIFICATION_TO_P11_Q_P08_01.md` | `c7cfd8a` | **09:05:24 +0700** |
| P11's first owner-correction commit | `ce0cc2b` | 09:07:25 — **+2 min 01 s** |
| P11's final correction commit | `002748d` | 09:09:56 — **+4 min 32 s** |

**Both negatives were false at the instant they were committed.** Both are now **struck in place with
the superseded text preserved**, and replaced only by statements the notification's own text supports.

## 2. What did NOT change, and why that is the uncomfortable part

**`Q-P11-04`'s substantive disposition is unaffected and was not re-opened.** P11 withdrew `F-02`
and withdrew the derived method rule — which is exactly what the notification supports.

**P11 reached the right conclusion while asserting it had never been told.** The conclusion was
sound; **the provenance record attached to it was false**, so a reader auditing the disposition would
have found it unsupported by anything P11 admitted holding. **The defect is in the receipt record,
not the accounting.**

**Not adopted:** P08's §3 settlement/balance distinction is marked `SUPPORTED INTERPRETATION` **by
P08 itself** and is taken as input, not fact. **`RC-05` remains required; `AAS+-PS-VETO-01` `C-6`
remains NOT DISCHARGED. P11 discharges nothing.**

## 3. Claim-class sweep — five patterns, every occurrence reported

`owes P11` · `not (yet) received` · `awaiting|await` · `outstanding` ·
`no notification|never notified|not notified|absent|has not been sent/delivered/arrived/provided`,
over **every `*.md` in the P11 package**.

| | |
|---|---|
| In this claim class | **2 — both repaired** |
| Further occurrences | **0** |

**Inspected and excluded, with reasons published rather than filtered away:** `B-29` (*"P08's
`AAS+-VETO-01` … is absent from the package"*) is a **CORR2-era claim about a different artefact**,
**not tested here**, and flagged to `RC-02` as adjacent and unverified; `B-25`, `B-28`, `EC-08`,
`D-10`, `DEP-14` are decision/monetary claims, not receipts; ~60 `absent` hits are the domain sense
of the word. **The over-broad pattern's false positives are listed so a reader can see the sweep did
not miss quietly.**

## 4. A genuinely unconsumed inbound — recorded, not repaired

`P06_TO_P11_COUNT_CORRECTION_NOTICE.md` @ **`b5f5a21`**, `09:11:29` — **1 min 33 s after** P11's
final commit. **P11 asserts nothing about it, so no P11 negative concerning it is stale.** It is an
**unconsumed inbound**, not a package defect. **Not consumed here** — it sits on the `RC-04` surface
and consuming it would widen the remit. **Routed as a dependency to `RC-02`/`RC-04`.**

**New:** `P11-G-14` — *an inbound is received when the producer publishes it at a resolvable ref, not
when the consumer notices; re-read every "not received" against the producer's ref immediately before
publishing.*
