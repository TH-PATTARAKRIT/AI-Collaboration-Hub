#!/usr/bin/env python3
"""PREP-003 Checkpoint 01/02 — replace the single ordinal research_status with NINE
INDEPENDENT DIMENSION COLUMNS, so that Function-Complete becomes computable (CORR-F-38).

Each dimension takes one of: VERIFIED | NOT_VERIFIED | NA
NA requires an explicit reason recorded in the same row (§5: unknown != N/A).

APPLICABILITY is decided by a DECLARED RULE TABLE keyed on Learning Item class — not per row.
"""
import json,csv,collections,os
W='../work/'
P=json.load(open(W+'LEARNING_POPULATION.json'))
def det(r):
    try: return json.loads(r['detail'])
    except Exception: return {}

DIMS=['PROCESS','CONFIGURATION','OPTIONAL_FUNCTION','SOURCE','RUNTIME','DATA_MODEL',
      'SECURITY','CROSS_MODULE','EDGE']

# ---- DECLARED APPLICABILITY RULE TABLE (class -> dimension -> applicable?) ----
# A dimension is NA for a class when the class cannot, by its nature, carry that dimension.
A = {   # PROCESS CONFIG OPTION SOURCE RUNTIME DATA SECURITY XMOD EDGE
 'MENU'      :(1,1,1,1,1,0,1,0,0),
 'MENUX'     :(1,1,1,1,1,0,1,0,0),
 'ACTION'    :(1,1,1,1,1,0,1,0,0),
 'VIEW'      :(0,1,1,1,1,0,1,0,0),
 'BUTTON'    :(1,1,1,1,1,0,1,0,1),
 'FIELD'     :(0,1,1,1,1,1,1,1,0),
 'SETTING'   :(0,1,1,1,1,1,0,1,0),
 'AUTOMATION':(1,1,1,1,1,1,0,1,1),
 'BEHAVIOUR' :(1,0,0,1,1,1,0,1,1),
 'CONSTRAINT':(0,0,0,1,1,1,0,0,0),
 'RULE'      :(0,0,0,1,1,0,1,0,0),
 'ACL'       :(0,0,0,1,1,0,1,0,0),
 'GROUP'     :(0,1,1,1,1,0,1,0,0),
 'SEQUENCE'  :(0,1,0,1,1,1,0,0,0),
 'SYSPARAM'  :(0,1,1,1,1,0,0,0,0),
 'OBJECT'    :(1,1,1,1,1,1,1,1,1),
 'GATEDELEM' :(0,1,1,1,1,0,1,0,0),
 'HANDOFF'   :(0,0,0,1,1,0,0,1,0),
}
NA_REASON={
 'PROCESS':'the class is a declaration, not an invocable behaviour',
 'CONFIGURATION':'the class carries no configuration condition',
 'OPTIONAL_FUNCTION':'the class cannot be optionally activated independently of its module',
 'DATA_MODEL':'the class holds no data of its own',
 'SECURITY':'the class carries no access-control surface of its own',
 'CROSS_MODULE':'the class has no cross-boundary relation of its own',
 'EDGE':'the class has no lifecycle and therefore no reverse/cancel/return path',
}

# ---- EVIDENCE SETS actually held ----
gated={r['learning_id'] for r in P if det(r).get('groups')}
gated|={r['learning_id'] for r in P if r['class']=='GATEDELEM'}
tog_classified={r['learning_id'] for r in P if r['class']=='SETTING'}
opt_resolved={r['learning_id'] for r in P if r['class']=='SETTING' and det(r).get('implied_group')}
opt_resolved|={r['learning_id'] for r in P if r['class']=='SETTING' and str(r['identity']).startswith('config.module_')}
S4={r['learning_id'] for r in P if r['research_status']=='S4_FUNCTION_VERIFIED'}
elem_obs={r['learning_id'] for r in P if r['reachability'].startswith(('RUNTIME REACHABLE','OPTIONAL MODULE DEPENDENT'))}
mod_inf={r['learning_id'] for r in P if r['reachability'].startswith('MODULE ')}
unmeas={r['learning_id'] for r in P if r['reachability'].startswith('UNMEASURED')}
# data/model evidence: fields carry type+attrs; objects carry base class; constraints carry detail
data_ok={r['learning_id'] for r in P if r['class'] in ('FIELD','CONSTRAINT','OBJECT','SEQUENCE') and det(r)}
data_ok|={r['learning_id'] for r in P if r['class']=='SETTING' and (det(r).get('related') or det(r).get('config_parameter') or det(r).get('implied_group'))}
sec_ok={r['learning_id'] for r in P if r['class'] in ('RULE','ACL','GROUP')}
sec_ok|=gated
xmod_ok={r['learning_id'] for r in P if r['class']=='HANDOFF'}
xmod_ok|={r['learning_id'] for r in P if r['class']=='FIELD' and det(r).get('related')}
edge_ok=set()   # only the two objects whose reversibility was established
for r in P:
    if r['class']=='OBJECT' and r['identity'] in ('stock.scrap','mrp.unbuild'): edge_ok.add(r['learning_id'])

