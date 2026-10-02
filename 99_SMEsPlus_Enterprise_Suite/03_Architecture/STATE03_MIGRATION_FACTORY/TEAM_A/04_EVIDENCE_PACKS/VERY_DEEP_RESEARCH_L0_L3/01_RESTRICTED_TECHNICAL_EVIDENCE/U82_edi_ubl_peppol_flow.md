# U82 — EDI/UBL/PEPPOL Full Flow (L3/L4)
**Unit**: U82
**Phase**: Second-Pass Depth Closure — P1 Core Business
**Scope**: UBL/CII XML generation, PEPPOL proxy upload, EDI document state machine, incoming processing
**Modules**: account_edi, account_edi_ubl_cii, account_peppol, account_edi_proxy_client
**Function-IDs targeted**: NEW:U82-FXX (EDI functions not yet catalogued)
**L-levels**: L3, L4
**Proof layers**: P2, P4
**Date**: 2026-10-02
**Status**: GATE-PASS
**Predecessor**: U27, U48

---

## Module Existence and License Confirmation

All four EDI modules confirmed present under addons/ as Community (LGPL-3):
- `account_edi` — license: LGPL-3
- `account_edi_ubl_cii` — license: LGPL-3
- `account_peppol` — license: LGPL-3
- `account_edi_proxy_client` — license: LGPL-3

Additional modules found: `account_peppol_advanced_fields`, `account_peppol_response`, `l10n_account_edi_ubl_cii_tests`.

---

