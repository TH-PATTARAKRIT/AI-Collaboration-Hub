# SA20 — CORR1: ADVERSARIAL CHALLENGE RESULT AND CORRECTIONS APPLIED

Status: **CORR1 applied. `SA18`'s `HOLD — NOT READY FOR BOSS FINAL GATE` stands, for stronger
reasons than `SA18` gave.**

An adversarial challenge was run against the complete package at `55cdfdf5`. It returned
**9 MATERIAL, 14 SUBSTANTIVE, 7 MINOR** findings and **falsified three of the package's negative
claims, including the one its headline rested on.**

Every correction below is applied **to the register text, by population** — not recorded here and
left standing there. A revision log is not a correction.

---

## 1. The finding that matters most

> **The package's most rigorous instrument was pointed at the countable and away from the
> consequential.**

Declared population, published pattern, positive control, negative control, published instrument
failures — all of that was applied to the corpus construction and the P-series counts, which the
challenger reproduced **exactly**. It was **not** applied to the four claims the package leads
with. Three of those four were falsified.

That is the correct diagnosis and it is accepted without qualification.

---

## 2. Falsified claims, and what replaces them

### 2.1 `SA00-F-03` / `XD-01` — the headline

**Falsified.** The claim *"the Account programme contains no treatment of the Sales-side
cancellation gate"* rested on the pattern `cancellation.gate` — **Group A's own coinage**. The
Account programme was never going to write another programme's phrase.

Verified independently before adopting the correction:

| Instrument | Result |
|---|---|
| `cancellation.gate` in `ACCOUNT_REOPEN` (the original) | 0 |
| `cancel` in the Order-to-Cash package (one token wider) | **24 files** |

The Order-to-Cash edge-case matrix carries a `CANCEL` row across order, delivery, invoice,
payment and matching, plus a cancellation-and-reversal section; its business event register
enumerates the invoice lifecycle states Group A asked about, each `FACT VERIFIED`.

**Restated:** the Account programme **did** establish the semantics. Nobody delivered them **into
Group A's register**, where the item has stood at `HOLD — WAITING FOR ACCOUNTING/AR-AP AUTHORITY`
since 2026-08-31. **A routing and notification failure between two programmes, not an absence of
input.**

**The package contradicted itself and did not catch it.** `SA02` §6 already argued the opposite
in plain terms — *"The input therefore **exists** in one programme"*. Two registers held
incompatible positions and no internal control compared them.

**Consequence for Boss:** `SA19` §20 Decision 1 was framed on the falsified premise and is
**reframed** — see §5.

### 2.2 `SA05` BN-05 — dropship

**Falsified.** *"No subject-scoped evidence found for dropship in the corpus"* was published with
**no pattern, no unit and no count**, in a register whose own rule is *"Patterns are published
with their results, not described."*

Verified: **66 unique paths** across the remote; **12 occurrences** in the Group A purchase
capability model — inside the very programme this package admitted to its own baseline at
`SA00-F-02` — recording dropship as a capability at status `VERIFIED FACT`, with its mechanism,
its received-quantity netting rule, and a database-confirmed purchase-line-to-sales-line link
explicitly flagged *for a future cross-module phase to open*. This phase is that phase.

**Restated in place.** `HOLD` is retained on a narrower and genuine ground: whether title passage
without own-warehouse movement requires a recorded inventory event is undetermined, and that is
accounting-material.

### 2.3 `SA01-C-01` — an over-wide universal inside a correction

*"the `prompt/` branch carries 1,109 files and **0** matching `R4_L12` by any pattern"*. The
literal `R4_L12` gives 0; the hyphenated form — which is how the branch and session ID are
actually written — gives **2**. The correction's conclusion stands; the phrase **"by any
pattern"** does not, and it is the exact defect `SA00-I-02` exists to prevent.

---

## 3. Corrections applied to the register text

