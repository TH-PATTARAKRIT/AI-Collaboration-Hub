# U131 — Function-ID Mapping G10–G16 (restricted technical evidence)

> RESTRICTED — TECHNICAL EVIDENCE — NOT FOR NEUTRAL DISTRIBUTION
> Status: DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION
- Unit: U131
- Scope: GAP-034 — Function-ID mapping for units U47–U68 (G10–G16 capability groups)
- Source revision: 19.0.post20260921 (Odoo 19 Community only)
- Date: 2026-10-02
- Scope notes: F-ID mapping pass for units whose handoff packets carry "FUNCTION MAPPING REQUIRED" or no existing Function-ID citations. Pointer is the handoff packet for each unit; anchor is the Capabilities in scope section. F-ID naming follows the convention established in U01–U46: DOMAIN-FNN where DOMAIN is a 2–4 letter abbreviation and NN is a two-digit ordinal. New domains introduced in this unit: EDI, AUTH, SYS, CRM, HRM, PAY, SMS, STK, WEB, WST, MKT, POS. Extensions to existing domains: BRP (→F10, F11), MSG (→F05), MFG (→F06, F07), PDT (→F05), IAV (→F07), SDV (→F08).

---

## Existing domain reference (as of U01–U130)

| Domain | Meaning | Highest F-ID used |
|--------|---------|------------------|
| ACR | Account configuration / accrual | ACR-F02 |
| BRP | Bank reconciliation and payment | BRP-F09 |
| GRV | Goods receipt voucher | GRV-F07 |
| IAV | Inventory accounting valuation | IAV-F06 |
| INV | Invoicing | INV-F04 |
| MCT | Multi-company transactions | MCT-F05 |
| MFG | Manufacturing | MFG-F05 |
| MSG | Messaging (mail) | MSG-F04 |
| PCO | Purchase contract / order | PCO-F04 |
| PDT | Product master | PDT-F04 |
| PUR | Purchase | PUR-F005 |
| RCN | Reconciliation | RCN-F03 |
| RPT | Reporting | RPT-F02 |
| RTG | Routing | RTG-F04 |
| SDV | Sales delivery voucher | SDV-F07 |
| THX | Thai export localization | THX-F03 |
| TXC | Tax configuration | TXC-F12 |

---

## New domains introduced in U131

| Domain | Meaning | Rationale |
|--------|---------|-----------|
| AUTH | Authentication / identity | auth_passkey introduces FIDO2 passkey flows not covered by any existing domain |
| CRM | Customer relationship management | crm_iap_mine and crm bridge modules form a distinct pipeline domain |
| EDI | Electronic document interchange | account_edi_ubl_cii, PEPPOL, UBL/CII/Factur-X form a structured e-invoicing domain |
| HRM | Human resources management | hr sub-module cluster (homeworking, skills, timesheet) is a distinct HR sub-domain |
| MKT | Marketing and mass mailing | mass_mailing, marketing_card, UTM tracking form a marketing execution domain |
| PAY | Payment processing | payment module (providers, tokens, capture/void/refund) is not BRP (bank-side); PAY covers provider-side transactions |
| POS | Point of sale | point_of_sale session/order lifecycle is a distinct commerce domain |
| SMS | SMS messaging | sms module (sms.sms, IAP, Twilio) is a channel domain separate from mail (MSG) |
| STK | Stock operations | stock sub-models not in IAV: lots, reorder rules, batch transfers, scrap |
| SYS | System base framework | ir.* base models (module, view, qweb, http, filters) and web infrastructure |
| WEB | Web client | web module: home/session controllers, RPC endpoints, webclient data methods |
| WST | Website platform | website module and all website_* bridge modules |

---

