# [SMEPLUS-26-09-06-SAAS-CELL-001]
# Research — First Image Menu Naming & Visual Identity

Status: RESEARCH / EVIDENCE PACKAGE — NOT BOSS FREEZE
Jira: ERPPLUS-151
Boss: Sole Final Approver
Principle: No Evidence = No Progress

## 1. Research Question

How should SMEsPlus name and visually present top-level ERP modules so that Thai users recognize purpose immediately, avoid unnecessary relearning, and still perceive a distinctive SMEsPlus product identity?

## 2. Current Boss Intent

The target is not to be different merely for novelty. The first image should let users recognize what a module is and predict what it does without having to learn a new vocabulary first.

Working principle:

> Recognition before differentiation.
> Familiar language; distinctive SMEsPlus identity.

## 3. External Evidence

### 3.1 Nielsen Norman Group — Menu Design
Source: https://media.nngroup.com/media/articles/attachments/PDF_Menu-Design-Checklist.pdf

Key evidence:
- Use clear, specific, familiar wording for navigation labels.
- Avoid internal jargon.
- Use descriptive labels so users can anticipate the destination.
- Keep labels concise for scanability.
- Standardize terminology across navigation.
- Front-load key terms in vertical menus.

Implication for SMEsPlus:
Do not force users to learn invented product vocabulary when familiar business terminology already communicates the destination accurately.

### 3.2 Apple Human Interface Guidelines — Menus and Icons
Sources:
- https://developer.apple.com/design/human-interface-guidelines/menus
- https://developer.apple.com/design/human-interface-guidelines/icons

Key evidence:
- Menu labels should clearly and succinctly describe what they do.
- Familiar icons improve recognition.
- Do not use an icon if it cannot clearly represent the item.
- Interface icons should use simple, recognizable visual metaphors.
- Visual treatment should be consistent across an icon family.

Implication for SMEsPlus:
Visual differentiation should be achieved through a coherent icon language and interaction system, not by replacing familiar business words with unfamiliar labels.

### 3.3 Microsoft Fluent 2 — Navigation and Brand Recognition
Sources:
- https://fluent2.microsoft.design/components/web/react/core/nav/usage
- https://fluent2.microsoft.design/iconography
- https://fluent2.microsoft.design/design-principles
- https://fluent2.microsoft.design/color

Key evidence:
- Navigation labels should be brief and clear.
- Use simple recognizable icons for navigation categories.
- Consistent taxonomy/order increases predictability and customer confidence.
- Fluent explicitly recommends building from what users already understand.
- Distinct brand recognition can come from signature experiences, color, iconography, typography, sound and interaction rather than unfamiliar terminology.

Implication for SMEsPlus:
The desired strategy is compatible with a mature design-system approach: familiar business taxonomy + unmistakable SMEsPlus visual/interaction identity.

### 3.4 ERP Market Vocabulary Evidence

#### Odoo 19
Source: https://www.odoo.com/documentation/19.0/applications.html
Uses familiar application/domain names such as:
- Accounting
- Sales
- Purchase
- Inventory
- Manufacturing
- Quality
- Project

Additional evidence:
- Sales covers quotation -> sales order -> delivery/invoice process.
  Source: https://www.odoo.com/documentation/19.0/applications/sales/sales.html
- Purchase covers RFQ, purchase agreements and purchase orders.
  Source: https://www.odoo.com/documentation/19.0/applications/inventory_and_mrp/purchase.html
- Inventory covers warehouse/location/movement, not only on-hand stock.
  Sources:
  - https://www.odoo.com/documentation/19.0/applications/inventory_and_mrp/inventory.html
  - https://www.odoo.com/documentation/19.0/applications/inventory_and_mrp/inventory/warehouses_storage/inventory_management.html

#### SAP Business One
Source: https://help.sap.com/docs/PRODUCT_ID/68a2e87fb29941b5bf959a184d9c6727/4510027ecf465d7ae10000000a11466f.html?locale=en-US&state=PRODUCTION&version=9.3
Uses recognizable categories such as:
- Financials
- Sales – A/R
- Purchasing – A/P
- Business Partners
- Inventory
- Production

SAP Inventory explicitly includes goods receipt, goods issue, inventory transfer and inventory count, showing that Inventory is wider than current stock quantity only.
Source: https://help.sap.com/docs/SAP_BUSINESS_ONE/68a2e87fb29941b5bf959a184d9c6727/452365de9e152b31e10000000a1553f7.html

#### Microsoft Dynamics 365
Source: https://www.microsoft.com/en-us/dynamics-365/what-is-dynamics-365
Uses recognizable business capability names such as:
- Sales
- Finance
- Supply Chain Management
- Project Operations
- Human Resources
- Commerce
- Field Service

