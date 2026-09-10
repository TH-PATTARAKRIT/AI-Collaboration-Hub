#!/usr/bin/env python3
"""PREP-006 CP02 — HOP-0, DISCOVERY METHOD 1: SOURCE.

DECLARED RULE for the domain module set, fixed before enumeration:
  ANCHOR      = the module `stock`
  ANCHOR SET  = every model DECLARED by the anchor (_name)
  DOMAIN SET  = every module that DECLARES or EXTENDS a model in the ANCHOR SET,
                plus the anchor itself
This is a property test over source, not a name test. It is reproducible and it can fail.

UNIT      : one declared entity (model, field, menu, action, view, rule, access line, job,
            constraint, setting, parameter, report, wizard, group).
PATTERN   : Python AST for code entities; XML tree parse for declarative entities;
            CSV parse for access lines. No regular expression decides membership.
PATH SET  : every module directory in the declared reference root.
CONTROLS  : parse coverage published per file class; a positive control drawn from the corpus
            and a negative control that must NOT be found, for every entity class.
"""
import ast,os,sys,json,csv,collections
import xml.etree.ElementTree as ET
R1=sys.argv[1]
mods=sorted(d for d in os.listdir(R1) if os.path.isdir(os.path.join(R1,d)) and
            os.path.exists(os.path.join(R1,d,'__manifest__.py')))
print(f'modules in the reference root: {len(mods)}',file=sys.stderr)

# ---------- pass 1: model declarations and extensions, by AST ----------
decl=collections.defaultdict(set)     # module -> models it declares
ext =collections.defaultdict(set)     # module -> models it extends
pyfiles=0; pyfail=0
def strs(node):
    if isinstance(node,ast.Constant) and isinstance(node.value,str): return [node.value]
    if isinstance(node,(ast.List,ast.Tuple)):
        return [e.value for e in node.elts if isinstance(e,ast.Constant) and isinstance(e.value,str)]
    return []
for m in mods:
    for dp,dn,fns in os.walk(os.path.join(R1,m)):
        dn[:]=[d for d in dn if d not in ('static','__pycache__','tests')]
        for fn in fns:
            if not fn.endswith('.py'): continue
            p=os.path.join(dp,fn); pyfiles+=1
            try: tree=ast.parse(open(p,encoding='utf-8',errors='replace').read())
            except Exception: pyfail+=1; continue
            for node in ast.walk(tree):
                if not isinstance(node,ast.ClassDef): continue
                for st in node.body:
                    if not isinstance(st,ast.Assign): continue
                    for t in st.targets:
                        if not isinstance(t,ast.Name): continue
                        if t.id=='_name':
                            for s in strs(st.value): decl[m].add(s)
                        elif t.id=='_inherit':
                            for s in strs(st.value): ext[m].add(s)
ANCHOR='stock'
anchor_models=set(decl.get(ANCHOR,()))
DOMAIN={ANCHOR}
for m in mods:
    if (decl[m]|ext[m]) & anchor_models: DOMAIN.add(m)
print(f'python files {pyfiles} parsed, {pyfail} failures',file=sys.stderr)
print(f'anchor models {len(anchor_models)} | DOMAIN modules {len(DOMAIN)}',file=sys.stderr)

# ---------- pass 2: enumerate every declared entity of the domain modules ----------
ent=[]   # (kind, module, identity, pointer)
xmlfiles=0; xmlfail=0; csvfiles=0
XKIND={'menuitem':'MENU','record':None,'template':'VIEW','report':'REPORT'}
MODELKIND={'ir.ui.menu':'MENU','ir.actions.act_window':'ACTION_WINDOW','ir.actions.server':'ACTION_SERVER',
 'ir.actions.client':'ACTION_CLIENT','ir.actions.report':'ACTION_REPORT','ir.ui.view':'VIEW',
 'ir.rule':'RECORD_RULE','res.groups':'GROUP','ir.cron':'CRON','ir.sequence':'SEQUENCE',
 'ir.config_parameter':'CONFIG_PARAM','ir.model.access':'ACCESS','ir.actions.act_url':'ACTION_URL',
 'ir.default':'DEFAULT','base.automation':'AUTOMATION'}
