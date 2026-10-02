# U187 — UTM Tracking: Neutral Knowledge Reference
**Unit:** U187 | **Group:** G15 | **Priority:** P3  
**Scope:** Odoo Community 19.0 — neutral business-level description, no raw code keywords  
**Date:** 2026-10-02

---

## VDR Claims Table (9 Claims)

| # | Claim ID | Scope | Claim Statement | Evidence Source | Confidence | Gate | Notes |
|---|---|---|---|---|---|---|---|
| 1 | U187-C01 | utm.campaign fields | A marketing campaign record stores two name-type fields: a human-readable title (the display name) and a computed unique identifier derived from the title. It also carries an owner user, a lifecycle stage, a colour index, a multi-value tag list, and a flag marking it as automatically generated. The active flag controls visibility in searches. | `utm/models/utm_campaign.py` | HIGH | PASS | `_rec_name = 'title'`; `name` is slug-style, unique DB constraint |
| 2 | U187-C02 | utm.mixin fields | The tracking mixin injects three optional relationship fields into any consumer model: references to the campaign, the traffic source, and the delivery medium. All three carry a database index optimised for sparse population (not-null B-tree), meaning queries filter efficiently even when most rows have no UTM data. | `utm/models/utm_mixin.py` lines 18–23 | HIGH | PASS | `btree_not_null` index on all three fields |
| 3 | U187-C03 | utm.mixin default population | When a user opens a new record that inherits the tracking mixin, the system automatically reads browser cookies to pre-fill the three UTM fields. This requires an active web request. The logic is skipped for ordinary salespeople to avoid overwriting intentional empty values; it applies to superusers regardless. If the cookie holds a text string rather than a database ID, the system finds or creates the matching lookup record automatically. | `utm/models/utm_mixin.py` lines 26–46 | HIGH | PASS | Salesman group exclusion: `sales_team.group_sale_salesman` |
| 4 | U187-C04 | URL param → cookie mapping | Three URL query parameters (`utm_campaign`, `utm_source`, `utm_medium`) are captured on every HTTP response and persisted as browser cookies (`odoo_utm_campaign`, `odoo_utm_source`, `odoo_utm_medium`) for 31 days. The capture logic lives in the HTTP dispatch layer and fires after every page request, not only on landing pages. The cookie domain is the host of the current request. | `utm/models/ir_http.py` + `utm_mixin.py:tracking_fields()` | HIGH | PASS | Cookie TTL: `31 * 24 * 3600` seconds |
| 5 | U187-C05 | sale.order UTM linkage | Sales orders inherit the tracking mixin. The three UTM relationship fields are overridden to use a soft-delete policy: when a campaign, source, or medium record is deleted, the reference on existing orders is set to null rather than blocking the delete. When a sales order is invoiced, the three UTM references are copied verbatim onto the resulting invoice document, continuing the attribution chain into accounting. | `sale/models/sale_order.py` lines 284–286, 1433–1435 | HIGH | PASS | Invoice preparation method `_prepare_invoice()` copies UTM triplet |
| 6 | U187-C06 | consumer model coverage | In Community edition the tracking mixin is applied to: sales orders, accounting move documents (added by the sale addon, not by the accounting addon itself), CRM pipeline leads and opportunities, recruitment job applications, and tracked marketing links. Survey responses indirectly gain UTM context through the CRM survey bridge. | Multiple addons | HIGH | PASS | `account.move` UTM is in `sale/models/account_move.py`, NOT base `account` |
| 7 | U187-C07 | utm.stage lifecycle | Campaign stages are a simple ordered list with a name and a sequence number. One default stage named "New" is always installed (not a demo record). Campaigns require a stage; the stage cannot be deleted while campaigns reference it. The kanban board always displays all stages, even empty ones. | `utm/models/utm_stage.py` + `utm_stage_data.xml` | HIGH | PASS | `ondelete='restrict'` on campaign.stage_id; stage data is always-install not demo |
| 8 | U187-C08 | No revenue fields in core UTM | The UTM module itself carries no revenue, turnover, or conversion-value fields on any of its models. Revenue attribution is achieved indirectly: the sale addon copies UTM fields onto invoice records, and business-intelligence reporting must aggregate invoice amounts grouped by the UTM triplet. There is no prebuilt revenue summary on the campaign model in Community. | All UTM model files searched | HIGH | PASS | No `revenue`, `amount`, or `turnover` field found in any utm model |
| 9 | U187-C09 | Company scope: shared, no medium _compute_name, tags on campaigns | UTM records (campaigns, sources, mediums, stages, tags) carry no company field and are visible and reusable across all companies in a multi-company deployment. The medium model has no computed name method — the name is a plain text field with a unique constraint managed via the shared uniqueness utility. Campaigns carry a many-to-many tag list (utm.tag) for categorisation; tags have a name and a colour. | All UTM model files | HIGH | PASS | No `company_id` on any UTM model; `utm.medium.name` = plain Char; `tag_ids` M2M on `utm.campaign` |

---

## Functional Summary

### What UTM tracking does in Odoo

UTM (Urchin Tracking Module) tracking allows businesses to identify which marketing channel, campaign, or source generated a lead, order, or other business event. When a prospect clicks a marketing link containing standard UTM query parameters, Odoo captures those parameters in browser cookies. When the visitor subsequently submits any tracked form — a contact form, a webshop order, a job application — the stored cookie values are used to pre-populate the attribution fields on the new record.

### Campaign lifecycle

Campaigns progress through configurable stages displayed on a kanban board. They can be tagged for categorisation. An "automatically generated" flag distinguishes campaigns created on-the-fly from URL params versus those created deliberately by a marketing manager.

### Attribution chain

The full attribution chain in Community is:
1. Marketing link carrying UTM params is clicked.
2. Browser cookie is set for 31 days.
3. Visitor creates a CRM lead, sales order, or job application.
4. The system reads the cookie and links the record to the appropriate campaign, source, and medium.
5. When the sales order is invoiced, the invoice inherits the same UTM triplet.

### Scope limitations (Community vs Enterprise)

Community provides the data model and cookie capture mechanism. It does not provide:
- Revenue dashboards on campaigns
- ROI/cost tracking per campaign
- Email marketing campaign management (that is in `mass_mailing` which uses `utm.source.mixin`)
- Social media campaign management

---

## Lookup Records Seeded at Install

### Mediums (10 records, noupdate=1)
Website, Phone, Direct, Email, Banner, X (Twitter), Facebook, LinkedIn, Television, Google Adwords

### Sources (10 records, noupdate=1)
Search engine, Lead Recall, Newsletter, Facebook, X, LinkedIn, Monster, Glassdoor, Craigslist, Referral

### Stages (1 record, always-install)
"New" at sequence=10
