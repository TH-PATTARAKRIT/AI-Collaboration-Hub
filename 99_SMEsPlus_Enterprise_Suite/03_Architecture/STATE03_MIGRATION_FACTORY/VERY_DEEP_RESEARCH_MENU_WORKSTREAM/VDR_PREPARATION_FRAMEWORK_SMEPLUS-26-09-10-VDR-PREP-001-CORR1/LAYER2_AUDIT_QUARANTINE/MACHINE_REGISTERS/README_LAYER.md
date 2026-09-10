# MACHINE_REGISTERS — layer declaration and reproduction instructions

**LAYER 2 — AUDIT QUARANTINE.** Every file in this directory carries reference-ERP identifiers and is
Boss / PMO / AI-Audit only. Nothing here may be transcribed onto a LAYER 1 surface.

Added after the SMEs Core independent challenge, which found (C-21) that the files in this directory
carried no layer declaration of their own and (C-18) that the shipped instruments could not be
re-executed because their intermediate inputs were not shipped.

## Reproduction order

```
python3 enum_menus.py        <R1> menus_R1_v19e.jsonl     # whole-root menu census
python3 enum_models.py       <R1> models_R1_v19e.json     # whole-root model-declaration census
python3 enum_fields_all.py   <R1> fields_all_R1.json      # whole-root field census
python3 enum_actions_all.py  <R1> actions_all_R1.json     # whole-root action census
#   derive inv_subtree_ids.json / inv_fam_final.json / inv_modset_final.json  (see 00B §1)
python3 enum_final.py        <R1>                         # domain surface -> F_*.jsonl
python3 build_population_v2.py <R1>                       # -> LEARNING_POPULATION.csv
python3 pmo_sweep.py         <package dir>                # four disjoint-unit integrity checks
```

`<R1>` is the absolute path of the adopted primary root, published in `00A_EVIDENCE_BASE_AND_PATH_SET.md` §4.

## Files

| File | What it is |
|------|-----------|
| `roots_v2.txt` / `roots_census_v2.txt` | the enumerated PATH SET (50 roots) and its generation census |
| `menus_R1_v19e.jsonl`, `models_R1_v19e.json`, `fields_all_R1.json`, `actions_all_R1.json` | whole-root censuses (intermediates) |
| `inv_subtree_ids.json`, `inv_fam_final.json`, `inv_modset_final.json`, `model_base.json` | the derived domain boundary |
| `F_*.jsonl` | the domain surface census, one file per element class |
| `LEARNING_POPULATION.csv` | the Source Learning Population, v2 |
| `hop2_resolution.json`, `serveraction_resolution.txt` | `SR-01` menu resolution |
| `gapinv02_resolution.txt`, `gapinv08_resolution.txt` | `SR-08` and `SR-10` traces |
| `MANIFEST_SHA256.json` | produced by `pmo_sweep.py`; hashes every file in the package |

## Known limitation of `pmo_sweep.py`

Check 1 treats a table cell beginning with an identifier as a definition, so `defined_twice`
over-reports. It is a screen, not an authority. Check 4 separates vendor tokens into a substring class
and a **word-boundary** class, because `quant` is a substring of the ordinary English word *quantity*
and matching it as a substring produced a false leak report on a clean LAYER 1 file.
