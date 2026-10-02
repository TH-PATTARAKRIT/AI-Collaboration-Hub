# U104 — PEPPOL Response Handling: Neutral Knowledge Layer
> ALL CONTENT: DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION

## Overview

The PEPPOL business-level response module extends the base PEPPOL electronic invoicing capability to support bidirectional status communication between trading partners. It enables both sending and receiving formal acknowledgement, approval, and rejection messages that travel over the PEPPOL network in addition to the invoice documents themselves.

## Neutral Reference Index

| Neutral-ref | Plain-language description |
|---|---|
| N-U104-01 | A dedicated data model stores PEPPOL business response records, each representing one status communication event associated with a specific invoice document |
| N-U104-02 | Each response record carries the unique network message identifier from the PEPPOL transport layer, stored in a way that supports fast database lookups |
| N-U104-03 | Seven distinct status codes can appear on a response record, covering the full PEPPOL business response lifecycle from initial acknowledgement through final payment notification |
| N-U104-04 | A separate state field tracks whether the response message itself has been successfully transmitted through the network, is still in transit, encountered an error, or was rejected by the network as unsupported |
| N-U104-05 | Response records are tightly coupled to their parent invoice document and are automatically removed if the invoice is deleted |
| N-U104-06 | The invoice document lifecycle is extended with three additional terminal states reflecting the outcome of inbound PEPPOL responses from the trading partner |
| N-U104-07 | A collection field on the invoice model groups all response records associated with that invoice for display and computation purposes |
| N-U104-08 | A computed eligibility flag consolidates four independent conditions that must all hold before a response can be sent for a given invoice |
| N-U104-09 | When multiple response records exist for an invoice, the overall invoice state is resolved by a priority rule: rejection overrides approval, approval overrides simple acknowledgement |
| N-U104-10 | Before allowing a response to be sent, the system checks that the invoice has a network identifier, belongs to the purchase side, has no conflicting terminal response already recorded, and that the counterpart has advertised response capability |
| N-U104-11 | Confirming and posting a purchase invoice automatically generates and transmits an approval response to the sender without requiring any manual step |
| N-U104-12 | Cancelling a purchase invoice with an active PEPPOL response capability automatically opens a guided interface for the user to specify rejection reasons |
| N-U104-13 | The core response transmission routine validates input, calls the network proxy service, and records local response objects in a pending state awaiting network confirmation |
| N-U104-14 | Rejection responses are refused unless accompanied by at least one reason from the designated reason catalogue, enforced both in the core routine and in the wizard interface |
| N-U104-15 | The PEPPOL network proxy is called via an internal service endpoint that accepts a list of document identifiers, the desired status, and optional clarification details |
| N-U104-16 | Immediately after a successful proxy call, the locally created response objects are placed in a pending transmission state, awaiting status confirmation from the network |
| N-U104-17 | Incoming PEPPOL response documents are XML files parsed in memory to extract the business status code and any accompanying reason or action messages |
| N-U104-18 | The business status code is located at a specific position in the XML structure: inside the document response container, within a response element, in the response code leaf node |
| N-U104-19 | Status detail elements in the incoming XML are sorted into three groups during parsing: rejection reasons, suggested corrective actions, and miscellaneous unclassified messages |
| N-U104-20 | The message ingestion pipeline identifies incoming response documents by their document type label, processes them to create local records and chatter entries, then passes any remaining non-response messages to the parent handling logic |
| N-U104-21 | An incoming response is only recorded if its status code is one of the recognised values in the system catalogue, preventing storage of unknown codes |
| N-U104-22 | Upon receiving any new inbound PEPPOL document, the system automatically sends an acknowledgement back to the sender to confirm receipt |
| N-U104-23 | The periodic network polling job is extended to include pending outbound response records, so their transmission status is checked alongside outbound invoice documents |
| N-U104-24 | When the network indicates a response is not yet ready to be retrieved, the record is left unchanged and the next polling cycle will retry |
| N-U104-25 | When the network indicates it does not support the response service for a given recipient, the record is moved to a terminal not-serviced state |
| N-U104-26 | A scheduled task periodically compares the document types registered with the network proxy against the locally declared set, adding missing types and removing obsolete ones |
| N-U104-27 | If the service synchronisation job encounters an error for any trading partner, it schedules a retry attempt four hours later |
| N-U104-28 | A reference catalogue model holds the standard PEPPOL codes for rejection reasons and corrective action suggestions, each with a machine code, short name, and plain-language description |
| N-U104-29 | The module declares its document type capability to the network layer using the official PEPPOL UBL invoice response transaction identifier string |
| N-U104-30 | Changing the purchase journal setting for PEPPOL immediately triggers re-evaluation of which document types should be registered with the network proxy |
| N-U104-31 | A computed field on the trading partner record summarises whether that partner has advertised support for receiving PEPPOL business response messages |
| N-U104-32 | Partner response support is only set to true when both the partner verification passes and the specific response document type identifier appears in the partner service catalogue |
| N-U104-33 | A dedicated procedure looks up the partner in the PEPPOL network directory and records all advertised receivable document types locally for use in eligibility checks |
| N-U104-34 | The rejection wizard aggregates the user-selected reasons and actions, groups affected invoices by company, and triggers one response transmission call per company |
| N-U104-35 | The rejection wizard blocks submission if no reason has been selected, surfacing a user-facing validation message |
