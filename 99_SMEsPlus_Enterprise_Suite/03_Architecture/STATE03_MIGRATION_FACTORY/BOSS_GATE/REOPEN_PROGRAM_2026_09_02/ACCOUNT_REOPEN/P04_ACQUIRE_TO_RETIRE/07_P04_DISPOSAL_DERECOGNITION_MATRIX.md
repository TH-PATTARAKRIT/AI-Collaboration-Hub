# 07 — P04 DISPOSAL AND DERECOGNITION MATRIX

Layer: **2 — audit quarantine**.

The three prior Asset packages covered the retire end thinly: sale was documented,
disposal was documented as "sale without proceeds", and **derecognition criteria,
transfer, impairment, asset scrap and the Thai evidence requirements were never
researched at all**. This file closes as much of that as primary evidence allows.

---

## 1. What the estate distinguishes

Exactly **two** actions, both routed through the same closing method:

| Action | Proceeds | Entry reference | Effect |
|--------|----------|-----------------|--------|
| **Dispose** | none | "Disposal" | the whole net book value falls to the company loss account |
| **Sell** | lines of a **posted customer invoice**, selected in the wizard | "Sale" | one debit per distinct invoice income account, neutralising the revenue already booked, then the residual difference to gain or loss |

**Scrap does not exist.** Not found under the asset module using case-insensitive
`scrap`. Scrapping must be recorded as a disposal — which, as §5 shows, is the
wrong evidence trail for Thai purposes.

## 2. The disposal entry, exactly as built

Worked example — cost 10 000, accumulated depreciation 4 000, proceeds 7 000:

| Account | Dr | Cr | Meaning |
|---------|----|----|---------|
| Fixed-asset account | | **10 000** | gross cost removed |
| Accumulated depreciation | **4 000** | | accumulated depreciation cleared |
| The customer invoice's income account | **7 000** | | the revenue already booked is neutralised |
| Company **gain** account | | **1 000** | the gain |

The identity is

```
gain (loss) = net proceeds − carrying amount
carrying amount = original value − accumulated depreciation
```

Salvage value sits **inside** the carrying amount, because it is never
depreciated.

### 2.1 Six behaviours of that entry

| ID | Behaviour | Class |
|----|-----------|-------|
| **P04-F-13** | **The entry is created in DRAFT and the system never posts it**, while the asset has already been written to the closed state | FACT VERIFIED, **High** |
| **P04-F-26** | A **zero** difference still writes a **zero-value line to the loss account**, because the branch tests "greater than zero" | FACT VERIFIED |
| **P04-F-27** | The stored "net gain on sale" figure uses a book value that **includes children's book value**, while the posted difference is computed **per asset**. The two can diverge | PRIOR EVIDENCE (P2 `CTR-05`), re-confirmed |
| **P04-F-19** | The wizard's gain/loss account fields reach the entry **only by rewriting the company default**, with elevated privilege | FACT VERIFIED, **High for control** |
| **P04-F-23** | A blank account causes that leg to be **dropped**, producing an unbalanced draft entry | FACT VERIFIED, **High** |
| **P04-F-28** | Disposal is refused at or before the user fiscal lock date | FACT VERIFIED (a working control) |

## 3. Mechanics verified this session

| Question | Answer | Class |
|----------|--------|-------|
| Is a catch-up depreciation posted before a mid-period disposal? | **Yes.** All draft entries after the disposal date are deleted, all posted entries after it are reversed or deleted, a pro-rata entry to the disposal date is inserted **and posted**, and only then is the disposal entry built. Corroborated by the estate's own test | FACT VERIFIED |
| Is the accumulated depreciation cleared in full? | Yes — one line for the whole depreciated amount, including any imported previously-recognised depreciation | FACT VERIFIED |
| Is partial disposal supported? | **No.** No parameter, field or branch exists. The disposal always uses the full original value. The only granularity is to capitalize as N assets **at creation** and dispose of them individually | FACT VERIFIED |
| What if the asset is not fully depreciated? | Handled by construction — the residual carrying amount falls into the difference line and lands in the loss account, at its value **on the disposal date** | FACT VERIFIED |
| What happens to child assets? | **All children are closed too**, each with its own disposal entry. The sale path is blocked if any child is still draft or running, or carries residual value. A child that is already closed with zero residual passes that guard **yet is still fed the same customer-invoice lines as the parent** | FACT VERIFIED for the guard; the last clause is **UNRESOLVED** — no test exercises it. Registered **P04-B-18** |
| Can a closed asset be re-opened? | Yes. The stored gain is reset to zero and the schedule is rebuilt — but **the disposal entry is not automatically reversed** | PRIOR EVIDENCE, re-confirmed |
| Does the re-open path work after a disposal? | **UNRESOLVED.** The re-open path runs the modify machinery, which refuses if any draft entry predates the operation date — and the draft disposal entry left by P04-F-13 is exactly such an entry. No test covers this path. Registered **P04-B-19** | UNRESOLVED |