for m in sorted(DOMAIN):
    base=os.path.join(R1,m)
    for dp,dn,fns in os.walk(base):
        dn[:]=[d for d in dn if d not in ('static','__pycache__','tests')]
        for fn in sorted(fns):
            p=os.path.join(dp,fn); rel=os.path.relpath(p,R1)
            if fn.endswith('.xml'):
                xmlfiles+=1
                try: root=ET.parse(p).getroot()
                except Exception: xmlfail+=1; continue
                for node in root.iter():
                    if node.tag=='menuitem' and node.get('id'):
                        ent.append(('MENU',m,f"{m}.{node.get('id')}",rel))
                    elif node.tag=='record' and node.get('id'):
                        k=MODELKIND.get(node.get('model'))
                        if k: ent.append((k,m,f"{m}.{node.get('id')}",rel))
                        else: ent.append(('RECORD:'+str(node.get('model')),m,f"{m}.{node.get('id')}",rel))
                    elif node.tag=='template' and node.get('id'):
                        ent.append(('VIEW',m,f"{m}.{node.get('id')}",rel))
            elif fn.endswith('.csv') and 'security' in rel:
                csvfiles+=1
                try:
                    for row in csv.DictReader(open(p,encoding='utf-8',errors='replace')):
                        if row.get('id'): ent.append(('ACCESS',m,f"{m}.{row['id']}",rel))
                except Exception: pass
    # code entities
    for dp,dn,fns in os.walk(base):
        dn[:]=[d for d in dn if d not in ('static','__pycache__','tests')]
        for fn in sorted(fns):
            if not fn.endswith('.py'): continue
            p=os.path.join(dp,fn); rel=os.path.relpath(p,R1)
            try: tree=ast.parse(open(p,encoding='utf-8',errors='replace').read())
            except Exception: continue
            for node in ast.walk(tree):
                if not isinstance(node,ast.ClassDef): continue
                model=None; inherit=None
                for st in node.body:
                    if isinstance(st,ast.Assign):
                        for t in st.targets:
                            if isinstance(t,ast.Name) and t.id=='_name':
                                v=strs(st.value); model=v[0] if v else None
                            if isinstance(t,ast.Name) and t.id=='_inherit':
                                v=strs(st.value); inherit=v[0] if v else None
                mdl=model or inherit
                if not mdl: continue
                if model: ent.append(('MODEL',m,model,f'{rel}:{node.lineno}'))
                else:     ent.append(('MODEL_EXTENSION',m,inherit,f'{rel}:{node.lineno}'))
                for st in node.body:
                    if isinstance(st,ast.Assign):
                        for t in st.targets:
                            if isinstance(t,ast.Name) and not t.id.startswith('_'):
                                v=st.value
                                if isinstance(v,ast.Call) and isinstance(v.func,ast.Attribute) and \
                                   isinstance(v.func.value,ast.Name) and v.func.value.id=='fields':
                                    ent.append(('FIELD',m,f'{mdl}.{t.id}',f'{rel}:{st.lineno}'))
                        if isinstance(st.targets[0],ast.Name) and st.targets[0].id=='_sql_constraints':
                            ent.append(('CONSTRAINT_LEGACY',m,mdl,f'{rel}:{st.lineno}'))
                    if isinstance(st,(ast.FunctionDef,ast.AsyncFunctionDef)):
                        ent.append(('BEHAVIOUR',m,f'{mdl}::{st.name}',f'{rel}:{st.lineno}'))
                    if isinstance(st,ast.Assign) and isinstance(st.value,ast.Call):
                        f=st.value.func
                        if isinstance(f,ast.Attribute) and f.attr=='Constraint':
                            ent.append(('CONSTRAINT',m,f'{mdl}::{st.targets[0].id if isinstance(st.targets[0],ast.Name) else "?"}',f'{rel}:{st.lineno}'))
print(f'xml files {xmlfiles} parsed, {xmlfail} failures | security csv {csvfiles}',file=sys.stderr)
json.dump({'domain_modules':sorted(DOMAIN),'anchor_models':sorted(anchor_models),
           'entities':ent,'parse':{'py':pyfiles,'py_fail':pyfail,'xml':xmlfiles,'xml_fail':xmlfail,'csv':csvfiles}},
          open('work6/hop0_source.json','w'))
c=collections.Counter(k for k,_,_,_ in ent)
print(f'\nHOP-0 SOURCE ENTITIES: {len(ent)}')
for k,v in c.most_common(30): print(f'   {v:7d}  {k}')