## Claims

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|---|---|---|---|---|---|---|---|---|
| U82-001 | U82-F01 | account_edi/models/account_edi_format.py:7 | `_name = 'account.edi.format'` | DEF | | | account.edi.format model defined in account_edi; fields: name (Char), code (Char required, unique) | NR-U82-001 |
| U82-002 | U82-F01 | account_edi/models/account_edi_format.py:58 | `def _get_move_applicability(self, move):` | DEF | | | _get_move_applicability() returns dict of callables: post, cancel, post_batching, cancel_batching, edi_content; core dispatch function for EDI processing | NR-U82-002 |
| U82-003 | U82-F01 | account_edi/models/account_edi_format.py:71 | `def _needs_web_services(self):` | DEF | | | _needs_web_services() returns False by default; overridden by formats that require async web-service calls | NR-U82-003 |
| U82-004 | U82-F02 | account_edi/models/account_edi_document.py:14 | `_name = 'account.edi.document'` | DEF | | | account.edi.document model defined; links account.move to account.edi.format via move_id and edi_format_id | NR-U82-004 |
| U82-005 | U82-F02 | account_edi/models/account_edi_document.py:26 | `state = fields.Selection([('to_send', 'To Send'), ('sent', 'Sent'), ('to_cancel', 'To Cancel'), ('cancelled', 'Cancelled')])` | DEF | | | account.edi.document state machine has four states: to_send, sent, to_cancel, cancelled | NR-U82-005 |
| U82-006 | U82-F02 | account_edi/models/account_edi_document.py:200 | `def _process_documents_no_web_services(self):` | DEF | | | _process_documents_no_web_services() processes synchronous EDI formats immediately (no web service needed) | NR-U82-006 |
| U82-007 | U82-F02 | account_edi/models/account_edi_document.py:207 | `def _process_documents_web_services(self, job_count=None, with_commit=True):` | DEF | | | _process_documents_web_services() processes async EDI formats that require web services; uses locking to prevent concurrent processing | NR-U82-007 |
| U82-008 | U82-F02 | account_edi/models/account_edi_document.py:236 | `def _cron_process_documents_web_services(self, job_count=None):` | DEF | | | _cron_process_documents_web_services() is the cron entry point; searches all to_send/to_cancel documents with state=posted and processes them | NR-U82-008 |
| U82-009 | U82-F03 | account_edi/models/account_move.py:233 | `def _post(self, soft=True):` | OVERRIDE | | | account.move._post() override creates account.edi.document records with state='to_send' for each applicable EDI format on the journal, then calls _process_documents_no_web_services() | NR-U82-009 |
| U82-010 | U82-F03 | account_edi/models/account_move.py:261 | `self.env['account.edi.document'].create(edi_document_vals_list)` | CALL | | | EDI documents are created inside _post() after super() call; one document per format per move | NR-U82-010 |
| U82-011 | U82-F03 | account_edi/models/account_move.py:263 | `self.env.ref('account_edi.ir_cron_edi_network')._trigger()` | CALL | | | EDI cron is triggered immediately after _post() to process web-service documents | NR-U82-011 |
| U82-012 | U82-F03 | account_edi/models/account_move.py:343 | `def _get_edi_document(self, edi_format):` | DEF | | | _get_edi_document() filters edi_document_ids by edi_format to return the specific EDI document for a format | NR-U82-012 |
| U82-013 | U82-F04 | account_edi_ubl_cii/models/account_edi_xml_ubl_20.py:18 | `_name = "account.edi.xml.ubl_20"` | DEF | | | AccountEdiXmlUBL20 is the base UBL 2.0 abstract model; inherits account.edi.ubl | NR-U82-013 |
| U82-014 | U82-F04 | account_edi_ubl_cii/models/account_edi_xml_ubl_20.py:39 | `def _export_invoice(self, invoice):` | DEF | | | _export_invoice() generates UBL 2.0 XML for an invoice: validates taxes, builds document_node dict, runs constraints, calls dict_to_xml(), returns (bytes, errors) | NR-U82-014 |
| U82-015 | U82-F04 | account_edi_ubl_cii/models/account_edi_xml_ubl_20.py:55 | `return etree.tostring(xml_content, xml_declaration=True, encoding='UTF-8'), set(errors)` | RETURN | | | _export_invoice() returns UTF-8 encoded XML bytes and a set of error strings | NR-U82-015 |
| U82-016 | U82-F05 | account_edi_ubl_cii/models/account_edi_xml_ubl_21.py:4 | `_name = 'account.edi.xml.ubl_21'` | DEF | | | AccountEdiXmlUbl_21 is the UBL 2.1 abstract model; inherits account.edi.xml.ubl_20 | NR-U82-016 |
| U82-017 | U82-F06 | account_edi_ubl_cii/models/account_edi_xml_ubl_bis3.py:11 | `_name = "account.edi.xml.ubl_bis3"` | DEF | | | AccountEdiXmlUBLBIS3 is the PEPPOL BIS Billing 3.0 abstract model; inherits account.edi.xml.ubl_21 and account.edi.ubl_pint_eu | NR-U82-017 |
| U82-018 | U82-F06 | account_edi_ubl_cii/models/account_edi_xml_ubl_bis3.py:50 | `return 'urn:cen.eu:en16931:2017#compliant#urn:fdc:peppol.eu:2017:poacc:billing:3.0'` | RETURN | | | BIS3 CustomizationID for billing is 'urn:cen.eu:en16931:2017#compliant#urn:fdc:peppol.eu:2017:poacc:billing:3.0' | NR-U82-018 |
| U82-019 | U82-F07 | account_edi_ubl_cii/models/account_edi_ubl.py:28 | `_name = "account.edi.ubl"` | DEF | | | AccountEdiUBL abstract model provides base helper methods for all UBL formats; inherits account.edi.common | NR-U82-019 |
| U82-020 | U82-F08 | account_edi_ubl_cii/models/account_edi_common.py:299 | `_name = 'account.edi.common'` | DEF | | | AccountEdiCommon abstract model is the base for all EDI document generation and import | NR-U82-020 |
| U82-021 | U82-F09 | account_edi_ubl_cii/models/account_move_send.py:128 | `if invoice.with_context(sending_method=invoice_data['sending_methods'])._need_ubl_cii_xml(invoice_data['invoice_edi_format']):` | GUARD | | | XML generation for UBL/CII is triggered in _hook_invoice_document_before_pdf_report_render() only if _need_ubl_cii_xml() returns True | NR-U82-021 |
| U82-022 | U82-F09 | account_edi_ubl_cii/models/account_move_send.py:130 | `xml_content, errors = (` | CALL | | | builder._export_invoice() is called to generate XML bytes; builder is resolved via partner._get_edi_builder(invoice_edi_format) | NR-U82-022 |
| U82-023 | U82-F09 | account_edi_ubl_cii/models/account_move_send.py:145 | `'res_field': 'ubl_cii_xml_file',  # Binary field` | ASSIGN | | | Generated XML is stored in ir.attachment linked to account.move via binary field ubl_cii_xml_file | NR-U82-023 |
| U82-024 | U82-F10 | account_edi_ubl_cii/models/res_partner.py:332 | `def _get_edi_builder(self, invoice_edi_format):` | DEF | | | _get_edi_builder() dispatches format code to concrete abstract model: ubl_bis3→account.edi.xml.ubl_bis3; facturx/zugferd→account.edi.xml.cii; xrechnung→account.edi.xml.ubl_de; nlcius→account.edi.xml.ubl_nl | NR-U82-024 |
| U82-025 | U82-F10 | account_edi_ubl_cii/models/res_partner.py:211 | `def _get_ubl_cii_edi_format(self):` | DEF | | | _get_ubl_cii_edi_format() returns partner's invoice_edi_format field or falls back to _get_suggested_ubl_cii_edi_format() | NR-U82-025 |
| U82-026 | U82-F11 | account_peppol/models/account_move_send.py:261 | `def _call_web_service_after_invoice_pdf_render(self, invoices_data):` | OVERRIDE | | | PEPPOL send is triggered in _call_web_service_after_invoice_pdf_render(); groups invoices by edi_user and calls _send_peppol_documents() | NR-U82-026 |
| U82-027 | U82-F11 | account_peppol/models/account_move_send.py:297 | `def _send_peppol_documents(self, invoices_data_peppol, edi_user, params):` | DEF | | | _send_peppol_documents() calls edi_user._call_peppol_proxy() with endpoint '1/send_document'; on success sets peppol_move_state='processing' and triggers cron for status check after 5 minutes | NR-U82-027 |
| U82-028 | U82-F11 | account_peppol/models/account_move_send.py:182 | `'receiver': f"{partner.peppol_eas}:{partner.peppol_endpoint}",` | ASSIGN | | | PEPPOL document payload contains receiver as EAS:endpoint format, filename, and base64-encoded XML | NR-U82-028 |
| U82-029 | U82-F11 | account_peppol/models/account_move_send.py:178 | `if len(xml_file) > 64000000:` | GUARD | | | PEPPOL send enforces a 64 MB size limit on XML documents | NR-U82-029 |
| U82-030 | U82-F12 | account_peppol/models/account_move.py:16 | `peppol_move_state = fields.Selection(` | DEF | | | peppol_move_state on account.move has states: ready, to_send, skipped, processing, done, error | NR-U82-030 |
| U82-031 | U82-F12 | account_peppol/models/account_move.py:52 | `def _compute_peppol_move_state(self):` | DEF | | | _compute_peppol_move_state() auto-sets state to 'ready' when company can send, partner is valid, move is posted sale document, and no current state | NR-U82-031 |
| U82-032 | U82-F13 | account_peppol/models/account_edi_proxy_user.py:177 | `def _cron_peppol_get_new_documents(self):` | DEF | | | _cron_peppol_get_new_documents() cron polls proxy endpoint '1/get_all_documents' for incoming PEPPOL messages; filters by proxy_state='receiver' | NR-U82-032 |
| U82-033 | U82-F13 | account_peppol/models/account_edi_proxy_user.py:314 | `messages = edi_user._call_peppol_proxy(` | CALL | | | Incoming documents fetched from proxy with direction='incoming' filter via '1/get_all_documents' endpoint | NR-U82-033 |
| U82-034 | U82-F13 | account_peppol/models/account_edi_proxy_user.py:355 | `all_messages = edi_user._call_peppol_proxy(` | CALL | | | After filtering duplicates, actual document content fetched via '1/get_document' endpoint | NR-U82-034 |
| U82-035 | U82-F13 | account_peppol/models/account_edi_proxy_user.py:217 | `def _peppol_import_invoice(self, attachment, peppol_state, uuid, journal=None):` | DEF | | | _peppol_import_invoice() creates account.move from incoming PEPPOL document; detects self-billed invoices by type_code (389/527/261); routes to purchase journal by default | NR-U82-035 |
| U82-036 | U82-F13 | account_peppol/models/account_edi_proxy_user.py:365 | `edi_user._call_peppol_proxy(` | CALL | | | After successful import, proxy is ACKed via '1/ack' endpoint with processed message UUIDs | NR-U82-036 |
| U82-037 | U82-F14 | account_peppol/models/account_edi_proxy_user.py:61 | `def _call_peppol_proxy(self, endpoint, params=None):` | DEF | | | _call_peppol_proxy() wraps _make_request() with PEPPOL-specific error handling; checks is_token_out_of_sync before calling; raises UserError on proxy errors | NR-U82-037 |
| U82-038 | U82-F14 | account_peppol/models/account_edi_proxy_user.py:48 | `def _get_peppol_proxy_endpoint(self, endpoint, proxy_type=None):` | DEF | | | _get_peppol_proxy_endpoint() constructs full proxy path as '/api/{proxy_type}/{endpoint}' | NR-U82-038 |
| U82-039 | U82-F15 | account_edi_proxy_client/models/account_edi_proxy_user.py:25 | `_name = 'account_edi_proxy_client.user'` | DEF | | | account_edi_proxy_client.user model stores proxy user: id_client, edi_identification, private_key_id (certificate.key), refresh_token, proxy_type, edi_mode (prod/test/demo) | NR-U82-039 |
| U82-040 | U82-F15 | account_edi_proxy_client/models/account_edi_proxy_user.py:96 | `def _make_request(self, url, params=False, *, auth_type: Literal['hmac', 'asymmetric'] = 'hmac'):` | DEF | | | _make_request() sends JSON-RPC 2.0 POST to proxy URL; signed with HMAC (refresh_token) or asymmetric (private key) auth; handles refresh_token_expired by calling _renew_token() | NR-U82-040 |
| U82-041 | U82-F15 | account_edi_proxy_client/models/account_edi_proxy_auth.py:12 | `class OdooEdiProxyAuth(requests.auth.AuthBase):` | DEF | | | OdooEdiProxyAuth implements requests.AuthBase; adds headers odoo-edi-client-id, odoo-edi-timestamp, odoo-edi-signature to outgoing requests | NR-U82-041 |
| U82-042 | U82-F16 | account_peppol/tools/peppol_iap_connector.py:12 | `PEPPOL_PROXY_URLS = {` | CONST | | | PEPPOL proxy URLs: prod='https://peppol.api.odoo.com', test='https://peppol.test.odoo.com'; configured via proxy_type selection on edi_user | NR-U82-042 |
| U82-043 | U82-F15 | account_edi_proxy_client/models/account_edi_proxy_user.py:168 | `def _register_proxy_user(self, company, proxy_type, edi_mode):` | DEF | | | _register_proxy_user() generates RSA private key, calls '/iap/account_edi/2/create_user' on proxy, creates account_edi_proxy_client.user record | NR-U82-043 |
| U82-044 | U82-F13 | account_peppol/models/account_edi_proxy_user.py:382 | `def _peppol_process_new_messages(self, messages):` | DEF | | | _peppol_process_new_messages() decrypts incoming messages via _decrypt_data(), creates ir.attachment, calls _peppol_import_invoice() | NR-U82-044 |
| U82-045 | U82-F13 | account_peppol/models/account_edi_proxy_user.py:377 | `def _peppol_get_decoded_document(self, content):` | DEF | | | _peppol_get_decoded_document() decrypts document: extracts enc_key and document fields, calls _decrypt_data() (RSA+Fernet symmetric decryption) | NR-U82-045 |
| U82-046 | U82-F12 | account_peppol/models/account_edi_proxy_user.py:412 | `def _peppol_get_message_status(self):` | DEF | | | _peppol_get_message_status() cron polls '1/get_document' for moves in state='processing'; updates peppol_move_state from proxy response; ACKs processed UUIDs | NR-U82-046 |
| U82-047 | U82-F06 | account_edi_ubl_cii/models/account_edi_xml_ubl_bis3.py:8 | `CHORUS_PRO_PEPPOL_ID = "0009:11000201100044"` | CONST | | | Chorus Pro (French government portal) has hardcoded PEPPOL ID '0009:11000201100044' | NR-U82-047 |
| U82-048 | U82-F10 | account_edi_ubl_cii/models/account_edi_common.py:57 | `DEPRECATED_PEPPOL_EAS = {'0037', '0213', '9955', '0193'}` | CONST | | | Four EAS codes are marked deprecated in Community: 0037, 0213, 9955, 0193 | NR-U82-048 |
| U82-049 | U82-F13 | account_peppol/models/account_edi_proxy_user.py:479 | `def _peppol_process_participant_status(self, proxy_user):` | DEF | | | Participant status states map: draft→not_registered, sender, smp_registration, receiver, rejected; local account_peppol_proxy_state updated from proxy response | NR-U82-049 |
| U82-050 | U82-F11 | account_peppol/models/account_move_send.py:355 | `self.env.ref('account_peppol.ir_cron_peppol_get_message_status')._trigger(at=fields.Datetime.now() + timedelta(minutes=5))` | CALL | | | After successful PEPPOL send, message status cron is triggered 5 minutes later to check delivery acknowledgment | NR-U82-050 |

