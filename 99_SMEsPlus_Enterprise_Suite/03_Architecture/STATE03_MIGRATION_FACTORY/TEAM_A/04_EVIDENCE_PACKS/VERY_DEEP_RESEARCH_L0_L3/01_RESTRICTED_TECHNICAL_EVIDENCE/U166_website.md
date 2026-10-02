# U166 — website: Base Website/CMS Module — Restricted Technical Evidence
**Unit:** U166 | **Group:** G12 | **Priority:** P2
**Source:** Odoo Community 19.0.post20260921 (READ-ONLY)
**Evidence Level:** L3 (Deep)
**Date:** 2026-10-02

---

## 1. MODULE MANIFEST — `website/__manifest__.py`

**Source path:** `odoo/addons/website/__manifest__.py`

### 1.1 Module Identity
- `name`: `'Website'`
- `category`: `'Website/Website'`
- `sequence`: `20`
- `summary`: `'Enterprise website builder'`
- `version`: `'1.0'`
- `application`: `True`
- `license`: `'LGPL-3'`

### 1.2 Dependencies (`depends`)
```
digest, web, html_editor, http_routing, portal, social_media,
auth_signup, mail, google_recaptcha, utm, html_builder
```
Key dependencies:
- `portal` — portal user authentication/views
- `mail` — messaging / mail integration
- `auth_signup` — customer self-registration
- `http_routing` — base URL routing layer
- `html_builder` — block-based visual editor
- `google_recaptcha` — form spam protection

### 1.3 External Python Dependencies
- `geoip2` — for visitor geolocation (IP → country); apt package `python3-geoip2`

### 1.4 Hooks
- `post_init_hook`: `post_init_hook` — runs on install and upgrade
- `uninstall_hook`: `uninstall_hook` — cleanup on removal

### 1.5 Data Files (Key)
- `security/website_security.xml` — groups/rules (loaded first)
- `data/website_visitor_cron.xml` — cron for visitor cleanup
- `views/website_visitor_views.xml` — visitor list/form views
- `views/res_config_settings_views.xml` — website configuration

---

## 2. WEBSITE MODEL — `website/models/website.py`

**Source path:** `odoo/addons/website/models/website.py`

### 2.1 Model Definition
```
_name = 'website'
_description = "Website"
_order = "sequence, id"
```

### 2.2 Core Fields
| Field | Type | Notes |
|---|---|---|
| `name` | Char | Website Name, required |
| `sequence` | Integer | default=10, ordering |
| `domain` | Char | e.g. `https://www.mydomain.com` |
| `domain_punycode` | Char | computed, ASCII-safe IDN version |
| `company_id` | Many2one(res.company) | required, default current company |
| `language_ids` | Many2many(res.lang) | default all active langs, required |
| `default_lang_id` | Many2one(res.lang) | required |
| `auto_redirect_lang` | Boolean | redirect to browser's language, default True |
| `homepage_url` | Char | e.g. `/contactus` or `/shop` |
| `theme_id` | Many2one(ir.module.module) | installed theme |
| `user_id` | Many2one(res.users) | Public User, required |
| `partner_id` | Many2one (related) | Public Partner |
| `menu_id` | Many2one(website.menu) | computed, main menu |
| `favicon` | Binary | website favicon |
| `logo` | Binary | website logo |
| `robots_txt` | Html | Robots.txt content, designer-only |
| `cookies_bar` | Boolean | display cookies consent bar |
| `cdn_activated` | Boolean | CDN switch |
| `cdn_url` | Char | CDN base URL |
| `cdn_filters` | Text | regex patterns for CDN URLs |
| `google_analytics_key` | Char | GA integration |
| `google_maps_api_key` | Char | Maps integration |
| `custom_code_head` | Html | custom `<head>` snippet |
| `custom_code_footer` | Html | custom `</body>` snippet |
| `block_third_party_domains` | Boolean | default True — blocks trackers |
| `auth_signup_uninvited` | Selection | `b2b` (invite) / `b2c` (free) |
| `specific_user_account` | Boolean | accounts scoped to this website |

### 2.3 Social Media Fields
`social_twitter`, `social_facebook`, `social_github`, `social_linkedin`, `social_youtube`, `social_instagram`, `social_tiktok`, `social_discord` — all Char, defaults from main company.
`social_default_image` — Binary override for social share image.

### 2.4 Uniqueness Constraint
```python
_domain_unique = models.Constraint('unique(domain)', 'Website Domain should be unique.')
```