## VDR Claims Table

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|---|---|---|---|---|---|---|---|---|
| VDR-U131-C001 | BRP-F10 | 04_HANDOFF_PACKETS/HP_U47.md | CAP-U47-01 Capabilities in scope | C1 | account installed | C1, F-ID, GAP | Unit U47 CAP-U47-01 maps to BRP-F10: the bank statement line model uses _inherits delegation to account.move and maintains is_reconciled / amount_residual via SQL-computed running balance; reconciliation undoes via remove_move_reconcile with reset to suspense lines. | N-U131-001 |
| VDR-U131-C002 | BRP-F11 | 04_HANDOFF_PACKETS/HP_U47.md | CAP-U47-08 Capabilities in scope | C1 | account installed | C1, F-ID, GAP | Unit U47 CAP-U47-08 maps to BRP-F11: the reconcile model defines automated bank statement matching rules (partner lookup, account lookup, tolerance thresholds) used to propose counterpart entries during bank reconciliation. | N-U131-002 |
| VDR-U131-C003 | BRP-F12 | 04_HANDOFF_PACKETS/HP_U47.md | CAP-U47-03 Capabilities in scope | C1 | account installed | C1, F-ID, GAP | Unit U47 CAP-U47-03 maps to BRP-F12: the Payment Register wizard batches outstanding invoice lines into a single account.payment record, supports partial payment, currency conversion, and writeoff journal entries. | N-U131-003 |
| VDR-U131-C004 | RCN-F04 | 04_HANDOFF_PACKETS/HP_U47.md | CAP-U47-06 Capabilities in scope | C1 | account installed | C1, F-ID, GAP | Unit U47 CAP-U47-06 maps to RCN-F04: the partial reconcile model stores each pairwise matching between two account.move.lines with an amount_currency, and drives the tax cash-basis engine that posts cash-basis tax entries when payment is matched to invoice. | N-U131-004 |
| VDR-U131-C005 | EDI-F01 | 04_HANDOFF_PACKETS/HP_U48.md | CAP-U48-03 through CAP-U48-09 Capabilities in scope | C1 | account_edi_ubl_cii installed | C1, F-ID, GAP | Unit U48 CAPs 03–09 map to EDI-F01: the account_edi_ubl_cii module exports invoices in UBL 2.0/2.1, CII/Factur-X, and Peppol BIS 3 formats via an inheritance chain of node-builder mixins; each format type is controlled by a dedicated edi.format record and document builder class. | N-U131-005 |
| VDR-U131-C006 | EDI-F02 | 04_HANDOFF_PACKETS/HP_U48.md | CAP-U48-10 Capabilities in scope | C1 | account_edi_ubl_cii installed | C1, F-ID, GAP | Unit U48 CAP-U48-10 maps to EDI-F02: the inbound EDI import flow parses a UBL or CII XML attachment attached to an incoming email or uploaded manually and creates a draft vendor bill with mapped header, party, tax, and line fields. | N-U131-006 |
| VDR-U131-C007 | AUTH-F01 | 04_HANDOFF_PACKETS/HP_U49.md | CAP-U49-01 through CAP-U49-20 Capabilities in scope | C1 | auth_passkey installed | C1, F-ID, GAP | Unit U49 maps to AUTH-F01: the auth_passkey module implements FIDO2 passkey authentication storing public keys via raw SQL in the auth.passkey.key model; the login hook overrides _login to bypass MFA for passkey-verified users; start-auth and start-registration routes handle WebAuthn challenge/response. | N-U131-007 |
| VDR-U131-C008 | SYS-F01 | 04_HANDOFF_PACKETS/HP_U50.md | CAP-U50-01 through CAP-U50-11 Capabilities in scope | C1 | base installed | C1, F-ID, GAP | Unit U50 maps to SYS-F01: the base ir.* model set covers module state machine (ir.module.module), view inheritance and architecture combining (ir.ui.view), QWeb template rendering (ir.qweb), HTTP routing (ir.http), outgoing mail server, saved search filters, export templates, profiling records, country/state reference data, currency with exchange rates, and decimal precision. | N-U131-008 |
| VDR-U131-C009 | CRM-F01 | 04_HANDOFF_PACKETS/HP_U51.md | CAP-U51-01 Capabilities in scope | C1 | crm_iap_mine installed | C1, F-ID, GAP | Unit U51 CAP-U51-01 maps to CRM-F01: the crm_iap_mine module enriches lead pipeline via IAP lead mining, sending company criteria to the IAP endpoint and creating new CRM leads from returned company data. | N-U131-009 |
| VDR-U131-C010 | HRM-F01 | 04_HANDOFF_PACKETS/HP_U51.md | CAP-U51-09 through CAP-U51-20 Capabilities in scope | C1 | hr installed | C1, F-ID, GAP | Unit U51 CAPs 09–20 map to HRM-F01: the HR sub-module cluster covers homeworking calendar, hourly cost on employee, maintenance integration, recruitment SMS, skills linkage to events and slides, timesheet/attendance bridge. | N-U131-010 |
| VDR-U131-C011 | MSG-F05 | 04_HANDOFF_PACKETS/HP_U52.md | CAP-U52-01 through CAP-U52-10 Capabilities in scope | C1 | mail installed | C1, F-ID, GAP | Unit U52 maps to MSG-F05: the mail core covers mail.template rendering via Jinja/QWeb, mail.compose.message wizard for bulk and single send, mail.alias and mail.alias.domain for inbound routing, mail.followers for subscription management, and mail.notification for delivery tracking. | N-U131-011 |
| VDR-U131-C012 | MFG-F06 | 04_HANDOFF_PACKETS/HP_U53.md | CAP-U53-05 through CAP-U53-09 Capabilities in scope | C1 | mrp installed | C1, F-ID, GAP | Unit U53 CAPs 05–09 map to MFG-F06: the MRP work order lifecycle defines scheduling (plan_workorder), duration tracking, and workcenter capacity on mrp.workorder and mrp.workcenter; mrp.routing.workcenter attaches operations to bill-of-materials routing steps. | N-U131-012 |
| VDR-U131-C013 | MFG-F07 | 04_HANDOFF_PACKETS/HP_U53.md | CAP-U53-10 through CAP-U53-14 Capabilities in scope | C1 | mrp installed | C1, F-ID, GAP | Unit U53 CAPs 10–14 map to MFG-F07: the MRP unbuild order reverses a finished production order returning components to stock; mrp_product_expiry enforces lot expiry on manufacturing orders; mrp_subcontracting_landed_costs and mrp_subcontracting_repair extend the subcontracting flow. | N-U131-013 |
| VDR-U131-C014 | PAY-F01 | 04_HANDOFF_PACKETS/HP_U54.md | CAP-U54-01 through CAP-U54-04 Capabilities in scope | C1 | payment installed | C1, F-ID, GAP | Unit U54 CAPs 01–04 map to PAY-F01: the payment module defines payment.provider configuration (state machine, acquirer credentials, capture mode), payment.token lifecycle (active/archived), and the manual capture / void / refund flow via action_capture / action_void / action_refund on payment.transaction; the payment link wizard generates shareable URLs. | N-U131-014 |
| VDR-U131-C015 | PDT-F05 | 04_HANDOFF_PACKETS/HP_U54.md | CAP-U54-05 through CAP-U54-10 Capabilities in scope | C1 | product installed | C1, F-ID, GAP | Unit U54 CAPs 05–10 map to PDT-F05: the product catalog mixin adds a standardized add-to-cart / price computation API reused by sale and ecommerce; combo products group multiple components with individual pricing; product.supplierinfo stores vendor pricelist lines with minimum quantities and lead times; product.document attaches technical files to product variants. | N-U131-015 |
| VDR-U131-C016 | SDV-F08 | 04_HANDOFF_PACKETS/HP_U56.md | CAP-U56-01 through CAP-U56-08 Capabilities in scope | C1 | sale installed | C1, F-ID, GAP | Unit U56 CAPs 01–08 map to SDV-F08: the sale bridge modules wire sale order margins into expense, MRP, and timesheet cost flows; the Gelato and project-stock-account bridges add fulfillment channels; sale_service defines service product invoicing policy; sale_sms attaches SMS notifications to sale order confirmation. | N-U131-016 |
| VDR-U131-C017 | SMS-F01 | 04_HANDOFF_PACKETS/HP_U56.md | CAP-U56-09 through CAP-U56-24 Capabilities in scope | C1 | sms installed | C1, F-ID, GAP | Unit U56 CAPs 09–24 map to SMS-F01: the sms module defines sms.sms for outbound message records, SmsApi for IAP-based delivery, sms.template for dynamic content, sms.tracker for delivery status, and the sms.composer wizard for bulk dispatch; the Twilio submodule routes delivery through a Twilio company-level configuration and handles incoming status webhooks. | N-U131-017 |
| VDR-U131-C018 | STK-F01 | 04_HANDOFF_PACKETS/HP_U57.md | CAP-U57-01 through CAP-U57-04 Capabilities in scope | C1 | stock installed | C1, F-ID, GAP | Unit U57 CAPs 01–04 map to STK-F01: stock.lot stores lot/serial traceability with expiry dates; stock.warehouse.orderpoint defines min/max reorder rules with lead-time scheduling; stock.rule encodes procurement routing logic (buy / manufacture / resupply); stock.move.line represents detailed per-lot or per-package operation lines. | N-U131-018 |
| VDR-U131-C019 | STK-F02 | 04_HANDOFF_PACKETS/HP_U57.md | CAP-U57-05 through CAP-U57-08 Capabilities in scope | C1 | stock installed | C1, F-ID, GAP | Unit U57 CAPs 05–08 map to STK-F02: replenishment wizards compute orderpoint quantities and create purchase or manufacture orders; stock.picking.batch groups multiple transfers for wave or batch picking; stock.scrap records component loss with a dedicated scrap location move; configuration settings expose lot tracking, package, and batch picking switches. | N-U131-019 |
| VDR-U131-C020 | IAV-F07 | 04_HANDOFF_PACKETS/HP_U58.md | CAP-U58-01 Capabilities in scope | C1 | stock_account installed | C1, F-ID, GAP | Unit U58 CAP-U58-01 maps to IAV-F07: the stock_account module extends stock.valuation.layer to record the accounting side of every inventory move, linking each valuation layer to an account.move entry for AVCO and standard-cost methods; the account.move reconciliation for landed costs is also handled here. | N-U131-020 |
| VDR-U131-C021 | WEB-F01 | 04_HANDOFF_PACKETS/HP_U59.md | CAP-U59-01 through CAP-U59-19 Capabilities in scope | C1 | web installed | C1, F-ID, GAP | Unit U59 maps to WEB-F01: the web module delivers the home controller and web client bootstrap, the session controller, the call_kw RPC endpoint, the binary and attachment serving controller, the export and report controllers, the action controller, and the web_read / web_save / web_search_read / web_read_group model methods; web_tour and web_hierarchy provide guided tours and hierarchical list views. | N-U131-021 |
| VDR-U131-C022 | WST-F01 | 04_HANDOFF_PACKETS/HP_U60.md | CAP-U60-01 through CAP-U60-12 Capabilities in scope | C1 | website installed | C1, F-ID, GAP | Unit U60 maps to WST-F01: the website module implements copy-on-write view isolation per website instance, visitor tracking with session attribution, URL rewriting and canonical management, website menu tree management, a generic form controller, the blog publishing system, and website-scoped CRM lead capture with IAP company reveal. | N-U131-022 |
| VDR-U131-C023 | WST-F02 | 04_HANDOFF_PACKETS/HP_U61.md | CAP-U61-01 through CAP-U61-15 Capabilities in scope | C1 | website installed | C1, F-ID, GAP | Unit U61 maps to WST-F02: the website extension modules add a karma-gated forum, public partner directory, online HR recruitment with livechat chatbot, link short-tracking with UTM attribution, live chat visitor widget, email subscription management, multi-website payment provider and donation flow, karma-based public user profile, task submission portal, and eLearning courses with quizzes and enrollment. | N-U131-023 |
| VDR-U131-C024 | EDI-F03 | 04_HANDOFF_PACKETS/HP_U62.md | CAP-U62-01 through CAP-U62-05 Capabilities in scope | C1 | account_peppol installed | C1, F-ID, GAP | Unit U62 CAPs 01–05 map to EDI-F03: the account_peppol module manages PEPPOL access point registration and proxy state via an account.edi.proxy.user record, sends and receives PEPPOL documents through the proxy API, verifies partner PEPPOL identifiers, and adds advanced EAS/GLN fields; account_qr_code_sepa generates SEPA-compliant QR code payment data on invoices. | N-U131-024 |
| VDR-U131-C025 | MKT-F01 | 04_HANDOFF_PACKETS/HP_U62.md | CAP-U62-12 through CAP-U62-13 Capabilities in scope | C1 | mass_mailing installed | C1, F-ID, GAP | Unit U62 CAPs 12–13 map to MKT-F01: the mass_mailing module defines mailing.mailing for bulk email campaigns with A/B testing, unsubscribe management, and delivery statistics; bridge modules wire mass mailing to events, SMS, CRM leads, and sale orders. | N-U131-025 |
| VDR-U131-C026 | PAY-F02 | 04_HANDOFF_PACKETS/HP_U63.md | CAP-U63-01 Capabilities in scope | C1 | payment installed | C1, F-ID, GAP | Unit U63 CAP-U63-01 maps to PAY-F02: the payment provider webhook architecture pattern defines a signed notification controller, a _verify_notification_data abstract method for provider-specific signature validation, and a _process_notification_data flow that looks up the transaction by reference and drives it through the state machine (authorized / done / error / cancel). | N-U131-026 |
| VDR-U131-C027 | POS-F01 | 04_HANDOFF_PACKETS/HP_U64.md | CAP-U64-01 through CAP-U64-05 Capabilities in scope | C1 | point_of_sale installed | C1, F-ID, GAP | Unit U64 CAPs 01–05 map to POS-F01: the point_of_sale module defines pos.session lifecycle (opening / closing cash control), pos.order processing with tax computation and product catalog, pos.config with multi-payment-method setup, and extension modules for loyalty, gift cards, and restaurant table management. | N-U131-027 |
| VDR-U131-C028 | WST-F03 | 04_HANDOFF_PACKETS/HP_U65.md | CAP-U65-01 through CAP-U65-07 Capabilities in scope | C1 | website_sale installed | C1, F-ID, GAP | Unit U65 CAPs 01–07 map to WST-F03: the website_sale module delivers the ecommerce product catalog with pricelist rendering, the cart and checkout flow with address collection, integration with payment providers via the payment form controller, conversion of website sale orders into confirmed sale orders, and bridge modules for events, mass mailing, gift cards, and wishlists. | N-U131-028 |
| VDR-U131-C029 | EDI-F04 | 04_HANDOFF_PACKETS/HP_U68.md | CAP-U68-01 Capabilities in scope | C1 | account_peppol installed | C1, F-ID, GAP | Unit U68 CAP-U68-01 maps to EDI-F04: PEPPOL response processing parses inbound PEPPOL document responses (acknowledgement / rejection / processing error codes) returned by the access point proxy and updates the corresponding account.move edi state accordingly. | N-U131-029 |
| VDR-U131-C030 | POS-F02 | 04_HANDOFF_PACKETS/HP_U68.md | CAP-U68-02 through CAP-U68-06 Capabilities in scope | C1 | point_of_sale installed | C1, F-ID, GAP | Unit U68 CAPs 02–06 map to POS-F02: the POS payment provider extension modules (Mercado Pago, Mollie, Pine Labs, QFPay, Razorpay) each provide a payment method configuration model and a JavaScript payment terminal handler that drives the provider-specific capture flow from within the POS session frontend. | N-U131-030 |

