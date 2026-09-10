#!/usr/bin/env python3
"""PREP-004 Checkpoint 01 — locate PostgreSQL dump artefacts BY FORMAT, not by extension.
Declared PATH SET: $HOME (including ~/Library, declared separately) + every /Volumes entry.
Declared PATTERN: first 5 bytes == b'PGDMP' (custom/directory/tar archive header)
                  OR first 512 bytes contain b'PostgreSQL database dump' (plain SQL)
Declared UNIT: one file.
Positive control: a synthetic PGDMP file written into the scan set must be found."""
import os,sys,json
ROOTS=[os.path.expanduser('~')]+[os.path.join('/Volumes',d) for d in sorted(os.listdir('/Volumes'))]
SKIP_NAMES={'.git','node_modules','.venv','__pycache__','.Trash','Caches','.cache'}
out=[];scanned=0;errs=0;skipped_symlink=0
# positive control
import tempfile
ctl=os.path.join(tempfile.gettempdir(),'PREP004_POSCTL.dump')
open(ctl,'wb').write(b'PGDMP'+b'\x00'*64)
ROOTS.append(tempfile.gettempdir())
seen=set()
for root in ROOTS:
    if not os.path.isdir(root): continue
    if os.path.islink(root): skipped_symlink+=1; print(f"SKIP symlink root {root}",file=sys.stderr); continue
    for dp,dn,fns in os.walk(root,followlinks=False):
        dn[:]=[d for d in dn if d not in SKIP_NAMES]
        for fn in fns:
            p=os.path.join(dp,fn)
            try:
                st=os.lstat(p)
                if not os.path.isfile(p) or os.path.islink(p): continue
                if st.st_size<1024: continue
                rp=os.path.realpath(p)
                if rp in seen: continue
                seen.add(rp)
                scanned+=1
                with open(p,'rb') as fh: head=fh.read(512)
                if head[:5]==b'PGDMP':
                    out.append({'path':p,'size':st.st_size,'fmt':'PGDMP','mtime':st.st_mtime})
                elif b'PostgreSQL database dump' in head:
                    out.append({'path':p,'size':st.st_size,'fmt':'PLAIN','mtime':st.st_mtime})
            except (PermissionError,OSError): errs+=1
json.dump({'roots':ROOTS,'scanned':scanned,'unreadable':errs,'symlink_roots_skipped':skipped_symlink,
           'hits':sorted(out,key=lambda x:-x['size'])},open('work4/dump_sweep.json','w'),indent=1)
ctl_found=any(h['path']==ctl for h in out)
print(f"scanned={scanned} unreadable={errs} hits={len(out)} POSITIVE_CONTROL_FOUND={ctl_found}")
os.remove(ctl)
