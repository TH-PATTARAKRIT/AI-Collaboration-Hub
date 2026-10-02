# U62 — PEPPOL, IoT Base, Lunch, Mass Mailing, Payment Providers (Neutral Knowledge)

> NEUTRAL — PUBLIC CONSUMPTION. No snake case identifiers, no file paths, no code, no backticks.
> Revision: 2026-10-02
> Source: Odoo 19 Community (post20260921), source analysis only

---

## Section 1: PEPPOL E-Invoicing Network

### What is PEPPOL?

PEPPOL is a pan-European public procurement online network that enables businesses to exchange electronic business documents — primarily invoices and credit notes — across national borders using standardized formats and a four-corner exchange model. In the four-corner model, the sender's corner (Odoo) connects to the PEPPOL network through an access point, and the receiver's corner retrieves the document through their own access point. Odoo 19 implements the sender and receiver roles using a cloud intermediary service operated by Odoo (the IAP proxy).

### Registration Lifecycle

A company starts in the "not registered" state. When it initiates registration, it first becomes a sender — meaning it can send PEPPOL documents but cannot yet receive them. The system then attempts to register the company's endpoint in the PEPPOL Service Metadata Publisher (SMP), which is a distributed directory that maps business identifiers to access point endpoints. During this phase the company is in the "SMP registration" state and the system polls for confirmation approximately every hour. Once the SMP registration is confirmed, the company transitions to "receiver" state and can both send and receive. If registration is rejected, the company enters the "rejected" state, which is terminal and requires manual intervention to clear.

### Business Identifiers (EAS Codes)

Every participant on the PEPPOL network is identified by a combination of a scheme code (the Electronic Address Scheme, or EAS code) and the actual endpoint value. Different countries use different schemes. For example, Swedish organizations use their organization numbers, Danish and Norwegian organizations use their own national formats. Odoo validates the format of endpoint values for several European countries and sanitizes them by stripping non-numeric characters where required. For countries not covered by explicit validation rules, Odoo accepts the value as entered.

There is no Thailand-specific EAS code built into the core PEPPOL module. Thai businesses wishing to use PEPPOL would need to use a generic EAS code or rely on any Thailand-specific extension added outside this module.

### Document Sending

When an invoice is ready to be sent via PEPPOL, the system checks whether the recipient company is registered on the PEPPOL network. This check uses a DNS-based lookup service (NAPTR records) accessed through Odoo's IAP proxy rather than a direct DNS query. The lookup result is cached against the partner record on a per-company basis, meaning different companies in the same Odoo database can have different verification states for the same partner.

The document format used is UBL BIS Billing 3.0 (also called PEPPOL BIS). Two mandatory validations are applied: the recipient must have a valid EAS endpoint identifier, and the sending company must also have one. These validations are only applied when sending through PEPPOL, not for regular electronic invoice generation.

Once sent, a document transitions through states: queued for sending, currently being processed, successfully delivered, or in error. Cancellation of a sent invoice is blocked once the document has been handed off to the PEPPOL network, to prevent inconsistency between what the recipient received and what the sender claims was sent.

### Document Receiving

The system periodically polls the IAP proxy for new incoming PEPPOL documents, fetching up to 50 at a time. Incoming documents are deduplicated using a unique message identifier, so the same document cannot be imported twice even if the polling detects it multiple times. After processing, the system acknowledges receipt back to the IAP proxy. If there are more than 50 documents waiting, the cron re-triggers the record immediately to continue processing.

Self-billing documents (where the buyer generates the invoice on behalf of the supplier) use specific document type codes and are routed to the sales journal.

### Document Formats

The default supported document types include the standard PEPPOL BIS Billing invoice and credit note (version 3.0) as well as their the record-billing variants, and the Dutch SI-UBL 2.0 format. These are registered with the SMP so that counterparties can discover which formats this installation can receive.

### Advanced Fields (Deprecated)

A companion module provides additional PEPPOL-specific fields on invoices, including contract references, project references, originator document references, despatch document references, additional document references, accounting cost codes, and delivery location GLN numbers. All of these fields are marked as deprecated in Odoo 19, meaning they remain available for backward compatibility but are not recommended for new implementations. Migration from older Odoo versions that used these fields should plan accordingly.

### Webhook and Token Security

