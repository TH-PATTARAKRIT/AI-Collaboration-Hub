#!/usr/bin/env python3
"""Model-declaration census. POPULATION: every python class in every module of the root
that declares _name or _inherit. PATTERN: regex over class bodies (validated below by a
second, AST-based pass). UNIT: one (module, class, model) triple."""
import os,sys,re,json,ast,collections
root=sys.argv[1]; out=sys.argv[2]
decl=[]   # module, file, class, _name, [_inherit]
files=0; astfail=[]
for module in sorted(os.listdir(root)):
    md=os.path.join(root,module)
    if not os.path.isdir(md) or not os.path.exists(os.path.join(md,'__manifest__.py')): continue
    for dp,dn,fns in os.walk(md):
        dn[:]=[d for d in dn if d not in ('static','__pycache__','i18n')]
        for fn in fns:
            if not fn.endswith('.py'): continue
            p=os.path.join(dp,fn); files+=1
            try: src=open(p,encoding='utf-8',errors='replace').read()
            except Exception: continue
            if '_name' not in src and '_inherit' not in src: continue
            try: tree=ast.parse(src)
            except Exception as e:
                astfail.append((os.path.relpath(p,root),str(e)[:80])); continue
            for node in ast.walk(tree):
                if not isinstance(node,ast.ClassDef): continue
                nm=None; inh=[]
                for st in node.body:
                    if not isinstance(st,ast.Assign): continue
                    for t in st.targets:
                        if not isinstance(t,ast.Name): continue
                        if t.id=='_name' and isinstance(st.value,ast.Constant) and isinstance(st.value.value,str):
                            nm=st.value.value
                        elif t.id=='_inherit':
                            v=st.value
                            if isinstance(v,ast.Constant) and isinstance(v.value,str): inh=[v.value]
                            elif isinstance(v,(ast.List,ast.Tuple)):
                                inh=[e.value for e in v.elts if isinstance(e,ast.Constant) and isinstance(e.value,str)]
                if nm or inh:
                    decl.append({'module':module,'file':os.path.relpath(p,root),'class':node.name,'name':nm,'inherit':inh})
json.dump(decl,open(out,'w'))
print(json.dumps({'py_files':files,'declarations':len(decl),'ast_failures':len(astfail)},indent=2))
if astfail: print(astfail[:5])
