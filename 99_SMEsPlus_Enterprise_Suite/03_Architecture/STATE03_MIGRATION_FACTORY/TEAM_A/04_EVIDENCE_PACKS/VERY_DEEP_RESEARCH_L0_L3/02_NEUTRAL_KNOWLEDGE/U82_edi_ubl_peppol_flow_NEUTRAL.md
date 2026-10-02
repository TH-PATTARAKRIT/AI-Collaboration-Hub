# U82 Neutral Knowledge — EDI/UBL/PEPPOL Flow
> NEUTRAL LAYER — no source paths, no class/method names, no file extensions, no snake_case, no backticks

| NR-ID | Statement |
|---|---|
| NR-U82-001 | An EDI format record carries a unique code identifier and a display name; the code acts as the primary key for format dispatch. |
| NR-U82-002 | The EDI dispatch function inspects an invoice move and returns a collection of callable handlers — one for posting, one for cancellation, and optional batching and content functions — enabling the framework to route any invoice through its format-specific processing. |
| NR-U82-003 | EDI formats declare whether they require asynchronous web service calls; formats that do not require them are processed synchronously during invoice posting. |
| NR-U82-004 | Each posted invoice can have one electronic document record per registered EDI format; the electronic document serves as the state carrier and attachment holder for that format's output. |
| NR-U82-005 | The electronic document lifecycle has four states: queued for sending, sent, queued for cancellation, and cancelled. |
| NR-U82-006 | Synchronous EDI formats are processed immediately at invoice posting time without any background worker involvement. |
| NR-U82-007 | Asynchronous EDI formats are processed by a background worker that uses row-level locking to prevent two processes from handling the same document concurrently. |
| NR-U82-008 | A scheduled task searches all electronic documents in a sendable state on posted invoices and processes them in configurable batch sizes; when a batch is incomplete it re-triggers itself. |
| NR-U82-009 | When an invoice is confirmed, the system iterates all EDI formats enabled on the invoice's journal, creates a pending electronic document for each applicable format, then immediately processes all synchronous formats and schedules asynchronous ones. |
| NR-U82-010 | One electronic document record is created per EDI format per invoice at confirmation time. |
| NR-U82-011 | The asynchronous EDI scheduled task is triggered immediately after invoice confirmation so outbound processing begins as quickly as possible. |
| NR-U82-012 | A helper on the invoice model retrieves the single electronic document matching a given format from the invoice's document collection. |
| NR-U82-013 | The base UBL 2.0 generation model is an abstract mixin that provides the foundational XML construction logic for all UBL-family formats. |
| NR-U82-014 | The invoice export method validates taxes, constructs a structured document tree, runs format-specific constraints, converts the tree to XML bytes via a shared utility, and returns both the byte content and any collected errors. |
| NR-U82-015 | The XML generation output is a tuple of UTF-8 encoded XML declaration bytes and a set of error strings; an empty error set indicates success. |
| NR-U82-016 | The UBL 2.1 format extends UBL 2.0 with additional document sections including due date, credit note type codes, and buyer reference. |
| NR-U82-017 | The PEPPOL BIS Billing 3.0 format extends UBL 2.1 and additionally inherits European Union PINT profile logic. |
| NR-U82-018 | The BIS Billing 3.0 customization identifier for standard outbound invoicing is a specific PEPPOL standards URI confirming EN16931 compliance. |
| NR-U82-019 | The common UBL helper abstract model provides shared utility methods for classifying tax types (recycling contribution, excise, reverse charge, early payment) used across all UBL format variants. |
| NR-U82-020 | The shared EDI generation base provides document tree conversion utilities, UOM-to-UNECE mapping, tax exemption reason mapping, and XML parsing helpers used by both UBL and CII formats. |
| NR-U82-021 | XML generation for UBL and CII formats is performed as a pre-PDF hook during the Send and Print flow, triggered only when the invoice requires electronic XML output based on format and sending method. |
| NR-U82-022 | The format builder object is resolved from the partner's configured format code, and its export method is called to produce the XML bytes. |
| NR-U82-023 | The generated XML file is stored as a binary field attachment directly on the invoice record, linked by a dedicated file field. |
| NR-U82-024 | Format dispatch maps each format code to a specific format-specific abstract model: the PEPPOL format uses the BIS Billing 3.0 model; Factur-X and ZUGFeRD use the CII model; XRechnung uses the German UBL variant. |
| NR-U82-025 | A partner's effective EDI format is either explicitly configured on the partner record or automatically suggested based on the partner's country code using a country-to-format mapping table. |
| NR-U82-026 | The PEPPOL sending logic is triggered in a post-PDF web service hook that groups invoices by their proxy user account and dispatches batched calls to the PEPPOL proxy. |
| NR-U82-027 | The PEPPOL document send method calls the proxy endpoint for batch document transmission; on success it records the proxy-assigned message UUID on each invoice and sets the invoice's PEPPOL state to pending reception; a status check is scheduled five minutes later. |
| NR-U82-028 | Each document sent to the PEPPOL proxy contains the receiver identifier as an EAS code plus endpoint value pair, the filename, and the base64-encoded XML content. |
| NR-U82-029 | Documents larger than 64 megabytes cannot be sent via PEPPOL; an error is recorded on the invoice if this limit is exceeded. |
| NR-U82-030 | The PEPPOL status field on an invoice has six values: ready to send, queued, skipped, pending reception, done, and error. |
| NR-U82-031 | A posted sale invoice automatically enters the ready-to-send state when the company is registered on PEPPOL, the partner is verified as a PEPPOL participant, and no prior PEPPOL state exists. |
| NR-U82-032 | A scheduled task for receiving documents runs only for companies registered in receiver mode on the PEPPOL network. |
| NR-U82-033 | Incoming document retrieval uses a polling model: the system requests all unacknowledged incoming messages from the proxy using a direction filter. |
| NR-U82-034 | After deduplication, the actual encrypted document content is retrieved in a second proxy call using the message identifiers. |
| NR-U82-035 | Incoming PEPPOL documents are imported as either purchase invoices or self-billed sale invoices based on the document type code found in the XML; type codes 389, 527, and 261 indicate self-billing. |
| NR-U82-036 | After successful import, the proxy server is acknowledged with the processed message identifiers to prevent redelivery. |
| NR-U82-037 | The PEPPOL proxy call wrapper validates synchronization state before making any request; desynchronized tokens cause an immediate user-facing error with reconnection instructions. |
| NR-U82-038 | The PEPPOL proxy endpoint path is constructed as a versioned API path under the proxy type namespace. |
| NR-U82-039 | The proxy user record stores the client identifier, the participant's unique EDI identification, an RSA private key reference, a rotating refresh token, the proxy type, and the operating mode (production, test, or demo). |
| NR-U82-040 | All proxy requests use JSON-RPC 2.0 format; authentication is either HMAC-signed with the refresh token or asymmetric-signed with the private key as a fallback for resynchronization; expired refresh tokens trigger automatic renewal. |
| NR-U82-041 | The proxy authentication layer adds three custom HTTP headers to every outgoing request: the client identifier, a Unix timestamp, and a cryptographic signature computed over the request payload. |
| NR-U82-042 | Two PEPPOL proxy environments are available: a production endpoint and a test endpoint, both operated by the Odoo IAP service. |
| NR-U82-043 | Proxy user registration generates an RSA key pair locally, stores the private key in the database, and sends the public key to the proxy server to obtain a client identifier and initial refresh token. |
| NR-U82-044 | Incoming message processing decrypts each document, creates an attachment record, then attempts invoice import; only successfully imported documents are acknowledged to the proxy. |
| NR-U82-045 | Incoming PEPPOL documents are encrypted with a symmetric key that is itself encrypted with the recipient's RSA public key; decryption requires first decrypting the symmetric key, then decrypting the document payload. |
| NR-U82-046 | A scheduled task monitors invoices in pending-reception state by polling the proxy for delivery status; confirmed deliveries update the invoice state and are acknowledged; processing errors set the invoice to error state. |
| NR-U82-047 | The French government Chorus Pro portal has a hardcoded PEPPOL participant identifier used to detect when invoices are destined for French public sector recipients. |
| NR-U82-048 | Four PEPPOL Electronic Address Scheme codes are marked as deprecated in the EAS mapping and may require migration for affected participants. |
| NR-U82-049 | PEPPOL participation has five states at the proxy level — draft (not registered), sender, SMP registration in progress, receiver, and rejected — which are synchronized to a local company field. |
| NR-U82-050 | A five-minute deferred trigger is set on the status-check scheduled task immediately after each successful PEPPOL transmission, ensuring timely acknowledgment tracking without blocking the sending flow. |