The IAP proxy can push real-time notifications to the Odoo installation via a webhook endpoint. Webhook tokens are generated using a hash-based signature with a 30-day validity period. If the connection becomes out of sync (for example, if the database was restored from a backup), the system detects the desynchronization through an invalid signature error and initiates a reconnection protocol. A keepalive cron maintains the webhook registration by periodically refreshing it, but only for companies that are in sender or receiver state.

### Thailand Relevance

PEPPOL is increasingly being adopted in Southeast Asia, and Thailand has shown interest in PEPPOL-based e-invoicing. The core module provides the network connectivity and UBL BIS format support. Thailand-specific EAS codes and any locally mandated variations would need to be handled by localization extensions outside this module. The module the record is fully functional for Thai businesses that register as PEPPOL participants.

---

## Section 2: SEPA QR Code Payments

### What is SEPA QR?

The SEPA Credit Transfer QR code (also called EPC QR code) is a European standard for encoding payment details in a QR code that customers can scan with their banking applications to pre-fill a payment transfer. It is defined by the European Payments Council and uses a specific 12-line text format.

The format requires that the account be an IBAN account within the SEPA zone, the currency be Euro, and the payment amount be within the boundaries of a standard credit transfer. The QR code is 128 by 128 pixels and encodes the beneficiary's name (truncated if necessary), IBAN, payment amount, and optionally a remittance reference or unstructured description.

### Thailand Relevance

SEPA is a strictly European payment scheme covering the EU and associated countries. It has no applicability to Thai domestic payments, where the equivalent QR-based payment standard is PromptPay. A Thai company with European bank accounts could theoretically use SEPA QR for payments from European counterparties, but this would be an edge case. For the purposes of the Thailand-focused SMEsPlus deployment, this module has low direct relevance.

---

## Section 3: Data Recycle

### What is Data Recycle?

The data recycle module provides a configurable data lifecycle management system for Odoo records. Administrators define recycling rules that specify which model to target, which date field to use as the age indicator, how old records must be before they qualify for recycling, and what action to take (archive or permanently delete).

### Manual vs. Automatic Mode

In manual mode, qualifying records are collected into a review queue where an administrator can inspect them before deciding to proceed or discard. In automatic mode, the action is applied without human review — records are archived or deleted immediately once they meet the age threshold.

The batch sizes differ between modes: automatic mode processes 5,000 records at a time, while manual mode collects up to 50,000 records per run. This difference exists because automatic mode immediately applies the action for each batch, which is slower, while manual mode only creates review entries.

### Commit Strategy

To prevent a single large recycling run from holding a database lock or being rolled back entirely on timeout, the system commits each processed batch to the database separately. This means that if a run is interrupted partway through, the completed batches remain committed.

### Notifications

When records are ready for recycling in manual mode, the system can notify users. However, notifications are restricted to system administrators — regular users do not receive them. The notification frequency is configurable to prevent excessive alerting.

### Archive vs. Delete

Archiving marks a record as inactive (the "active" flag set to false), hiding it from normal views while preserving its data. This action is only possible on models that support the active flag. Deletion permanently removes the record. Soft-discarding a review entry (marking it as inactive without taking action on the original record) is also available for cases where an administrator decides a record should not be recycled after all.

---

## Section 4: IoT Base

### What is IoT Base?

The IoT Base module is the frontend foundation for Odoo's Internet of Things integration. It provides JavaScript-based utilities and a device controller that run in the browser. It has no server-side business logic and no database models.

The module's sole declared dependency is the core web module, and it is categorized as a hidden module, meaning it does not appear in the user-facing module list and is only installed as a dependency of higher-level IoT modules.

All device discovery, connection management, and proxy communication logic runs in the browser, making the actual runtime behavior dependent on the IoT Box hardware, the network configuration, and the browser environment. Static analysis of this module cannot reveal details about how specific devices communicate.

---

## Section 5: Withholding Tax at Point of Sale (Thailand Critical)

### What is Withholding Tax?

Withholding tax (WHT) is a mechanism by which the payer of certain types of income (typically services) is required to deduct a percentage of the payment and remit it directly to the tax authority, rather than the recipient receiving the full amount and paying tax separately. In Thailand, withholding tax is mandatory for a wide range of business-to-business service payments, making it one of the most important accounting requirements for Thai businesses.

### Module Purpose

This module bridges the general withholding tax accounting module with Odoo's Point of Sale application. When both the withholding tax module and the POS module are installed, this bridge module installs automatically.

