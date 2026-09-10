#!/usr/bin/env python3
"""VDR-PREP-001-CORR1 : mechanical menu-surface enumerator.
POPULATION : every menu node defined anywhere in the declared addons root.
PATTERN    : <menuitem .../> elements AND <record model="ir.ui.menu"> records, in any
             .xml file listed or not listed in a manifest (widened deliberately).
UNIT       : one menu node = one row.
Emits JSONL. Also emits a positive-control count.
"""
import os, sys, json, re
import xml.etree.ElementTree as ET

root = sys.argv[1]
out  = sys.argv[2]

menus = {}       # full_xmlid -> dict
parse_fail = []
files_scanned = 0
raw_menuitem_regex_hits = 0

MENUITEM_RE = re.compile(r'<menuitem\b')
RECMENU_RE  = re.compile(r'<record[^>]*model=["\']ir\.ui\.menu["\']')

def full(xid, module):
    return xid if '.' in xid else f"{module}.{xid}"

def walk_menuitems(elem, module, path, parent_xmlid, depth, order):
    for child in list(elem):
        if child.tag != 'menuitem':
            # menuitem can be nested under <odoo>/<data> only; recurse containers
            if child.tag in ('data', 'odoo', 'openerp'):
                walk_menuitems(child, module, path, parent_xmlid, depth, order)
            continue
        xid = child.get('id')
        if not xid:
            continue
        fx = full(xid, module)
        par = child.get('parent')
        par = full(par, module) if par else parent_xmlid
        menus[fx] = {
            'xmlid': fx, 'module': module, 'name': child.get('name'),
            'parent': par, 'sequence': child.get('sequence'),
            'action': full(child.get('action'), module) if child.get('action') else None,
            'groups': child.get('groups'), 'active': child.get('active'),
            'web_icon': child.get('web_icon'),
            'defined_in': path, 'form': 'menuitem',
        }
        walk_menuitems(child, module, path, fx, depth+1, order)

def handle_record(rec, module, path):
    xid = rec.get('id')
    if not xid:
        return
    fx = full(xid, module)
    d = {'xmlid': fx, 'module': module, 'name': None, 'parent': None,
         'sequence': None, 'action': None, 'groups': None, 'active': None,
         'web_icon': None, 'defined_in': path, 'form': 'record'}
    for f in rec.findall('field'):
        n = f.get('name')
        if n == 'name':   d['name'] = f.get('eval') or (f.text or '').strip()
        elif n == 'parent_id': d['parent'] = full(f.get('ref'), module) if f.get('ref') else None
        elif n == 'sequence': d['sequence'] = f.get('eval') or (f.text or '').strip()
        elif n == 'action':
            r = f.get('ref')
            if r: d['action'] = full(r, module)
        elif n == 'groups_id': d['groups'] = f.get('eval')
        elif n == 'active': d['active'] = f.get('eval') or (f.text or '').strip()
    if fx in menus:
        # a record that updates an existing menuitem
        for k, v in d.items():
            if v not in (None, ''):
                menus[fx][k] = v
        menus[fx]['form'] = menus[fx]['form'] + '+record'
    else:
        menus[fx] = d

for module in sorted(os.listdir(root)):
    mdir = os.path.join(root, module)
    if not os.path.isdir(mdir) or not os.path.exists(os.path.join(mdir, '__manifest__.py')):
        continue
    for dirpath, dirnames, filenames in os.walk(mdir):
        dirnames[:] = [d for d in dirnames if d not in ('static', '__pycache__', 'i18n', 'tests')]
        for fn in filenames:
            if not fn.endswith('.xml'):
                continue
            p = os.path.join(dirpath, fn)
            files_scanned += 1
            try:
                txt = open(p, encoding='utf-8', errors='replace').read()
            except Exception as e:
                parse_fail.append((p, 'read:'+str(e))); continue
            if not (MENUITEM_RE.search(txt) or RECMENU_RE.search(txt)):
                continue
            raw_menuitem_regex_hits += len(MENUITEM_RE.findall(txt)) + len(RECMENU_RE.findall(txt))
            rel = os.path.relpath(p, root)
            try:
                tree = ET.fromstring(txt)
            except Exception as e:
                parse_fail.append((rel, 'xml:'+str(e))); continue
            walk_menuitems(tree, module, rel, None, 0, 0)
            for rec in tree.iter('record'):
                if rec.get('model') == 'ir.ui.menu':
                    handle_record(rec, module, rel)

with open(out, 'w') as fh:
    for m in menus.values():
        fh.write(json.dumps(m)+'\n')

print(json.dumps({
    'root': root,
    'files_scanned': files_scanned,
    'regex_element_hits': raw_menuitem_regex_hits,
    'menu_nodes_parsed': len(menus),
    'parse_failures': len(parse_fail),
}, indent=2))
for p, e in parse_fail[:10]:
    print('FAIL', p, e[:120])
