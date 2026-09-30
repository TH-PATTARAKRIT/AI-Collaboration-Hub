> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 Custom Module Study: 19_attachment_dedup_fix

## 0. Header
- Module: 19_attachment_dedup_fix
- License (confirmed in manifest): LGPL-3 (addons/19_attachment_dedup_fix/__manifest__.py:21)
- Author (manifest): Yin Htay (addons/19_attachment_dedup_fix/__manifest__.py:15)
- Version (manifest): 19.0.0.0 (addons/19_attachment_dedup_fix/__manifest__.py:4)
- Path: addons_Extramodule/addons/19_attachment_dedup_fix
- Source revision studied: workspace on-disk copy (not verified against upstream)

## 1. Business capability
- Prevents a file upload from failing with the core message that an attachment "collides with an existing file" when a stored file with the same content fingerprint path already exists but holds different content (manifest description, 19_attachment_dedup_fix/__manifest__.py:6-12).
- The manifest states the target is product drawing uploads, and that the file is auto-renamed (e.g. name_1). The code studied does NOT contain any rename or product-drawing filter; it acts on every stored attachment whose storage mode is not the database (19_attachment_dedup_fix/models/ir_attachment.py:15-21). The rename claim is therefore not supported by code in this module (see section 6).
- Business effect: when a collision would occur, the uploaded content is silently altered (extra bytes appended, up to a bounded number of retries) so it is stored under a different fingerprint. The stored file is no longer byte-identical to what the user uploaded (models/ir_attachment.py:23-49).

## 2. Attachment to CORE
- Extends core model ir.attachment (base) via inheritance (19_attachment_dedup_fix/models/ir_attachment.py:13). Depends only on base (manifest:16).
- Override of core method _get_datas_related_values: ADDS before core. It pre-processes the payload when storage is not "db", then calls core (ir_attachment.py:15-21). Core method at core:base/models/ir_attachment.py:314.
- ALTERS CORE CONTROL: the core control that raises a user error when an existing stored file has different content (core:base/models/ir_attachment.py:141-143, message "The attachment collides with an existing file") is effectively bypassed in this path, because the module alters the payload before core computes the checksum. The core check itself is not edited.
- Uses core helpers _storage (core:base/models/ir_attachment.py:88), _full_path (core:base/models/ir_attachment.py:125) and _same_content (core:base/models/ir_attachment.py:340).
- New helper method _mutate_to_avoid_collision on ir.attachment (ir_attachment.py:23): on a differing-content collision appends one random byte and retries up to a maximum of 10 attempts; if still colliding, logs an error and returns data unchanged so core raises its original error (ir_attachment.py:37-42). Same-content (true duplicate) is left to core dedup (ir_attachment.py:33-34).

## 3. New objects, security, automation, external calls
- New models: none. New fields: none. Data files: none (manifest:17 empty).
- Security: no ACLs, groups or record rules added; no company scoping.
- Automation: none. External calls: none. Logging of collision events at info/error level (ir_attachment.py:38-47).
- Side effect noted: reads the filestore on disk during upload (ir_attachment.py:29-33).

## 4. Odoo 19 compatibility
- All referenced core members exist in the Community 19 tree: _storage, _full_path, _same_content, _get_datas_related_values (core:base/models/ir_attachment.py:88,125,340,314). No absent references found.
- Not checked: interaction with attachments stored through other core paths (e.g. write of raw content at core:base/models/ir_attachment.py:294, 779) beyond confirming they call _get_datas_related_values.

## 5. Custom-to-custom dependencies
- None declared (manifest depends: base only).

## 6. UNKNOWN - EVIDENCE INSUFFICIENT
- UNKNOWN - EVIDENCE INSUFFICIENT: whether any product-drawing-specific rename (drawing.pdf to drawing_1.pdf) exists elsewhere; the described rename is not present in this module's code.
- UNKNOWN - EVIDENCE INSUFFICIENT: whether appended random bytes corrupt or invalidate specific file types (e.g. signed PDFs) in practice.
- UNKNOWN - EVIDENCE INSUFFICIENT: which filestore/storage mode is configured in the target deployment.
