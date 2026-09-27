# G01 PLATFORM_BASE — PROOF — HTML_EDITOR (predeclaration stub; results pending)

Cases predeclared 2026-09-27T15:04:59Z; cases file sha256 a660285fc3698a57c9d13363ef551950768383a63f599450ebee106479e2d5dd. Execution not yet started.

# PREDECLARED PROOF CASES — G01 http_routing (PC-HROU) + html_editor (PC-HEDT)
Predeclared at: 2026-09-27T15:04:59Z (before any Stage-2 fetch). Anchor odoo/odoo@8d05257d83f9128953f580a066db67c48fcdb96f via raw.githubusercontent; blob = git hash-object (scratchpad only).
Layers: SRC = source-static; CFG = static configuration (manifest/data/ACL); RT = runtime (device OFFLINE -> NOT-EXECUTED, ready-to-run).
Verdicts: PASS (expected observed) | FAIL (fail condition observed) | INCONCLUSIVE (neither decidable from fetched text) | NOT-EXECUTED.

## http_routing
PC-HROU-01 | SRC | pre: none | steps: fetch 6 module files (__manifest__, __init__, controllers/main.py, models/ir_http.py, models/ir_qweb.py, views/http_routing_template.xml); hash | expected: blobs = 9321b408/ad6393ee/a0c0d359/d508ceb8/39ffe927/5c5e7d00 | fail: any mismatch
PC-HROU-02 | SRC | debug-via-URL -> traceback chain | steps: (a) web models/ir_http.py: locate routine setting session debug from a request query parameter, note any auth/group/user check; (b) http_routing ir_http.py _handle_error: confirms call to that routine; (c) base ir_qweb.py / http_routing ir_qweb: render values populate 'debug' from request/session; (d) template: debug block gated by 'editable or debug' and contains traceback | expected: (a)-(d) all present and no authentication/group gate on (a) | fail: an auth/group/internal-user gate on setting debug, OR _handle_error does not invoke it, OR template debug not sourced from session
PC-HROU-03 | SRC | traceback computed into error-page values unconditionally | expected: traceback value built without debug/editable condition in http_routing error value preparation | fail: traceback computed only when debug/authorised
PC-HROU-04 | SRC | redirect helper local-default (odoo/http.py) | expected: request.redirect default local=True; local mode drops scheme+netloc and leading slashes/backslashes; redirect_query delegates to it | fail: default non-local, or no stripping
PC-HROU-05 | SRC | logout parent sanitation (web controllers/session.py + http_routing override) | expected: parent logout redirects via local-default helper; override passes redirect unchanged | fail: parent uses non-local redirect with caller value
PC-HROU-06 | SRC | public translations route filtering (http_routing controllers/main.py -> web controllers/webclient.py) | expected: caller comma-list appended; no installed-state/allow-list filter in delegated handler | fail: filter/allow-list present
PC-HROU-07 | CFG | undeclared providers of 404 assets | steps: manifest deps; template refs; html_editor/web/bus manifests auto_install; website manifest | expected: depends=['web'] only; 404 refs /html_editor/shape/... and /contactus; html_editor/web/bus auto_install True | fail: dependency declared, or html_editor not auto_install
PC-HROU-08 | SRC | slug helper ownership (C04 PARTIAL) | steps: base models/ir_http.py defines _slug/_unslug; http_routing overrides | expected: both present in base | fail: absent from base
PC-HROU-09 | SRC | C03 PARTIAL: lang/canonical redirect activation gated by route flags | expected: multilang/website routing flags gate redirect branch | fail: redirects applied irrespective of route flags
PC-HROU-10 | SRC | C06/C09: canonical 301 only on GET/HEAD; POST not language-redirected | expected: method check present | fail: absent
PC-HROU-R01..R06 | RT | = A2 PR-HROU-01..06 (setup/expected/fail as in A2 §7) | NOT-EXECUTED (device OFFLINE)

## html_editor
PC-HEDT-01 | SRC | blob integrity: 11 module files listed in A2 §0.1 + addons/mail/tools/link_preview.py | expected: blobs as A2 (link_preview 18515419263f8fc005029601a5c7bc821cc9f727) | fail: mismatch
PC-HEDT-02 | SRC | SSRF guard absence in link_preview fetcher | steps: search fetcher for ip/host/private/loopback/allow/deny checks, scheme allow-list, redirect policy, timeout, body cap, returned fields | expected: no host/IP/private-range block; redirects followed; timeout 3 (per-op); streamed read without byte cap until head-close marker; title/description/image/etc returned | fail: any host/IP/private deny, redirect disabled, or byte cap present
PC-HEDT-03 | SRC | public route + internal fallback | expected: link_preview_external auth=public passes caller URL to fetcher; internal preview falls back to same fetcher for non-record URLs | fail: auth!=public or no fallback
PC-HEDT-04 | SRC | SVG storage via modify_image | steps: modify_image signature (caller data + mimetype); allow-list source; elevated copy; superuser MIME write | expected: caller bytes accepted; allow-list contains image/svg+xml; superuser reset of MIME after downgrade | fail: SVG not in allow-list, or no caller bytes, or no superuser reset
PC-HEDT-05 | CFG+SRC | undeclared deps actual import paths | steps: grep controllers/main.py and models for 'odoo.addons.' imports and env['mail.*'/'website'] uses; manifests of mail/website/iap | expected: module-level imports from odoo.addons.mail.tools and odoo.addons.iap.tools; mail.ice.server env call; website env browse; mail and website manifests depend on html_editor; declared deps base/bus/web | fail: imports absent or declared
PC-HEDT-06 | SRC | C04/X-HEDT-03 resolution | expected: html_editor slug calls go through a model method resolvable in base | fail: import from http_routing module path
PC-HEDT-07 | SRC | C02 PARTIAL import mechanism | steps: odoo/addons/__init__.py | expected: namespace package over addons path (no install-state gate at import) | fail: install-state gate; INCONCLUSIVE if not decidable
PC-HEDT-08 | SRC | media-library save (C08/X-04) | expected: requests.post/get without timeout; superuser create; MIME from remote header; no origin check | fail: timeout or origin check present
PC-HEDT-09 | SRC | Vimeo plain HTTP + no in-module caller (C09) | expected: http:// oembed; no route in controllers calls thumbnail fn | fail: https or in-module caller
PC-HEDT-10 | SRC | query-string editable injection (SF-06) | expected: models/ir_http.py injects editable/translatable from request params without user check | fail: gated by user/group
PC-HEDT-11 | SRC | C13 raw exception text returned | expected: catch-all returns str(e) | fail: generic message
PC-HEDT-12 | SRC | C20 database.uuid egress | expected: uuid in media search/download/AI payloads | fail: absent
PC-HEDT-R01..R10 | RT | = A2 PR-HEDT-01..10 | NOT-EXECUTED (device OFFLINE; no live SSRF or third-party probing permitted)
