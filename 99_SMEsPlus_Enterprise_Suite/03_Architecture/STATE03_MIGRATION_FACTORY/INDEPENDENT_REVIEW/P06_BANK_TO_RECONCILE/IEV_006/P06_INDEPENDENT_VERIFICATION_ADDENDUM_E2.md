# P06_INDEPENDENT_VERIFICATION_ADDENDUM_E2.md

**Prompt:** `[SMEPLUS-26-09-06-G02-P06-B2R-INDEPENDENT-EXTERNAL-CORRECTION-VERIFICATION-006]`
**Track:** INDEPENDENT EXTERNAL VERIFICATION · frozen surface `1b018c1`
**Supplements:** the package published at `dac6ac3` / `452f6447`. **Nothing there is withdrawn; one disposition in it is falsified.**
**Classification:** LAYER 2 — AUDIT QUARANTINE

---

## 1. What this addendum corrects about the audit itself

**AAS-03 Expert 2 (denominator / population / identity) returned after publication.** The published package disposed of its absence as follows:

> *"its remit is materially covered by Experts 1 and 4 … **no finding in this package depends on it**"* — `P06_INDEPENDENT_AAS03_CHALLENGE.md` §2, `P06_INDEPENDENT_AUTO_RESUME_STATE.md`

**That disposition is FALSIFIED.** Expert 2 returned **twelve material defects, of which seven were absent from the published 18**, and one of the seven is **in this verifier's own audit artefact**. The remit was not materially covered. **A gap disposed of as harmless turned out to hold a quarter of the findings — the disposition was a guess dressed as a judgement, and it was wrong.**

**`IEV-I-05` — recorded against this audit.** *The cheapest way to be wrong about a missing input is to reason about what it would probably have said.*

## 2. Terminal state and veto — unchanged

**`P06 INDEPENDENT VERIFICATION FOUND MATERIAL DEFECT — TARGETED REPAIR REQUIRED`** stands; these findings reinforce it.
**`AASP-VETO-07 — PRESERVED`** stands, now on a third ground: **a fifth consecutive enlargement of a population declared complete — and this time the population enlarged was the auditor's own.**

## 3. Expert 2's new material defects — each re-executed by this verifier

| ID | Defect | Verification |
|---|---|---|
| **`IEV-D-19`** | **`13_`:95 — *"Open-item population \| same, `P06-OQ-` \| **66**"*. Measured: **68**.** An **untouched row one line below the repaired `:94`**, using the same command, in the same claim class, never in any round's population — **nor in this audit's** | ran its own printed command over root `*.md` → **68** |
| **`IEV-D-20`** | ~~*"This verifier's own `P06_VERIFICATION_INSTRUMENT_CONTROL_REGISTER.md`:45"*~~ → **`G02_RECOVERY_2026_09_06/P06_VERIFICATION_TOOL_DEFECT_REGISTER.md`:45, on the SOURCE branch** **[XQ-R-03, 2026-09-07 — wrong file named; the IEV file carries no such row]**. It publishes a validation table row — *"65 `P06-B-*` … max id = 65 and contiguous \| **YES**"* — while `:54` of the same file raises `P06-B-66` and `P06-B-67` nine lines later.** A validation table marked **YES** over a figure the same document supersedes | read both lines; measured 67 |
| **`IEV-D-21`** | **`REV-E-22` and `REV-E-23` are counted as author errors and are not.** All of `REV-E-01`…`21` carry a definition line in `14_`, `39_`, `62_` or the contradiction supplement; **`REV-E-22` and `REV-E-23` carry none, in any file.** They are repair-marker families. `40_`:288 and the supplement's declared `UNIT: author error` publish **23**; the true author-error population is **21**. **`P06-B-58`, the reliance-risk blocker, is scaled on this number** | 21 of 21 have definitions; 0 of 2 do |
| **`IEV-D-22`** | **`VER-F-04` states *"Eleven false current statements survived"* and enumerates **17** line references.** *"Including"* licenses more than the count, not fewer. Described in its own file as *"the round's governing finding"* | counted the enumeration |
| **`IEV-D-23`** | **The propagation matrix's own denominator row does not sum.** `:20` — 30 total, 8 records *"(incl. 3 time-bounded)"*, 19 current: **8 + 19 = 27 ≠ 30**. Every other row of the nine reconciles exactly. In the file whose thesis is *"the method that matters is the denominator"* | arithmetic |
| **`IEV-D-24`** | **`57_`:29 — *"the v18 tree is filtered (791 of an **unknown full population**)"*.** Two superseded claims in one clause: the tree is **relocated**, and the full population is **known and is 1752**. `57_` carries a `REV-E-18` marker, so the file *was* opened — and this line was passed over by rounds 5, 6, 7 **and by this audit's 13-statement class-3 population** | read; cross-checked against `46_`:77, `56_`:20, `13_`:126 |
| **`IEV-D-25`** | **`40_` §5 heading *"Full register — all 51 blockers"* enumerates 54, sums to 55 only by including `P06-XC-01` — a different unit the same file's `:88` forbids adding — and omits `B-55` entirely.** Three populations for one quantity in the package's primary blocker register | parsed the enumeration |

