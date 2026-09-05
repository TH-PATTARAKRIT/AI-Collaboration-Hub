# P11 — PEER INTAKE DELTA 03 · `SR-02` CORROBORATED FROM SOURCE, AND ESCALATED

Session `SMEPLUS-26-09-04-ACC-P11-CORE-RECON-REV2-001` · Layer 1 clean-room
Source: `research/account-p04-acquire-to-retire-2026-09-04-001` @ `3c10b4e4249e54d8ddf99a36a305ccab0fc23eb5`
(`20_P04_SCOPE_OWNERSHIP_MATRIX.md` §4.2, `11_P04_CROSS_PROCESS_OWNERSHIP.md` §6–§7)

> **Recommendation only. Boss is the sole Final Approver.**
> **P11 reads no reference source.** `P04-F-66` below is `PEER-PUBLISHED` at the SHA above and is
> classified by its owner as **`FACT VERIFIED`**. P11 cites it; P11 does not restate it as its own
> verification.

---

## 1. What changed

P11's `SR-02` derived the second traversal mechanism — the lock cascade — **from standing invariants,
without reading source**. P04 read the accounting core directly and returned it **stronger**, with
three details P11 did not have:

| # | `P04-F-66` — `FACT VERIFIED` at `3c10b4e` |
|---|---|
| 1 | The effective **hard** lock date of a company is the **maximum over its entire parent chain** — not inherited from the immediate parent, but the max across **every ancestor** — computed **with elevated privilege** and **with archived companies included in the traversal** |
| 2 | The **soft** lock dates traverse the same chain, and the source carries an **explicit comment stating that elevated privilege is required because the user might not have access to a parent company**. The code documents that it deliberately reaches companies the caller cannot see |
| 3 | The hard lock is **irreversible by two explicit guards**: removing it raises, and setting it earlier than the current value raises |

> **P11's derivation said the traversal *would be* a cross-tenant financial effect if the hierarchy
> could span. P04's source reading says the traversal is privileged *by design*, self-documented as
> reaching companies the caller cannot access, and its result cannot be undone.**
>
> The inference was right. The mechanism is worse than the inference.

## 2. `P11-F-06` — the compound, and it is the version the Boss must decide against

P04 combines `P04-F-66` with its own `P04-B-31`: an entry aimed at a locked period is **silently
re-dated forward rather than refused**, in the accounting core's **generic posting routine**, so it
applies **product-wide**.

> ### `P11-F-06` — A hierarchy edge crossing a tenant boundary produces **no visible failure**.
>
> It produces **silently mis-periodised entries in the other tenant's books.**
>
> The receiving tenant sees **no error, no refusal and no trace**. It sees numbers in the wrong year.
> The mechanism that would normally surface the breach — a refusal — is the exact mechanism the
> posting routine replaces with a silent date mutation.

**Why this is materially worse than what `D-12` previously put to the Boss.** The earlier framing was
*"a parent in tenant A could irreversibly close a period for a company in tenant B"* — a visible,
attributable act with an obvious victim. The compound is **undetectable from inside the affected
tenant**, and it corrupts period attribution rather than blocking work. A tenant cannot report, escalate
or even notice a harm it has no signal for.

**Classification — CORRECTED at `P11_PEER_INTAKE_DELTA_04.md` §2, `P11-E-17`.**

> **The text below was published and is FALSE. It is retained struck through, per the carry-forward
> rule, because a correction that deletes its error leaves no lineage.**
>
> ~~`P11-F-06` is `P11-DERIVED` from two `FACT VERIFIED` peer findings; the composition is P11's, the
> components are P04's. Neither component was composed by its owner, because `P04-F-66` and
> `P04-B-31` sit in different files answering different questions — which is the whole argument for a
> cross-process seat existing at all.~~

**The truth.** The compound — including the exact phrase *"silently mis-periodised entries in the
other tenant's books"* — was composed **by P04**, in `20_P04_SCOPE_OWNERSHIP_MATRIX.md` at `3c10b4e`
under the heading *"Compounding with `P04-B-31`"* — **the same commit P11 cited two lines earlier as
the source of `P04-F-66`** — and was sent to P11 verbatim before intake. `P11-F-06` is therefore
**`PEER-PUBLISHED`, owner P04**, carried by P11.

**What P11 did contribute, stated exactly because it is smaller:** P11's `SR-02` question is what sent
P04 to read the lock-date implementation. **The value was the prompt, not the composition.**

## 3. `T0-13` — a new tolerance-zero boundary

P11 opens one, and states plainly that it is the **first** tolerance-zero boundary this session has
opened.

