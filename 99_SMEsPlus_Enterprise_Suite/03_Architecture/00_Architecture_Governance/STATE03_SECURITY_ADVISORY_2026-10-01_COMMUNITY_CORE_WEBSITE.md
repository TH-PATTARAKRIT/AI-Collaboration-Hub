# STATE03 Security Advisory — Community-Core Public Website/Mail/Livechat Surface (2026-10-01)

Document ID: `STATE03-SECURITY-ADVISORY-2026-10-01-U19`
Status: `DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION` — this session has confirmed mechanical integrity (file hashes match) and internal/cross-claim consistency, but **has no access to the actual Odoo 19 source tree or restored database itself** (that access is DeepSeek's local environment only) and so has not independently re-derived the cited source pointers. Not a runtime confirmation. Not a claim that any of these modules are installed or reachable on any live/production system — `CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET`.
Source: DeepSeek (Primary Source/Dump Research Worker, separate `STATE03_Odoo19 Deep Research` session), Atomic Boundary `U19` (`website_community`), read-only static source study + read-only DB configuration reconciliation, branch `claude/local-odoo-source-research`, commit `e4a14969`. Reconciled here by this session (`STATE03 BUSINESS PROCESS VERIFICATION AND INTEGRATION CONTROLLER`). Full technical evidence: `TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/01_RESTRICTED_TECHNICAL_EVIDENCE/U19_website_community.md` (claim IDs `VDR-U19-C###` cited below).
Purpose: **Flag findings that are actionable regardless of STATE03's own research-methodology status**, so they reach a decision-maker promptly instead of waiting behind the ordinary evidence-tier review cycle. This document does not change any STATE03 register's evidence status, and does not assert a Gate PASS or Formal Coverage.

**Difference from the 2026-09-30 advisory**: that document covered **custom/third-party modules**. This one covers **Odoo 19 Community-core modules** (`website`, `mail`, `mail_group`, `rating`, `html_editor`, `im_livechat`, and their first-party website-bridge modules) — so, unlike the earlier findings, these are not specific to this deployment's own customizations; they are standard Community behavior, and in several cases the actual exposure depends on **this deployment's own configuration** (notably, a missing reCAPTCHA secret key — see §1).

## 1. Highest-severity, systemic finding: reCAPTCHA is installed but silently inert on every route that declares it

**Finding**: `google_recaptcha` is installed, but no `recaptcha_private_key` / `recaptcha_public_key` is configured in this deployment (`VDR-U19-C064`). The verifier function (`google_recaptcha/models/ir_http.py:82`) returns `'no_secret'` when the private key is empty, and the caller treats `'no_secret'` as a **pass**, identical to a verified human (`VDR-U19-C065`: `recaptcha_result in ['is_human', 'no_secret']`). The HTTP dispatcher only invokes this check for routes that declare `captcha=...` on an unsafe method (`VDR-U19-C063`).

**Why it matters**: every public route in this unit that relies on `captcha=` for bot/abuse protection — the generic website-form-to-record endpoint, account signup/password-reset, event registration, and the mass-mailing subscribe endpoint (`VDR-U19-C045`, `C067`, `C203`, `C211`, `C299`) — currently has that protection **silently disabled**, with no error or warning surfaced anywhere. This is a single missing configuration value multiplying the real-world severity of every other finding in this document.

**What is NOT yet known**: whether this specific deployment's production/live configuration (as opposed to the studied source-tree/DB-restore snapshot) also lacks the key. This is a configuration fact, not a code defect — the fix, if confirmed needed, is to set the key, not to patch source.

## 2. Public form-to-record creation with no effective abuse gate

`POST /website/form/<model_name>` is `auth=public`, explicitly **CSRF-exempt for anonymous sessions by design** (a source comment cites breaking embedded cross-site forms as the reason — `VDR-U19-C046`, `C270`), and (per §1) effectively has no working captcha either. It creates records via `SUPERUSER` rights on an allow-listed set of models — in this deployment's own configuration: `crm.lead`, `project.task`, `mail.mail` (immediate send), `mailing.contact`, `hr.applicant` — through an allow-listed field set per model (`VDR-U19-C104` in the technical evidence's DB-reconciliation note). The combination (public, no CSRF, no working captcha, elevated-rights create) means: **currently, nothing in this install's own configuration stops scripted mass submission of these forms** — spam leads/tasks/mail/contacts/applications, and PII capture into fields the designer whitelisted (including an IP-reveal field already whitelisted on `crm.lead`).

