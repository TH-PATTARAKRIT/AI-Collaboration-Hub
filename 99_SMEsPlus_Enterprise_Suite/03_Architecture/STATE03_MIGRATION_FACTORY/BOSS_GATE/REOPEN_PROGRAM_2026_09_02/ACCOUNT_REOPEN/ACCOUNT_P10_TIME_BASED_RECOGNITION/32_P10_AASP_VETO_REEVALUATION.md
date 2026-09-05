# P10 — AASP-VETO-01 RE-EVALUATION

Session: `SMEPLUS-26-09-04-ACC-P10-TBR-CROSS-PROCESS-RECON-001` · Layer 1
**REVISION 3.** Revision 2 narrowed the veto on three grounds. **All three failed under independent challenge and all three failures were verified by P10.** Revision 3 restores what revision 2 gave away.

---

## 1. The Veto as Originally Issued

> **`AASP-VETO-01`** — no implementation of any P10 mechanism may start until the Boss rules whether a posting constraint may alter a recognition period.

## 2. Why Revision 2 Was Wrong

| # | Revision 2's narrowing ground | Verdict |
|---|-------------------------------|---------|
| `G-1` | "The decision is no longer binary — the tolerance-zero boundary is adopted programme-wide and two of the options already satisfy it" | **DOES NOT HOLD.** The boundary is an **open peer blocker** carried as `BOSS DECISION REQUIRED` / `UNRESOLVED`, with none of that peer's thirteen boundaries resolved. P10 promoted a proposed close condition to an adopted rule. `34` `W-27` |
| `G-2` | "The veto is no longer the first constraint — a peer holds a broader veto that fires earlier" | **DISPROVED, and it was the reverse.** The peer's veto is scoped to that peer's own model, is implementation-only, and its own text says it **does not block the other processes**. It does not bind P10 at all. **`AASP-VETO-01` is not redundant — it is the only veto standing between a ruling on the event identity and someone building a recognition mechanism.** P10 narrowed the one instrument that was actually load-bearing, on a misreading. `34` `W-28` |
| `G-3` | "The trace-preserving option cannot be implemented anyway until the ledger provides a period field" | **DOES NOT HOLD.** A shipped lock-exception mechanism preserves the true posting date with **no period object and no ledger change**. `34` `W-29` |

Three grounds, none of which holds, each verified from primary source by P10 after the challenge raised it.

## 3. The Clause That Should Never Have Been Written

Revision 2 stated:

> *"It does not lift on evidence, because no further evidence bears on it — the behaviour is fully characterised."*

**That is a negative claim about P10's own evidence base, asserted with no search — the `P10-R-08` defect, in the document that governs the package's binding veto.** It was falsified four times inside the same round:

1. the landing period is selected by the journal's sequence numbering format, not by one convention;
2. a shipped lock-exception mechanism supplies an option nobody had counted;
3. a test **does** exercise the live path under a lock and simply declines to assert where the money lands;
4. three of four deployed databases have **no lock set at all**, so the defect cannot currently fire in them, while the fourth — the one P10 wrongly declared unreadable — carries four locks.

**A veto that declares itself immune to evidence is a governance risk, not a protection.** The clause is struck.

## 4. What the Deployment Fact Actually Does

Revision 2 argued the veto could not lift because "the deployed estate runs the path that silently re-dates, in every one of the 44 companies examined". **A lock violation requires a lock.** No company in either of those databases has one. The claim was unsupported by the data it cited.

The corrected reading **does not weaken the veto — it changes what the veto is protecting against**:

> The estate is almost entirely **un-exposed today**. The veto is therefore not holding back remediation of a live misstatement; it is holding a design choice open **before the first company closes a period**. That is the cheapest moment to take it, and the most expensive one to get wrong.

## 5. Grounds That Should Be Added, Not Removed

This round produced a **new defect class** the original veto's grounds do not mention: a **corrective reversal lands in a different period from the entry it corrects** — now verified with an executed positive control, in which a January entry's reversal is dated end of February. The reopen-and-regenerate interaction sits beside it.

The veto's subject ("any P10 recognition mechanism") is broad enough to cover correction. Its **stated grounds** were entirely about generation. **Widen the grounds; the subject already covers it.**

## 6. Restated Veto — Revision 3

> **`AASP-VETO-01` (revision 3)** — no implementation of any P10 recognition mechanism may start until **both**:
>
> (a) Boss decision `D-5` — the accounting-event identity — is taken; and
> (b) Boss decision `P10-D-02` selects among the options classified in `28` **revision 2**, decided **jointly with the peer boundary `T0-13`**, which is an open blocker and the same question in another vocabulary.
>
> **Grounds** cover generation, **correction and reversal**, and the reopen path.
>
> The veto does **not** block design work, option analysis, or specification of the thin recognition layer.
>
> It lifts when both decisions are taken. **The clause asserting that no evidence bears on it is withdrawn** — evidence has borne on it four times in one round, and more is obtainable.

## 7. Interaction With Peer Vetoes — corrected

| Veto | Owner | Actual scope | Relationship to P10 |
|------|-------|--------------|---------------------|
| Peer management-accounting veto | `P09` | That peer's own model; implementation only; **explicitly does not block other processes** | **Does not bind P10.** Revision 2's claim that it binds first is withdrawn |
| Peer costing veto | `P04` | Separate subject, not discharged | No interaction |
| `AASP-VETO-01` rev 3 | `P10` | P10 recognition mechanisms | **The only veto binding P10's implementation** |

Revision 2's governance observation — "the fastest way to discharge three vetoes is to take one decision" — is **withdrawn**. The three vetoes are not co-extensive, and only one of them is P10's to hold.

## 8. Standing Correction to Method

Three of this veto's grounds failed because P10 **inherited peer conclusions without reading the peers' own status fields**. The peer's blocker register said `UNRESOLVED`; the peer's veto text said "does not block other processes". Both were one file away.

> **A peer's position must be read from the peer's register, not from a peer's summary or from another process's account of it** — the programme's adversarial-section rule, applied to peers rather than to one's own prior rounds.