| id | Boundary | Status |
|---|---|---|
| **`T0-13`** | ~~A financial effect may not cross a tenant boundary silently.~~ **WIDENED at Delta 04 §1 — this drafting was too narrow and would be satisfied by a system that still misstates a fiscal year inside one company.** Governing text: **an accounting fact may not be silently mutated, at any scope** — refuse, or leave an attributable trace | **`UNRESOLVED`** |

This sits **beside** `T0-04` (tenant isolation), not inside it. `T0-04` asks whether a boundary is
crossed. `T0-13` asks whether the crossing is **detectable**, and the two have different remedies: an
isolation invariant closes `T0-04`; only a refusal-or-trace guarantee closes `T0-13`.

**Tolerance-zero tally, corrected:** **13 boundaries, `0` resolved** — 12 inherited, 1 opened here.
`P03` additionally hands forward 8 financial-integrity boundaries of its own, 2 designated
`Tolerance = 0`. `CONDITIONAL PASS` remains unavailable **by rule**.

## 4. `D-12` — restated for the Boss

The decision is unchanged in form and changed in stakes.

> **`D-12` — Rule whether a company hierarchy may span a tenant boundary. P11 recommends `NO`.**
>
> **What the Boss is deciding against, restated:** not *"may a parent close a child's period"* but
> **"may an act in one tenant silently mis-periodise another tenant's books, with no error, no
> refusal and no trace, through a traversal the source documents as deliberately reaching companies
> the caller cannot access, producing a lock that cannot be undone."**
>
> **The ruling still does not discharge the hold.** `P11-SR-02`'s position is unchanged: a ruling is
> not an enforcement, no published invariant makes tenant assignment binding, and the lift condition
> at `P11_PEER_INTAKE_DELTA_02.md` §2 stands. What the corroboration changes is the **cost of getting
> the ruling wrong**, not the ruling's status.

## 5. The counting disagreement — reconciled, because that is P11's job

P04 declined to reconcile its tally with P11's, recording both and noting *"the number is not the
point"*. **P04 is right that the number is not the point, and P11 still owes the reconciliation** —
publishing two counts of one phenomenon without stating what separates them is the defect itself.

| Framing | Declared population | Window | Count |
|---|---|---|---|
| **P11's** *"fourth in the programme, second in this session"* | instances **recorded in a P11 register** | programme to date | 4 / 2 |
| **P04's** *"five instances, five different actors"* | instances **observed by, or reported to, P04** | this wave | 5 |

> **Neither is a denominator of the other. P11's population is narrower — it counts only what reached
> a P11 register — and P11 published it *without declaring that boundary*.**

`P11-E-15`: a count published without its declared population, in the file arguing that counts must
declare their population. By P04's own unit that makes it a **sixth** instance, and by P11's it is not
an instance at all — which is precisely why the unit had to be declared before the tally could be read.

**The reconciled statement, with the unit fixed** — *and the actor count itself CORRECTED at
`P11_PEER_INTAKE_DELTA_05.md` §3 as `P11-E-18`: it is **four** distinct actors, not five; P04 repeats,
and P11 inherited the figure without executing it* — the enumeration defect has recurred **at least six
times across ~~five~~ four actors** — a parallel research stream, P04's first draft, the independent adversarial
reviewer briefed specifically to catch it, P04 again on a field count, P11's inert intake script, and
P11's undeclared tally. **None was careless. Every one was caught by executing the count rather than
reading the report** — and the one that was not executed is the one still being argued about.

## 6. Adopted from P04 without amendment

- **`P04-B-44`** — the equipment determination now carries its **expiry trigger** in P04's own matrix. P04 adds that the **work centre was the first** such case, so **two** of its scope determinations depend on the system not yet complying with TAS 2. P04's conclusion — *"a scope matrix built against a non-compliant system has a shelf life"* — is adopted and generalised as a P11 position: **`SCP-09` — a scope determination taken against behaviour the programme is obliged to change must record its expiry trigger; it is a dated reading, not a standing fact.** `P11-F-05` becomes its first instance.
- **`P04-REV-10`** — P04 found five blocker identifiers cited in one file and absent from its register, caught by **running a cross-reference, not by reading**. This is `P11-G-01` confirmed from a second direction, and it strengthens the obligation P11 already accepted for its own three class-level blocker rows.

## 7. Net effect

| Measure | Before | After |
|---|---|---|
| Tolerance-zero boundaries | 12 inherited, 0 resolved | **13, 0 resolved** — `T0-13` opened |
| Programme-level findings | 5 | **6** — `P11-F-06` |
| Scope positions | 8 | **9** — `SCP-09` |
| P11 blockers | 15 | **16** — `P11-B-16` carries `T0-13` |
| Session errors logged | 14 | **15** — `P11-E-15` |
| Recommendation | `HOLD` | **`HOLD` — unchanged** |

**This delta closes nothing.** It strengthens one derivation, opens one tolerance-zero boundary, and
raises the stakes of a decision already routed to the Boss.