### 2.5 Multi-Website Support
Multi-website is supported in Community but gated behind a feature group:
```python
# website.py line 328-331
if not self.env.user.has_group('website.group_multi_website') and self.search_count([]) > 1:
    ...
    groups.write({'implied_ids': [(4, self.env.ref('website.group_multi_website').id)]})
```
The `group_multi_website` is a settings-controlled group (`res_config_settings.py`):
```python
group_multi_website = fields.Boolean("Multi-website", implied_group="website.group_multi_website")
```
**Conclusion:** Community DOES support multiple websites per database, but the multi-website management UI is unlocked only when `group_multi_website` is enabled in Settings → Website.

### 2.6 `get_current_website()` Logic
Priority order:
1. Session-forced website (`force_website_id`)
2. Context `website_id`
3. Domain-matching against `request.httprequest.host`
4. Fallback: first website in DB (if `fallback=True`)

Domain matching is cached via `@tools.ormcache('domain_name', 'fallback')` on `_get_current_website_id`.

### 2.7 CDN Defaults
```python
DEFAULT_CDN_FILTERS = [
    "^/[^/]+/static/",
    "^/web/(css|js)/",
    "^/web/image",
    "^/web/content",
    "^/web/assets",
    "^/website/image/",
]
```

---

## 3. IR_HTTP ROUTING — `website/models/ir_http.py`

**Source path:** `odoo/addons/website/models/ir_http.py`

### 3.1 Model
```python
class IrHttp(models.AbstractModel):
    _inherit = 'ir.http'
```

### 3.2 `routing_map()` Override
Uses `request.website_routing` (website ID) as the routing key, enabling per-website routing maps:
```python
def routing_map(self, key=None):
    if not key and request:
        key = request.website_routing
    return super().routing_map(key=key)
```

### 3.3 `_match()` Override
Sets `request.website_routing` before URL matching:
```python
@classmethod
def _match(cls, path):
    if not hasattr(request, 'website_routing'):
        website = request.env['website'].with_context(lang=None).get_current_website()
        request.website_routing = website.id
    return super()._match(path)
```

### 3.4 `_generate_routing_rules()` Override
Injects URL rewrite rules (`website.rewrite`) into the routing map per website ID. Handles:
- 308 redirects: maps old URL → new URL
- 404 rules: suppresses specific URLs for that website

### 3.5 `_serve_page()` Class Method
Core CMS page dispatch:
```python
@classmethod
def _serve_page(cls):
    req_page = request.httprequest.path
    WebsitePage = request.env['website.page'].sudo()
    page_info = WebsitePage._get_page_info(request)
    ...
    if page_info:
        return WebsitePage.browse(page_info['id'])._get_response(request)
    return False
```

### 3.6 `_serve_fallback()` Override
Falls through: `_serve_page()` → `_serve_redirect()` → 404. `_serve_redirect()` checks `website.rewrite` for 301/302 redirects.

### 3.7 Visitor Tracking Hook
```python
@classmethod
def _register_website_track(cls, response):
    if request.env['ir.http'].is_a_bot(): return False
    if response.status_code != 200: return False
    ...
    request.env['website.visitor']._handle_webpage_dispatch(website_page)
```
Bot requests are excluded. Only 200 responses trigger tracking.

### 3.8 Auth Method Override
```python
@classmethod
def _auth_method_public(cls):
    if not request.session.uid:
        website = ...get_current_website()
        if website:
            request.update_env(user=website._get_cached('user_id'))
```
Assigns the website-specific public user for unauthenticated requests.

### 3.9 Slug Generation (`_slug`)
Prefers `seo_name` over `name` for URL slugs:
```python
if value.id and value.seo_name:
    return super()._slug((value.id, value.seo_name))
```

### 3.10 URL Rewriting (`_url_for`)
Applies `website.rewrite` rewrites before delegating to parent.

---

## 4. WEBSITE PAGE — `website/models/website_page.py`

**Source path:** `odoo/addons/website/models/website_page.py`

### 4.1 Model
```python
class WebsitePage(models.Model):
    _name = 'website.page'
    _inherits = {'ir.ui.view': 'view_id'}
    _inherit = [
        'website.published.multi.mixin',
        'website.searchable.mixin',
        'website.page_options.mixin',
    ]
    _description = 'Page'
    _order = 'website_id'
```

