#!/usr/bin/env python3
"""Extract a COPY block from a plain PostgreSQL dump without a server.
POPULATION: the rows the dump itself carries. PATTERN: the COPY header line and its
column list, terminated by a lone '\\.'  UNIT: one row."""
import sys,io,csv
path,table=sys.argv[1],sys.argv[2]
want=f'COPY public.{table} '
cols=None; rows=[]
with open(path,encoding='utf-8',errors='replace') as fh:
    inblk=False
    for line in fh:
        if not inblk:
            if line.startswith(want):
                cols=line[line.index('(')+1:line.index(')')].replace('"','').split(', ')
                inblk=True
            continue
        if line.rstrip('\n')=='\\.':
            break
        rows.append(line.rstrip('\n').split('\t'))
if cols is None:
    print(f'TABLE NOT PRESENT IN DUMP: {table}',file=sys.stderr); sys.exit(2)
w=csv.writer(sys.stdout)
w.writerow(cols)
for r in rows: w.writerow(r)
print(f'{table}: {len(rows)} rows, {len(cols)} cols',file=sys.stderr)
