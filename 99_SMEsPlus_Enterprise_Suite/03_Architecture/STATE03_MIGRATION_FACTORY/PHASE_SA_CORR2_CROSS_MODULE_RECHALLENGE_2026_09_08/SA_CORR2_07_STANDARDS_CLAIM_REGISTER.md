# SA_CORR2_07 — STANDARDS CLAIM REGISTER
## CP-SA-C2-60 (first half) — STANDARDS CLAIMS CONTROLLED

Session: `[SMEPLUS-26-09-08-PHASE-SA-CORR2-XMOD-001]`
Governing law: master prompt §8. Evidence frame: `SA_CORR2_00` §2 (v2 corpus).

**No certification, compliance or conformance is claimed anywhere in this register.** Its purpose is
to classify every such statement that exists in the corpus and to correct the unqualified ones.

---

## 1. Classification scheme (master prompt §8), and the population

`VERIFIED REQUIREMENT MAPPING` · `CONTROL DESIGN TARGET` · `EVIDENCE-BACKED CONFORMANCE` ·
`CERTIFICATION/ATTESTATION VERIFIED` · `UNQUALIFIED CLAIM — CORRECTION REQUIRED` · `NOT APPLICABLE` ·
`UNKNOWN / RESEARCH REQUIRED`.

**The unit of classification is the STATEMENT, not the file.** A file may carry a prohibition and a
mapping and an overclaim.

| Clause | Declaration |
|---|---|
| POPULATION | v2 corpus, 3,789 unique text blobs (U1) / 3,561 unique text paths (U2), **including the mainline tree** |
| PATTERN | per standard, case-**sensitive** where the token is an acronym, executed and published below |
| POSITIVE CONTROL | `BD-ACC-01` → 34 blobs; `HACCP` → 2 blobs. Both fire |
| NEGATIVE CONTROL | `zzqq_unmatchable_token` → 0 |
| SECOND SHAPE | every zero re-run under a case-insensitive path-join shape |

---

## 2. Standards named in the corpus — measured

UNIT = unique text blob (U1).

| Standard | Blobs | | Standard | Blobs |
|---|---|---|---|---|
| ISO 27001 | 9 | | PDPA | 63 |
| ISO 9001 | 8 | | **COSO** | **2** |
| ISO 27701 | 3 | | TFRS | 45 |
| ISO 22301 / 37301 | 2 / 2 | | TAS | 147 |
| ISO 20000-1 / 27017 / 42001 | 2 / 2 / 2 | | IFRS | 25 |
| ISO 22000 / HACCP | 2 / 2 | | IAS | 87 |
| IATF 16949 | 2 | | **PCI** | **0** |
| ISO 13485 / 45001 / 14001 / 50001 | 2 each | | **HIPAA** | **0** |
| SOC 1 / SOC 2 | 3 / 9 | | **NIST** *(word-bounded)* | **1** |
| GDPR | 8 | | SOX / Sarbanes / COBIT / ITGC | 1 each |

**`PCI` and `HIPAA` are genuinely zero** — confirmed on a second command shape with firing positive
controls. For these two the register means *the claims do not exist*, not merely *not found*.

### 2.1 Three false-friend traps, two inherited and one new

Published because each would have put a control framework on an applicability list that the corpus
has never cited — the `SA00-I-01` class.

| Token | Unbounded / case-insensitive | Corrected | Cause |
|---|---|---|---|
| `NIST` | 8 blobs | **1** | Matches inside `ADMINISTRATIVE`, `ADMINISTERED` — and, **not previously recorded, inside `DETERMINISTIC` / `NON-DETERMINISTIC`**, which this programme writes constantly |
| `SOX` | 1 | **1** | `SA11` §9.2 reported *"175 hits inside one binary document"*. **Not reproducible here — and not thereby refuted:** the corpus extracts only `.md/.txt/.csv`, and the path set contains 19 `.pdf`, 6 `.zip`, 4 `.docx` and 1 `.jpg` never extracted. `SA11`'s figure came from a byte search this corpus does not perform |
| **`COSO`** | **18 blobs** | **2** | **New. Case-insensitive `COSO` matches `Ecosoft`**, a Thai localization vendor name. Any COSO count run case-insensitively is ~9× inflated. Case-sensitive **2** corroborates `SA11` §9.2's *"COSO is cited exactly once"* once the mainline is added |

**A fourth collision, on an identifier rather than a standard:** word-bounded `AUD-10` returns 23
blobs, of which about 22 are **`M-AUD-10`**, an unrelated accounting finding. `AUD-10` is a Boss
standards rule. **Counting `AUD-10` citations without disambiguating overstates them by an order of
magnitude.**

---

