# SA_AR_09 — FINAL INTERNAL ADVERSARIAL CHALLENGE

## CP-SA-AR-90 — FINAL INTERNAL CHALLENGE COMPLETE

**This is `INTERNAL ADVERSARIAL SELF-CHALLENGE`, not independent assurance.** It ran against the frozen
content of `SA_AR_00`…`SA_AR_08`, on the eleven classes master prompt §10 names. **Every finding was
verified against primary evidence before adoption, and every adopted finding was applied to the text —
not to a disposition table.**

---

## 1. RESULT

| | Count |
|---|---:|
| Classes attacked | **11** |
| Findings raised | **6** |
| Verified and adopted | **4** |
| Refuted by evidence | **2** |
| Findings that reversed a conclusion of this round | **0** |
| Findings that corrected a figure in this round | **2** (`AR-C-01`, `AR-C-02`) |
| **Instrument failures caught by their own controls** | **2** — §3 |

---

## 2. THE ELEVEN CLASSES

| # | Class | Result |
|---:|---|---|
| 1 | **False Boss escalation** | **0.** All 24 re-tested at primary source; 11 of 11 authority quotations resolve in files outside the parent pack |
| 2 | **Duplicated decision IDs** | **0.** Every identifier appears in exactly **one** family membership row — but see `AR-C-01` |
| 3 | **Already-ruled decisions** | **0** across 189 of 189 refs, with a firing positive control |
| 4 | **Wrong authority owner** | **0 wrong — 1 overstated.** `F8`'s *"five independent instruments"* was verified at **one**. Now stated as verified-at-one (`SA_AR_03` §4.1) |
| 5 | **Hidden Category 3 gaps** | **0.** All 13 obligation rows re-read; the reverse error (SMEs Core work graded Category 2) also searched and found 0 |
| 6 | **Omitted downstream module consequences** | **0 omissions found.** Every card now carries an explicit Manufacturing/Purchase/Sales row, which the parent cards did not |
| 7 | **Suppressed source clauses** | **0 new.** The known instance — `SA_CORR2_02` §3.1's second clause — is quoted **in full** in `F4`, with the withdrawal recorded |
| 8 | **Overconfident recommendations** | **1 adopted** — `AR-C-02` |
| 9 | **Incorrect independence claims** | **0.** Sweep for any sentence treating self-challenge as assurance returns empty; the ineligibility of this session's own model is stated at `SA_AR_06` §2 |
| 10 | **Stale mainline references** | **0.** Every mainline figure re-measured this session and labelled as-at-publication |
| 11 | **Evidence-count defects** | **2 adopted** — `AR-C-01`, `AR-C-02` |

---

## 3. THE TWO INSTRUMENT FAILURES, AND WHY THEY MATTER MORE THAN THE FINDINGS

> **Both returned a clean-looking zero. Both were false. Both were caught only by a control, not by
> reading the output.**

**`AR-I-01` — the multi-ref search.** Test A over all 189 refs in a single `git grep` returned **0
candidate hits and 0 hits for `MTI-D-01/-02/-03`**, which are known to be ruled. Re-executed one ref
per iteration, the control fires on all three ruling files. **Had the positive control been omitted,
this round would have published "0 already ruled" from an instrument that never ran.**

**`AR-I-02` — the SHA resolution check.** A relative path put `git cat-file` outside the repository and
**all 11 cited object ids returned `UNRESOLVED`** — a result that reads as eleven broken citations.
Re-run with an absolute path plus a known-good and a known-bad control: **11 of 11 resolve, `deadbeef`
correctly does not.**

**The lesson this round records against itself:** the programme's rule is *prove the filter can fire*,
and in one session it was violated twice by the same executor while writing the document that states
it. **Every zero in this package is now paired with a control, and the two that were not are published
above rather than quietly re-run.**

---

## 4. THE FOUR ADOPTED FINDINGS

### `AR-C-01` — an identifier census of this pack returns 23, not 24

**Verified:** every family membership row extracted; **23 distinct identifiers**, none duplicated; the
family counts sum to **24**. The gap is the **over-receipt tolerance default**, a named `F2` decision
that has never been given an identifier.

**Applied** at `SA_AR_04` §1 as an explicit note, so a reader counting by identifier is not left to
conclude a decision is missing. **Not "fixed" by inventing an id** — issuing identifiers for Boss
decisions is not this session's act.

### `AR-C-02` — `F5`'s own card said "four policy points" and listed five

**Verified:** the primary register defines `POH-D-01`…`-05` as five elections plus `POH-D-06` as the
restatement act. The card's plain-language line said *four* and then enumerated **five**; its Business
problem row said *five*. **A card contradicting itself two rows apart.**

**Inherited, not invented:** the parent pack's `F5` question sentence reads *"rule the four policy
elections underneath them."* **The error is three rounds old and this is the first round to count the
list against its own number.** Corrected to five.

### `AR-C-03` — `F8`'s "five independent instruments" was verified at one

**Applied** at `SA_AR_03` §4.1: the phrase is confirmed in `03_INVENTORY_FUNCTIONAL_DESIGN_V1.md`; the
other three named instruments were **not** re-verified this round, and the pack now says so. **One
confirmed instrument is sufficient to retain `C-02`; a claim of five checked at one is not repeatable
as five.**

### `AR-C-04` — the parent's raw-zero veto sweep does not reproduce

**Verified:** `CF-V-01`'s and `CF-V-02`'s patterns return **4** and **2** hits over the current
package, not zero, because a package that states its own prohibitions matches its own patterns. **Every
hit classified; 0 breaches.** `SA_AR_07` §2 now publishes the classification and states explicitly that
a raw zero is *not* claimed.

---

## 5. THE TWO REFUTED

| Candidate finding | Why refuted |
|---|---|
| *"`SA_AR_04` contains a vendor-ERP token"* | The single hit is the word **"product."** ending an English sentence — *"two generations of one reference product."* **False positive of the `product\.` pattern.** No vendor token exists |
| *"Four checkpoint headers assert `VERIFIED`, which is a self-declared verdict"* | The four are the **master prompt's own mandated checkpoint names** (`CP-SA-AR-00`, `-20`, `-80`) and each **matches its file's actual result**. **Every file carries `Boss remains the sole Final Approver`, and `SA_AR_00` carries `Checkpoint completion is NOT Boss approval`.** Distinct from the parent round's `CHF-09`, where a header asserted a result its own file contradicted |

---

## 6. WHAT THIS CHALLENGE CANNOT DO

1. **It cannot find what the author cannot see.** The two largest corrections in this chain — a
   suppressed clause and a too-narrow negative — were both caught, but by *independent* challengers, and
   this session has none.
2. **Its own repairs are unreviewed.** Four corrections were applied and no second party checked them.
3. **Six findings from an internal pass is a low yield**, and the programme's own record says the
   comparable independent number is an order of magnitude higher. **A small number here is not evidence
   of a clean package; it is evidence of a weak control.**

## 7. Checkpoint

> ## `CP-SA-AR-90 — FINAL INTERNAL CHALLENGE COMPLETE`
> **11 classes · 6 findings · 4 adopted and applied to the text · 2 refuted with reasons ·
> 2 instrument failures published against this round · 0 conclusions reversed · 0 independence claimed.**

No Evidence = No Progress. Never Skip Gate. Boss remains the sole Final Approver.