---

## F-ID assignment summary

| F-ID | Unit(s) | Domain | Capability cluster |
|------|---------|--------|-------------------|
| BRP-F10 | U47 | BRP | Bank statement line model and reconciliation engine |
| BRP-F11 | U47 | BRP | Reconcile model / bank statement matching rules |
| BRP-F12 | U47 | BRP | Payment register wizard |
| RCN-F04 | U47 | RCN | Partial reconcile model and tax cash-basis engine |
| EDI-F01 | U48 | EDI | UBL/CII document export architecture (UBL 2.x, Factur-X, BIS 3) |
| EDI-F02 | U48 | EDI | Inbound EDI import flow |
| AUTH-F01 | U49 | AUTH | Passkey FIDO2 authentication |
| SYS-F01 | U50 | SYS | Base framework — ir.* models and reference data |
| CRM-F01 | U51 | CRM | CRM IAP lead mining and bridge modules |
| HRM-F01 | U51 | HRM | HR sub-module cluster |
| MSG-F05 | U52 | MSG | Mail core: template, alias, followers, compose wizard |
| MFG-F06 | U53 | MFG | MRP work order scheduling and workcenter |
| MFG-F07 | U53 | MFG | MRP unbuild, subcontracting, expiry |
| PAY-F01 | U54 | PAY | Payment provider configuration, token, capture/void/refund |
| PDT-F05 | U54 | PDT | Product catalog mixin, combo products, supplier pricelist |
| SDV-F08 | U56 | SDV | Sale bridge modules (expense/MRP/timesheet margins) |
| SMS-F01 | U56 | SMS | SMS core: sms.sms, IAP delivery, Twilio |
| STK-F01 | U57 | STK | Stock lot/serial tracking, reorder rules, procurement rules |
| STK-F02 | U57 | STK | Replenishment wizards, batch picking, scrap |
| IAV-F07 | U58 | IAV | Inventory valuation architecture (stock_account) |
| WEB-F01 | U59 | WEB | Web client bootstrap, RPC, action controller |
| WST-F01 | U60 | WST | Website core: COW isolation, visitor tracking, URL rewriting |
| WST-F02 | U61 | WST | Website extension modules |
| EDI-F03 | U62 | EDI | PEPPOL registration, document sending, partner verification |
| MKT-F01 | U62 | MKT | Mass mailing core |
| PAY-F02 | U63 | PAY | Payment provider webhook architecture |
| POS-F01 | U64 | POS | POS session lifecycle, order processing, payment methods |
| WST-F03 | U65 | WST | Website sale: catalog, cart, checkout, payment |
| EDI-F04 | U68 | EDI | PEPPOL response processing |
| POS-F02 | U68 | POS | POS payment provider extensions |

**Note on U66/U67:** Both handoff packets have empty Capabilities in scope sections; no F-ID mapping is possible for these units pending content remediation.