## 3. `UNQUALIFIED CLAIM — CORRECTION REQUIRED`

### 3.1 The one instance, and it is verified on every branch

**Path:** `99_SMEsPlus_Enterprise_Suite/16_Learning_Analysis/01_SYSTEM_OVERVIEW.md`, lines 213–220.

```text
## 🔐 Compliance & Governance
### **Standards Compliance**
- ISO 27001 (Information Security)
- ISO 9001 (Quality Management)
- SOC 2 (Security & Availability)
- GDPR (Data Protection)
- Local regulations (Thailand)
```

No qualifier, no evidence reference, no scope limit, no attestation.

**`SA11-F-05`'s "live on every branch" is verified, by the right instrument.** A diff-based corpus
**cannot** answer an every-branch presence question — a file byte-identical everywhere appears once.
Tested instead by a per-branch tree lookup:

```
for each of 183 branches:  git rev-parse '<branch>:99_.../16_Learning_Analysis/01_SYSTEM_OVERVIEW.md'
→ present on 183 of 183 · byte-identical to mainline on 183 of 183 · absent on 0
```

> **`C2-F-19`.** The claim is on **183 of 183 branches, byte-identical**, including this session's
> own. `SA11-F-05` is confirmed in full. Recorded as a method point too: an internal challenge in
> this round could only prove it present on mainline, because it used the corpus. **The corpus was
> the wrong instrument for that question and the right one costs one command.**

**`C2-F-20` — one line of the claim escapes every standards pattern.** Line 220,
`- Local regulations (Thailand)`, is part of the same unqualified list and matches **no** ISO / SOC /
GDPR pattern. A remediation driven by a standards-token sweep would correct four lines and leave the
fifth — and the fifth is the statutory one, which is the most consequential.

**Rules violated, quoted from the decisions themselves** (all three read from the mainline tree):

> SMEsPlus MUST NOT self-declare that a customer is ISO/SOC/PDPA/GDPR compliant or certified solely
> because the software contains supporting functions. — Boss decision `03` §2
> `AUD-10 — SMEPLUS SUPPORTS CERTIFICATION / ASSURANCE; SMEPLUS DOES NOT SELF-DECLARE CUSTOMER CERTIFICATION.`
> SMEsPlus does NOT claim that the customer is certified merely because SMEsPlus implements
> standards-aligned controls. … **Standard Alignment belongs to the Function. Certification belongs
> to the Customer.** — Boss decision `05` §12
> The exact applicability of each framework must be evidence-reviewed and version-controlled.
> **No blanket compliance claim is created by this register.** — Boss decision `05` §5

**Already repudiated inside the corpus**, and the two documents have coexisted unreconciled:
`KNOWLEDGE_CONSOLIDATION_REPORT.md` records the file as describing a generic system that does not
reconcile with the evidence base, its compliance claims *"[not appearing] anywhere else in the
repository's governance model"*, logged as `GAP-KC-01`.

**Disposition: `UNQUALIFIED CLAIM — CORRECTION REQUIRED`. Remedy is retraction or explicit
quarantine — a governance act. This session has no authority to retract published material and does
not attempt it.** Carried to `SA_CORR2_13` as a Boss governance item.

### 3.2 It is the only one — established three ways

| Instrument | Result |
|---|---|
| Every named-standard token above, line-level, joined to paths | 1 unqualified claim |
| Compliance-assertion verbs — `compliant with\|complies with\|conforms to\|conformant\|adheres to\|certified (to\|against\|under)\|is certified\|ISO-certified\|GDPR-compliant\|PDPA-compliant\|fully compliant` | **36 hits, all read.** None is an unqualified named-standard claim about SMEsPlus |
| The heading form `standards? compliance` | 7 blobs — 6 are code-review checklist items, 1 is `SA11` quoting the claim |

All six files in `16_Learning_Analysis/` were swept individually. **Only `01_SYSTEM_OVERVIEW.md`
carries a named-standard compliance claim.**

**`CERTIFICATION/ATTESTATION VERIFIED` — 0 instances.** No certificate, service-auditor report or
attestation of any kind exists in the corpus.

---

## 4. Classification of every other standards statement

