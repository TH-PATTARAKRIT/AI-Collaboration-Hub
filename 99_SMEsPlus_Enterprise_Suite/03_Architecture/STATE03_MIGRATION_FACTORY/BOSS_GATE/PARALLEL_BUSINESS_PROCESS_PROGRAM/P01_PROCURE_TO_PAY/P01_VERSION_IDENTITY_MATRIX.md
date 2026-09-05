# P01 — VERSION IDENTITY MATRIX

Session: `SMEPLUS-26-09-05-…-EVIDENCE-VERSION-DEPLOYMENT-INTEGRITY-001`
Layer: **1.**

The directive requires nine version facets to be established **separately**, and forbids using
informal generation terminology without mapping it to evidence. This document does that.


> ### ⚠ SUPERSEDED IN PART — `ERR-P01-23`
>
> This document states that **no deployed series-18 database exists** and that P01's source and
> deployment evidence **do not overlap on any series**. **Both are false.** A series-18
> deployment exists on this host with **4 companies, 15,522 journal entries, 47,801 valuation
> layers, and the goods-received clearing account configured**. See
> `P01_SERIES18_DEPLOYMENT_DISCOVERY.md`. **No accounting finding is withdrawn** — each remains
> bound to the database it was measured in.

---

## 1. THE NINE FACETS, PER DEPLOYMENT

| Facet | `E-1` (`D1`,`D2`) | `E-2` (`D3`) | `E-3` (`D4`) |
|---|---|---|---|
| **1. Database engine version** | PostgreSQL 15.15 / 15.18 | PostgreSQL 15.7 | **PostgreSQL 18.4** |
| **2. ERP application version** | **19.0** | **16.0** | **19.0** |
| — evidence | 251/251 and 232/232 installed modules carry `19.0.x` | 189 of 190 carry `16.0.x`, 1 unset | 452 of 453 carry `19.0.x`, 1 unset |
| **3. Source branch version** | **not established** — no source root is proven to be this build | **NO SOURCE ROOT AT ALL in P01's declared path set** | **not established** |
| **4. Custom module version** | mixed; at least one custom family's deployed version matches no copy in the declared path set | **the deployed withholding module version matches no copy in the declared path set** | not enumerated |
| **5. Module manifest version** | read from the deployed registry, not from source | as above | as above |
| **6. Migration lineage** | **none evident** — the version histogram is homogeneous | **none evident** — homogeneous at 16.0 | **none evident** — homogeneous |
| **7. File / archive label** | database name + timestamp only | same | same |
| **8. Deployment date** | companies created 2026-03-18 → 2026-04-29 | company created **2023-06-20** | company created 2026-02-02 |
| **9. Label provenance** | **the analyst.** No artifact asserted a product version for any archive | **the analyst — and it was wrong** | **the analyst — and it was wrong** |

---

## 2. CLASSIFICATION OF THE MISMATCH

The directive requires exactly one value. Of the six permitted:

> ### `UNKNOWN` — **is not** the answer, and neither are the four artifact-side options.
>
> **The correct classification is that none of the artifact-side categories applies: the archives
> were never mislabelled, never migrated, and never internally inconsistent. The mismatch was
> introduced entirely by the research.**

Reasoning, against each permitted value:

| Permitted value | Applies? | Why |
|---|---|---|
| `MISLABELLED ARCHIVE` | **No** | The archive names carry no version claim to be wrong |
| `OLD DATABASE UNDER NEW DIRECTORY` | **No** | The archives sit in a download area, not in a versioned tree |
| `MIGRATION ARTIFACT` | **No** | Every registry is version-homogeneous — 251/251, 232/232, 189/190, 452/453 |
| `SOURCE/DB VERSION MISMATCH` | **Partly, and this is the real residue** | The deployments are series 19.0 and 16.0; **P01's source path set contains series 18 and 19 and no series 16** |
| `MODULE VERSION MISMATCH` | **Yes, for the custom layer** | At least one deployed custom module family matches no source copy in the declared path set |
| `UNKNOWN` | No | It is now known |

**Recorded classification:** `SOURCE/DB VERSION MISMATCH` **plus** `MODULE VERSION MISMATCH`,
with the root cause being an **analyst-side labelling error, not an artifact defect**.

---

## 3. WHAT "GENERATION 16" MEANS, MAPPED TO EVIDENCE

