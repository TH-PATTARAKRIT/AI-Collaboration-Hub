# 06 — GATE-06 B-37 REPAIR CLOSURE TEST

Timestamp: `2026-09-08T19:28+07:00`
Owner surface: P11 `490ccdd81a4fed79d36b7b9d3bbc25deedd597b4`
Verifier: ChatGPT GPT-5.6 Sol
Status: **PASS — RECOMMEND B-37 CLOSED**

## Defect under test

B-37 recorded that `P11_AUTO_RESUME_STATE.md` could instruct a successor to use superseded peer heads as live authority.

## Current control surface

`P11_AUTO_RESUME_STATE.md` now has a section explicitly titled current 2026-09-08 one-prompt final closure heads and instructs successors to use that table, not the lineage table.

Current moved peers:
- P06 `a533fe92d6f6855e0b362179403476520cc9aafa`
- P08 `ca577be42e6ba9535e1911dc0bad1dfab74a8aa8`
- P09 `ab8c0131c46e8154ad7efae18de2a54af2f17362`

The old CORR3 snapshot is struck and labelled LINEAGE ONLY / SUPERSEDED.

## Independent delta reproduction

The rebuilt final P11 instrument was executed twice with:
1. the historical CORR3 peer pins: P06 `1b018c1`, P08 `00ccd66`, P09 `4778792`;
2. the final peer pins above.

Observed:
- CORR3 UNION = **817**
- FINAL UNION = **825**
- added = **8**
- removed = **0**

This independently reproduces the owner-published movement `817 -> 825, +8, -0`; the pin swap was measured rather than silently applied.

All ten final pins independently resolved as substantive commits and ancestors of their declared branches.

## Verdict

The exact B-37 defect — current successor control pointing at superseded heads — is repaired and independently reproducible.

Recommendation: **B-37 CLOSED**.