## 4. Against TAS 16 — the standard the estate is measured by

Source `TAS-16M`: คู่มืออธิบายมาตรฐานการบัญชี ฉบับที่ 16 เรื่อง ที่ดิน อาคารและอุปกรณ์,
สภาวิชาชีพบัญชี ในพระบรมราชูปถัมภ์, เผยแพร่ 27 กุมภาพันธ์ 2563.

The document states on every page that it is **not part of the financial
reporting standards** (`คู่มืออธิบายมาตรฐานการบัญชีนี้ ไม่ถือเป็นส่วนหนึ่งของมาตรฐานการรายงานทางการเงิน`).
Every row below is therefore classified against the **manual**, not against the
standard text. `HOLD-03` from the prior package — retrieval of the TAS 16
standard text itself — **remains open**.

### 4.1 Derecognition criteria — researched for the first time

Quoted from `TAS-16M`, section การตัดรายการ:

> กิจการต้องตัดรายการมูลค่าตามบัญชีของรายการที่ดิน อาคารและอุปกรณ์ออกจากบัญชี เมื่อเข้าเงื่อนไขข้อใดข้อหนึ่งดังต่อไปนี้
> 1) กิจการจำหน่ายสินทรัพย์ หรือ
> 2) กิจการคาดว่าจะไม่ได้รับประโยชน์เชิงเศรษฐกิจในอนาคตจากการใช้สินทรัพย์หรือจากการจำหน่ายสินทรัพย์

| # | Requirement | Estate position | Verdict |
|---|-------------|-----------------|---------|
| **D-1** | Derecognise on **disposal** | Present — the dispose/sell path | **Met in mechanism.** Not met in effect while the entry stays in draft (P04-F-13) |
| **D-2** | Derecognise when **no future economic benefit is expected** from use or disposal | **No trigger of any kind exists.** The estate has no "no longer expected to yield benefit" state, no idle state, and no impairment concept | **NOT MET.** Registered **P04-B-20** |
| **D-3** | Gain or loss = **net consideration received on disposal − carrying amount**, recognised in profit or loss | The identity matches exactly | **Met** |
| **D-4** | Disposal may take **several forms** — sale, finance lease, **donation** (`โดยการขาย โดยการให้เช่า ภายใต้สัญญาเช่าเงินทุน หรือโดยการบริจาค`) | The estate models **sale** and **no-proceeds disposal** only. A donation is expressible only as a no-proceeds disposal, which loses the donation's own tax and VAT character | **Partly met.** Registered **P04-B-21** |
| **D-5** | The **disposal date** is the date the recipient obtains **control**, determined under the revenue standard | The disposal date is a **free-text wizard field defaulting to today**, with no link to any control-transfer event | **NOT MET.** Registered **P04-B-22** |
| **D-6** | Sale and leaseback is accounted under the leases standard | No lease module exists in the population | **NOT MET** — no host |
| **D-7** | On derecognition of a revalued asset, the **revaluation surplus is transferred directly to retained earnings**, not through profit or loss | No revaluation surplus exists; downward revaluation is posted to **depreciation expense** | **NOT MET.** Registered **P04-B-11** |

### 4.2 Impairment and compensation — also first researched here

`TAS-16M` requires that impairment, derecognition and third-party compensation
be treated as **separate economic events, accounted for separately**:

> การด้อยค่าหรือการสูญเสียของรายการที่ดิน อาคารและอุปกรณ์ รวมถึงสิทธิเรียกร้องที่จะได้รับค่าชดเชยจากบุคคลที่สาม และการซื้อหรือการก่อสร้างสินทรัพย์เพื่อการเปลี่ยนแทนในภายหลัง ถือเป็นเหตุการณ์ทางเศรษฐกิจที่แยกจากกัน และต้องบันทึกบัญชีแยกจากกัน