The directive warns against using the phrase without mapping it. Mapped:

> **"Series 16.0" means: 189 of the 190 installed modules in that deployment carry a version
> string beginning `16.0.`, read from the deployed module registry's version column.**

It does **not** mean the database engine is version 16 — that engine is PostgreSQL 15.7. The two
numbers are unrelated, and conflating them is precisely the trap this matrix exists to close.

Cross-check performed: a literal search for `18.0.1.` in the registries returns hits in **all
three** later databases — every one of them inside a module's **description changelog text**,
not a version column. A structured probe over version columns returns **zero** modules at series
18 in any deployment. **The discrepancy between the two probes was chased to its cause rather
than left standing.**

---

## 4. THE MATERIAL CONSEQUENCE

| # | Consequence |
|---|---|
| 1 | **The generation P01 analysed in source — series 18 — has no deployed representative anywhere in the estate.** Every series-18 source finding is unvalidated against any running system here |
| 2 | **The only deployment with real accounting history is series 16, and P01 has read no series-16 source.** A series-16 root exists on the volume, outside the declared path set, and was never searched |
| 3 | The deployed-versus-source comparison P01 has been drawing spans **16.0 → 19.0**, three major series, not one |
| 4 | Deployed custom modules exist whose code is **not in the declared path set at all** — so the code actually running has not been located |

---

## 5. OPEN

| ID | Item | Status |
|---|---|---|
| `VI-01` | Which source tree each deployment was built from | **HOLD — SOURCE EVIDENCE REQUIRED** |
| `VI-02` | The series-16 source root, never searched | **NOT YET SEARCHED — class C, known-reachable** |
| `VI-03` | Deployed custom modules with no matching source | under independent challenge this round |
| `VI-04` | Whether any series-18 deployment exists outside this estate | **UNKNOWN — class D** |

---

# ADDENDUM — THE SERIES-16 SOURCE QUESTION, SETTLED

## A.1 The custom layer — **FOUND**

A series-16 **custom** addon root exists on the volume, was never in P01's declared path set, and
**is the source of the series-16 deployment's custom layer.** Six of six module versions match
the deployment's registry, two of them exactly and four through the framework's series-prefixing
convention.

**This closes the prior round's gap** *"the deployed withholding code matches no copy in the
declared path set."* It matched no copy **in that path set**; the path set was incomplete.

Classification: **FACT VERIFIED.**

## A.2 The core layer — **PROVEN ABSENT FROM THIS ESTATE**

- **POPULATION:** core source trees present on the volume.
- **UNIT:** one tree, identified by its release-version declaration.
- **PATTERN:** locate every release declaration under a core directory to depth 8, and read its
  declared series.
- **PATH SET:** the whole volume, plus the download area's unextracted archives.
- **RESULT (corrected):** **13 core trees — 4 at series 19, 9 at series 18, and 0 at series 14
  through 17.** All nine unextracted source archives are series 18 or 19. The only series-16
  artifact of any kind is the custom addon directory of §A.1.
- **A correction to this very enumeration:** the first run used a path filter requiring the
  release file to sit under a directory named for the application, and **that filter dropped one
  series-18 tree** — 12 instead of 13, 8 instead of 9. An independent expert's count differed
  from mine, which is how it was caught. Re-run without the filter, the population is 13 and the
  **series-16 conclusion is unchanged**. Recorded as `ERR-P01-20`.
- **DECLARED FALSE-NEGATIVE MODES:** a tree deeper than eight levels; a core tree with no release
  declaration; anything outside this volume and this download area; an archive whose name does
  not indicate its series **(mitigated — archive names were read, not assumed)**.

> **Classification: `VERIFIED ABSENCE` — class A within the stated scope.**

## A.3 WHY THIS MATTERS, AND WHY IT IS NOT A RESEARCH FAILURE

The only deployment with real accounting history is series 16. Its **custom** layer can now be
read. Its **core** layer cannot be read **because the artifact does not exist here.**

> **The gap between P01's deployment evidence and P01's source evidence cannot be closed by more
> analysis of this estate.** It requires either a series-16 core tree obtained from outside, or
> read-only runtime access to that deployment.

This is materially different from the round's other findings. The three falsified claims came
from a boundary that was declared and never tested. **This boundary was tested and the artifact
is genuinely absent** — which is what a class-A negative is supposed to look like.
