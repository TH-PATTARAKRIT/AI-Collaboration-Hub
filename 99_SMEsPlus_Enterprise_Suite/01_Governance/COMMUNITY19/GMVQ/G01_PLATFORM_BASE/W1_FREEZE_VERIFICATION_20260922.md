# GMVQ W1 Freeze Verification — 2026-09-22

**Scope:** G01 PLATFORM_BASE / Wave 1  
**Boss authority:** APPROVE ALL / standing rolling-freeze authorization  
**Status:** CONTROLLED FREEZE VERIFICATION

## W1 Standard Freeze

The uploaded `FREEZE_W1-STD.json` declares:
- 23 modules
- Standard Questions = 55
- module-specific floor = 40
- combined minimum research depth = 95
- freeze hash = `c64693eee3957388907637ad028ebdeea6fbeb19a093d1c459c5289f45f5c213`

Verification performed:
1. Reconstructed the exact Standard 55 bank bytes from the controlled file.
2. SHA-256 matched the manifest exactly: `f6726f111932aecce4432daf3e412d0c9de3291fa45fa8908e9e89ee79cb540d`.
3. Replayed the `freeze_batch.py` payload algorithm using batch ID `W1-STD`, the exact 23-module membership, filename and bank SHA-256.
4. Replayed freeze hash matched exactly: `c64693eee3957388907637ad028ebdeea6fbeb19a093d1c459c5289f45f5c213`.
5. Question-bank lint: PASS — exactly 55 unique Standard QIDs with disconfirming controls.

**Disposition:** `W1-STD = FROZEN / VERIFIED`.

## Rolling module freezes executed

- `W1-B01` = base + mail + web; 50 MVQ per module; freeze hash `558ec88047aef5c8e7ea0e2675b1c43ef358ec29b172d6878068330f3fba7177`.
- `W1-B02` = auth_signup + base_automation + bus; >=40 MVQ per module; freeze hash `cd966040f720456420057fe98fdb1176fbb9b0e85b456891f4dab82ea3ba0202`.

These rolling freezes authorize Lane A / Lane B to use the frozen QIDs for those batches. A change to a frozen question invalidates answers filed against that changed bank.

## Governance boundary

- Question counts are Minimum Research Depth controls, not Formal Coverage.
- `MODULE + QID` is Research Evidence Join Key only.
- Formal Coverage remains NOT AUTHORIZED until Canonical Function-ID denominator is Boss-frozen.
- No Evidence = No Progress.