with impairment itself governed by TAS 36, and compensation from a third party
for an impaired, lost or retired asset recognised in profit or loss **when the
entity becomes entitled to it**.

| Requirement | Estate position | Verdict |
|-------------|-----------------|---------|
| Impairment recognised under TAS 36 | **No impairment concept.** The nearest behaviour, downward revaluation, posts to **depreciation expense** — i.e. it records an impairment as accelerated depreciation | **NOT MET, and actively mis-stated.** Registered **P04-B-10** |
| Insurance or other compensation recognised separately when receivable | **No mechanism found.** A compensation receipt has no path onto or beside the asset | **NOT MET.** Registered **P04-B-23** |
| Replacement asset accounted separately | Present — a replacement is simply a new asset | Met |

> **P04-F-29.** The estate's downward revaluation is posted to depreciation
> expense and is **labelled in the ledger as an ordinary depreciation**
> (P04-F-15). An impairment recorded this way is indistinguishable from
> depreciation in the general ledger, in the depreciation schedule report, and
> in any statutory disclosure derived from either. This is not a presentation
> preference — the manual requires the two to be **separate events, separately
> recorded**.
> Class: **FACT VERIFIED** (estate) against **ACCOUNTING STANDARD INTERPRETATION**
> (manual). Severity **High**.

### 4.3 Depreciation cessation — new evidence bearing on a standing Boss decision

`TAS-16M`, on when depreciation stops:

> การคิดค่าเสื่อมราคาจะสิ้นสุดลงเมื่อกิจการตัดรายการสินทรัพย์นั้นหรือจัดประเภทสินทรัพย์นั้นเป็นสินทรัพย์ที่ถือไว้เพื่อขาย … **กิจการไม่อาจหยุดคิดค่าเสื่อมราคาของสินทรัพย์เมื่อกิจการไม่ได้ใช้งานสินทรัพย์นั้นหรือปลดจากการใช้งานประจำ เว้นแต่สินทรัพย์นั้นได้คิดค่าเสื่อมราคาเต็มจำนวนแล้ว**

and, on the units-of-production method:

> หากกิจการใช้วิธีการคิดค่าเสื่อมราคาตามปริมาณการใช้ ค่าเสื่อมราคาอาจมีค่าเท่ากับศูนย์ได้เมื่อไม่มีการผลิต

Three consequences, all new to this programme:

| ID | Consequence | Bears on |
|----|-------------|----------|
| **P04-F-30** | Depreciation **may not be stopped** merely because an asset is idle or withdrawn from routine use — **unless it is already fully depreciated**. The estate's pause function therefore has **no accounting justification for an idle owned asset**, only a tax one, and the tax one is itself open (`HOLD-05`) | The pause function; `HOLD-05` |
| **P04-F-31** | An asset **still in internal use after being fully depreciated legitimately carries a zero depreciation charge**. The Boss decision on continuous internal usage after full depreciation is therefore **consistent with TAS 16 as to the financial ledger** — the standard itself contemplates exactly that outcome | **BD-01** — supports it on new evidence |
| **P04-F-32** | Under the **units-of-production** method a period charge of **zero when there is no production** is expressly contemplated. This is a different lever from the normal-capacity denominator of TAS 2 ¶13. TAS 16 governs the size of the **charge**; TAS 2 governs its **absorption into inventory**. Conflating them is what makes the two readings of the 100 %-attribution instruction look equally valid | **BD-02 / BLK-07** — see `09` §4 |

## 5. Thai tax and evidence at the retire end — the dropped items, closed

A prior package raised two Thai items at the retire end — documentation
requirements for disposal and write-off, and the tax treatment of gain on
disposal — and both **fell out of every later register without being closed**.
They are re-opened and addressed here.

### 5.1 Destruction of goods and scrap — the regime that does NOT apply to fixed assets

