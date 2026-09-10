# PMO_FINAL_VERIFICATION_REPORT.md
# PMO verification — evidence integrity, not conclusions

Session `[SMEPLUS-26-09-10-VDR-PREP-002]` · Layer: **LAYER 1 — CLEAN-ROOM.**

---

## 1. Scope of this verification, and what it cannot do

PMO verifies **evidence integrity**: that the package says what its evidence says, that its
identifiers resolve, that its tables are structurally sound, that its clean-room boundary holds, and
that its governance rule was obeyed. **PMO does not verify that the research conclusions are right** —
that is what independent challenge is for, and it found two of them wrong.

**Two limitations are declared before the results, not after:**

1. **All four checks have the *package* as their unit.** None can detect a missing evidence base. That
   is why `GAP-INV-17` (the census run after the choice) and `GAP-INV-09C` (small-N transactional
   evidence) are carried as coverage bounds, not as footnotes.
2. **The producer ran these checks on its own work.** Under this session's own rules that is a
   **screen, not a certification**.

## 2. The four disjoint-unit checks

| # | Unit | Result |
|---|------|--------|
| 1 | **identifier** | **CLEAN** — 82 identifiers defined, 82 cited, **0 cited-but-undefined**, 0 numbering gaps within families defined here |
| 2 | **table row** | **CLEAN** — 0 structurally broken rows across all package markdown |
| 3 | **file** | **CLEAN** — 68 files, 0 junk artefacts, **0 zero-byte files**, manifest hashed and self-consistent |
| 4 | **clean-room token** | **CLEAN** — **0 vendor tokens in any LAYER 1 file**; every file carries a layer declaration; Layer 2 quarantined |

**Check 4 was independently re-run by a reviewer with a wider token list than the producer's own
(23 dotted prefixes, 15 substrings, 10 word-boundary terms) and returned 0 on every Layer-1 file.**

## 3. Instrument corrections made to the verification itself

The sweep is not exempt from the framework it enforces. Four defects in it were found and fixed this
session:

| ID | Defect in the sweep | Effect |
|----|--------------------|--------|
| `CORR-F-34` | dotted identifier prefixes matched as **bare substrings** | reported a leak on the English sentence *"…real stock."* — the same class as matching a stem inside a longer ordinary word. Dotted prefixes now require a following identifier character |
| — | the definition pattern recognised headings only | identifiers defined in **table cells** read as undefined |
| — | the identifier pattern was blind to **four families** cited from a third corpus | the sweep could not have reported the omission a reviewer found (`R3B-15`) |
| — | a file above the stated commit threshold was committed, and a **failed extraction was committed as a `.csv`** | corrected: failed extractions are now recorded as a README, never as an empty or placeholder file, and the one deliberate large-file exception is stated |

**A verification instrument that has never been corrected has not been tested.**

## 4. Governance verification — the control that failed in the prior session

| Check | Command | Result |
|-------|---------|--------|
| Freeze recorded before reviewers were launched | commit SHA `1d6238a5…` in the challenge brief | **YES** |
| Working tree clean at freeze | `git status --porcelain -- <package>` | **0 lines** |
| **Commits to the package during the open round** | `git log <SHA>..HEAD -- <package>` | **0 — round VALID** |
| Diff against the frozen SHA at round close | `git diff --stat <SHA> -- <package>` | **0** |
| Independently verified by a reviewer | same three commands, run by R3-B | **same result** |

**The rule was tested under pressure.** The producer found **ten** of its own defects while the round
was open — two of them falsifying published claims — and **applied none of them until it closed**,
holding them in a file outside the package path. That file is committed as evidence.

## 5. Prohibited-wording verification

| Check | Result |
|-------|--------|
| Any AI role issuing `FINAL APPROVED` | **none** — the only occurrences are the prohibition itself |
| Producer self-awarding `PASS` on its own work | **none** — instrument controls read `EXECUTED — RESULT RECORDED`; the one `PASS` token in a Layer-1 report is a threshold cell whose result reads *partially met* |
| Any Boss-reserved question settled | **none** — all 14 Boss decisions carried as **OPEN** with evidence or a recommendation attached |
| Reference behaviour promoted to SMEsPlus design | **none** — dispositions are stated as *candidate positions* |
| Prior invalidated challenge treated as valid | **none** — R1 is cited as *evidence*, never as *certification* |

Independently confirmed by R3-B on all five.

## 6. Corrections applied to register text, not to a revision log

**46 findings** were dispositioned this round — 36 from two independent reviewers, 10 producer-found
during the freeze window. Every accepted finding was **edited into the register that carries the
claim**, including:

- **two retractions** written into the affected findings as `WITHDRAWN` with the reason and the
  corrected statement in place;
- **one withdrawn column** recomputed against the correct source, with the six affected population
  rows corrected;
- **eleven numeric corrections** applied at every site the figure appears.

**Verification that the corrections landed:** the stale figures were swept for by value across the
package after application. The identifier check (82/82) confirms every new finding, gap, decision and
correction is both defined and cited.

## 7. PMO disposition

**Evidence integrity: `CLEAN`.**
**Certification: `NOT GRANTED` — and not available from PMO.**

The package's integrity controls pass, its governance rule was obeyed and verified mechanically, and
its corrections are in the text. **But the corrected package has not been independently re-challenged**
— the producer verified its own corrections, which this framework explicitly says is insufficient.

PMO therefore verifies the evidence and **declines to certify the conclusions**. That distinction is
the point of the role.
