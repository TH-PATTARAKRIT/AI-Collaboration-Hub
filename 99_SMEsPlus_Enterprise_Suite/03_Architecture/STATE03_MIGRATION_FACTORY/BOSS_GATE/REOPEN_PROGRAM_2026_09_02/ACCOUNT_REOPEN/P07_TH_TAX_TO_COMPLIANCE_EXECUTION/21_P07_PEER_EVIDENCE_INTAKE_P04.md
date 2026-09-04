# P07 — PEER EVIDENCE INTAKE FROM P04, AND DISPOSITION OF ROUTED QUESTIONS

Session ID: `SMEPLUS-26-09-04-ACC-P07-TAX-TH-REV2-001`
Peer: P04 Acquire-to-Retire, branch `research/account-p04-acquire-to-retire-2026-09-04-001`, files `07 §4-§5`, `13 §4`
Classification: `LAYER 2 — AUDIT QUARANTINE`
Date: `2026-09-04`

## 1. Intake Rule Applied

The Common Execution Constitution permits parallel peer evidence to be consumed without
waiting. It does **not** permit a peer's summary to be adopted as this package's statutory
basis: `09 §1` requires authoritative retrieval for every legal claim. So each peer source
below carries an explicit verification state, and **only independently verified sources
enter `09`**.

| State | Meaning |
|---|---|
| `VERIFIED` | Retrieved and read at the Revenue Department's own publication by this session |
| `ACCEPTED-AS-PEER` | Consistent and material, but not independently retrieved here; **not** used to support a P07 conclusion |
| `OUT OF P07 SCOPE` | Real, but not within the VAT / withholding / tax-document surface this session researched |

## 2. Intake Table

| # | Peer source | State | Effect on P07 |
|---|---|---|---|
| 1 | มาตรา 77/1(8) "ขาย" and 77/1(9) "สินค้า" | **`VERIFIED`** — retrieved at `rd.go.th/5205.html` | **Material. Closes a gap this package had.** Enters `09` as `S-36` / `S-37`. See §3. |
| 2 | คำสั่งกรมสรรพากร ที่ ป.36/2536 (15 Nov 1993), hire purchase / instalment sale | **`VERIFIED`** — retrieved at `rd.go.th/3606.html` | **Material. Supplies a s.78/3 special tax point this package had recorded as not found.** Enters `09` as `S-38`. See §4. |
| 3 | ป.79/2541 and ป.84/2542, destruction of goods and scrap | `ACCEPTED-AS-PEER` | Bears on `P04-B-24`; see §5. Not used to support any P07 conclusion. |
| 4 | ข้อหารือ กค 0811/09658 (14 Sep 1999), destruction of damaged fixed assets | `ACCEPTED-AS-PEER` | A ruling on its own facts. Persuasive, not general. §5. |
| 5 | คู่มืออธิบายมาตรฐานการบัญชี ฉบับที่ 16 | `OUT OF P07 SCOPE` | Accounting-standard interpretation. P04's own classification of it as *not* a statutory requirement is the correct discipline and is noted with approval. |

## 3. `S-36` / `S-37` — A Gap This Package Had

Verified text, `rd.go.th/5205.html`:

- **"ขาย"** = `จำหน่าย จ่าย โอนสินค้าไม่ว่าจะมีประโยชน์หรือค่าตอบแทนหรือไม่` — a sale
  **does not require consideration**. The section then deems further acts to be sales,
  including (ก) conditional sale where ownership has not passed, (ข) delivery to an agent
  for resale, (ค) export, (ง) applying goods otherwise than to the direct conduct of the
  business per Director-General criteria, (จ) goods short against the stock report,
  (ฉ) goods remaining on cessation, (ช) other cases by regulation.
- **"สินค้า"** = `ทรัพย์สินที่มีรูปร่างและไม่มีรูปร่างที่อาจมีราคาและถือเอาได้` — tangible
  **and** intangible property. Not limited to property held for resale.

**This package did not cover deemed supplies at all.** `02_P07_VAT_EVENT_MODEL.md` treated
the source business event as a sale, a service or an import, all consideration-based;
`04_P07_TAX_POINT_MATRIX.md` had no row for a supply without consideration; `01` had no
requirement for it. That is a genuine scope gap in P07, not a defect the peer inherited —
it was found by a peer reading a definition this session never retrieved.

Consequences now recorded (`P07-F-58`): every no-consideration transfer — donation,
scrapping, application of goods to a non-business purpose, stock shortfall, goods on hand
at cessation — is a supply for VAT, and the researched system has **no output-tax event and
no tax document for any of them**, compounding `P07-F-26` (no tax-invoice object). The
`(ง)` limb is bounded by Director-General criteria that were **not** retrieved, so the
*extent* of the deeming is held at `U-23`; the *definitional* limb — that consideration is
not required — is verified and is not held.

## 4. `S-38` — A Special Tax Point This Package Recorded as Not Found

Verified text, `rd.go.th/3606.html`. For a hire-purchase or instalment-sale contract where
ownership does not pass on delivery, relying on Revenue Code s.78(2) and s.86:

- `ความรับผิดในการเสียภาษีมูลค่าเพิ่มของผู้ให้เช่าซื้อเกิดขึ้นเมื่อถึงกำหนดชำระราคาตามงวด`
  — liability arises **as each instalment falls due**, not at delivery and not at inception;
- `ผู้ให้เช่าซื้อต้องออกใบกำกับภาษีให้แก่ผู้เช่าซื้อทุกครั้งเมื่อถึงกำหนดชำระราคาตามงวด`
  — **a tax invoice must be issued on every instalment due date**.