| Source | Content |
|--------|---------|
| คำสั่งกรมสรรพากร ที่ **ป. 79/2541** (3 November 1998) — *แนวทางปฏิบัติ กรณีการทำลายของเสีย สินค้าที่เสื่อมคุณภาพ สินค้าที่มีตำหนิ สินค้าที่หมดสมัยนิยม สินค้าที่หมดอายุ และเศษซาก* | Covers **ของเสีย · สินค้าเสื่อมคุณภาพ · สินค้ามีตำหนิ · สินค้าหมดสมัยนิยม · สินค้าหมดอายุ · เศษซาก**. Requires approval by an authorised person; witnesses drawn from warehouse, accounting, sales or audit; the **auditor invited as a witness** and certifying **in writing** attached to the statements |
| คำสั่งกรมสรรพากร ที่ **ป. 84/2542** (13 May 1999) | Revokes and replaces clause 3.2 of the above. Requires notice to the responsible officer **ล่วงหน้าเป็นเวลา 30 วันก่อนวันทำลาย** — 30 days in advance of the destruction date; officials **may** attend; no notice is required where destruction is already under official supervision |

> **P04-F-33.** These instructions are addressed to **goods, inventory and
> scrap**. Fixed assets do **not** appear in their operative scope.
> Class: **FACT VERIFIED** from the instruction text.

### 5.2 Destruction of a damaged fixed asset — the regime that does apply

Ruling **กค 0811/09658**, 14 September 2542 (1999). A company destroyed damaged
computer equipment and carpeting without prior notice and asked whether the
remaining book value was deductible. The operative answer:

> หากบริษัทฯ สามารถพิสูจน์ได้ว่ามีการทำลายทรัพย์สินดังกล่าวจริง และมีผู้สอบบัญชีของบริษัทฯ รับรอง การกระทำดังกล่าว ถือเป็นผลเสียหายจากการประกอบกิจการโดยตรงไม่ต้องห้ามตามมาตรา 65 ตรี (13)

| ID | Position | Class |
|----|----------|-------|
| **P04-LAW-01** | Where the company can **prove the destruction actually occurred** and **its auditor certifies it**, the remaining book value is a loss arising directly from the business and is **not prohibited** by Revenue Code s.65 ter (13) | **FACT VERIFIED** from the ruling text |
| **P04-LAW-02** | On the facts of that ruling, deduction was allowed **without prior notice** to the officer, with the ruling directing future destructions to the instruction at §5.1 | **FACT VERIFIED** from the ruling text |
| **P04-LAW-03** | Whether the 30-day advance-notice regime of ป.84/2542 extends to **fixed assets** — given that its own scope names goods and scrap, while the ruling points a taxpayer towards it — is **not settled by these two sources**. A single ruling is persuasive, not general | **HOLD / EVIDENCE REQUIRED** — routed to the Accounting-Tax track. Registered **P04-B-24** |

This closes the prior package's dropped disposal-documentation item as far as
primary evidence permits, and states precisely what remains open.

### 5.3 What this means for the SMEsPlus design

| Requirement | Source | Design consequence |
|-------------|--------|--------------------|
| Prove destruction actually occurred | P04-LAW-01 | The retire event must carry **evidence attachments**, not just a date and an amount |
| Auditor certification | P04-LAW-01 | A **certification artefact** distinct from the accounting entry, retained with the asset |
| Possible 30-day advance notice | P04-LAW-03 | If confirmed, a **notification date must precede the destruction date by 30 days**, and the system must be able to prove it did. This is a *dated control*, not a document field |
| Scrap ≠ disposal ≠ sale, for evidence purposes | §5.1 vs §5.2 | The estate's single disposal action **cannot carry three different evidence regimes**. This is why P04-B-12 (scrap as a distinct event) is an evidence requirement and not a cosmetic one |

### 5.5 Value-added tax on the disposal of a fixed asset — researched and closed

Raised at `15` Level 3 by the statutory expert as an item **no package had
addressed**, and researched immediately rather than left open.

**Source `P04-LAW-F` — ประมวลรัษฎากร มาตรา 77/1 (8) และ (9).**

| Provision | Operative text | Consequence |
|-----------|----------------|-------------|
| มาตรา 77/1 (8) — **"ขาย"** | *จำหน่าย จ่าย โอนสินค้า **ไม่ว่าจะมีประโยชน์หรือค่าตอบแทนหรือไม่*** | A "sale" for VAT **does not require consideration**. Sub-paragraphs additionally deem certain acts a sale, including **(ง)** applying goods to a purpose other than the direct conduct of the business, per criteria issued by the Director-General; **(จ)** goods missing from the stock record; **(ฉ)** goods remaining on cessation of business |
| มาตรา 77/1 (9) — **"สินค้า"** | *ทรัพย์สินที่มีรูปร่างและไม่มีรูปร่าง* … | "Goods" is **tangible and intangible property**. It is **not** limited to property held for resale. A fixed asset is goods |

