#!/usr/bin/env python3
"""POPULATION_V4 — apply the SMEs Core challenge corrections to V3.
Every rule below is traceable to a challenge finding; no figure moves for any other reason."""
import csv,json,collections
DIMS=['PROCESS','CONFIGURATION','OPTIONAL_FUNCTION','SOURCE','RUNTIME','DATA_MODEL','SECURITY','CROSS_MODULE','EDGE']
rows=list(csv.DictReader(open('work3/POPULATION_V3.csv')))
log=collections.Counter()

for r in rows:
    ident=r['identity']; meth=ident.split('::')[-1]
    # --- R1  restore the 180 off-table NA cells (A-01/B-02/C-01) ------------
    if r['class']=='BUTTON' and r['DIM_PROCESS']=='NA':
        r['DIM_PROCESS']='NOT_VERIFIED'; r['NA_PROCESS']=''
        if meth in ('None','cancel_button'):
            # B-03: the exclusion reason was FALSE. These are framework discard
            # controls declared INSIDE the domain; no method executes anywhere.
            r['DET_PROCESS']='DETERMINED'; r['RV_PROCESS']='NOT_RESEARCH_VERIFIED'
            r['PROCESS_CONDITION']=('FRAMEWORK DISCARD CONTROL — declared in a domain module with '
                'special="cancel"; no method executes in this or any domain (corrected: the prior '
                'reason "belongs to another domain" was false against source)')
            log['R1a_button_reason_corrected']+=1
        else:
            r['DET_PROCESS']='NOT_DETERMINED'; r['RV_PROCESS']='NOT_RESEARCH_VERIFIED'
            log['R1b_button_genuinely_external']+=1
    if r['class']=='MENUX' and r['DIM_PROCESS']=='NA':
        r['DIM_PROCESS']='NOT_VERIFIED'; r['NA_PROCESS']=''
        r['DET_PROCESS']='NOT_DETERMINED'; r['RV_PROCESS']='NOT_RESEARCH_VERIFIED'
        log['R1c_menux_process_restored']+=1
    if r['class']=='HANDOFF' and r['DIM_RUNTIME']=='NA':
        r['DIM_RUNTIME']='NOT_VERIFIED'; r['NA_RUNTIME']=''
        r['DET_RUNTIME']='NOT_DETERMINED'; r['RV_RUNTIME']='NOT_RESEARCH_VERIFIED'
        log['R1d_handoff_runtime_restored']+=1
    # --- R2  class-constant grades are not depth (A-05/B-05/B-06/B-07) -----
    for d,reason in (('SOURCE','unconditional literal, no per-item test'),
                     ('DATA_MODEL','class constant'),('CROSS_MODULE','class constant')):
        if r['RV_'+d]=='RESEARCH_VERIFIED':
            r['RV_'+d]='NOT_RESEARCH_VERIFIED'; log['R2_'+d]+=1
    # --- R3  SECURITY grade is inverted (B-06) -----------------------------
    if r['RV_SECURITY']=='RESEARCH_VERIFIED':
        r['RV_SECURITY']='NOT_RESEARCH_VERIFIED'; log['R3_security_retracted']+=1
    # --- R4  RUNTIME: drop items installed on no deployment (A-06/B-08) ----
    if r['RV_RUNTIME']=='RESEARCH_VERIFIED' and r['reachability'].startswith('OPTIONAL MODULE DEPENDENT'):
        r['RV_RUNTIME']='NOT_RESEARCH_VERIFIED'; log['R4_runtime_never_installed']+=1
    # --- R5  EDGE numerator was a hardcoded identity list (B-15) -----------
    if r['RV_EDGE']=='RESEARCH_VERIFIED':
        r['RV_EDGE']='NOT_RESEARCH_VERIFIED'; log['R5_edge_retracted']+=1
    # --- R6  PROCESS 17: no facet payload, graded off a 63-row status (A-12)
    if r['RV_PROCESS']=='RESEARCH_VERIFIED':
        r['RV_PROCESS']='NOT_RESEARCH_VERIFIED'; log['R6_process_retracted']+=1
    # --- R7  the three container menus (C-09) ------------------------------
    if r['learning_id'] in ('LI-INV-MENU-0028','LI-INV-MENU-0034','LI-INV-MENU-0042'):
        for d in ('PROCESS','CONFIGURATION','OPTIONAL_FUNCTION','RUNTIME','SECURITY'):
            r['DIM_'+d]='NA'; r['DET_'+d]='NA'; r['RV_'+d]='NA'
            r['NA_'+d]='grouping container — invokes nothing (kind=CONTAINER in its own detail field)'
        log['R7_containers_corrected']+=1
    # --- R8  degenerate columns removed (A-09/C-06) ------------------------
    r['DETERMINED_COMPLETE']='YES' if all(r['DET_'+d] in ('DETERMINED','NA') for d in DIMS) else 'NO'
    r['RESEARCH_COMPLETE'] ='YES' if all(r['RV_'+d]  in ('RESEARCH_VERIFIED','NA') for d in DIMS) else 'NO'
    r.pop('FUNCTION_COMPLETE',None); r.pop('VERIFIED_DIMS',None); r.pop('APPLICABLE_DIMS',None)
    r['APPLICABLE_DIMS']=sum(1 for d in DIMS if r['DIM_'+d]!='NA')
    r['RESEARCH_VERIFIED_DIMS']=sum(1 for d in DIMS if r['RV_'+d]=='RESEARCH_VERIFIED')

with open('work3/POPULATION_V4.csv','w',newline='') as fh:
    w=csv.DictWriter(fh,fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
json.dump(rows,open('work3/POPULATION_V4.json','w'))

print("CORRECTIONS APPLIED"); [print(f"   {v:6d}  {k}") for k,v in sorted(log.items())]
print()
print(f"{'DIMENSION':20s}{'APPLIC':>8s}{'DETERM':>8s}{'DET%':>8s}{'RES-VER':>9s}{'RV%':>8s}")
ta=td=tv=0
for d in DIMS:
    a=sum(1 for r in rows if r['DIM_'+d]!='NA')
    dt=sum(1 for r in rows if r['DET_'+d]=='DETERMINED')
    v=sum(1 for r in rows if r['RV_'+d]=='RESEARCH_VERIFIED')
    ta+=a; td+=dt; tv+=v
    print(f"{d:20s}{a:8d}{dt:8d}{100.0*dt/a:7.2f}%{v:9d}{100.0*v/a:7.2f}%")
print(f"{'ALL CELLS':20s}{ta:8d}{td:8d}{100.0*td/ta:7.2f}%{tv:9d}{100.0*tv/ta:7.2f}%")
print()
print("DETERMINED-COMPLETE items:",sum(1 for r in rows if r['DETERMINED_COMPLETE']=='YES'),"of",len(rows))
print("RESEARCH-COMPLETE items  :",sum(1 for r in rows if r['RESEARCH_COMPLETE']=='YES'),"of",len(rows))
print("Overall Verified Coverage:",f"{100.0*sum(1 for r in rows if r['RESEARCH_COMPLETE']=='YES')/len(rows):.2f}%")