Market conclusion:
Mature ERP vendors generally do not create unfamiliar names for fundamental business domains solely to differentiate the product.

## 4. SMEsPlus Research Finding

### Finding FIMG-01 — Familiar business words are an asset, not a weakness
If a term is already deeply learned by users and accurately represents the domain, SMEsPlus gains usability by preserving that recognition.

### Finding FIMG-02 — Product differentiation should move to the visual and interaction layer
SMEsPlus should build a recognizable design DNA through:
- Domain icon family
- Shape/grid/stroke language
- Brand accent system
- Selected/active states
- Motion/interaction pattern
- Typography/hierarchy
- AI assistance pattern
- Control/evidence visibility

### Finding FIMG-03 — Top-level domain and child function must not be mixed
Examples:
- Top-level: ขาย (Sales)
- Child: ใบเสนอราคา (Quotation), คำสั่งขาย (SO), ส่งสินค้า (Delivery)

A parent domain should not be named with one child document type, e.g. ขาย (SO), if the parent covers the full sales domain.

### Finding FIMG-04 — Inventory should not be reduced to “สินค้าคงเหลือ”
Inventory includes receiving, issuing/delivery, transfer, on-hand, counting, replenishment, lot/serial and movement history.

Recommended candidate parent label for Thai comprehension testing:
- คลังสินค้า (Inventory)

### Finding FIMG-05 — First Image should be measurable
Candidate measures:
1. Recognition Time — time to infer purpose
2. Unaided Comprehension — meaning understood without explanation
3. Navigation Accuracy — user chooses correct module for a task
4. Ambiguity Rate — number of plausible incorrect interpretations
5. Relearning Cost — amount of training/explanation required
6. Visual Recall — ability to identify the module from icon/visual identity after exposure

## 5. Current Candidate Labels for Human Test — NOT FROZEN

- ขาย (Sales)
- จัดซื้อ (Procurement)
- คลังสินค้า (Inventory)
- ผลิต (Manufacturing)
- บัญชีและการเงิน (Finance)

These are candidates for evidence testing, not approved final labels.

## 6. Human Evidence Plan

### Round A — Blind Unaided Comprehension
Show text label only.
Question: “เห็นชื่อนี้แล้วคิดว่าเข้าไปทำอะไรได้บ้าง?”
Do not show English/canonical explanation or competing ERP examples before response.

### Round B — Task Matching
Example tasks:
- Create quotation for customer
- Create purchase order for supplier
- Receive goods
- Deliver goods
- Transfer goods between warehouses
- Check on-hand stock

Measure whether the user selects the expected parent module.

### Round C — T(E) vs E(T)
Compare:
- ขาย (Sales)
- Sales (ขาย)

Measure comprehension time, navigation accuracy and preference separately. Preference alone must not determine the winner.

### Round D — Visual Identity Test
Show identical familiar labels with candidate SMEsPlus icon families.
Measure:
- immediate semantic recognition
- cross-module confusion
- brand recall
- visual consistency

## 7. Proposed Acceptance Gate

Research proposal only:
- >96% comprehension/navigation accuracy: PASS candidate
- 90–96%: REVIEW
- <90%: RENAME/RETEST

A threshold is not yet constitutional until Boss approves the measurement method, sample design and gate.

## 8. Figma Evidence

Existing stress-test file:
https://www.figma.com/design/wQRiN7UmlN2c016KrqdPOC

Current panels compare:
A. Canonical Product Names
B. Thai User Menu
C. Hybrid

Next visual round should test familiar labels + distinctive SMEsPlus domain icon language.

## 9. Slack Human Survey Status

Blind Thai Menu Comprehension Test was posted in SMEsPlus Slack.
Survey link:
https://scglegacy.slack.com/archives/C0BBYGPN6G4/p1788679679919629

Status at research publication time: NO RESPONSES YET.
Therefore no Thai user comprehension percentage may be claimed yet.

## 10. Advisory Recommendation

Recommended direction:

> DO NOT DIFFERENTIATE THROUGH UNFAMILIAR MENU VOCABULARY.
> DIFFERENTIATE THROUGH SMEPLUS VISUAL LANGUAGE, INTERACTION, CONTROL, KNOWLEDGE AND AI.

Thai working form:

> ชื่อให้คนเข้าใจ — ภาพและความสามารถให้คนจำว่าเป็น SMEsPlus

Proposed First Image principle:

> The first image should allow a user to recognize what a module is and predict where to act without unnecessary relearning.

## 11. Controls

- No menu name is frozen by this research package.
- No invented percentage is permitted without respondent evidence.
- Reference systems are evidence/benchmark only; no architecture cloning is authorized.
- SMEsPlus remains clean-room and SMEsPlus-first.
- Boss remains sole Final Approver.
