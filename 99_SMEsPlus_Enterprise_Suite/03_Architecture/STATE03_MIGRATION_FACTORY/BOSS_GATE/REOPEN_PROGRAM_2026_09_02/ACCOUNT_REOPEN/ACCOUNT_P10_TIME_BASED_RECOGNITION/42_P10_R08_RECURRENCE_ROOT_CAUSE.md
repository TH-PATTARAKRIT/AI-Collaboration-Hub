# P10 — R-08 RECURRENCE ROOT CAUSE

Session: `SMEPLUS-26-09-05-ACC-P10-TBR-DECISION-INTEGRITY-EVIDENCE-REPAIR-001` · Layer 1
Checkpoint `CP-P10D05`.

---

## 1. The Three Instances

| # | Instance | The negative asserted | The search that was not done |
|---|----------|----------------------|------------------------------|
| `I-1` | **`P10-R-08`**, original | *"This session had source evidence only — no database, runtime or UI access"* | Nobody listed the download directory. Four deployed archives were there |
| `I-2` | **Recurrence, in the correcting document** | *"The host's tooling cannot open the fourth archive"* | One binary was run from the default path. A newer build of the same tool was already installed elsewhere on the host |
| `I-3` | **Recurrence, in the veto document** | *"No further evidence bears on it — the behaviour is fully characterised"* | No search at all. Four items of bearing evidence surfaced in the same round |

## 2. Why the First Correction Did Not Prevent the Second

The lesson recorded at `I-1` was: *test the evidence base before declaring it.*

That is an **exhortation**. It names a virtue, not an act. It has no object, no output, and nothing that can be shown to have been done or not done. When the author reached `I-2` it had, in its own view, tested the evidence base — it ran a tool and read the error. The exhortation was satisfied on its own terms and the defect recurred anyway.

**Root cause: the corrective control was unfalsifiable.** A rule that cannot be shown to have been broken cannot prevent the thing it names.

## 3. The Specific Mechanism at `I-2`

1. A tool was invoked by bare name, resolving through the shell's default path.
2. It returned a version-incompatibility error naming the archive's format version.
3. The error was read as a **property of the archive** rather than as a **property of the invoked binary**.
4. No search was made for another build. One existed, installed, on the same machine.
5. The conclusion — *the archive cannot be read* — was recorded in **six places**, and classed `C — NOT SEARCHED`, which is the correct class for *"we did not look"* and the wrong class for *"we looked with one tool"*.

Step 3 is the error. Steps 4 and 5 are its propagation.

## 4. Why `I-3` Is the Same Defect in a Different Costume

`I-3` asserts that no further evidence bears on a governance instrument. It is a negative about the evidence base, and it was written with no search — the purest form of the defect, in the document with the most authority in the package.

## 5. The Replacement Control — falsifiable

> **P10-internal control, proposed for programme adoption:** a negative about your own capability must name **the tool, its version, the search performed for alternatives, and the command output.**

Each of the four is an artefact that either exists in the record or does not. The rule can be checked mechanically and can be shown to have been broken. Applied retrospectively:

| Instance | Tool named? | Version named? | Alternatives searched? | Output recorded? | Rule satisfied? |
|----------|-------------|----------------|------------------------|------------------|-----------------|
| `I-1` | no | no | no | no | No |
| `I-2` | partly | **no** | **no** | yes | No |
| `I-3` | n/a | n/a | **no** | **no** | No |

Every instance fails the replacement rule at the *alternatives* column. That column is the control.

## 6. The Second, Independent Defect Found Alongside It

Distinct from R-08 and recorded separately at `44`: **the evidence that settled the corrected conclusion had already been extracted and was never read.** R-08 is *not looking*. This one is *looking away from what you already have*. A package can satisfy the R-08 replacement rule perfectly and still commit it.

## 7. Classification

| Item | Class |
|------|-------|
| The three instances and their sequence | **FACT VERIFIED** — from P10's own documents |
| That a newer tool was installed and opens the archive | **FACT VERIFIED** — executed, 26,804 table-of-contents entries |
| That the original lesson's unfalsifiability caused the recurrence | **SUPPORTED INTERPRETATION** |
| That the replacement rule would have caught all three | **SUPPORTED INTERPRETATION** — it catches all three retrospectively, which is weaker than prospective proof |
