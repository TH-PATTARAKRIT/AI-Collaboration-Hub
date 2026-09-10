import os,sys,json,ast,collections
R=sys.argv[1]; rows=[]; fails=0; files=0; mods=0
for module in sorted(os.listdir(R)):
    md=os.path.join(R,module)
    if not os.path.isdir(md) or not os.path.exists(os.path.join(md,'__manifest__.py')): continue
    mods+=1
    for dp,dn,fns in os.walk(md):
        dn[:]=[d for d in dn if d not in ('static','__pycache__','i18n')]
        for fn in fns:
            if not fn.endswith('.py'): continue
            p=os.path.join(dp,fn); files+=1
            src=open(p,encoding='utf-8',errors='replace').read()
            if 'fields.' not in src: continue
            try: tree=ast.parse(src)
            except Exception: fails+=1; continue
            for node in ast.walk(tree):
                if not isinstance(node,ast.ClassDef): continue
                nm=None; inh=[]
                for st in node.body:
                    if isinstance(st,ast.Assign):
                        for t in st.targets:
                            if isinstance(t,ast.Name) and t.id=='_name' and isinstance(st.value,ast.Constant): nm=st.value.value
                            elif isinstance(t,ast.Name) and t.id=='_inherit':
                                v=st.value
                                inh=[v.value] if isinstance(v,ast.Constant) else [e.value for e in getattr(v,'elts',[]) if isinstance(e,ast.Constant)]
                tgt=nm or (inh[0] if inh else None)
                if not tgt: continue
                for st in node.body:
                    if isinstance(st,ast.Assign) and isinstance(st.value,ast.Call):
                        f=st.value.func
                        if isinstance(f,ast.Attribute) and isinstance(f.value,ast.Name) and f.value.id=='fields':
                            kw={k.arg:k.value for k in st.value.keywords if k.arg}
                            comodel=None
                            if st.value.args and isinstance(st.value.args[0],ast.Constant) and isinstance(st.value.args[0].value,str):
                                comodel=st.value.args[0].value
                            if 'comodel_name' in kw and isinstance(kw['comodel_name'],ast.Constant): comodel=kw['comodel_name'].value
                            store=ast.unparse(kw['store']) if 'store' in kw else None
                            compute='compute' in kw
                            for t in st.targets:
                                if isinstance(t,ast.Name):
                                    rows.append({'module':module,'model':tgt,'declared_name':nm,'field':t.id,
                                      'type':f.attr,'comodel':comodel,'store':store,'compute':compute,
                                      'file':os.path.relpath(p,R)})
json.dump(rows,open(sys.argv[2],'w'))
print(json.dumps({'modules':mods,'py_files':files,'field_rows':len(rows),'ast_fail':fails},indent=2))
