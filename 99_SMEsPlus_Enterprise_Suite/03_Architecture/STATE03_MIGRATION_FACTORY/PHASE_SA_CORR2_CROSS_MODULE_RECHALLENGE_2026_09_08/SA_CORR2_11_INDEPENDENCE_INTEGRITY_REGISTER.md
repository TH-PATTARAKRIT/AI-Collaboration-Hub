# SA_CORR2_11 — INDEPENDENCE INTEGRITY REGISTER
## CP-SA-C2-90 — INDEPENDENCE STATUS VERIFIED

Session: `[SMEPLUS-26-09-08-PHASE-SA-CORR2-XMOD-001]`
Governing law: master prompt §11. Governing ruling: Boss decision `04`, read verbatim from mainline.

---

## 1. The declaration, made before any result in this package is read

**Every challenge layer used in this round is an agent of the same model as the author.**

Under master prompt §11 they are therefore labelled, without exception:

> ### `INTERNAL ADVERSARIAL SELF-CHALLENGE`

They are **not** labelled `INDEPENDENT ASSURANCE`. They are not certification. They discharge no
veto. They do not satisfy the programme's independence standard.

This is stated first because `SA13` §1 established the practice of stating it first, and because a
register that reports impressive findings and discloses its independence limit at the end has
already misled the reader who stopped halfway.

---

## 2. The standard, quoted from the ruling rather than paraphrased

Boss decision `04_BOSS_DECISION_SMT_GRC_ASSURANCE_STRUCTURE`, read from the `origin/SMEsPlus` tree —
**the first time in this programme's Phase SA lineage that it has been read from its source rather
than cited through a prior register** (`C2-I-02`):

> ## 6. Independence Rule
> **DESIGNER != INDEPENDENT CERTIFIER**
> **IMPLEMENTER != SOLE VERIFIER OF OWN CONTROL**
> **AI AGENT != INDEPENDENT ASSURANCE AUTHORITY**
> Internal review may support readiness, but external certification/attestation requires the
> applicable independent qualified body/practitioner.

> `GRAO-03 — DESIGNER MUST NOT SELF-DECLARE INDEPENDENT CERTIFICATION.`
> `GRAO-04 — AI MAY ASSIST CONTROL REVIEW; AI DOES NOT REPLACE QUALIFIED INDEPENDENT ASSURANCE.`
> `GRAO-05 — SECURITY SCANNING, VAPT, ISO CERTIFICATION AND SOC ATTESTATION ARE DISTINCT ASSURANCE ACTIVITIES.`
> `GRAO-09 — NO EVIDENCE = NO VERIFIED CONTROL EFFECTIVENESS.`
> `GRAO-10 — BOSS REMAINS SOLE FINAL APPROVER FOR SMEPLUS GOVERNANCE DECISIONS.`

And the programme's own prior ruling: `XRD-009` is recorded `NOT SATISFIED` on the ground that
**same-model verification is not structural independence**; `PHASE-S/Q-BOSS-02` — who may act as an
eligible challenger — is **raised and unanswered**.

---

## 3. What was actually run in this round, and what each layer is worth

| Layer | Relationship to the author | Label | What it found |
|---|---|---|---|
| Five SMEs Core domain extractions (supply routing; service/project/quality/equipment; exceptions; governance/standards; cross-proof/commercial) | Same model, separate contexts, no access to the author's conclusions at dispatch | `INTERNAL ADVERSARIAL SELF-CHALLENGE` | The material that falsified `SA05`'s seven `HOLD` natures and three of `SA09`'s four missing classes |
| One adversarial challenge of the **frozen** CORR2 package at commit `e280611a` | Same model; given the package and told to falsify it | `INTERNAL ADVERSARIAL SELF-CHALLENGE` | `SA_CORR2_10` |
| The author's own pre-commit sweeps (clean-room tokens, identifier integrity, arithmetic enumeration, evidence-pointer resolution) | The author | **`SELF-CHECK` — not a challenge at all** | `SA_CORR2_12` |

### 3.1 `C2-F-27` — the independence claim is now *evidenced*, in both directions

`SA13` §1 **declared** the limit. `SA20` §6 improved on that: the internal challenge found eight
defects and passed the headline, and the adversarial challenge then falsified it — so the limit was
demonstrated rather than asserted.

**CORR2 supplies the third data point, and it points the other way.**

| Round | Self-review found | External-to-the-author review found |
|---|---|---|
| Phase SA (`SA13` §2) | 8 | — |
| CORR1 (`SA20`) | — | 30 declared (21 dispositioned) |
| **CORR2** | **2 arithmetic check-claims false; 3 clean-room leaks** — all found by the author's own mechanical sweeps | **the material that moved 7 business natures, 4 exception classes and 6 inventory/accounting rows** |

