#!/usr/bin/env python3
"""PMO pre-commit sweep — four checks with DISJOINT units.
1 identifier | 2 table row | 3 file/manifest hash | 4 clean-room token per file."""
import os,re,sys,json,hashlib,collections
PKG=sys.argv[1]
L1=[];L2=[]
files=[]
for dp,dn,fns in os.walk(PKG):
    for fn in sorted(fns):
        p=os.path.join(dp,fn); files.append(p)
md=[p for p in files if p.endswith('.md')]
def layer(p):
    head=open(p,encoding='utf-8',errors='replace').read(4000)
    if 'LAYER 2' in head: return 2
    if 'LAYER 1' in head: return 1
    return 0
# ---- 1 IDENTIFIER (unit: identifier)
IDPAT=re.compile(r'\b((?:MM|CD|FT|FN|OD|XM|SS|HA|EB)-F-\d{2}|GAP-INV-\d{2}|CRITICAL-GAP-\d{2}|BOSS-DEC-\d{2}|CORR-F-\d{2}|SR-\d{2}|LI-INV-[A-Z]+-\d{4}|CORR-\d{3}[A-Z]?)\b')
defined=collections.defaultdict(list); cited=collections.defaultdict(list)
DEFLINE=re.compile(r'^\s*(?:###+\s*|\|\s*`?)((?:MM|CD|FT|FN|OD|XM|SS|HA|EB)-F-\d{2}|GAP-INV-\d{2}|CRITICAL-GAP-\d{2}|BOSS-DEC-\d{2}|CORR-F-\d{2}|SR-\d{2})\b')
for p in md:
    for i,line in enumerate(open(p,encoding='utf-8',errors='replace'),1):
        m=DEFLINE.match(line)
        if m: defined[m.group(1)].append(f'{os.path.relpath(p,PKG)}:{i}')
        for t in IDPAT.findall(line):
            if t.startswith('LI-INV'): continue
            cited[t].append(f'{os.path.relpath(p,PKG)}:{i}')
undef=sorted(set(cited)-set(defined)); uncited=sorted(k for k in defined if len(cited[k])<=len(defined[k]))
dup=sorted(k for k,v in defined.items() if len(v)>1)
# numbering gaps
fams=collections.defaultdict(set)
for k in set(defined)|set(cited):
    m=re.match(r'(.+?)-(\d+)$',k)
    if m: fams[m.group(1)].add(int(m.group(2)))
gaps={f:sorted(set(range(1,max(v)+1))-v) for f,v in fams.items() if sorted(set(range(1,max(v)+1))-v)}
# ---- 2 TABLE ROW (unit: table row)
badrows=[]
for p in md:
    lines=open(p,encoding='utf-8',errors='replace').read().split('\n')
    hdr=None
    for i,l in enumerate(lines,1):
        s=l.strip()
        if not s.startswith('|'): hdr=None; continue
        n=len([c for c in re.split(r'(?<!\\)\|',s)[1:-1]])
        if hdr is None:
            hdr=n; continue
        if set(s.replace('|','').replace(' ','')) <= set('-:'):
            if n!=hdr: badrows.append((os.path.relpath(p,PKG),i,'separator',n,hdr))
            continue
        if n!=hdr: badrows.append((os.path.relpath(p,PKG),i,'row',n,hdr))
# ---- 3 FILE (unit: file)
manifest={}
for p in sorted(files):
    rel=os.path.relpath(p,PKG)
    if rel=='MANIFEST_SHA256.json': continue   # a manifest cannot hash itself
    manifest[rel]=hashlib.sha256(open(p,'rb').read()).hexdigest()
junk=[k for k in manifest if '__pycache__' in k or k.endswith('.pyc') or k.endswith('.DS_Store')]
empty=[k for k in manifest if os.path.getsize(os.path.join(PKG,k))==0]
# ---- 4 TOKEN (unit: file, counting vendor tokens)
# Two token classes. SUBSTRING tokens are unambiguous identifier fragments.
# WORD tokens are also ordinary English words and MUST be matched on word boundaries,
# otherwise 'quant' matches 'quantity' and the scrub reports a leak that is not one.
SUB=['openerp','stock.','product.','ir.ui','ir.actions','ir.model','ir.cron','ir.rule','res.config',
     'res.groups','res.partner','account.move','mrp.','uom.','_action_','__manifest__','.py',
     'l10n_','scgl_','smesplus_','odoo']
WORD=['quant','quants','orderpoint','orderpoints','picking','pickings','sudo','addons','Odoo','ODOO']
tokrep=[]
for p in md:
    txt=open(p,encoding='utf-8',errors='replace').read()
    n=sum(txt.lower().count(t.lower()) for t in SUB)
    n+=sum(len(re.findall(r'\b'+re.escape(t)+r'\b',txt)) for t in WORD)
    hits=[t for t in SUB if t.lower() in txt.lower()]+[t for t in WORD if re.search(r'\b'+re.escape(t)+r'\b',txt)]
    tokrep.append((os.path.relpath(p,PKG),layer(p),n,hits))
print(json.dumps({
 'CHECK_1_IDENTIFIER':{'defined':len(defined),'cited':len(cited),
   'cited_never_defined':undef,'defined_never_cited_elsewhere':uncited,
   'defined_twice':dup,'numbering_gaps':gaps},
 'CHECK_2_TABLE_ROW':{'markdown_files':len(md),'broken_rows':len(badrows),'detail':badrows[:20]},
 'CHECK_3_FILE':{'files':len(manifest),'junk_artifacts':junk,'zero_byte':empty},
 'CHECK_4_TOKEN':{'files_scanned':len(tokrep),
   'token_classes':{'substring':len(SUB),'word_boundary':len(WORD)},
   'LAYER1_files_with_vendor_tokens':[(f,n,h) for f,l,n,h in tokrep if l==1 and n>0],
   'UNLABELLED_files':[(f,n) for f,l,n,h in tokrep if l==0],
   'LAYER2_token_totals':sum(n for f,l,n,h in tokrep if l==2)},
}, indent=2))
json.dump(manifest,open(os.path.join(PKG,'MANIFEST_SHA256.json'),'w'),indent=1,sort_keys=True)
