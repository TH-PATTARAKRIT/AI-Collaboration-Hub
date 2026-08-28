# EC-01 — Source Identity & Integrity Verification

Session: `[SMEPLUS-26-08-28-DEEP-CD-001]`  
Decision Authority: Boss — Sole Final Approver  
Authorization: `DEC-DEEP-CD-003`  
Status: `ACTIVE / HOLD UNTIL EVIDENCE VERIFIED`

## Objective

Cryptographically and structurally identify the three current source archives before any claim of current-source coverage or progression to EC-02.

## Controlled Inputs

| Source ID | Artifact | Intake Status | Current Verification |
|---|---|---|---|
| SRC-INT-001 | `01_ACCOUNT(1).zip` | RECEIVED | SHA-256 / member inventory pending |
| SRC-INT-002 | `02_OTHER(1).zip` | RECEIVED | SHA-256 / member inventory pending |
| SRC-INT-003 | `addons_extra(1).zip` | RECEIVED | SHA-256 / member inventory pending |

## Mandatory Evidence Per Archive

- SHA-256 digest
- byte size
- timestamp and version context
- archive member inventory
- archive member count
- manifest/module indicators where available
- evidence location
- owner
- verifier/reviewer
- verification timestamp
- verification status
- gate impact

## Current Evidence Position

The artifacts are recorded as received, but byte-level inspection is not yet available as inspectable evidence in the active execution runtime. Therefore no SHA-256 value, member count, module count, or current archive content claim is asserted in this record.

This is a controlled HOLD, not a failure and not progress completion.

## Gate Test

EC-01 PASS requires all three archives to be independently identifiable and reproducible from inspectable evidence. Receipt alone is insufficient.

## Downstream Dependency

EC-02 — Current Source Manifest + 66-Record Delta Reconciliation — is sequence-authorized but cannot be marked active/pass until EC-01 evidence is verified.

## Governance

- No Evidence = No Progress.
- Never Skip Gate.
- CLASS-D remains quarantined.
- No source implementation is transferred into target architecture.
- PR #62 remains Draft/Open/Not Merged.
