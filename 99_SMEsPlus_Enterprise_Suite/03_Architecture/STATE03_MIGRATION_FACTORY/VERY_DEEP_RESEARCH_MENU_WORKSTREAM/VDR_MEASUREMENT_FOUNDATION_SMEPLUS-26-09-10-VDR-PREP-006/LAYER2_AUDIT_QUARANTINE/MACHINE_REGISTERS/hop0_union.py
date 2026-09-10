#!/usr/bin/env python3
"""PREP-006 CP02/CP04 — HOP-0 CANONICAL POPULATION = the UNION of two logically independent
discovery methods, with the discovery method recorded per item.

An item found by only one method is NOT a defect in the other — it is the finding. Both
directions are reported.
"""
import json,collections,csv
S=json.load(open('work6/hop0_source.json'))
Rt=json.load(open('work6/hop0_runtime.json'))
DOM=set(S['domain_modules'])
# --- normalise both sides to (KIND, IDENTITY) -------------------------------------------
src=collections.defaultdict(list)
for k,m,i,p in S['entities']:
    if k.startswith('RECORD:'): k='DATA_RECORD'
    if k=='MODEL_EXTENSION': k='MODEL_EXTENSION'
    src[(k,i)].append((m,p))
def norm_runtime(kind,ident):
    """SECOND DEFECT CAUGHT BEFORE PUBLICATION: the two methods name the same thing in two
    different namespaces. Runtime names a field `<module>.field_<model_underscored>__<field>`
    and a model `<module>.model_<model_underscored>`; source names them `<model>.<field>` and
    `<model>`. Compared unnormalised they can NEVER match, and BOTH would read 0 — a perfect,
    entirely artefactual disagreement. Normalised here, with a control below."""
    _,_,local=ident.partition('.')
    if kind=='FIELD' and local.startswith('field_'):
        body=local[len('field_'):]
        if '__' in body:
            mdl,_,fld=body.rpartition('__')
            return mdl.replace('_','.')+'.'+fld
    if kind=='MODEL' and local.startswith('model_'):
        return local[len('model_'):].replace('_','.')
    if kind=='CONSTRAINT' and local.startswith('constraint_'):
        return local[len('constraint_'):]
    return ident

run=collections.defaultdict(list)
domain_models={i for (k,i) in src if k in ('MODEL','MODEL_EXTENSION')}
for key,deps in Rt['entities'].items():
    k,_,i=key.partition('|')
    if k=='FIELD_RT':
        # DEFECT CAUGHT BEFORE PUBLICATION: comparing "every field on a domain model" (runtime)
        # against "every field DECLARED BY a domain module" (source) compares two different
        # populations, and the resulting disagreement would be an artefact of the mismatch,
        # not a finding. Runtime fields are therefore matched to source ONLY through the
        # xmlid-attributed FIELD stream, which is the like-for-like population; the wider
        # set is retained separately as the domain's runtime field SURFACE.
        mdl=i.rsplit('.',1)[0]
        if mdl not in domain_models: continue
        k='FIELD_ON_DOMAIN_MODEL_ANY_OWNER'
    if k.startswith('RECORD:'): k='DATA_RECORD'
    run[(k,norm_runtime(k,i))].append(deps)
# CONTROL on the normaliser, drawn from the corpus: a runtime field identity must normalise
# onto a source identity that exists, and a fabricated one must not.
_ctl=[i for (k,i) in run if k=='FIELD' and (k,i) in src]
print(f'NORMALISER CONTROL: runtime FIELD identities that land on a source identity: {len(_ctl)}'
      f' | example {_ctl[0] if _ctl else "NONE — normaliser failed"}')
assert norm_runtime('FIELD','stock.field_stock_move__value')=='stock.move.value'
assert norm_runtime('FIELD','stock.zz_not_a_field')=='stock.zz_not_a_field'
keys=set(src)|set(run)
rows=[]
for (k,i) in sorted(keys):
    ins=(k,i) in src; inr=(k,i) in run
    method='BOTH' if (ins and inr) else ('SOURCE ONLY' if ins else 'RUNTIME ONLY')
    mod=src[(k,i)][0][0] if ins else (i.split('.',1)[0] if '.' in i else '')
    ptr=src[(k,i)][0][1] if ins else ''
    deps=sorted({d for ds in run.get((k,i),[]) for d in ds}) if inr else []
    rows.append({'kind':k,'identity':i,'module':mod,'discovery':method,
                 'source_pointer':ptr,'observed_on':';'.join(deps),'n_deployments':len(deps)})
with open('work6/HOP0_POPULATION.csv','w',newline='') as fh:
    w=csv.DictWriter(fh,fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
json.dump(rows,open('work6/HOP0_POPULATION.json','w'))
print(f'HOP-0 CANONICAL POPULATION: {len(rows)} entities')
print()
d=collections.Counter(r['discovery'] for r in rows)
for k,v in d.most_common(): print(f'   {v:7d}  {k}   ({100.0*v/len(rows):.1f}%)')
print()
print(f"{'KIND':22s}{'TOTAL':>8s}{'BOTH':>8s}{'SRC ONLY':>10s}{'RT ONLY':>9s}")
by=collections.defaultdict(lambda: collections.Counter())
for r in rows: by[r['kind']][r['discovery']]+=1
for k in sorted(by,key=lambda x:-sum(by[x].values())):
    c=by[k]; t=sum(c.values())
    print(f"{k:22s}{t:8d}{c['BOTH']:8d}{c['SOURCE ONLY']:10d}{c['RUNTIME ONLY']:9d}")
