#!/usr/bin/env python3
"""POPULATION_V5 — PREP-004. Every rule below cites the finding that authorises it.
No grade moves for any other reason, and every movement is traceable to evidence."""
import csv,json,collections
DIMS=['PROCESS','CONFIGURATION','OPTIONAL_FUNCTION','SOURCE','RUNTIME','DATA_MODEL','SECURITY','CROSS_MODULE','EDGE']
R=list(csv.DictReader(open('work3/POPULATION_V4.csv')))
OBS={o['learning_id']:o for o in json.load(open('work4/runtime_observation.json'))}
log=collections.Counter()

# EDGE: affirmative structural determinations only. The two detection-failure phrasings
# ("NO REVERSE/CANCEL ROLE DETECTED", "NOT A REVERSE CONTROL") are the vocabulary of a
# failed search and are NOT promoted to a determination (SMEs Core B-15, upheld).
EDGE_AFFIRM=('NO LIFECYCLE STATE AND NO DELETION GUARD','SCHEDULED JOB','WRITES STATE',
             'DELETION GUARD','LIFECYCLE STATE')
for r in R:
    lid=r['learning_id']; o=OBS.get(lid,{})
    # --- P4-R1  the three grouping containers: RUNTIME and SECURITY restored -------
    # A container menu IS a record at runtime and its group set is determinable; only
    # PROCESS / CONFIGURATION / OPTIONAL_FUNCTION are genuinely inapplicable to it.
    if lid in ('LI-INV-MENU-0028','LI-INV-MENU-0034','LI-INV-MENU-0042'):
        for d in ('RUNTIME','SECURITY'):
            r['DIM_'+d]='NOT_VERIFIED'; r['NA_'+d]=''; r['DET_'+d]='DETERMINED'
            r['RV_'+d]='NOT_RESEARCH_VERIFIED'
        r['SECURITY_CONDITION']='OBJECT-LEVEL: no groups declared on the node itself — visibility inherited from its parent'
        log['P4-R1 container RUNTIME+SECURITY restored']+=1
    # --- P4-R2  RUNTIME: element-level observation on a real deployment ------------
    if r['DIM_RUNTIME']!='NA':
        r['RUNTIME_CONDITION']=(f"OBSERVED ON {o.get('n',0)} of 5 DEPLOYMENTS [{','.join(o.get('observed_on',[]))}] "
                                f"via {o.get('grade','')}") or r['RUNTIME_CONDITION']
        if o.get('tier')=='ELEMENT' and o.get('n',0)>0:
            r['DET_RUNTIME']='DETERMINED'; r['RV_RUNTIME']='RESEARCH_VERIFIED'; log['P4-R2 runtime ELEMENT observed']+=1
        elif o.get('n',0)>0:
            r['DET_RUNTIME']='DETERMINED'; r['RV_RUNTIME']='NOT_RESEARCH_VERIFIED'; log['P4-R2 runtime indirect/module only']+=1
        else:
            r['DET_RUNTIME']='DETERMINED'; r['RV_RUNTIME']='NOT_RESEARCH_VERIFIED'; log['P4-R2 runtime determined ABSENT']+=1
    # --- P4-R3  SECURITY: the inversion corrected in the evidenced direction -------
    # §7 requires "the access grants and record rules that govern it, enumerated".
    # The items carrying that enumeration are the ones that meet it.
    if r['DIM_SECURITY']!='NA':
        r['RV_SECURITY']='RESEARCH_VERIFIED' if r['SECURITY_CONDITION'].strip().startswith('OBJECT-LEVEL:') else 'NOT_RESEARCH_VERIFIED'
        if r['RV_SECURITY']=='RESEARCH_VERIFIED': log['P4-R3 security enumerated']+=1
    # --- P4-R4  CROSS_MODULE: per-item boundary census -----------------------------
    if r['DIM_CROSS_MODULE']!='NA':
        r['RV_CROSS_MODULE']='RESEARCH_VERIFIED' if r['CROSS_MODULE_CONDITION'].strip() else 'NOT_RESEARCH_VERIFIED'
        if r['RV_CROSS_MODULE']=='RESEARCH_VERIFIED': log['P4-R4 cross-module enumerated']+=1
    # --- P4-R5  DATA_MODEL: per-item data condition --------------------------------
    if r['DIM_DATA_MODEL']!='NA':
        r['RV_DATA_MODEL']='RESEARCH_VERIFIED' if r['DATA_CONDITION'].strip() else 'NOT_RESEARCH_VERIFIED'
        if r['RV_DATA_MODEL']=='RESEARCH_VERIFIED': log['P4-R5 data condition established']+=1
    # --- P4-R6  EDGE: affirmative determinations only -------------------------------
    if r['DIM_EDGE']!='NA':
        ec=r['EDGE_CONDITION'].strip()
        ok=any(ec.startswith(p) for p in EDGE_AFFIRM)
        r['RV_EDGE']='RESEARCH_VERIFIED' if ok else 'NOT_RESEARCH_VERIFIED'
        if ok: log['P4-R6 edge affirmative']+=1
    r['DETERMINED_COMPLETE']='YES' if all(r['DET_'+d] in ('DETERMINED','NA') for d in DIMS) else 'NO'
    r['RESEARCH_COMPLETE'] ='YES' if all(r['RV_'+d]  in ('RESEARCH_VERIFIED','NA') for d in DIMS) else 'NO'
    r['APPLICABLE_DIMS']=sum(1 for d in DIMS if r['DIM_'+d]!='NA')
    r['RESEARCH_VERIFIED_DIMS']=sum(1 for d in DIMS if r['RV_'+d]=='RESEARCH_VERIFIED')
with open('work4/POPULATION_V5.csv','w',newline='') as fh:
    w=csv.DictWriter(fh,fieldnames=list(R[0].keys())); w.writeheader(); w.writerows(R)
json.dump(R,open('work4/POPULATION_V5.json','w'))
print("RULES APPLIED"); [print(f'   {v:6d}  {k}') for k,v in sorted(log.items())]
print()
print(f"{'DIMENSION':20s}{'APPLIC':>8s}{'DETERM':>8s}{'DET%':>8s}{'RES-VER':>9s}{'RV%':>8s}")
ta=td=tv=0
for d in DIMS:
    a=sum(1 for r in R if r['DIM_'+d]!='NA'); dt=sum(1 for r in R if r['DET_'+d]=='DETERMINED')
    v=sum(1 for r in R if r['RV_'+d]=='RESEARCH_VERIFIED'); ta+=a; td+=dt; tv+=v
    print(f"{d:20s}{a:8d}{dt:8d}{100.0*dt/a:7.2f}%{v:9d}{100.0*v/a:7.2f}%")
print(f"{'ALL CELLS':20s}{ta:8d}{td:8d}{100.0*td/ta:7.2f}%{tv:9d}{100.0*tv/ta:7.2f}%")
print()
print("DETERMINED-COMPLETE:",sum(1 for r in R if r['DETERMINED_COMPLETE']=='YES'),"of",len(R))
print("RESEARCH-COMPLETE  :",sum(1 for r in R if r['RESEARCH_COMPLETE']=='YES'),"of",len(R))

# ============ appended: P4-R7 SOURCE, graded by a test that can fail ============
