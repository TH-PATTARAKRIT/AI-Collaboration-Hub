# EC-03 — Ksolves Module Classification Decision Pack

Session: `[SMEPLUS-26-08-28-DEEP-CD-001]`  
Date: 2026-08-29 Asia/Bangkok  
Gate: `EC-03 — Classification / License / CLASS-D Control`  
Decision Authority: Boss — Sole Final Approver  
Prepared By: ChatGPT L99 / Clean-Room Evidence Gate Review  
Status: `READY FOR GOVERNANCE DECISION / NO CLASS ASSIGNED BY AI`

## 1. Decision Required

Two current observed modules are outside the approved 1,502-module A/B/C/D classification baseline:

| Module | Current License Evidence | Current Project Treatment | Formal A/B/C/D Status |
|---|---|---|---|
| `ks_dashboard_ninja` | OPL-1 | metadata / black-box behavioral only; no implementation transfer | UNCLASSIFIED |
| `ks_dn_advance` | OPL-1 | metadata / black-box behavioral only; no implementation transfer | UNCLASSIFIED |

Current observed source = 1,504 modules. Approved STEP040301 baseline remains 1,502 modules.

No class is assigned by this document.

## 2. Existing Project Class Controls

### CLASS-A

Research may proceed only to the extent supported by license and governance. Output must still be normalized into business semantics and independent target design.

### CLASS-B

Controlled functional/semantic learning. Structural translation is prohibited; independent design rationale remains mandatory.

### CLASS-C

Black-box or documented behavior only. Evidence uses observable inputs, outputs, lifecycle and business consequences. Implementation-body transfer is prohibited.

### CLASS-D

Quarantined. No source-body research, detailed extraction or target influence without explicit Boss/legal governance authorization.

The existing 12 CLASS-D identities remain separately quarantined and are not changed by this decision pack.

## 3. Evidence Position

Observed and already evidenced:

- both modules are present in the current 1,504 source inventory;
- both are recorded with OPL-1 license evidence in the current manifest inventory;
- project evidence identifies them as purchased third-party modules;
- current safe treatment is already `METADATA / BLACK-BOX BEHAVIORAL ONLY; NO IMPLEMENTATION TRANSFER`;
- no evidence currently authorizes their implementation bodies to influence SMEsPlus Core;
- no evidence currently requires reclassifying any of the existing 12 CLASS-D items.

## 4. Controlled Decision Options

### Option A — Assign CLASS-A

Effect: broader research treatment subject to licensing/governance controls.

Gate concern: not supported by current evidence. No evidence demonstrates that broad implementation-level research is necessary or appropriate for these purchased OPL-1 modules.

### Option B — Assign CLASS-B

Effect: controlled functional/semantic learning with stronger access than black-box-only treatment.

Gate concern: would expand the current safe boundary. Additional license/legal rationale should be recorded before this option is used.

### Option C — Assign CLASS-C

Effect: formalizes the current safe interim treatment:

```text
observable behavior / metadata / documented capability only
NO source-body transfer
NO method/class/table/schema translation
NO vendor-specific implementation influence on target design
```

Evidence alignment: strongest alignment with the treatment already applied in Team A and EC-03 evidence.

### Option D — Assign CLASS-D

Effect: full quarantine pending explicit future ruling.

Use when governance/legal review concludes that even black-box/documented behavior should not be consumed by the research/design process.

## 5. Evidence-Gate Recommendation

**Recommendation for Boss consideration: Option C — CLASS-C**, strictly as a project clean-room control position and **not as legal advice**.

Rationale:

1. It matches the already-evidenced safe interim treatment.
2. It preserves the ability to understand observable capability without implementation transfer.
3. It does not require source-body access.
4. It keeps the new Node.js/TypeScript SMEsPlus Core independent from the purchased vendor implementation.
5. It avoids silently expanding the research boundary while still allowing business-behavior comparison.

This recommendation does not itself close EC-03.

## 6. Decision Effect

If Boss selects CLASS-C for both modules:

- current 1,504 source can receive complete A/B/C/D assignment at the classification layer;
- `DR-GAP-003` may move to evidence review for closure, subject to the row-level classification register being updated and independently verified;
- `DR-GAP-014` **remains OPEN** because independent legal/license sign-off is a separate control;
- EC-03 therefore remains at least `PASS WITH CONTROL / LEGAL HOLD` until the independent legal/license requirement is dispositioned.

If Boss selects CLASS-D:

- both modules join quarantine and remain excluded from source-body research;
- DR-GAP-003 can still be structurally resolved once the classification register is updated and verified;
- DR-GAP-014 remains separately open.

If Boss selects CLASS-A or CLASS-B:

- additional license/governance evidence should be attached before any access boundary is expanded.

## 7. Mandatory Non-Actions

Regardless of option:

- do not copy vendor code;
- do not translate vendor ORM/classes/methods/tables into target design;
- do not provide proprietary source details to the development team;
- do not alter the existing 12 CLASS-D quarantine without a separate ruling;
- do not treat a class decision as legal/license sign-off;
- do not close global DR9 or authorize build/release/deploy.

## 8. Boss Decision Record

```text
[ ] OPTION A — CLASS-A for both Ksolves modules
[ ] OPTION B — CLASS-B for both Ksolves modules
[ ] OPTION C — CLASS-C for both Ksolves modules (Evidence-Gate Recommendation)
[ ] OPTION D — CLASS-D / QUARANTINE for both modules
[ ] CUSTOM — item-by-item classification or other controlled ruling
```

Boss Decision: `PENDING`  
Decision Date: `TBD`  
Decision Evidence: `TBD`

`No Evidence = No Progress.`  
`Never Skip Gate.`