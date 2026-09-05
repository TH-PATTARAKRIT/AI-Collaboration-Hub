# D27 — P09_EVIDENCE_BASE_CENSUS_B5_DISCHARGE

**Session:** SMEPLUS-26-09-05-ACC-P09-P2A-DENOMINATOR-SIGN-PLATFORM-INTEGRITY-001
**Layer:** 1 — clean-room. Artefact filenames, owners and build strings are held in Layer 2.
**Subject:** discharge of `B5`, raised to CRITICAL by `D26` — *the programme's evidence base was an author-chosen path set.*

---

## 0. WHY THIS RAN NOW

`D26` raised `B5` to CRITICAL and the resume state recorded the round **STOPPED — awaiting material event.** That was wrong. `B5` is discharged by a command, not by an event, and the command was available. **A blocker you raised and can execute yourself is not a reason to stop.** Recorded as an execution-discipline error against this round.

## 1. WHAT THE PROGRAMME HAD DECLARED

| Round | Declared population | Declared as |
|---|---|---|
| `AI05` first version | 2 usable artefacts | inventory of nine artefacts |
| `AI05` corrected | 4 dumps in one directory | corrected after a display-limit false negative |
| `39c3784` | **6 artefacts, 5 restored** | **"exhaustive"** |
| `D26` | *"more than 14"* | a lower bound, never measured |

**"Exhaustive" was published over a set chosen by convenience of location.** Every headline figure in this package rests on one artefact from that set.

## 2. THE CENSUS — TWO INDEPENDENT KEYS

A census keyed one way cannot audit itself, so the population was built twice.

**PATH SET:** the home directory and every mounted volume root, enumerated from the mount table — **not chosen**: four roots.
**KEY 1 — filename:** `*.dump`, `*.backup`, `*.pgdump`, and `*.sql` above 1 MB.
**KEY 2 — content:** first five bytes equal the archive format's magic number, **any extension**, over every file above 1 MB.
**UNIT:** a distinct database artefact, keyed on (basename, byte size). Copies count once.
**LIMITS:** no `head`, no depth limit, no exclusions; counts reported separately from listings.

### 2.1 Result — and Key 2 caught what Key 1 missed

> **19 distinct database artefacts.** The declared figure was **6**.

**The single largest artefact on this host — roughly 1.9 GB, seven times the next largest and twelve times the deployment carrying every headline in this package — carries a non-standard extension and was invisible to the filename key.** It was found only by the content key.

**This is a defect in this document's own first draft.** §2 originally declared 18 artefacts on a filename-keyed census, with the standing archive rule — *search by format, not extension* — already on the register. Corrected before publication. Recorded as `D27-E-03`.

| Class | Distinct artefacts | Previously in the evidence base |
|---|---|---|
| large archives (>20 MB) | **11** | 5 |
| simulation-lab archives (3–4 MB) | **7** | **0** |
| plain-SQL archive | **1** | **0** |

Locations never previously searched: two cloud-storage trees, a messaging application's media store, a backup directory in the home root, and a simulation lab in the home root.

### 2.2 Convergence check

In the 1–20 MB band the two keys return **the same 7 artefacts**. The keys diverge only in the band where Key 1 failed. Reported because a census that agrees with itself everywhere has not been tested.

## 3. THE POPULATION SEPARATED BY GENERATION — *BEFORE* ANY COUNT

Every artefact was opened with the archive client's table-of-contents lister, read-only. **Nothing was restored, no runtime started, nothing written.**

| Generation | Distinct artefacts | Status for the theorem |
|---|---|---|
| **plan/distribution** — the representation this programme analyses | **17** | **in scope** |
| **predecessor tag/group** representation | **2** | **out of scope, on grounds** |

**Both out-of-scope artefacts are the two largest on the host** — the ~1.9 GB archive and the 271 MB archive. They carry the predecessor management-dimension model: no distribution payload, no negated-balance arithmetic.

> **The zeroing theorem does not transfer to them.** They are not additional evidence for the finding and not counter-evidence against it. **They are a different subject.**

**This cuts against `D26`'s framing of `B5`, and the correction belongs to `D26`, not to the reader.** `B5`'s worst case — *the largest unexamined artefact might overturn the headline* — **did not materialise.** But that could only be established by measuring. Pooling those two artefacts on the strength of their size would have produced a fresh denominator error inside the round convened to correct denominator errors.

## 4. THE FOUR NEWLY-READ IN-SCOPE ARTEFACTS

**UNIT:** the (entry, dimension value) group. **POPULATION:** every such group holding at least one management record — **not pre-filtered to both-legged entries**, which was a published defect of an earlier round.

| Artefact | Journal rows | Management records | Groups | Netting exactly 0 |
|---|---|---|---|---|
| **W** — messaging-store archive, 38 MB | **39,840** | **0** | — | — |
| **M** — cloud master database, 52 MB | **0** | **0** | — | — |
| **C** — personal-cloud archive, 29 MB | 956 | 84 | **25** | **25 — 100.00 %** |
| **T** — the formerly undecidable artefact, 64 MB | 32 | 2 | 0 | — (both records carry no journal-row reference) |

### 4.1 What these add

**Artefact `W` is the strongest new datum.** A database with **39,840 posted journal rows and not one management record** — a fully transacting deployment where the management dimension exists as schema and was never populated at all. **`D26`'s two-mechanism distinction is reinforced from the opposite direction:** `W` shows the dimension unpopulated, `C` shows it populated and annihilating. Neither state produces attribution.