### 4.2 Key Fields
| Field | Type | Notes |
|---|---|---|
| `url` | Char | Page URL, required |
| `view_id` | Many2one(ir.ui.view) | delegated, required, cascade |
| `website_id` | Many2one (related via view_id) | stored, cascade |
| `arch` | Text (related) | QWeb template XML content |
| `website_indexed` | Boolean | indexing flag, default True |
| `date_publish` | Datetime | scheduled publish date |
| `menu_ids` | One2many(website.menu) | linked menu entries |
| `is_in_menu` | Boolean | computed, True if menu_ids |
| `is_homepage` | Boolean | computed, True if url == homepage_url |
| `is_visible` | Boolean | computed = published AND date constraint |
| `is_new_page_template` | Boolean | adds to "+New" templates |
| `view_write_uid` | Many2one (related) | last content editor |
| `view_write_date` | Datetime (related) | last content update date |

### 4.3 Publication Logic
```python
def _compute_visible(self):
    for page in self:
        page.is_visible = page.website_published and (
            not page.date_publish or page.date_publish < fields.Datetime.now()
        )
```

### 4.4 Website Scope
`website_id` is stored and comes through `view_id.website_id`. Pages with `website_id=False` are global (visible across all websites). Pages with a specific `website_id` are scoped to that website.

### 4.5 Cache
`_CACHE_DURATION = 3600` (1 hour) — rendered pages are cached for performance.

---

## 5. MULTI-WEBSITE SUPPORT

### 5.1 Availability in Community
Multi-website IS available in Community edition. The feature is toggled via:
- Config setting: `group_multi_website` in `res.config.settings`
- Implied group: `website.group_multi_website`

When enabled, the backend UI shows website selectors on menus, pages, products, etc.

### 5.2 Domain-Based Routing
Each `website` record has a `domain` field. The `_get_current_website_id` method matches the incoming HTTP host against stored domains (cached via `ormcache`). A unique constraint ensures no two websites share a domain.

### 5.3 `website.multi.mixin`
Models that can be scoped to a website inherit this:
```python
class WebsiteMultiMixin(models.AbstractModel):
    _name = 'website.multi.mixin'
    website_id = fields.Many2one("website", ondelete="restrict", index=True)
    
    def can_access_from_current_website(self, website_id=False):
        ...
        if (website_id or record.website_id.id) not in (False, request.env['website'].get_current_website().id):
            can_access = False
```

---

## 6. SEO METADATA — `website/models/mixins.py`

### 6.1 `WebsiteSeoMetadata` Abstract Model
```python
_name = 'website.seo.metadata'
```
Fields:
| Field | Type | Notes |
|---|---|---|
| `website_meta_title` | Char | Page `<title>`, translated |
| `website_meta_description` | Text | Meta description, translated |
| `website_meta_keywords` | Char | Meta keywords, translated |
| `website_meta_og_img` | Char | OpenGraph image URL |
| `seo_name` | Char | URL slug override, translated |
| `is_seo_optimized` | Boolean | computed: all 3 meta fields set |

### 6.2 OpenGraph and Twitter Card Generation
`_default_website_meta()` generates:
- `og:type`, `og:title`, `og:site_name`, `og:url`, `og:image`
- `twitter:card`, `twitter:title`, `twitter:image`

`get_website_meta()` merges record-specific overrides over these defaults.

### 6.3 `seo_name` in URL Slugs
`IrHttp._slug()` preferentially uses `value.seo_name` over `name` for generating URL slugs, enabling human-readable URLs independent of record names.

---

## 7. WEBSITE MENU — `website/models/website_menu.py`

**Source path:** `odoo/addons/website/models/website_menu.py`

### 7.1 Model
```python
_name = 'website.menu'
_description = "Website Menu"
_parent_store = True
_order = "sequence, id"
```

### 7.2 Fields
| Field | Type | Notes |
|---|---|---|
| `name` | Char | translated |
| `url` | Char | computed/stored, default `#` |
| `page_id` | Many2one(website.page) | linked CMS page, cascade |
| `controller_page_id` | Many2one(website.controller.page) | linked model page |
| `website_id` | Many2one(website) | cascade |
| `parent_id` | Many2one(website.menu) | hierarchy |
| `child_id` | One2many(website.menu) | children |
| `parent_path` | Char | indexed, _parent_store |
| `sequence` | Integer | ordering |
| `new_window` | Boolean | open in new tab |
| `is_visible` | Boolean | computed |
| `group_ids` | Many2many(res.groups) | visibility restriction |
| `is_mega_menu` | Boolean | computed from mega_menu_content |
| `mega_menu_content` | Html | translated, no-sanitize |
| `mega_menu_classes` | Char | CSS classes for mega menu |

