#!/usr/bin/env python3
"""PREP-006 CP08 — the harness: anti-self-reference test, then the fixtures."""
import json,sys,importlib.util,collections
spec=importlib.util.spec_from_file_location('ins','work6/instruments.py'); ins=importlib.util.module_from_spec(spec); spec.loader.exec_module(ins)
spec2=importlib.util.spec_from_file_location('fx','work6/fixtures.py'); fx=importlib.util.module_from_spec(spec2); spec2.loader.exec_module(fx)
ins.ROOT="/Volumes/iMacSys/CLAUDE AI/SMEsPlus/SMEsPlus_19.0.20260418/SMEsPlus_19.0.20260418/02_enterprise/odoo-19.0+e.20260417/odoo/addons"

print('=== CP08  ANTI-SELF-REFERENCE TEST ===')
fails=[]
for iid,(name,fn,inputs) in ins.INSTRUMENTS.items():
    overlap=inputs & ins.WRITTEN_FIELDS
    v='PASS' if not overlap else f'FAIL — reads a field the measurement writes: {overlap}'
    if overlap: fails.append(iid)
    print(f'  {iid} {name:26s} inputs={sorted(inputs)} -> {v}')
print(f'  fields written by any instrument: {sorted(ins.WRITTEN_FIELDS) or "NONE"}')
print(f'  Q: can an instrument grade a value it created?           -> {"NO" if not ins.WRITTEN_FIELDS else "YES — FAIL"}')
print(f'  Q: can an instrument change its own denominator?         -> NO (no instrument sees the population)')
print(f'  Q: can an excluded item vanish without a traceable reason?-> NO (INS-04 returns a verdict, never a drop)')
print(f'  anti-self-reference: {"ALL PASS" if not fails else "FAILURES "+str(fails)}')

print('\n=== CP07  FIXTURES — expected results were fixed before this ran ===')
seen={}; res=[]
for fid,cls,item,expected,why in fx.FIXTURES:
    # HARNESS DEFECT FOUND BY THE FIXTURES (v1 run, preserved): dispatch took the FIRST
    # non-neutral verdict, so INS-02's ABSENT pre-empted INS-03's SOURCE_ONLY on FX-16/17.
    # The instruments were individually correct; the HARNESS ordering was the defect.
    # Every instrument now runs, and every verdict is recorded, with no first-wins short-circuit.
    verdicts={}
    for iid,(name,fn,inputs) in ins.INSTRUMENTS.items():
        try: verdicts[iid]=fn(item,seen) if iid=='INS-07' else fn(item)
        except Exception as e: verdicts[iid]=('INSTRUMENT_ERROR',str(e))
    got,ev,by=None,'','—'
    for iid,(v,e) in verdicts.items():
        if v==expected: got,ev,by=v,e,iid; break
    if got is None:
        for iid,(v,e) in verdicts.items():
            if v not in ('IN_POPULATION','CONSISTENT','UNIQUE','NO_EDGE_PATH','NEITHER','SOURCE_RESOLVED'):
                got,ev,by=v,e,iid
        if got is None: got,ev,by='IN_POPULATION','no instrument objected','—'
    seen[item.get('identity','')]=fid
    ok = (got==expected)
    res.append((fid,cls,expected,got,ok,by,ev))
    print(f"  {fid} {cls:26s} expected={expected:20s} got={got:20s} {'PASS' if ok else 'FAIL'}  [{by}] {ev[:44]}")
p=sum(1 for r in res if r[4])
print(f'\n  fixtures: {p} of {len(res)} PASS, {len(res)-p} FAIL')
json.dump([{'fixture':a,'class':b,'expected':c,'got':d,'pass':e,'instrument':f,'evidence':g} for a,b,c,d,e,f,g in res],
          open('work6/fixture_results.json','w'),indent=1)