## 3. Link-preview route fetches an arbitrary caller-supplied URL server-side (SSRF-shaped)

`POST /html_editor/link_preview_external` is public (`VDR-U19-C247`) and calls `mail/tools/link_preview.py:33`, which does `requests.get(url, timeout=3, headers=headers, allow_redirects=True, stream=True)` with **no private-address or scheme filtering shown in that function** (`VDR-U19-C248`). Whether an actual network/firewall egress control sits in front of this in a given deployment is unconfirmed (`RUNTIME/AWT REQUIRED`), but the code path itself, as traced, lets an anonymous caller make the server fetch any URL it supplies and follow redirects — the shape of a server-side request forgery primitive, regardless of whether this specific environment currently has compensating network controls.

## 4. Other findings worth a decision-maker's attention (lower severity / narrower exposure)

| Area | Finding | Claim ID(s) |
|---|---|---|
| Donations | The donation minimum amount is a client-supplied URL parameter the server does not independently re-validate against a configured floor | `VDR-U19-C240`, `C305` |
| Mass-mailing subscribe | `list_id` is used directly without checking the list's own `is_public` flag, and subscription is created with no double opt-in / verification email | `VDR-U19-C300`, `C301` |
| Mail-group tokens | Subscribe/unsubscribe confirm compares the action token with `==` rather than constant-time `consteq` in one route, while a sibling one-click-unsubscribe route in the same module does use `consteq` — inconsistent hardening, not confirmed exploitable | `VDR-U19-C222` vs `C223` |
| Mail-group notifications | An anonymous caller can trigger a subscribe/unsubscribe confirmation email to any address supplied as a parameter, with no captcha call in that path | `VDR-U19-C302` |
| Rating tokens | A rating `access_token` lookup has no expiry and no "already consumed" gate, so a once-leaked rating link stays usable indefinitely | `VDR-U19-C228` |
| Live chat | `get_session` is a public route that creates a `discuss.channel` with `sudo()` on every call, with no captcha, throttle, or token check traced | `VDR-U19-C176`, `C291` |
| Third-party data sharing | A daily cron sends visitor IP addresses, grouped by configured rules, to an external lead-enrichment (IAP) endpoint | `VDR-U19-C106` |
| Public key exposure | The Google Maps API key configured for the website is returned to any anonymous caller via a dedicated public JSON route | `VDR-U19-C255` |
| Link shortener | A latent code bug: `new_code` is assigned an integer (`search_count` result) and then `.read()` is called on it in the duplicate-code branch, which cannot work — flagged by DeepSeek as a likely dead/broken code path, not a security issue | `VDR-U19-C254` |

## 5. What is NOT installed (reduces surface)

`website_sale` and other e-commerce modules are **not installed** in the studied configuration — no checkout/order flow exists on this surface. Only one enabled custom payment provider plus a demo/test-state provider exist (no live third-party payment gateway confirmed active).

## 6. Reconciliation into STATE03 canonical registers

`U19`'s claims carry **no existing Function-ID** — DeepSeek itself flagged every claim `FUNCTION MAPPING REQUIRED`: no domain in the existing 53-entry Function-ID index (goods receipt, inventory adjustment, sales delivery, manufacturing, multicompany isolation, partial fulfilment, period cut-off, product routing, reconciliation provenance) covers public-website capabilities. This advisory is therefore **not yet reconciled into any pilot's `22_UNKNOWN_AND_GAPS.md`** — whether a new domain/Gx is warranted for public-website/community capabilities is a scope question for Boss/PMO, not something this session decides unilaterally. Tracked in `STATE03_VDR_CLAUDE_VERIFICATION_LOG.md`.

## 7. What this document is not

Not a Gate PASS, not Formal Coverage, not a claim of installed/live exposure, not authorization for any remediation code change, and not a substitute for a proper security review by whoever owns the actual running environment(s). It exists solely so this class of finding is not stuck behind STATE03's ordinary documentation-tier review cycle. `N/A — DENOMINATOR NOT VALIDATED` for any implied coverage figure. Boss remains Sole Final Approver.
