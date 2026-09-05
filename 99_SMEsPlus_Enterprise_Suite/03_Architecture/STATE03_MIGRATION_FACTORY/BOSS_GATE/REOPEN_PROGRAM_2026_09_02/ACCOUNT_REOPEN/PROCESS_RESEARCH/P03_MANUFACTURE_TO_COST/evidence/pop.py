import subprocess,re
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
h,mo=tbl("mrp_production")
i=lambda n:h.index(n)
from collections import Counter
print("=== CP-P03R01  MO POPULATION (iSMEs) ===")
print("total MO rows:",len(mo))
print("states:",dict(Counter(r[i('state')] for r in mo)))
print("companies on MOs:",dict(Counter(r[i('company_id')] for r in mo)))
dates=[r[i('date_start')][:7] for r in mo if r[i('date_start')]!='\\N']
print("date_start range:",min(dates) if dates else None,"->",max(dates) if dates else None)
done=[r for r in mo if r[i('state')]=='done']
print("DONE MOs:",len(done))
print("  cols present:", [c for c in ('extra_cost','product_id','qty_produced','bom_id') if c in h])
# bom linkage
if 'bom_id' in h:
    print("  DONE MOs with a BOM:",sum(1 for r in done if r[i('bom_id')]!='\\N'))