| ID | Position | Class |
|----|----------|-------|
| **P04-LAW-04** | A VAT-registered person **selling a fixed asset is making a sale of goods**. Output tax arises and a tax invoice must be issued | **FACT VERIFIED** from the Revenue Code definitions |
| **P04-LAW-05** | Because consideration is **not** required by the definition, **a disposal by donation is also a sale** for VAT purposes | **FACT VERIFIED** as to the definition; **SUPPORTED INTERPRETATION** as to the tax base and any exemption, which were not researched |
| **P04-LAW-06** | Applying an asset to a non-business purpose, an asset **missing from the record**, and assets **remaining on cessation** are each deemed a sale under a sub-paragraph, with (ง) governed by criteria issued by the Director-General that this session did not retrieve | **SUPPORTED INTERPRETATION** — the deeming provisions are verified; their scope for fixed assets is not |

#### What this does to the estate's two retire paths

| Path | VAT consequence | Estate behaviour | Verdict |
|------|-----------------|------------------|---------|
| **Sell** — proceeds taken from a **posted customer invoice** | Output tax arises; the customer invoice carries it | The tax is on the customer invoice, which exists **independently** of the asset entry. **Nothing checks that the two agree** | **Workable, unverified.** `P04-B-38` narrowed to a reconciliation gap |
| **Dispose** — **no proceeds, no customer invoice** | Where the disposal is a **donation**, or is a deemed sale under a sub-paragraph, **output tax still arises** | The no-proceeds path produces **no customer invoice and therefore no tax invoice**. Nothing prompts one | **DEFECT** |

> **P04-F-63.** The estate's no-proceeds disposal path is the **only** way to
> record a donation, a scrapping, or a write-off — and it produces **no tax
> invoice**, while Thai VAT law defines a sale without requiring consideration
> and separately deems several such acts to be sales. A donation recorded
> through the disposal path is, on the face of the definitions, **an unrecorded
> output-tax event**.
> Class: **FACT VERIFIED** as to the estate; **SUPPORTED INTERPRETATION** as to
> the tax outcome, which depends on the Director-General's criteria and on any
> exemption. Severity **High**. Routed to the Accounting-Tax track as
> **P04-B-39**.

This is a second, independent reason why **scrap must be a retire event distinct
from disposal** (`P04-BD-07`): the two differ not only in their evidence regime
(§5.1 versus §5.2) but in whether an output-tax event arises at all.

### 5.4 Tax gain or loss on disposal — still open

A prior package established that Thai tax gain or loss on disposal is computed on
the **tax written-down value**, which the estate does not hold, so the
reconciliation is external. That finding stands and is imported.

The prior item on the **tax treatment of gain on disposal** was left on
`HOLD / EVIDENCE REQUIRED` and then dropped. It is **re-opened here unchanged**
and registered **P04-B-25**. This session did not research it; saying so is the
point — it must not disappear from the register a second time.

---

## 6. Summary of the retire end

| ID | Finding | Class |
|----|---------|-------|
| **P04-F-13** | The derecognition entry is created in draft and never posted by the system | FACT VERIFIED, High |
| **P04-F-29** | An impairment is recorded as, and labelled as, ordinary depreciation | FACT VERIFIED, High |
| **P04-F-33** | The Thai destruction instructions cover goods and scrap; fixed-asset destruction rests on a **different** authority with **different** evidence | FACT VERIFIED |
| **P04-F-34** | Of seven TAS 16 derecognition requirements, **one is met, two are partly met, and four have no host in the estate** | FACT VERIFIED (estate) vs manual |
| **P04-F-30/31/32** | New TAS 16 evidence on depreciation cessation, full depreciation and units-of-production zero charge — bearing directly on `BD-01` and `BLK-07` | ACCOUNTING STANDARD INTERPRETATION |
| **P04-F-19** | Every disposal silently rewrites the company's gain and loss account defaults | FACT VERIFIED, High |
| **P04-F-63** | The no-proceeds disposal path — the only way to record a donation, a scrapping or a write-off — produces **no tax invoice**, while the VAT definition of a sale does not require consideration | FACT VERIFIED (estate) / SUPPORTED INTERPRETATION (tax), High |
