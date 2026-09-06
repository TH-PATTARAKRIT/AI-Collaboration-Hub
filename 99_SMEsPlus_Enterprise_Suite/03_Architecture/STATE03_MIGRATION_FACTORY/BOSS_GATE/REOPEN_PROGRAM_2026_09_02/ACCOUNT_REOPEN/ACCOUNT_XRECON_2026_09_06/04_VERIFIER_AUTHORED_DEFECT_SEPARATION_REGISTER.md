# 04_VERIFIER_AUTHORED_DEFECT_SEPARATION_REGISTER

**Session** `[SMEPLUS-26-09-06-ACC-P06-P08-P09-P11-XRECON-001]` · branch `audit/account-xrecon-2026-09-06-001`

> **Why this register exists.** A defect the auditor introduced is not a defect in the audited package.
> Counting them together inflates the owner's repair queue and lets the auditor's own errors ride on the
> authority of its findings. **Class C is separated here and is excluded from every owner's source queue.**

---

## 1. Separation summary

| Track | Total material defects published | **Authored by the audited party** | **Authored by the verifier** |
|---|---|---|---|
| **P06 IEV** | **25** | **23** | **2** |
| **P08 IEV** | **17** | **17** | **0** |
| **XRECON (this session)** | — | — | **0 introduced; 2 instrument failures self-detected — see §4** |

## 2. P06 — the two verifier-authored defects

### `IEV-I-03` / `41_`:6 — a broken supersession pointer the verifier itself inserted

**Counted inside the 25, and correctly so** — it is live on the source package and a reader will hit it.
**But its author is the verifier, in its prior role as the `REV-E-23` repair actor.**
`41_`:6's supersession pointer cites five lines and **all five are wrong by exactly 3** — inserting the
3-line pointer shifted the file it points into, sending readers to a blank line and a table separator.

| Field | Value |
|---|---|
| Owner of the **repair** | **P06 source** — it is on P06's file (routed as requirement 5) |
| Owner of the **error** | **the verifier** |
| Why it matters | it is evidence for `XRD-009`: the actor that repaired is the actor that audited |

### `IEV-D-20` / `INSTRUMENT_CONTROL_REGISTER`:45 — a validation row certifying a superseded figure

**This one is entirely inside the verifier's own artefact** and is `XRD-002`.
A validation table publishes *"65 `P06-B-*` … max id = 65 and contiguous | **YES**"* while `:54` of the same
file raises `P06-B-66` and `P06-B-67` **nine lines later**.

**The addendum left it standing deliberately** — *"it is left standing here so the defect is legible rather
than quietly repaired"*. **XRECON endorses that choice** and requires the repair to retain the original row
as marked-superseded rather than overwrite it.

**XRECON confirmed the true figure independently:** 67, two instrument forms, `diff`-identical identifier
sets, contiguous 01–67, synthetic-injection control 67 → 68. See `01_` `XS-01`.

### `IEV-I-01` and `IEV-I-05` — not defects in any package, but the two most transferable findings

| ID | What happened |
|---|---|
| **`IEV-I-01`** | The verifier's **first instrument failed silently.** Nine claim-class sweeps held their glob list in a shell variable; **zsh does not expand those.** The positive control returned **0 occurrences of `P06` across an 87-file P06 package.** *"Without it I would have certified nine clean classes on nine fabricated zeros and recommended discharge"* |
| **`IEV-I-05`** | The verifier **disposed of a missing challenger by reasoning about what it would probably have said** — *"its remit is materially covered … no finding in this package depends on it"*. Expert 2 then returned **12 material defects, 7 absent from the published 18**, one of them in the verifier's own artefact. *"The cheapest way to be wrong about a missing input is to reason about what it would probably have said"* |

**`IEV-I-04`** — one challenger of four did not return before publication; recorded as a gap, not a clean
result. **That gap is `IEV-I-05`.**

## 3. P08 — zero verifier-authored defects, and one verifier-only finding

**No defect among the 17 is attributed to the P08 verifier.** Two items are nonetheless recorded here:

| Item | Nature |
|---|---|
| **`IVR-F-13`** | **The verifier's own finding, raised by no challenger** — the handoff identifier namespace is collided across two live artefacts. Not a verifier *defect*; a verifier *contribution*, and the origin of `XRD-006` |
| **`XRD-007`** | **A verifier-authored publication defect found by this session.** `IVR-INB-03`/`-04` cross-reference *"bounded repair requirement 2"* (and *"2 and 4"*), but terminal-report requirement 2 is the *"3 at 1e-7"* deletion — which **the same addendum says is unaffected** — and requirement 4 is the capability denominator. **The FX cause-clause repair has no requirement number.** Class C, owner P08 IEV |

**Also recorded to the verifier's credit:** it recorded **five challenger errors rather than adopting them**,
and noted that **a challenger withdrew a finding on its own control**.

## 4. XRECON's own instrument failures — recorded first-person

**This session introduced no defect into any package. It did commit two instrument failures, both caught by
controls before anything was published.**

| ID | Failure | How it was caught | Consequence had it stood |
|---|---|---|---|
| **`XR-I-01`** | **`git grep -o` returns nothing in this environment.** The first cross-Pxx peer-SHA sweep returned **zero matches across the entire P11 package** — a clean, plausible, publishable negative | **Positive control.** `9356557`, a SHA known to be present, **also returned zero.** Instrument failure, not a finding | XRECON would have published *"P11 cites no P09 SHA"* — **the exact opposite of the truth**, and `XRD-005` and `XRD-008` would never have been found |
| **`XR-I-02`** | **`\b` word-boundary is unsupported by `git grep`'s ERE.** `\bP06-B-[0-9]{2}\b` returned **0** against a population of **67** | Run as the **second form** of a two-form count whose first form returned 67. The disagreement exposed it | A validated-looking zero on a populated set — the same shape as `IEV-I-01` |

**Both are the defect class this programme already knows** (`prove-the-filter-can-fire`,
`counting-command-validation`). **They recurred anyway, in the session convened to reconcile them.** That is
recorded not as self-criticism but as evidence for the finding below.

## 5. What the separation shows

**Three of eleven root defects are verifier-authored** (`XRD-001`, `XRD-002`, `XRD-007`) — **27%.**

Add the two P06 auditor self-findings (`IEV-I-01`, `IEV-I-05`) and this session's two (`XR-I-01`,
`XR-I-02`), and the pattern is unambiguous:

> **The verification layer fails at the same rate and in the same shapes as the layer it verifies.**
> Every failure above is an instrument that could not fire, a population declared from remembered wording,
> or a figure published in the present tense after it stopped being true. **Not one is a wrong claim about
> the ERP.**

**The control that worked, every time, was the positive control** — and in three of four cases it was the
*only* thing standing between a fabricated zero and a published finding.

**The control that failed, every time, was an actor reasoning about evidence it did not have** — P06's
Expert-2 disposition, P11's inherited peer heads, P08's requirement cross-reference.
