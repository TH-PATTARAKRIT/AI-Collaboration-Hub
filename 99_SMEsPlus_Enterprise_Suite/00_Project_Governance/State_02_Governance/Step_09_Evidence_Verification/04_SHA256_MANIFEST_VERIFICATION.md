# 04 — SHA-256 Manifest Verification (State 02 · Step 09 · reconciled · EV-03)

STATE02_VERIFICATION_TARGET_COMMIT: `9fa57fdc17f28906af503745b9291e54be7a2aa6`
Prepared By: Claude Code · 2026-07-14 (UTC) · Reviewer/Verifier: PENDING INDEPENDENT

---

## 1. Finalization package manifest (regenerated after EV-D06/D13/D16 corrections)

File: `STATE02_FINALIZATION/PACKAGE_MANIFEST_SHA256.txt` (blob `e805801f` @ target). Regenerated because
docs 03 (EV-D06), 05 (EV-D13 GI-70), and 17 (EV-D16) were edited.

```bash
$ cd .../STATE02_FINALIZATION
$ sha256sum -c <(grep -v '^#' PACKAGE_MANIFEST_SHA256.txt)
```
Result: **18 of 18 files OK** (docs 00–17). Header pins the reconciled target by name
(`STATE02_VERIFICATION_TARGET_COMMIT`) and points to where the full 40-char SHA is recorded (this package
`03` + PR #29 description) — the manifest is contained within the target commit, so its own commit SHA is
recorded externally rather than self-referenced. **EV-D09** (manifest must pin the full target, not just
"PR head") is addressed: the moving "PR head" phrasing is removed; the full SHA is pinned in the Step 09
manifest (below) and in `03`.

## 2. This Step 09 package manifest (pinned to the target)

Header requirements met: `STATE02_VERIFICATION_TARGET_COMMIT` (full 40-char SHA), `STEP09_PACKAGE_BRANCH`,
Generated UTC, Algorithm SHA-256, Encoding UTF-8, Line Endings LF. Covers files 00–10; excludes itself.

Generate:
```bash
cd .../Step_09_Evidence_Verification
sha256sum 00_*.md 01_*.md 02_*.md 03_*.md 04_*.md 05_*.md 06_*.md 07_*.md 08_*.md 09_*.md 10_*.md \
  > PACKAGE_MANIFEST_SHA256.txt   # header prepended with the pinned target SHA
```
Producer recompute:
```bash
sha256sum -c <(grep -v '^#' PACKAGE_MANIFEST_SHA256.txt)
```
Producer result (recorded at commit + PR #29):
```text
MANIFEST CHECK COMPLETED
Producer Recompute: 11/11 matched
```

Claude Code does **not** state INDEPENDENTLY VERIFIED. Independent recompute (finalization 18/18 + Step 09
11/11) is reserved for the appointed Independent Evidence Verifier (doc 08 handoff).

Verification Status: **PENDING INDEPENDENT VERIFICATION.**