**Plus, adopted as NARROWED:** `47_`:67/:69 cite a denominator of *"twenty-three"* CRITICAL/HIGH against a grid placing **22**, with `B-27` absent from the grid · `EVIDENCE_MANIFEST_G02`:86 reports *"**4 of 4** (`B-59` … `B-62`, **plus `B-63`**)"* — five against four · `PROPAGATION_MATRIX`:45 enumerates five locations under a count of four · `EVIDENCE_MANIFEST_G02`:129-146 heads a column of 25 marker occurrences **"R7 repairs"** against `:154`'s 21.

## 4. The finding that goes deepest — a printed search pattern that cannot fire

**`IEV-D-26`.** `56_`:99 publishes the archive-search pattern `payment_return\|bounce\|dishonou?r\|post_dated\|postdated` and the result *"No bank-return concept"*, over the declared 961-directory archive. **No command, no `-E`/`-F` flag and no path expression is printed with it.**

Expert 2 tested it against a controlled fixture containing real spellings plus a literal control:

- **As BRE** (where `\|` *is* alternation): the `dishonou?r` branch matched **0 of 2** real spellings — in BRE `?` is a literal, so that branch can only match the literal string `dishonou?r`.
- **As ERE** (`-E`, where `\|` is a literal pipe): the **entire pattern matched 0 of 5**. Total silence.

**Under either mode the printed search is defective**, and in BRE the `bounce`/`payment_return` branches still fire — which is why the result reads as a plausible finding rather than a crash. `FTB-F-07` then generalises that negative to **1752 directories**.

**This is the package's own `prove-the-filter-can-fire` standard, unmet on a live negative — and it is the first defect in this programme found in the *regex grammar* of a published search rather than in its path set or its phrasing.**

## 5. What Expert 2 confirms — and it is substantial

**Every reproducible count in the package reproduces, several to the file.** The round-5 census (30/15) reproduces **per file, and is path-set-insensitive**. The round-6 census reconciles 47 − 7 = 40 / 24 − 4 = 20. **The round-7 census reconciles to exactly 21 across exactly 14 files** under the declared unit. `46_`'s severity distribution 6/17/20/3/7/2 = 55 covers `B-01…B-55` with **zero duplicates and zero omissions**. `34_`:51's tally, `REV-E-21`'s *"6 of 15"*, the evidence-base denominators (791/961/904/1752 with **no rival value anywhere**), and `ICC-F-06`'s dead-branch finding all reproduce. **No identifier is cited-but-undefined and none is defined twice.** And **of 84 published per-file hashes, 63 match and all 21 that differ are files this round edited — no unaccounted-for file changed.**

**`57_` is named the model negative-claim file**: the only negative in the package where population, pattern, path set **and** exclusion class are all four present.

## 6. Expert 2's own bottom line, adopted

> *"Eleven of the twelve material defects are one shape: a figure was measured correctly at time T and published in the present tense, and the sentence that made it wrong was written by the round that repaired it."*

**The package owns the rule** — `46_`:124, *"a printed command and a printed result date differently: the command stays live and the result freezes"* — **and applied it in one place of the six where it was needed.**

## 7. Revised totals

| | Published at `dac6ac3` | **Now** |
|---|---|---|
| Material defects | 18 | ~~25~~ → **26** — *enumerated `IEV-D-01`…`IEV-D-26`, contiguous. The 25 was summed over §3's table; `IEV-D-26` is defined in §4, in prose, outside it* **[XQ-R-02, 2026-09-07]** |
| Of which authored by this verifier | 1 (`41_`:6) | **2** (`+ IEV-D-20`) — *both by this **actor**, in the round-7 source track; **neither sits inside an `IEV_006/` file**. The figure is true of the actor and false of the audit artefact* **[XQ-R-03, 2026-09-07]** |
| Challenger reports adjudicated | 3 of 4 | **4 of 4** |
| Claim classes with survivors | 7 of 9 | **7 of 9** *(class 3 population grows by `57_`:29; class 9 by `13_`:95)* |
| Repair requirements routed to P06 | 15 | **19** |

**Four further repair requirements, routed and not performed:** correct `13_`:95 to **68** · withdraw or re-scope the `REV-E-*` author-error count to **21** and re-scale `P06-B-58` · re-state `VER-F-04`'s eleven-versus-seventeen and the propagation matrix's non-summing row · **re-run `56_`:99's archive negative with a pattern proved to fire, and publish the command with its grep mode**.

**And one against this audit:** `P06_VERIFICATION_INSTRUMENT_CONTROL_REGISTER.md`:45 must be corrected to **67**; it is left standing here so the defect is legible rather than quietly repaired.
