# [SMEPLUS-26-09-06-SAAS-CELL-001]
# Boss Decision — Canonical English Default + Purchase Menu

## Decision Status
BOSS APPROVED

Boss is the sole Final Approver.

## Approved Product-Language Rule

SMEsPlus will use:

- **English as the Canonical Product Language and default UI language**
- **Thai as the secondary controlled localization language**
- Thai translation must be semantic and business-correct, not literal word-for-word translation
- Canonical IDs remain language-independent and stable

Working structure:

`Canonical ID -> Canonical English -> Localized Language`

Example:

`DOMAIN.PURCHASE -> Purchase -> th-TH: จัดซื้อ`

## Approved Menu Decision

For the purchasing domain, the Boss approved the direct user-facing English menu name:

**Purchase**

Thai controlled localization:

**จัดซื้อ**

Internal canonical identity remains separate from the mutable display label where required.

## Rationale

The Boss prefers **Purchase** over **Procurement** for the main user-facing menu because it is more direct, more familiar, and has lower interpretation cost for ordinary ERP users.

This supports the First Image principle:

> Familiar Name. Distinctive Image. Stable Memory.

The product should not create new vocabulary where a widely understood business term already exists.

## Current Approved First-Image Menu Direction

- Sales -> ขาย
- Purchase -> จัดซื้อ
- Inventory -> คลังสินค้า
- Manufacturing -> ผลิต
- Finance -> บัญชีและการเงิน

These labels are the approved direction for validation and product-language design. Human validation and final naming freeze remain subject to evidence and the existing First Image Gate.

## Governance

- No Evidence = No Progress.
- Never Skip Gate.
- English is canonical; localization does not redefine the canonical business concept.
- New capabilities must first define Business Meaning, then select a familiar English concept, then create Thai semantic localization, then validate First Image comprehension.
- Boss remains sole Final Approver.

## Scope Boundary

This decision does not authorize Team C, production deployment, database topology changes, or bypass of the existing validation gates.