> **The author's own sweeps caught only what a *mechanical* check can catch — a token count, an
> identifier enumeration, an arithmetic re-count. Every finding that changed a conclusion came from a
> layer that did not share the author's reading.** Even same-model separation was enough for that.
> **It was not enough for the one thing that matters most**: no layer in this round questioned the
> *frame* until one was explicitly told to, and the frame was wrong (`C2-I-02`).

That asymmetry is the argument for structural independence, made from this session's own data rather
than from the ruling.

### 3.2 The two self-checks that did fire, published

Because a self-check that never finds anything is not a control:

1. **Three clean-room leaks** in this round's own Layer 1 files — a third-party module technical
   name quoted verbatim *for precision*, and two reference object names inside a *published search
   pattern*. Parent baseline was 0. Found by a mechanical per-file token count, by nothing else, and
   the leaked text was **correct** in every case (`SA_CORR2_03` §2.2.1, `K2-15`).
2. **Two arithmetic check-claims that were false as written** — *"every identifier `AR-01`…`AR-29`
   appears exactly once"* and the same for `BN-01`…`BN-18`. Both read true to a human and failed a
   mechanical enumeration, because rows had been compressed into ranges. **This is the exact defect
   class this package convicts `SA20` of** (`N-05`), committed by the author, in a check line
   asserting its own correctness.

---

## 4. Structural independence — availability tested, not assumed

| Question | Answer | Basis |
|---|---|---|
| Is a materially separate assurance source available to this session? | **No** | Every challenge instrument available here is the same model and the same session's authority |
| Has an eligible independent challenger been commissioned by the programme? | **No** | `PHASE-S/Q-BOSS-02` is raised and unanswered |
| Does the Phase SA constitution require independent assurance before Boss Final Gate? | **The Boss ruling requires it for certification/attestation, not for a recommendation.** `GRAO-04`: AI may assist control review; it does not replace qualified independent assurance | Boss decision `04` §6 |
| Was an evidence-complete challenge package prepared, in case a reviewer becomes available? | **Yes** — the package is frozen at commit `e280611a`, integrity-manifested, and every claim carries a resolvable pointer | `SA_CORR2_12` |

**Status recorded, in the exact words master prompt §11 requires:**

> ### `EXTERNAL INDEPENDENT CHALLENGE — PENDING STRUCTURALLY INDEPENDENT REVIEW`

### 4.1 Is this a legitimate `HOLD` reason?

Master prompt §11 says it is *"if the Phase SA constitution requires independent assurance before
Boss Final Gate"*.

**Tested against the ruling rather than assumed. It is a `HOLD` reason for *certification*, and not
for a *recommendation to Boss*.** `GRAO-04` and §6 reserve independence for certification and
attestation; they explicitly permit internal review to *support readiness*. Producing a
recommendation, with its independence limit declared, is what this session is authorized to do —
and it is what `SA_CORR2_13` does.

> **So the absence of an independent challenger does not by itself block this Final Gate Pack.
> It blocks any claim that Phase SA has been independently assured — and no such claim is made.**

Stating it the other way, as an absolute bar, would have been the easier and more cautious-looking
answer. It would also have been wrong, and it would have withheld from Boss two decisions that are
Boss's alone.

---

## 5. `C2-F-28` — an independence gap the programme has not named

Every independence rule in the corpus governs **who reviews**. None governs **who chose the
evidence base**.

This round's largest single finding is `C2-I-02`: the declared PATH SET could not reach the
mainline, and 27% of the corpus — including every Boss decision body — was outside the population.
That defect was **inherited from the parent package**, survived a full internal challenge, survived
an adversarial correction round, and was found only when a specialist was asked to re-measure a
domain and noticed its own inputs were unreachable.

> **An adversarial reviewer who is handed the author's corpus inherits the author's blind spot in
> full, and no amount of adversarial energy inside that corpus can find it.**

The programme's controls test **conclusions against evidence**. They do not test **the evidence base
against the world**. `SA13` §2 `CH-08` recorded a version of this — *an evidence base is itself a
claim* — and the control that follows from it was never built.

**`ND-12` (governance determination):** *An assurance activity declares its population **and its
complement** — what the declared population structurally cannot contain — and a challenge is scoped
at the complement before it is scoped at the conclusions.* Independent rationale: three consecutive
rounds of this programme were wrong in the same way, and each round's challenge was pointed at the
findings rather than at the frame.

---

## 6. What this register does not claim

- It does **not** claim that any part of Phase SA has been independently assured.
- It does **not** claim the internal challenge layers are equivalent to independent review, and
  §3.1 gives the measured reason they are not.
- It does **not** claim `PHASE-S/Q-BOSS-02` has been answered. It is open and belongs to Boss.
- It does **not** discharge `XRD-009`, any veto, or any prior `NOT SATISFIED` finding.

---

`CP-SA-C2-90 — INDEPENDENCE STATUS VERIFIED (execution status).` Verified as **absent**, with the
availability tested and the consequence stated in both directions.

Checkpoint completion is **not** Boss approval.

Boss remains the sole Final Approver. No Evidence = No Progress. Never Skip Gate.