| # | Correction | Where | Verified |
|---|---|---|---|
| C-01 | `SA00-F-03` restated; the falsified sentence struck through, not deleted | `SA00` §9 | ✔ |
| C-02 | BN-05 restated; `HOLD` retained on a narrower ground | `SA05` §3 | ✔ |
| C-03 | Routing count corrected — **20 evidenced, 8 not, 28 total**; class rows now sum to 28 | `SA04` §1.1, §3; `SA19`; resume state | ✔ sums to 28 |
| C-04 | Accounting reconciliation corrected — **13 reconciled, 9 partial, 7 unknown**; §3's "eleven" corrected to the **nine** it actually lists | `SA07` §1.1, §3, gate line; `SA19`; `SA18`; resume state | ✔ sums to 29 |
| C-05 | Challenge-class count corrected **19 → 17** | `SA18` §1; `SA19` §16 | ✔ |
| C-06 | *"least-evidenced of all twenty-two domains"* corrected to **"of the seventeen mandated domains"** — SA-D18 at 4 blobs is lower among all 22 — at **every** occurrence | `SA05`, `SA16`, `SA18`, resume state | ✔ |
| C-07 | Population corrected **183 → 182**; `origin/HEAD` is a symbolic alias for `origin/SMEsPlus` and double-counted mainline | `SA00` §2 | ✔ |
| C-08 | **Eleven unresolvable branch citations** repaired by population; two bare-SHA citations given their branch | all files | ✔ every cited branch now resolves |
| C-09 | Residual reference warehouse-object name removed from `SA00` §7 — the token `SA12` claimed had been removed and had not | `SA00` §7 | ✔ |
| C-10 | `SA18` §2's falsification table marked partly superseded; attempts 1 and 2 recorded as **later succeeded** | `SA18` §2 | ✔ |
| C-11 | GB-08 FX ruling admitted to the baseline lock | `SA00` §10; `SA10` §2 | ✔ |
| C-12 | The three dropped readiness-pack gaps (`G-10` deletion path leaves no trace, `G-11` no accounting-period object, `G-12` statutory grouping) carried | `SA13` §4.2 | ✔ |
| C-13 | **`SA09` approval-rejection row returned to its owner's status.** It read `ESTABLISHED — via correction`; the corrective cycle records it under *"Explicitly Not Done"* and the terminal re-verification carries it as **A2**, `EVIDENCE MISSING / BOSS DECISION REQUIRED`, blocking the Pre-Development Gate. Exception count corrected **14 → 13 established, 4 → 5 not** | `SA09` §2, §2.1, gate line; `SA19`; resume state | ✔ |

---

## 4. Findings accepted and carried as open, not yet corrected

Recorded so the next session is not misled about what was fixed.

| Finding | Status |
|---|---|
| `SA13` §6's *"no promotion of another party's open item found in this package"* | **FALSIFIED** — `SA09` had promoted one. Corrected at C-13 below; the claim in `SA13` §6 is withdrawn |
| The three convergence claims (`SA07` §4, `SA04-F-01`, `SA18-F-01`) are one classification expressed three times; `SA06`/`SA07`/`SA04` cite `SA05`/`SA01` **in their own status columns** | **ACCEPTED IN FULL.** `SA18-F-01` conceded this in general terms and did not go far enough. `SA04-F-01`'s *"two independent measurements"* is the same defect, uncorrected |
| `SA07` §4's *"one-to-one"* seven-item mapping is wrong — 2 of 7 do not correspond, and the third instrument produced **four**, not seven | **ACCEPTED** |
| `SA04-F-01`'s *"every route with an Accounting endpoint is evidenced"* is broken by R-27 in the same paragraph | **ACCEPTED** |
| `SA13` §4.2 declares G-01/`XD-06` *"closed"* while `SA14` registers it `OPEN` | **ACCEPTED — `XD-06` remains OPEN; the `SA13` sentence overreached** |
| `SA12` §4 says "Four" Nature DNA determinations; there are eight — so ND-05…ND-08 **never went through the source-copying test** | **ACCEPTED** |
| `SA11-F-03`'s §5/§6 wording still asserts the absence that §7.1 corrects | **ACCEPTED — the *revision-log-is-not-a-correction* defect, committed inside the file documenting the fix** |
| `SA05-F-01`'s *"closing five domains closes all seven"* is asserted and untested; BN-07's own blocker is a Boss-ruling ambiguity, not a supply-routing gap | **ACCEPTED — `SA19` Decision 4 rests partly on this** |

---

## 5. What this does to the Boss decisions

**Decision 1 is reframed.** It was: *answer Group A's three questions*. The answers largely
**exist**, in Order-to-Cash. The decision Boss actually faces is narrower and different:

> **Direct that the existing Order-to-Cash invoice-lifecycle semantics be delivered into Group A's
> register, and decide the one question the semantics do not settle: which customer-invoice state,
> if any, carries blocking weight against cancellation of a sales commitment — or accept the
> current asymmetry as a disclosed risk trade-off.**

**Decision 2 is strengthened.** The joint cross-proof that was constituted and never convened is
exactly the control that would have caught this. The falsification is evidence *for* convening it.

**Decisions 3 and 4 are unchanged**, with the caveat that Decision 4's consolidation rests on an
untested clause (§4, last row).

---

## 6. What this says about the assurance, not just the package

Three of the package's four leading negatives were falsified by **widening a pattern by one
token**. The package documented that exact defect class (`SA00-I-02`), applied the discipline
rigorously to its countable claims, and did not apply it to its consequential ones.

**The rule that follows, and it is not new — it is the one the programme keeps re-learning:**

> A negative claim about another party's work must be searched in **that party's vocabulary**,
> never in the vocabulary of the party making the claim.

Every negative in this package was re-tested against that rule during CORR1. Those that survive
are listed in `SA18` §2 as corrected; those that did not are in §2 above.

**On independence.** `SA13` §1 declared that this session's challenge is same-model and does not
meet the programme's independence standard. **That declaration is now evidenced rather than
merely stated:** the internal challenge found eight defects and passed the headline; the
adversarial challenge falsified it. The adversarial pass was still same-model — a genuinely
independent challenger remains uncommissioned, and `PHASE-S/Q-BOSS-02` remains open.

---

`SA20 — CORR1 APPLIED. Package disposition unchanged: HOLD.`

Boss remains the sole Final Approver.