| Statement / source | Class |
|---|---|
| Boss decision `05` §5 A–D applicability register (ISO 9001, 27001, 27701, 22301, 37301, COSO; ISO 20000-1, 27017, 42001, SOC 1/2; TFRS, PDPA; ISO 22000/HACCP, IATF 16949, ISO 13485/45001/14001/50001) closing *"No blanket compliance claim is created by this register."* | `VERIFIED REQUIREMENT MAPPING` |
| Boss decision `04` §5 — *"VAPT results are security assurance evidence; they are not themselves an ISO certificate or SOC 1/SOC 2 attestation report."* | `VERIFIED REQUIREMENT MAPPING` |
| Boss decision `03` §2 and `AUD-05/06/10` | `NOT APPLICABLE` — prohibitions |
| `SA11` §2 — TAS 2 ¶12/¶13, TAS 16, Thai VAT, each carrying `STANDARD GAP` / `RESEARCH REQUIRED` / `EVIDENCE GAP` | `VERIFIED REQUIREMENT MAPPING` |
| `SA11` §3 nine control domains; `ND-06` *"a control that exists only in the user interface is not a control"* | `CONTROL DESIGN TARGET` |
| `THAILAND_BUSINESS_REALITY_USER_FITNESS_CONTROL_V1.md` — *"shall evaluate evidence/control requirements for organizational management systems such as ISO 9001 where relevant"* | `CONTROL DESIGN TARGET` |
| `38_STEP030211_ALL_24_GAPS_RESOLUTION_PLANNING_REGISTER.md` `GAP-014` — *"compliance control mappings (SOC2, ISO27001, etc.)"*, `PLANNED — READY FOR EXECUTION` | `CONTROL DESIGN TARGET` |
| `KNOWLEDGE_CONSOLIDATION_REPORT.md` `GAP-KC-01` — the repudiation, evidence-cited | `EVIDENCE-BACKED CONFORMANCE` *(of the repudiation, not of any standard)* |
| **`03_STEP040206_69_ITEM_REVALIDATION_REPORT.md`** — *"✓ DELTA-006 … TAS compliance (Thailand Accounting Standards)"* under **"Revalidation Confidence: HIGH"** | **`UNKNOWN / RESEARCH REQUIRED`** — §5 |
| PDPA body, 63 blobs — uniformly *"zero coverage anywhere"*, `MTI-D-05` unruled, `DECISION REQUIRED`, *"regime unconfirmed"* | `UNKNOWN / RESEARCH REQUIRED` |
| TAS / TFRS / IFRS / IAS body — e.g. *"TAS 2 ¶13 compliance is **unprovable**, not merely unproven"* | `VERIFIED REQUIREMENT MAPPING`, ¶13 items `EVIDENCE GAP` |
| A vendor-marketing page asserting the reference ERP *"supports"* IAS 2 NRV compliance, *"explicitly identified as uncorroborated commentary and excluded from evidence"* | `NOT APPLICABLE` — correctly excluded |
| The CORR2 prompts' own do-not lists naming ISO/SOC/GDPR | `NOT APPLICABLE` |

---

## 5. `C2-F-21` — a second, quieter overclaim, in a register downstream work inherits

`03_STEP040206_69_ITEM_REVALIDATION_REPORT.md`:

> `6. ✓ DELTA-006 (PS04-EXT-0022): l10n_th_reports_ext — TAS compliance (Thailand Accounting Standards)`

under a section headed **`Revalidation Confidence: HIGH`**.

**This is not a claim that SMEsPlus is TAS-compliant.** It is a scope justification quoting a
third-party component's self-described purpose. **It is still a problem**, for three reasons:

1. it carries a **`✓`** and a **`HIGH` confidence label** with no evidence that the component
   achieves TAS conformance;
2. it sits in an **in-scope revalidation register** that downstream work inherits as settled;
3. the corpus elsewhere records that **TAS 2 ¶13 conformance is *unprovable* on current evidence** —
   so a `✓` against `TAS compliance` contradicts the programme's own strongest finding on TAS.

**Classification: `UNKNOWN / RESEARCH REQUIRED`.** Disposition: **re-label**, from a tick to a
statement of what was actually revalidated (the component's presence and declared purpose).
1 distinct path, 1 branch. **This is a routine correction, not a Boss item** — it is recorded here
and routed to PMO, per master prompt §16's rule that routine operational corrections are not Boss
decisions.

---

## 6. What this register does not claim

- No certification is claimed. No compliance conclusion is drawn for any standard.
- Thai statutory items remain `HOLD / EVIDENCE REQUIRED`.
- **`SA11-F-03`/`F-04` stand unchanged**: the applicability register exists at Boss-decision level;
  the five mapping artefacts it mandates do not. CORR2 re-verified the absence and confirms it.
- The `SOX` binary-document figure in `SA11` §9.2 is **neither reproduced nor refuted** here, and
  the reason is stated (§2.1) rather than the figure silently dropped.

---

`CP-SA-C2-60` (standards half) — **1 unqualified claim, verified on 183 of 183 branches, correction
required by Boss governance act; 1 secondary overclaim routed to PMO; 0 certifications claimed
anywhere; 3 false-friend traps corrected.**

Boss remains the sole Final Approver. No Evidence = No Progress. Never Skip Gate.