It adds a single piece of data to what the POS front end loads when a session starts: a flag indicating whether a given tax should be treated as a withholding tax collected at payment time. This flag allows the POS interface to identify and correctly handle withholding tax deductions during checkout.

### Thailand Context

For Thai retail and service businesses operating a point of sale, correctly applying withholding tax at the moment of payment is a compliance requirement. Without this bridge module, the POS would not be aware of which taxes are withholding taxes and could not apply them correctly. With it, the existing WHT computation helpers from the accounting module are loaded into the POS session and made available for use.

The actual tax rates, tax codes, and the specific behavior of the WHT computation are configured at runtime through the base withholding tax module and its localization settings — this bridge module provides only the connection point.

---

## Section 6: Lunch Ordering System

### What is the Lunch Module?

The Lunch module provides an internal employee food ordering system. Employees can browse available food products from configured suppliers, place orders, and have their meal costs deducted from a prepaid wallet.

### Order Lifecycle

An order starts in the "To Order" state when an employee selects items. Once the responsible person or system marks it as ordered with the supplier, it moves to "Ordered." If the supplier's delivery has been dispatched, it can move to "Sent." When the food arrives and the order is confirmed as received, it moves to "Confirmed." Orders that are cancelled at any point move to "Cancelled."

### Wallet System

Each employee has a wallet balance representing prepaid credit. The balance is calculated by summing all cash movement records for that employee and adding any company-configured minimum threshold. The balance is displayed with two decimal places.

### Toppings and Customization

Products can have up to three independent customization categories (for example: size, sauce, and side). Each category maintains its own selection. This allows complex product configurations without conflating different types of choices.

### Supplier Scheduling

Lunch suppliers can be configured to send order notifications by phone or email, at a specific time each day. The scheduling is timezone-aware, and changes to the supplier's name, active status, notification method, send time, ordering period, or timezone trigger an automatic update to the scheduled delivery.

---

## Section 7: Mass Mailing

### What is Mass Mailing?

Mass Mailing provides a bulk email marketing capability within Odoo. It allows sending personalized emails to large lists of contacts, tracking deliverability and engagement, and managing subscriber preferences.

### Campaign States

A mailing campaign starts as a draft while being composed. When ready, it is queued for sending. The sending state indicates it is actively being processed. Once all messages have been dispatched, it transitions to the "Sent" (done) state.

### Contact Lists and Subscriptions

Contacts can be organized into mailing lists. Lists can optionally be made visible in subscriber preference pages, where subscribers can manage their own opt-in and opt-out choices. When merging two lists, the system deduplicates contacts by email address and respects existing opt-out records, so no opted-out contact inadvertently gets re-subscribed.

### Exclusion List and Blacklist

The global exclusion list (blacklist) contains email addresses that should never receive marketing emails. It is enabled by default on every mailing. Disabling the exclusion list is possible but carries a warning, as it would cause blacklisted contacts to receive emails — typically this would only be appropriate for transactional mailings where consent is established through other means.

Opt-out reasons are tracked on the blacklist: when a contact asks to be removed, the reason for opting out can be recorded. This reason is logged as an activity comment for traceability.

### Delivery Tracking

Every individual email sent is tracked through a trace record. The trace captures the journey of the email: whether it was sent, whether it bounced, whether the recipient opened it, whether they clicked a link, and whether they replied. A separate integer copy of the originating email identifier is kept even after the underlying email record is deleted, to preserve historical trace information.

Link clicks are tracked through a link tracker integration. The timestamp of the last click is stored, supporting multi-click scenarios.

### Split Testing

split testing allows sending different versions of a mailing to portions of the audience to determine which performs better. The test percentage (how much of the list receives each variant) defaults to 10 percent. The winner can be determined by open rate, click rate, reply rate, or manual selection. Test results are evaluated at the campaign level.

### Reply-To Behavior

Replies to mass mailings can be configured to go back to the originating Odoo document (such as a sale order or a project task), where they are added as messages in the chatter. Alternatively, replies can be directed to a specified email address.

### SMS Extension