---

## Registered EDI Formats (account_edi_ubl_cii)

From manifest and model listing, the following format codes are registered:
- `ubl_bis3` — PEPPOL BIS Billing 3.0 (AccountEdiXmlUBLBIS3, model: account.edi.xml.ubl_bis3)
- `facturx` / `zugferd` — CII D16B Factur-X/ZUGFeRD (AccountEdiXmlCII, model: account.edi.xml.cii)
- `xrechnung` — XRechnung UBL (German) (account.edi.xml.ubl_de)
- `nlcius` — NLCIUS (Dutch) (account.edi.xml.ubl_nl)
- `ubl_a_nz` — A-NZ Peppol BIS (Australia/NZ) (account.edi.xml.ubl_a_nz)
- `ubl_sg` — Singapore Peppol BIS (account.edi.xml.ubl_sg)
- `efff` — E-FFF (Belgian) (account.edi.xml.ubl_efff)
- `ubl_20` / `ubl_21` — Base UBL 2.0/2.1 (abstract)

---

## Community vs Enterprise Boundary

All four EDI modules (`account_edi`, `account_edi_ubl_cii`, `account_peppol`, `account_edi_proxy_client`) are licensed LGPL-3 and present in the Community distribution. The PEPPOL proxy backend (`https://peppol.api.odoo.com`) is operated by Odoo SA as an IAP service — usage requires an Odoo subscription but the client-side code is open source. No OEEL license modules were found for the core EDI/PEPPOL send/receive flow.
