# ROOMA_RECON / lane_b — RED TEAM repository intake — 2026-09-26
**SMEsPlus Enterprise Suite · ROOM A · STATE03 · Lane B (Gemini) audit**
Session ID: SMEPLUS-26-09-26-RTB-001 (assigned by RED TEAM under Boss item-4 approval; Boss may re-number) · STEP/Prompt: NOT ASSIGNED (ROOM A work-package)
Status: **PREPARED ONLY — READY FOR OWNER REVIEW** · not Boss Final Approval · no merge authorized
Branch: `lane-b/intake-20260926-001` from `origin/SMEsPlus` @ 9f338b8e

## What this is
A faithful copy of `~/ROOMB_WORKSPACE` on the RED TEAM Mac as of 2026-09-26 11:20 Asia/Bangkok — the Lane B
workspace (collectors, ops scripts, batch W1-STD, menu-tree census W1-SCREENS, reports, superseded versions).
Nothing in the 25–26 Sep Lane B programme was in the repository before this intake.

## What is deliberately NOT here
- `credentials/` (observer password file, mode 600) — never enters a repository.
- `__pycache__/`, `*.pyc`, `.DS_Store`.
- `batches/W1-SCREENS/screens/`, `raw/` — empty at intake (Stage 2 not started).

## What was altered in the copy (and only in the copy)
- `RUN_REPORT.txt`, `reports/RUN_20260926_0249.txt`: install paths of the reference runtime replaced by `<REDACTED_PATH>` (clean-room hygiene, HYG-001). Originals on the Mac untouched.
- Scripts (`*.py`, `*.sh`) are unchanged: they carry the scrub *patterns* and, in `ops/grant_laneb_via_odoo_shell.sh` / `ops/create_census_account_via_odoo_shell.sh`, launcher candidate paths on the study server. Disclosed, not hidden.
- `EVIDENCE_20260926.txt` (outgoing session) lists Mac paths of module manifests found by the NO-SOURCE scan. Kept as evidence; Boss may order a scrub commit.

## Integrity
`MANIFEST.sha256` covers every file in this folder except itself. Verify: `shasum -a 256 -c MANIFEST.sha256`.
Frozen references: installed-set hash `706e6df4008e0bac042a9821507ec0bc6868c4d9f98bcb93004a2535b1ca3c89` (299 modules, verified 26 Sep 11:08) ·
menu tree `c5d68d14e4a59cb46fb448a8ad5cbfd6537c5cf9f159684d7d70eec6bb5dee7d` (681 menus / 492 leaf screens, reproduced 3× on 26 Sep).

## Pointers
Session record: Claude Project `claude/REDTEAM_LANEB_SESSION_RECORD_SMEPLUS-26-09-26.md` ·
Decision package: `reports/RT-SEC-003_DECISION_PACKAGE_V1.00.md` (BOSSDEC-003 A–E approved 26 Sep, implementation pending one line — see session record) ·
Register: `reports/RT_REGISTER_LANEB_20260926.md`.

```
Governance: repository intake only. Not Boss Final Approval. No gate closure, merge, release or STATE closure is claimed.
```
