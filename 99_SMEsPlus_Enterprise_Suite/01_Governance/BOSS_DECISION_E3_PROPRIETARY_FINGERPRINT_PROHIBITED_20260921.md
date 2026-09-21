# Boss Decision — E3 Proprietary Fingerprint Prohibited

**Session:** `SMEPLUS-26-09-21-013`  
**Date:** 2026-09-21  
**Authority:** Boss  
**Status:** `BOSS APPROVED — BINDING`

## Decision

The proposed E3 control that would build or use a proprietary-source fingerprint / shingle corpus is **REJECTED and PROHIBITED**.

An Absolute Prohibition on proprietary Odoo source must not require reading, indexing, fingerprinting or shingling proprietary source in order to detect contamination.

## Binding E3 replacement

E3 becomes **COMMUNITY-ONLY CLEAN LINT**.

Allowed inputs:
- Canonical Community Master Register V1.xx
- authorized Odoo 19 Community source root
- source-neutral ROOM A deliverables
- compliance metadata and provenance records

Forbidden inputs:
- OEEL-1 source content
- OPL-1 source content
- unknown / non-allow-listed proprietary source content
- proprietary source fingerprints, shingles, embeddings, indexes, copied snippets or derivative corpora

Required behavior:
1. Fail on prohibited identifiers / source-derived implementation markers in ROOM B-bound deliverables.
2. Fail closed if the canonical Community register is unavailable after E5 activation.
3. Preserve existing lint self-tests.
4. Do not require proprietary text to prove proprietary text was not used.

## Verification at decision time

Current `clean_lint.py` in REV004:
- does **not** reference `addons_enterprise`
- points its source-text shingle mechanism at the authorized Community source root
- `--self-test` returns 0 and all 13 current controls pass
- still references the superseded `th_module_scope.tsv`, therefore **E5 remains open** until rebound to the Community Master Register V1.xx

This Boss decision closes E3 proprietary fingerprinting only. E1, E2, E4 and E5 continue under their existing governance states.