**Artefact `C` reproduces 956 journal rows — the identical figure peer P04 reported** for one of the two version-18 deployments. **I therefore do not claim `C` as an independent corroboration; it is most likely the same artefact P04 measured.** What is independent is the derivation: P04 reported 14 entries with 13 measurable; measuring (entry, dimension) groups instead of entries gives **25 groups, all 25 at exactly 0.00, gross absolute movement 0.00.** Same artefact, different unit, same conclusion.

**Artefact `M` is a configured but untransacted database** — zero journal rows, with the extraction control passing. It carries the dimension's schema and no accounting at all.

## 5. A CLOSED ITEM RE-OPENED, THEN DISCHARGED

`DEP-P09-23` recorded artefact `T` as **NOT DECIDABLE — the local restore client rejects its header version.** **It reads without error and lists 1,315 populated tables.**

The claim was true when written and was never rechecked after the client was upgraded to a newer major version for an unrelated purpose. **A capability claim about your own tooling expires when the tooling changes.** `DEP-P09-23` is **DISCHARGED**. Second occurrence of this failure in the programme.

## 6. WHAT THIS DOES AND DOES NOT CHANGE

| Item | Disposition |
|---|---|
| the zeroing theorem | **unchanged** — an algebraic result, not a population claim |
| the 99.6507 % / 17,465-entry headline | **unchanged in value, narrowed in scope**: one artefact out of **17** in scope, not one out of five |
| *"the analytic dimension is schema, not data"* | **strengthened** by artefact `W`; `D26`'s correction to it stands |
| `B5` | **NARROWED, NOT CLOSED** — census complete and double-keyed; **8 in-scope artefacts remain unread** |
| `DEP-P09-23` | **DISCHARGED** |
| `DEP-P09-30` | **superseded** — the simulation-lab set is enumerated, all 7 in scope, all 7 unread |
| `B7`, `B8` | **untouched.** No build selected; selection remains outside P09's authority |
| any statutory reading | **`HOLD — STATUTORY EVIDENCE REQUIRED`**, unchanged |

**No previously published count is restated by this document.** The census bounds the population; it does not re-measure anything inside it.

## 7. FOUR AUTHOR ERRORS, ALL CAUGHT BEFORE PUBLICATION

A first for this programme — the prior ratio was fourteen errors, zero self-caught.

**`D27-E-01` — unit conflation.** The first probe reported *"analytic tables present: 259 / 264 / 240 / 280."* Those were table-of-contents **lines mentioning the word** — indexes, constraints, comments — not tables. Re-derived with the table as the unit: **7 to 16.** The **ninth** denominator/unit error in the lineage, and the first caught before publication.

**`D27-E-02` — a loop that silently processed 10 of 16 files.** The archive client consumed the loop's own input stream. **No error, no empty row, no visible gap — the output looked like a complete table.** Among the six skipped was the 155 MB deployment on which every headline in this package rests.

**`D27-E-03` — a filename-keyed census.** Declared 18 artefacts; the content key found a **1.9 GB** archive the filename key could not see. Committed while the rule *search by format, not extension* was already on the register.

**`D27-E-04` — the one that would have been worst.** The measurement returned *"0 management records, 0 journal rows"* for artefact `M`. Checked in a second form, the extraction emitted **1,793 bytes — headers only, no data block**, while the table-of-contents entries were present. **The identical command had just returned 339,382 records from the control artefact.** The extraction form succeeds on some archives and returns an empty, well-formed result on others.

> Without a per-artefact positive control this document would have published *"four newly-found deployments contain no management records"* — **a confident false negative across four artefacts at once**, in the exact class as the display-limit failure that once inverted this programme's central finding. **Two of the four zeros were real and two were not, and they were indistinguishable in the output.**

## 8. THE TWO STANDING RULES THIS DOCUMENT ADDS

> **`NC-12` — COVERAGE ASSERTION.** Every enumeration that bounds a claim shall count what it *processed* and compare it against what its search *returned*, and publish both numbers. A result set is not a population until those two agree.
>
> Path set, pattern, unit and output limits each govern what a search *offers*. `D27-E-02` happened downstream of all four — in what the loop *consumed*. **This is a fifth rung, not a restatement of the four.**

> **`NC-13` — PER-ARTEFACT POSITIVE CONTROL.** A zero measured from an artefact counts as a zero only where the same command, on the same artefact, demonstrably returns rows for a table known to be populated. **A control that passed on a different artefact proves nothing about this one.**

## 9. WHAT THIS DOCUMENT DOES NOT DECLARE

No approval. No merge. No implementation authorisation. No freeze. No build selected. No statutory claim. No blocker closed except `DEP-P09-23`. **Boss is sole Final Approver.**

## CHECKPOINT

**`CP-P09D27` — EVIDENCE-BASE CENSUS COMPLETE, DOUBLE-KEYED; `B5` NARROWED.** Population **19 distinct artefacts** against a declared 6; **17 in scope**, 2 excluded on generation grounds; 4 newly measured; **8 in-scope artefacts unread**; `DEP-P09-23` discharged; four author errors caught before publication; rules `NC-12` and `NC-13` added.

**NEXT EXECUTABLE, requiring no event:** read the 8 unread in-scope artefacts — the 7 simulation-lab snapshots and the plain-SQL archive.