rows=[]
for r in P:
    cls=r['class']; app=A[cls]; lid=r['learning_id']
    out=dict(r)
    for k,dim in enumerate(DIMS):
        if not app[k]:
            out['DIM_'+dim]='NA'; out['NA_'+dim]=NA_REASON.get(dim,'not applicable to this class')
            continue
        out['NA_'+dim]=''
        if dim=='SOURCE': v='VERIFIED'
        elif dim=='RUNTIME':
            v='VERIFIED' if (lid in elem_obs or lid in mod_inf) else 'NOT_VERIFIED'
        elif dim=='CONFIGURATION':
            v='VERIFIED' if (lid in gated or lid in tog_classified) else 'NOT_VERIFIED'
        elif dim=='OPTIONAL_FUNCTION':
            v='VERIFIED' if lid in opt_resolved else 'NOT_VERIFIED'
        elif dim=='PROCESS': v='VERIFIED' if lid in S4 else 'NOT_VERIFIED'
        elif dim=='DATA_MODEL': v='VERIFIED' if lid in data_ok else 'NOT_VERIFIED'
        elif dim=='SECURITY': v='VERIFIED' if lid in sec_ok else 'NOT_VERIFIED'
        elif dim=='CROSS_MODULE': v='VERIFIED' if lid in xmod_ok else 'NOT_VERIFIED'
        elif dim=='EDGE': v='VERIFIED' if lid in edge_ok else 'NOT_VERIFIED'
        out['DIM_'+dim]=v
    # FUNCTION_COMPLETE = every APPLICABLE dimension VERIFIED
    out['FUNCTION_COMPLETE']='YES' if all(out['DIM_'+d] in ('VERIFIED','NA') for d in DIMS) else 'NO'
    out['APPLICABLE_DIMS']=sum(1 for d in DIMS if out['DIM_'+d]!='NA')
    out['VERIFIED_DIMS']=sum(1 for d in DIMS if out['DIM_'+d]=='VERIFIED')
    rows.append(out)
cols=[c for c in rows[0].keys()]
with open('POPULATION_V3.csv','w',newline='') as fh:
    w=csv.DictWriter(fh,fieldnames=cols); w.writeheader(); w.writerows(rows)
json.dump(rows,open('POPULATION_V3.json','w'))
print('rows:',len(rows))
print()
print(f"{'DIMENSION':20s} {'APPLICABLE':>10s} {'VERIFIED':>9s} {'NOT_VER':>8s} {'NA':>6s} {'COVER%':>7s}")
for d in DIMS:
    a=sum(1 for r in rows if r['DIM_'+d]!='NA')
    v=sum(1 for r in rows if r['DIM_'+d]=='VERIFIED')
    n=sum(1 for r in rows if r['DIM_'+d]=='NOT_VERIFIED')
    na=sum(1 for r in rows if r['DIM_'+d]=='NA')
    print(f"{d:20s} {a:10d} {v:9d} {n:8d} {na:6d} {100*v/a if a else 0:6.2f}%")
fc=sum(1 for r in rows if r['FUNCTION_COMPLETE']=='YES')
print()
print(f'FUNCTION-COMPLETE items: {fc} of {len(rows)}  = {100*fc/len(rows):.2f}%')
tot=sum(r['APPLICABLE_DIMS'] for r in rows); ver=sum(r['VERIFIED_DIMS'] for r in rows)
print(f'DIMENSION-CELL coverage : {ver} of {tot} applicable cells = {100*ver/tot:.2f}%')
