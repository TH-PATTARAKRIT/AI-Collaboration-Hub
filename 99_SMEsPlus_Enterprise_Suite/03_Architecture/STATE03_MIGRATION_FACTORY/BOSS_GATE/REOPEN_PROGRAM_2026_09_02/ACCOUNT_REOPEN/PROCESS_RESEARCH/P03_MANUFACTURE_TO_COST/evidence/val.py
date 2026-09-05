import subprocess,re
from collections import Counter
D="/Users/admin/Downloads/iSMEs_2026-07-11_05-03-27.dump"
def tbl(t):
    p=subprocess.run(["pg_restore","-f","-","--data-only","-t",t,D],capture_output=True,text=True,errors="replace")
    hdr=None;rows=[]
    for l in p.stdout.splitlines():
        m=re.match(r'^COPY public\.'+t+r' \((.*?)\) FROM stdin;',l)
        if m: hdr=[c.strip() for c in m.group(1).split(',')];continue
        if hdr is not None:
            if l=='\\.':break
            rows.append(l.split('\t'))
    return hdr,rows
hs,sm=tbl("stock_move"); I=lambda n:hs.index(n)
hv,svl=tbl("stock_valuation_layer"); J=lambda n:hv.index(n)
print("=== CP-P03R01b  DOES MATERIAL COST REACH THE MOs? ===")
print("stock_move rows:",len(sm),"| stock_valuation_layer rows:",len(svl))
print("SVL columns:",hv)
fin=[r for r in sm if r[I('production_id')]!='\\N']
raw=[r for r in sm if r[I('raw_material_production_id')]!='\\N']
print("finished moves (production_id set):",len(fin))
print("raw moves (raw_material_production_id set):",len(raw))
print("  finished done:",sum(1 for r in fin if r[I('state')]=='done'))
print("  raw done     :",sum(1 for r in raw if r[I('state')]=='done'))
# SVL -> move linkage
mv=J('stock_move_id') if 'stock_move_id' in hv else None
if mv is not None:
    svl_by_move={}
    for r in svl:
        k=r[mv]
        if k!='\\N': svl_by_move.setdefault(k,[]).append(r)
    finids={r[I('id')] for r in fin if r[I('state')]=='done'}
    rawids={r[I('id')] for r in raw if r[I('state')]=='done'}
    fh=finids & set(svl_by_move); rh=rawids & set(svl_by_move)
    print(f"  done FINISHED moves WITH an SVL: {len(fh)} / {len(finids)}")
    print(f"  done RAW      moves WITH an SVL: {len(rh)} / {len(rawids)}")
    vi=J('value')
    fv=sum(float(x[vi]) for k in fh for x in svl_by_move[k] if x[vi]!='\\N')
    rv=sum(float(x[vi]) for k in rh for x in svl_by_move[k] if x[vi]!='\\N')
    print(f"  TOTAL value on finished-move SVLs : {fv:,.2f}")
    print(f"  TOTAL value on raw-move SVLs      : {rv:,.2f}")
    print(f"  SUM (should be ~0 if FG value == material consumed): {fv+rv:,.2f}")
    nz=[k for k in fh if any(x[vi]!='\\N' and float(x[vi])!=0 for x in svl_by_move[k])]
    print(f"  done finished moves with NON-ZERO SVL value: {len(nz)}")
