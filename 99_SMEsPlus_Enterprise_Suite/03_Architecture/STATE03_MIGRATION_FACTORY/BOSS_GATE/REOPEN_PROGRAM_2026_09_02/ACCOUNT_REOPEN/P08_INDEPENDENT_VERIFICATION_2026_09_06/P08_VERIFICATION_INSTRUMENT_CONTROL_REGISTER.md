# P08_VERIFICATION_INSTRUMENT_CONTROL_REGISTER

Prompt `[SMEPLUS-26-09-06-P08-R2R-INDEPENDENT-EXTERNAL-CORRECTION-VERIFICATION-003]` · frozen surface `00ccd66`

**Every instrument this verifier used, with its controls and its blind spot.** The audited round failed twice on its own instruments — one sweep that could not fail, one script with a string-escaping bug that nearly rejected a correct finding. **A verifier that does not control its own instruments has no standing to report that.**

---

## 1. Instruments

| # | Instrument | Positive control | Failure control | Second method | Blind spot |
|---|---|---|---|---|---|
| `I-1` | **Frozen-SHA proof** — resolve `00ccd66`, compare to the source-branch tip and to the audit branch's copy | SHA resolves to a commit object with the expected subject and timestamp | a fabricated SHA fails to resolve | `git diff` between the two trees returns empty | none material — this is a content-hash comparison |
| `I-2` | **Correction-id enumeration** — regex `P08-CONTRA-\d+` over all 72 artefacts | the register alone yields **43** ids | a fabricated id (`-999`) returns **0** | **per-id direct grep**: ids 49–74 → **0 present, 26 absent**, identical to the bulk method | an id written in a different form (e.g. spelled out, or a typo) would be missed. Searched for `CONTRA` in any casing: no variant forms found |
| `I-3` | **Definition-bearing test** — an id counts as defined if a line containing it carries >60 further characters | 32 of 32 ids in range resolve as defined | the same test on an id cited only inside a range row returns undefined | manual read of a sample | a definition split across lines would read as undefined; none observed |
| `I-4` | **Version-marker coverage** — table rows carrying a version or database token | a row containing *"18.0 source"* matches | the same row with the token removed does not match | **second row definition** (pipe-count rather than leading-pipe): **identical 52/307** | **SHARED-REGEX BLIND SPOT, tested and reported** — both methods used one marker pattern. Widening it to admit prose (*"deployed"*, *"the estate"*) raises coverage to **64/307 = 20.8%**, but such rows **do not identify which of three lines**, which is the rule's purpose. **Strict 16.9%, loose 20.8%; neither approaches "every row"** |
| `I-5` | **Standing-table vs appended-correction comparison** — read each artefact's summary/disposition block, then its appended correction sections | four instances found and quoted | artefacts whose summary *was* updated (the handoff count in `54`) are correctly reported as updated, so the test discriminates | manual read of the full artefact in each case | a correction expressed only in prose, with no summary table to contradict, would not be detected by this instrument |

## 2. Controls this verifier did NOT run, and why that bounds the findings

| Not controlled | Consequence |
|---|---|
| **Re-extraction of every deployed table from the original dumps** | Delegated to the database challenger. Until it reports, **every count in this register that rests on the audited party's extracts is provisional** — the extracts are themselves an artefact of the party under audit |
| The 19.0 source line, swept broadly | Out of mandate — *closure may become deeper, never wider*. Sampled only against already-published claims |
| Peer packages | Forbidden by the mandate |
| Runtime behaviour of any module | No execution; all evidence is static source and offline extracts |

## 3. Rule applied to the verifier's own negatives

**`IVR-M-02`. Two methods returning the same number is not corroboration if they share a component.** `I-4`'s two row definitions returned an identical 52/307 — and they shared the marker regex. The agreement was therefore about row counting, not about marker detection. **The shared component was isolated and tested separately**, which is what produced the 16.9% / 20.8% band rather than a single unearned figure.
