# ASSET DEEP RESEARCH CONTINUATION — LAYER, METHOD AND READING ORDER

Session: `SMEPLUS-26-09-04-ASSET-DR-CONT-001`
Date: 2026-09-04
Branch: `research/asset-deep-continuation-2026-09-04-001`
Repository: `TH-PATTARAKRIT/AI-Collaboration-Hub`
Scope: Level 7 → Level Final
Terminal state: see `25_ASSET_BOSS_FINAL_GATE_PACK.md`.

---

## Clean-room layer

**This whole folder is LAYER 2 — AUDIT QUARANTINE**, except one file.

- **Layer 2** — files `01`–`24`. Contain reference-ERP model names, field technical
  names, file paths and line references. Boss / PMO / AI-Audit only. **Must not be
  transcribed into any Team-B-facing package.**
- **Layer 1** — `25_ASSET_BOSS_FINAL_GATE_PACK.md`. Clean-room business learning, written
  with no vendor model, field, file or version tokens. **The only file cleared to seed
  downstream SMEsPlus design material.**

A mechanical clean-room scan of `25` was run at commit time against the token set
`odoo · mrp · account.asset · account.move · workcenter · maintenance.equipment ·
costs_hour · prorata · analytic · res.company · ir.rule · .py · fields. · stock. ·
product.template · enterprise · v18 · 18.0`. **Zero matches.**

## Method

1. **Reconciliation before research.** The blocker population was taken from repository
   evidence, not from the prompt's arithmetic. Two baseline documents disagreed; the
   disagreement is reported in `03` §2 rather than resolved by preference.
2. **Re-test, do not re-derive.** Inherited conclusions were re-tested from primary
   source. Four mechanism corrections were issued, with the superseded text quoted so a
   reviewer can audit the change rather than trust it (`02` §4).
3. **Source is authoritative; the UI is a hypothesis about source.** Where a custom
   module's construct appeared inert, the **platform core** was read to prove it, rather
   than inferring from version knowledge (`16` §3).
4. **Check before concluding.** One apparent High defect — a live file depending on names
   defined only in a dead file — was checked and found to be a superseded duplicate with
   a live replacement. The check was run before the view was formed, and the near-miss is
   recorded (`16` §3) because it is how a false finding is avoided.
5. **Statutory evidence at its own class.** Standard text is a requirement; the
   standard-setter's explanatory manual, which disclaims being part of the standard, is
   an interpretation. They are never merged.
6. **Negatives are bounded.** Every "does not exist" states that it is bounded by the
   source available in this workspace. The one query that would remove the bound is
   priority one in `22` §4.

## Evidence roots

| ID | Root | Type |
|---|---|---|
| `EV-CODE` | Reference ERP v18 Enterprise, build `18.0+e.20250608`, 797 modules | Primary source code |
| `EV-CUST` | Project custom addon set, v18 line, `equipment_sequence` v18.0.1.6 | Primary source code |
| `EV-PLAT` | The platform core of `EV-CODE` | Primary source code |
| `EV-LAW-2` | TAS 2 *สินค้าคงเหลือ*, standard text | Thai primary standard |
| `EV-LAW-16` | TFAC official explanatory manual, TAS 16 | Standard-setter publication |
| `EV-LAW-DBD` | DBD prescribed line items, แบบ 2 (บริษัทจำกัด) | Thai primary regulation |
| `EV-RT` | Runtime read-out of the pilot database, 2026-08-26 | Carried from the baseline, **not refreshed** |

Full index with the fields §7 requires: `23_ASSET_EVIDENCE_INDEX.md`.

## Declared limitations

1. **No runtime or database evidence was obtained this session.** The pilot system was
   unreachable; container access was refused by the execution environment and no network
   route exists in this workspace. Two blockers are held as a result and no substitute
   evidence was accepted (`01` §6).
2. **The AAS+ audit is a structured self-challenge**, not an independent review. No human
   and no separate agent has reviewed this package (`20`, head).
3. **TAS 16 rests on TFAC's manual**, not the standard text, which was located but not
   retrievable by this session's network path. The affected conclusions are
   down-classified (`18` §4).

## Reading order for Boss

1. `25_ASSET_BOSS_FINAL_GATE_PACK.md` — the consolidated pack. **Layer 1. Start here.**
2. `03_ASSET_BLOCKER_RECONCILIATION_REGISTER.md` — what closed, what opened, and why.
3. `09_PRODUCTIVE_NONPRODUCTIVE_ALLOCATION_MODEL.md` §2–§3 — the decision the gate needs.
4. `20_ASSET_AAS_PLUS_AUDIT.md` — the failure, the veto, and the findings against this
   research.
5. `17_ASSET_CONTRADICTION_REGISTER.md` and `22_ASSET_FINAL_BLOCKER_REGISTER.md`.

## Deliverable map

| # | File | Level |
|---|---|---|
| 00 | This file | — |
| 01 | Session control | — |
| 02 | Prior research lineage register | 7 |
| 03 | Blocker reconciliation register | 7 (§3) |
| 04 | Boss decision incorporation | 7 |
| 05 | Asset accounting forensic report | 8 |
| 06 | Equipment / maintenance forensic report | 9 |
| 07 | Work centre / operation / routing forensic report | 10 |
| 08 | Depreciation → manufacturing cost trace | 11 |
| 09 | Productive / non-productive allocation model | 11 |
| 10 | Post-depreciation internal usage model | 12 |
| 11 | Allocation driver decision matrix | 13 |
| 12 | Manufacturing cost classification matrix | 14 |
| 13 | Asset period close model | 15 |
| 14 | Multi-company / SaaS control | 16 |
| 15 | Edge case test matrix | 17 |
| 16 | Source code / database learning | 18 |
| 17 | Contradiction register | 19 |
| 18 | Thai accounting / statutory register | 20 |
| 19 | Clean-room architecture synthesis | 21 |
| 20 | AAS+ independent audit | 22 |
| 21 | PMO gate review | 23 |
| 22 | Final blocker register | 24 |
| 23 | Evidence index | 7, 18 |
| 24 | Traceability matrix | — |
| **25** | **Boss Final Gate Pack** | **Final — Layer 1** |
