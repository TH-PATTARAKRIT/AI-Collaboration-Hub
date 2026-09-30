> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 custom module trace: nthub_binary_field_preview

Module: nthub_binary_field_preview · License (confirmed in manifest): LGPL-3 (nthub_binary_field_preview/__manifest__.py:42)
Author (manifest): Neoteric Hub (manifest:24) · Version (manifest): 19.0.1.0 (manifest:4)
Path: addons_Extramodule/addons_extra/nthub_binary_field_preview
Source revision studied: workspace on-disk copy (not verified against upstream)

## 1. Business capability
- Front-end only ("Attachment Preview" title, manifest:3). Adds a form/list field widget named `nt_binary_preview` for binary fields that shows a small image thumbnail with a zoom viewer for images, or a preview icon that opens the file in a new browser tab for non-images, plus a download button (nthub_binary_field_preview/static/src/js/nthub_binary_preview_viewerjs.js:140-167; static/src/xml/nthub_binary_preview.xml:2-93).
- It only takes effect on views where a developer sets the widget on a binary field (manifest description, manifest:20-22). The module itself changes no views and adds no menus (manifest:31-32 data list is empty).
- The manifest carries marketplace metadata (price 9 USD, live test URL empty) (manifest:26-28).

## 2. Attachment to CORE
- Declared dependencies: `base`, `web`, `mail`, `sale` (manifest:30). No Python code is loaded: the model import is commented out (nthub_binary_field_preview/__init__.py:2). So no core model, field, method, ACL, rule, numbering, posting or valuation is touched. No `ALTERS CORE CONTROL` item.
- Core web component extended: `BinaryField` / `binaryField` from the core web binary-field module (static/src/js/nthub_binary_preview_viewerjs.js:4,7,163-166; core:web/static/src/views/fields/binary/binary_field.js:13,77). The widget is registered as an extra entry in the "fields" registry under a new name, leaving core widget `binary` untouched (js:167; core registers `binary` at binary_field.js:105).
- Behavior added on top of core class: on mount and on re-render it requests the record's binary content through the standard web content URL for the current model, record id and field name, detects the file type from the response, and toggles thumbnail versus icon (js:35-138). It reuses core upload component and core update/download members (core:binary_field.js:42, 65; xml uses `FileUploader` and `onFileDownload`).
- The `sale` dependency: no reference to any sale object found in the module files read (JS, XML, manifest): UNKNOWN - EVIDENCE INSUFFICIENT whether it is required for any purpose.

## 3. New objects, security, automation, external calls
- No models, groups, ACLs, record rules, crons or server actions (no Python files besides package init and manifest).
- Access control relies entirely on the core content controller's own checks for the URL `/web/content/<model>/<id>/<field>`: the module issues these requests from the browser (js:38-45, 85-90, 145, 157). It fetches each file once as a full download just to read its type, and the request is made twice per render (one uncached fetch plus one to read the blob) (js:40-43): possible bandwidth cost on large files. Not tested.
- Debug console output is left in the widget code (js:10, 119).
- Bundled third-party library: Viewer.js v1.11.6, MIT license, under the module's static folder (static/src/js/viewer.js:2-6); its license differs from the module's LGPL-3. Loaded into the backend assets (manifest:35-37).
- No outbound calls to external hosts found in the JS/XML files read (only same-origin content URLs). Description page static/description/index.html was not reviewed (marketing page).

## 4. Odoo 19 compatibility (grep against Community 19)
- Found in core: `BinaryField` (core:web/static/src/views/fields/binary/binary_field.js:13), `binaryField` (:77), `FileUploader` import (:6), `update` (:42), `onFileDownload` (:65), fields registry (:105).
- The template header uses `owl="1"` attribute and a `<template xml:spacer>` wrapper (xml:1-2); whether Odoo 19 template loader still accepts this: not checked.
- The module reads `props.record.data.id` and `props.record.resId` (js:37, 45): whether `record.data.id` exists in the 19 relational model: not checked.
- Global `Viewer` is used without explicit import (js:51); depends on the library loading first in the bundle (manifest:35-37 lists viewer.js before the widget file at :37).

## 5. Custom-to-custom dependencies
- None on other custom modules; depends only on core modules base, web, mail, sale (manifest:30).

## 6. UNKNOWN - EVIDENCE INSUFFICIENT
- Runtime rendering in Odoo 19 (no code run): UNKNOWN - EVIDENCE INSUFFICIENT.
- Whether the widget respects attachment-level access restrictions on list views with many rows: UNKNOWN - EVIDENCE INSUFFICIENT.
- Why the sale and mail modules are listed as dependencies: UNKNOWN - EVIDENCE INSUFFICIENT.