The SMS extension adds an SMS mailing type alongside the standard email type. SMS mailings use IAP (Odoo's in-app purchase) credits for delivery. Credit availability is checked and surfaced as a warning flag. SMS mailings default to archiving their message records after sending, whereas email mailings do not archive by default.

### Bridge Modules

Several bridge modules connect mass mailing to other Odoo applications. CRM integration allows targeting leads and opportunities. Event integration allows targeting event registrants and, with the SMS variant, sending SMS to event participants. Sales integration allows targeting sale order customers. eLearning integration allows targeting channel subscribers. These bridges add the relevant model as a valid mailing target and provide contextual statistics.

---

## Section 8: Marketing Card

### What is Marketing Card?

Marketing Card enables creating shareable visual cards for social media campaigns. Cards are generated from configurable templates and associated with specific Odoo records.

### Supported Models

Card campaigns can target four record types: contacts, event sessions, event booths, and event registrations. This selection is fixed in the source code.

### Campaign Features

Each campaign tracks the number of cards generated, how many times cards were clicked, and how many times they were shared. A target URL can be configured for the primary call-to-action, and a separate reward URL can be configured to show a thank-you page after sharing. Post suggestions for social media platforms can be pre-written for users to copy and share.

The QWeb template rendering is unrestricted for card campaigns, meaning templates can include any content supported by the template engine. A background image and preview image are attached to the campaign for visual customization.

---

## Section 9: Payment Providers

### Overview

Odoo 19 Community includes integration with several third-party payment providers. Each provider follows a consistent pattern: provider-specific configuration fields, URL endpoints for test and production environments, a signature or authentication mechanism, and handling for the payment lifecycle (authorization, capture, refund, tokenization).

### Adyen

Adyen is a global payment platform used widely across Europe and Asia. The integration supports partial capture (capturing less than the originally authorized amount), partial refund, and tokenization (saving card details for future payments).

Authentication uses an API key sent in a request header. Webhook notifications from Adyen are signature-verified using an HMAC key. The system handles five webhook event types: authorization, cancellation, capture, capture failure, and refund.

When storing card details for future use, payment transactions are processed under the "Subscription" recurring model with "ContAuth" (contract authorization) shopper interaction. The shopper reference used with Adyen is derived from the Odoo partner identifier.

Production URLs use a domain pattern specific to Adyen's live environment, with a prefix provided by the merchant that differs from the test URL prefix.

### Amazon Payment Services (APS)

Amazon Payment Services (formerly known as PayFort) is a payment provider popular in the Middle East. The integration uses a form-based redirect flow where the customer is sent to the APS payment page.

Authentication is via a dual-key SHA-256 signature where both the request and response use separate secret keys, each of which wraps the sorted parameter string. Payment references are restricted to alphanumeric characters, hyphens, and underscores.

### AsiaPay (including SiamPay)

AsiaPay operates multiple regional payment brands. The brands available in the integration include PayDollar (Hong Kong and Asia), PesoPay (Philippines), SiamPay (Thailand), and BimoPay (Indonesia). SiamPay is directly relevant to Thai payment processing.

The integration supports three hash algorithms: SHA1, SHA256, and SHA512. Each account is limited to a single currency. Payment references are limited to 35 characters.

Signature computation uses a pipe-delimited concatenation of ordered field values appended with the secret key, then hashed with the selected algorithm. This pattern is applied for both outgoing payment requests and incoming confirmation callbacks.

SiamPay specifically supports Thai Baht transactions and is the primary way to integrate AsiaPay-based payments for Thai merchants using Odoo. The actual supported currency codes depend on AsiaPay's account configuration and are resolved at runtime.

### Authorize.Net

Authorize.Net is a US-based payment gateway. The integration supports only full (not partial) capture and refund, and supports tokenization via customer payment profiles.

Each gateway account is restricted to a single currency. A validation charge of one US cent is used for card validation flows. The integration uses Authorize.Net's XML API, and the URL points to different endpoints for test and production environments.

The refund flow includes a pre-check of the current transaction status on the Authorize.Net side: a voided transaction results in cancellation rather than a refund attempt, and an already-refunded transaction is marked as done immediately.

### Buckaroo

Buckaroo is a Netherlands-based payment service provider. The integration uses a SHA-1 signature computed over fields with certain key prefixes (the add, brq, and cust prefixes). Fields are sorted alphabetically by their lowercase key names before being concatenated.

The payment flow uses four return URL parameters despite them all pointing to the same URL, because all four are included in the signature verification. Payment status is determined by a numeric status code in the return data.

### Demo Provider

The demo provider is for development and testing purposes only. It simulates the full range of payment behaviors: successful payment, cancellation, error, and pending states. It explicitly prevents being enabled in a production configuration. All payment features are simulated, including partial capture, partial refund, and tokenization with a placeholder card reference. Amount validation is skipped entirely, as there are no actual funds involved.

---

## Section 10: Summary Notes for Thailand Scope

The following modules in this unit have direct or high Thailand relevance:

1. Withholding tax at POS — critical for Thai compliance. Connects WHT accounting to POS sessions, enabling correct WHT application at checkout. Auto-installs when both dependencies are present.

2. AsiaPay SiamPay — the SiamPay brand within the AsiaPay integration directly supports Thai payment processing via Baht-denominated transactions.

3. PEPPOL — Thailand is developing PEPPOL-based e-invoicing capacity. The core module provides full network connectivity and UBL BIS 3.0 format support. Thailand-specific EAS codes are not in the core module but can be added through localization extensions.

The following modules have indirect or low Thailand relevance:

4. SEPA QR code — European-only payment standard. Low direct Thai relevance.

5. Data Recycle, Lunch, Mass Mailing, Marketing Card, IoT Base — generic business modules with no localization dependency. Applicable to Thai deployments as to any other.

6. Adyen, APS, Authorize.Net, Buckaroo, Demo payment providers — none of these are specifically Thai payment providers, though Adyen and APS may be used by multinational businesses operating in Thailand.

---

## Neutral statement index

[N-U62-001] PEPPOL registration and proxy connection for electronic invoice exchange.
[N-U62-002] Business identifier assignment and EAS code validation.
[N-U62-003] Document sending flow through the PEPPOL four-corner model.
[N-U62-004] Document receiving and inbound processing from the PEPPOL network.
[N-U62-005] Supported electronic invoice formats and standards.
[N-U62-006] Webhook and access token security for PEPPOL callbacks.
[N-U62-007] Advanced partner identification fields for PEPPOL compliance.
[N-U62-008] SEPA QR code payment instructions embedded in invoices.
[N-U62-009] SEPA zone and currency constraints for QR payment codes.
[N-U62-010] Data recycle rules for automatic and manual record cleanup.
[N-U62-011] Commit strategy and batch sizing for data recycle operations.
[N-U62-012] Archive versus permanent deletion choices in data recycle.
[N-U62-013] IoT base module providing device connectivity infrastructure.
[N-U62-014] Withholding tax capture at the point of sale for Thailand compliance.
[N-U62-015] Lunch module order lifecycle and kitchen workflow.
[N-U62-016] Lunch wallet balance tracking via cash movement records.
[N-U62-017] Lunch topping categories and per-supplier scheduling.
[N-U62-018] Mass mailing campaign states and recipient list management.
[N-U62-019] split testing flows and winner selection for mass mailing.
[N-U62-020] Delivery trace states and failure type classification for mass mailing.
[N-U62-021] Blacklist management and opt-out handling for mass mailing.
[N-U62-022] Marketing card generation and link tracker integration.
[N-U62-023] Payment provider webhook signature verification patterns.
[N-U62-024] Adyen payment provider partial capture and tokenization.
[N-U62-025] APS payment provider SHA-256 signature scheme.
[N-U62-026] AsiaPay SiamPay provider for Thailand payment processing.
[N-U62-027] Authorize.Net payment provider validation and capture flow.
[N-U62-028] Buckaroo payment provider signature prefix filtering.
[N-U62-029] Demo payment provider for testing and simulation.
[N-U62-030] PEPPOL document state transitions and cancellation guard.
[N-U62-031] PEPPOL the record-billing type codes for reverse charge invoicing.
[N-U62-032] PEPPOL synchronization and out-of-sync handling.
[N-U62-033] PEPPOL NAPTR lookup for access point discovery.
[N-U62-034] Mass mailing list merge and SQL deduplication logic.
[N-U62-035] Mass mailing bridge modules for CRM, events, and sales.
[N-U62-036] Data recycle notification restrictions for administrators.
[N-U62-037] Lunch supplier location and address management.
[N-U62-038] Lunch order confirmation and cancellation workflow.
[N-U62-039] Marketing card supported model whitelist.
[N-U62-040] Payment provider feature support matrix (tokenization, refunds, capture).
[N-U62-041] PEPPOL batch invoice sending size and processing limits.
[N-U62-042] PEPPOL partner verification and address validation.
[N-U62-043] Withholding tax field integration with POS data transmission.
[N-U62-044] AsiaPay selectable hash algorithm (SHA-1, SHA-256, SHA-512).