### 7.3 URL Computation
```python
def _compute_url(self):
    for menu in self:
        if menu.is_mega_menu or menu.child_id:
            menu.url = "#"
        else:
            menu.url = (menu.page_id.url if menu.page_id else menu.url) or "#"
```
Mega menus and parent menus auto-set to `#`.

### 7.4 Multi-Website Display
```python
if not self.env.context.get('display_website') and not self.env.user.has_group('website.group_multi_website'):
    return super()._compute_display_name()
```
Website label added to menu name when multi-website is active.

---

## 8. VISITOR TRACKING — `website/models/website_visitor.py`

### 8.1 `website.track` Model
```python
_name = 'website.track'
_description = 'Visited Pages'
_order = 'visit_datetime DESC'
_log_access = False
```
Fields: `visitor_id`, `page_id` (website.page), `url` (Text), `visit_datetime`.

### 8.2 `website.visitor` Model
```python
_name = 'website.visitor'
_description = 'Website Visitor'
_order = 'id DESC'
```

Key fields:
| Field | Type | Notes |
|---|---|---|
| `name` | Char (related) | partner name |
| `access_token` | Char | unique; partner.id for logged-in, SHA1 hash for anon |
| `website_id` | Many2one(website) | readonly |
| `partner_id` | Many2one(res.partner) | computed, stored |
| `country_id` | Many2one(res.country) | readonly (GeoIP) |
| `lang_id` | Many2one(res.lang) | website language at creation |
| `timezone` | Selection | |
| `visit_count` | Integer | default 1; new visit after 8h gap |
| `website_track_ids` | One2many(website.track) | page visit history |
| `visitor_page_count` | Integer | computed |
| `page_count` | Integer | computed |
| `last_visited_page_id` | Many2one(website.page) | computed |
| `create_date` | Datetime | first connection |
| `last_connection_datetime` | Datetime | most recent page view |
| `is_connected` | Boolean | True if last view < 5 min ago |

### 8.3 Access Token Strategy
- Authenticated users: `partner_id.id` (integer cast)
- Anonymous users: `SHA1(remote_addr + user_agent + session_id)[:32]`

### 8.4 Dispatch Handler
```python
def _handle_webpage_dispatch(self, website_page):
    url = request.httprequest.url
    website_track_values = {'url': url}
    if website_page:
        website_track_values['page_id'] = website_page.id
    self._get_visitor_from_request(force_create=True, force_track_values=website_track_values)
```
Called from `IrHttp._register_website_track()` for non-bot, 200 responses on tracked views.

### 8.5 Cron Cleanup
`_cron_unlink_old_visitors()` with `batch_size=1000` — unlinks inactive visitors (previously archived, now hard-deleted to avoid DB bloat).

---

## 9. PORTAL + WEBSITE INTEGRATION

### 9.1 Dependency
`portal` is listed in `__manifest__.py` `depends`. The website controller `Website` inherits from `portal.controllers.web.Home`.

### 9.2 Published Multi-Mixin (`website.published.multi.mixin`)
```python
website_published = fields.Boolean(compute='_compute_website_published', ...)

def _compute_website_published(self):
    current_website_id = request.env['website'].get_current_website().id
    for record in self:
        record.website_published = record.is_published and (
            not record.website_id or record.website_id.id == current_website_id
        )
```
Published state is website-contextual: same record can appear published on one website and not another.

### 9.3 Portal User Auth
Portal users accessing website frontend receive the website's `user_id` (public user) if not authenticated. This is set in `_auth_method_public()`.

---

## 10. MAIN HTTP CONTROLLER — `website/controllers/main.py`

**Source path:** `odoo/addons/website/controllers/main.py`

### 10.1 Class
```python
class Website(Home):  # inherits from portal.controllers.web.Home
```

### 10.2 Index Route
```python
@http.route('/', auth="public", website=True, sitemap=True)
def index(self, **kw):
```
Fallback chain:
1. `homepage_url` reroute
2. `_serve_page()` for `/` CMS page
3. Controller match on homepage_url
4. First accessible menu redirect
5. 404

### 10.3 Multi-Website Force
```python
@http.route('/website/force/<int:website_id>', auth="user", website=True, sitemap=False, multilang=False, readonly=True)
def website_force(self, website_id, ...):
```
Requires `group_multi_website` + `group_website_restricted_editor`. Handles domain redirect for cross-domain website switching, then calls `website._force()`.

