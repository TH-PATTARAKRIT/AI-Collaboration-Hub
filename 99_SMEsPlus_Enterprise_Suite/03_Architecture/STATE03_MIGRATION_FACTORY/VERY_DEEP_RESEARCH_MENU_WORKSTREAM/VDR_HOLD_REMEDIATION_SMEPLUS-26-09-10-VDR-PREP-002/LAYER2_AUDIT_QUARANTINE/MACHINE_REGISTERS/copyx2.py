#!/usr/bin/env python3
"""Parse a single-table pg_restore --data-only output into CSV. Same UNIT as copyx.py."""
import sys,csv
path=sys.argv[1]
cols=None; rows=[]; inblk=False
with open(path,encoding='utf-8',errors='replace') as fh:
    for line in fh:
        if not inblk:
            if line.startswith('COPY '):
                cols=line[line.index('(')+1:line.index(')')].replace('"','').split(', ')
                inblk=True
            continue
        if line.rstrip('\n')=='\\.': break
        rows.append(line.rstrip('\n').split('\t'))
if cols is None:
    print('NO COPY BLOCK',file=sys.stderr); sys.exit(2)
w=csv.writer(sys.stdout); w.writerow(cols)
for r in rows: w.writerow(r)
print(f'{path}: {len(rows)} rows',file=sys.stderr)