`P07-N-07` recorded that no s.78/3 special tax point was found in the declared source set,
class `B`. That negative stands — nothing changes about the source set. What changes is that
the **statutory rule it was measured against is now known**, so the gap can be sized:

`P07-F-59` — a hire-purchase acquisition, which is the ordinary Thai route for machinery and
vehicles, requires one tax invoice per instalment over the life of the contract, each with
its own tax point. The researched system has no tax-invoice object (`P07-F-26`), no
instalment-driven tax point (`P07-F-02`), and no tax mapping to route the contract
(`P07-F-38`). The three findings compound rather than overlap: even if the tax point were
fixed, there is no document to issue; even if there were a document, its period would be
selected by the accounting date.

## 5. Disposition of the Three Routed Questions

### `P04-B-24` — does the 30-day destruction notice extend to fixed assets?

**Disposition: `HOLD — STATUTORY EVIDENCE REQUIRED`. P07 concurs with P04 and does not
answer it by inference.** The instruction's operative scope names goods, inventory and
scrap; a single ข้อหารือ directing one taxpayer towards that instruction is persuasive on
its facts and is not a general rule. Converting it into one would be exactly the
`B`-to-`A` upgrade the negative-claim standard prohibits.

**P07 adds a limb P04 did not name, and it is a VAT limb, not an income-tax one.** P04
framed the question entirely around deductibility under มาตรา 65 ตรี (13). But under the now
verified `S-36`, sub-paragraph (จ) deems **goods short against the stock report** to be a
sale. A destruction that is not properly evidenced therefore risks being treated as a
deemed supply carrying **output tax**, independently of whether the write-off is deductible.
Deductibility and deemed supply are separate consequences of one act. The evidence needed to
close `P04-B-24` must cover both; retrieving only the income-tax authority would close half
the question. Recorded as `U-24`.

### `P04-B-39` — no-proceeds disposal produces no tax invoice while VAT deems it a sale

**Disposition: promoted from an open question to a P07 finding at the definitional level,
with a bounded hold on scope.**

`S-36` is verified: consideration is not required for a sale, and `สินค้า` is not limited to
goods held for resale, so a fixed asset is goods. A donation is `จำหน่าย จ่าย โอน` on the
plain words. On the definitions alone, the peer's no-proceeds disposal path is an
**unrecorded output-tax event**. This is `P07-F-58`, and it is P07's finding to carry, not
P04's, because the missing artefact is a tax document and an output-tax event.

What remains held is the **extent**, not the existence: the (ง) limb operates by
Director-General criteria that were not retrieved, and any applicable exemption under s.81
was not examined. `U-23`. So the finding is stated as: *these acts fall within the
definition of a sale; whether a particular act is relieved requires the criteria and the
exemption list*.

### `P04-B-25` — Thai tax treatment of gain on disposal

**Disposition: `OUT OF P07 SCOPE AS RESEARCHED`, and P07 declines to answer it.**

P07 as directed covers VAT, withholding tax, tax documents, tax reports, correction and
filing. Gain on disposal is a corporate income tax question under Part 3 of the Revenue
Code. **Nothing in `09_P07_STATUTORY_SOURCE_REGISTER.md` bears on it** — the register holds
no corporate income tax authority at all, by design. Answering it from the VAT and
withholding sources this session retrieved would be inference across statutes, which is the
defect this programme has been correcting all week.

It is accepted as correctly routed **in the sense that it needs a tax owner**, and P07 is
the tax process. It is therefore carried as `U-25`, open, requiring its own retrieval of
corporate income tax authority. P07 flags that the question has now been raised in three
successive asset packages and dropped from each without closure; carrying it open with an
explicit evidence requirement is the way it stops being dropped.

`P04-B-05` (borrowing costs under TAS 23) is an accounting-standard question, not a tax
question, and is neither answered nor carried here.

## 6. Method Note — A Convergent Correction

P04 records that a search-result summary asserted a 30-day notice requirement for
fixed-asset write-off, and that reading the ruling in full showed the opposite on its facts,
so the summary was discarded.

This session made the same class of error and caught it the same way: a retrieval summary
indicated the reduced VAT rate expires 30 September 2026, twenty-six days after this
session's date, which would have made `P07-F-01` an imminent compliance cliff. Searching for
a later instrument showed a further extension to 30 September 2027 (`11 P07-C-21`,
`15 REV-E-07`).

Two independent sessions, the same failure mode — **a secondary summary contradicting the
primary text it purports to summarise** — and in both cases it was caught only by reading
the primary source. Recorded because it is now a pattern across sessions, not a one-off, and
it belongs in the programme's method register rather than in either package alone.

## 7. What Changed in This Package

| File | Change |
|---|---|
| `09` | `S-36`, `S-37`, `S-38` added as verified statutory sources; `P-11`, `P-12` added as derived positions; `U-23`, `U-24`, `U-25` added to the HOLD table |
| `01` | `R-V-25` (deemed supplies) and `R-V-26` (hire purchase) added |
| `02` | `§2A` added — deemed supplies, absent from the first issue |
| `04` | `TP-11` and `TP-12` added to the tax-point matrix |
| `00` | `P07-F-58`, `P07-F-59` registered |
| `12` | `P07-D-30` — peer dependency on P04 for the destruction evidence |
| `14` | digests regenerated |

Nothing already published was withdrawn by this intake. Two gaps were closed and three
questions dispositioned.