### 10.4 Constants
```
LOC_PER_SITEMAP = 45000    # max URLs per sitemap file
SITEMAP_CACHE_TIME = 12h   # sitemap cache TTL
MAX_FONT_FILE_SIZE = 10 MB
SUPPORTED_FONT_EXTENSIONS = ['ttf', 'woff', 'woff2', 'otf']
```

---

## CLAIMS SUMMARY TABLE (9-Column)

| # | Claim | Source File | Line(s) | Type | Confidence | Community? | Multi-W Impact | Notes |
|---|---|---|---|---|---|---|---|---|
| C01 | Module depends on portal, mail, auth_signup, http_routing, html_builder | `__manifest__.py` | 11-23 | STRUCTURAL | HIGH | YES | LOW | Core dependency chain |
| C02 | `website` model has unique domain constraint | `website.py` | 218-221 | STRUCTURAL | HIGH | YES | HIGH | Prevents domain conflicts across websites |
| C03 | `company_id` is required on each website record | `website.py` | 124 | STRUCTURAL | HIGH | YES | HIGH | Multi-tenant scoping |
| C04 | `language_ids` M2M allows multi-language per website | `website.py` | 125-127 | FUNCTIONAL | HIGH | YES | MEDIUM | Per-website language control |
| C05 | `get_current_website()` resolves via session > context > domain > fallback | `website.py` | 1375-1418 | BEHAVIORAL | HIGH | YES | HIGH | Core dispatch mechanism |
| C06 | Multi-website is gated by `group_multi_website` setting | `res_config_settings.py` | 104-106 | BEHAVIORAL | HIGH | YES | HIGH | Single toggle activates multi-site UI |
| C07 | `ir_http._match()` sets `request.website_routing` from current website | `ir_http.py` | 204-209 | BEHAVIORAL | HIGH | YES | HIGH | Per-website routing isolation |
| C08 | `_serve_page()` dispatches CMS pages from `website.page` model | `ir_http.py` | 298-321 | BEHAVIORAL | HIGH | YES | MEDIUM | Core CMS dispatch path |
| C09 | `_generate_routing_rules()` injects URL rewrites per website | `ir_http.py` | 120-149 | BEHAVIORAL | HIGH | YES | HIGH | Enables per-website URL rewriting |
| C10 | `website.page` inherits `ir.ui.view` via `_inherits` delegation | `website_page.py` | 27-33 | STRUCTURAL | HIGH | YES | LOW | Page = view + metadata |
| C11 | `website.page.url` is required; `website_indexed` defaults True | `website_page.py` | 38, 46 | STRUCTURAL | HIGH | YES | LOW | SEO and routing |
| C12 | Page visibility = published AND scheduled date check | `website_page.py` | 63-67 | BEHAVIORAL | HIGH | YES | LOW | Scheduled content support |
| C13 | `seo_name` field on SEO mixin drives URL slug generation | `mixins.py` + `ir_http.py` | 29, 66-71 | FUNCTIONAL | HIGH | YES | LOW | URL slug override |
| C14 | `website_meta_title/description/keywords` are per-record, translatable | `mixins.py` | 25-27 | FUNCTIONAL | HIGH | YES | LOW | Multilingual SEO |
| C15 | `website.menu` uses `_parent_store=True` for hierarchical navigation | `website_menu.py` | 20 | STRUCTURAL | HIGH | YES | MEDIUM | Efficient subtree queries |
| C16 | Mega menu content is stored as HTML, unsanitized | `website_menu.py` | 56 | STRUCTURAL | HIGH | YES | LOW | Designer-controlled rich menus |
| C17 | `website.visitor` uses SHA1 of IP+UA+session for anonymous tokens | `website_visitor.py` | 41-49 | BEHAVIORAL | HIGH | YES | LOW | Privacy-safe visitor identification |
| C18 | Visitor tracking only fires on 200 responses, non-bot requests | `ir_http.py` | 183-200 | BEHAVIORAL | HIGH | YES | LOW | Prevents spurious tracking |
| C19 | `website.track` records page+URL per visitor with 30-min dedup | `website_visitor.py` | 305-312 | BEHAVIORAL | HIGH | YES | LOW | Dedup prevents flooding |
| C20 | `WebsitePublishedMixin._compute_website_published` is website-contextual | `mixins.py` | 287-293 | BEHAVIORAL | HIGH | YES | HIGH | Published state differs per website |
