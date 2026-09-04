import sys,io
def blocks(path):
    out={}
    cur=None; rows=[]
    for line in io.open(path,encoding='utf-8',errors='replace'):
        if cur is None:
            if line.startswith('COPY '):
                cur=line.split()[1]; rows=[]
        else:
            if line.startswith('\\.'):
                out[cur]=rows; cur=None
            else:
                rows.append(line.rstrip('\n').split('\t'))
    return out
for path in sys.argv[1:]:
    b=blocks(path)
    print("FILE",path)
    for t,rows in b.items():
        print("  TABLE",t,"ROWS",len(rows))
        if 'rel' in t and rows and len(rows[0])==2:
            accs={}; comps=set()
            for r in rows:
                comps.add(r[0]); accs[r[1]]=accs.get(r[1],0)+1
            # column order unknown; report both readings
            a2={}; c2=set()
            for r in rows:
                c2.add(r[1]); a2[r[0]]=a2.get(r[0],0)+1
            print("    reading A (col1=company,col2=account): companies",len(comps),"accounts",len(accs),"accounts in >1 company",sum(1 for v in accs.values() if v>1))
            print("    reading B (col1=account,col2=company): accounts",len(a2),"companies",len(c2),"accounts in >1 company",sum(1 for v in a2.values() if v>1))
