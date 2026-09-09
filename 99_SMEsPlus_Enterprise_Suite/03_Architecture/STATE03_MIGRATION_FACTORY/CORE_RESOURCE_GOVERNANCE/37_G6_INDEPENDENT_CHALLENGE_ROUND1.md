# [SMEPLUS-26-09-09-CORE-RESOURCE-GOV-001]
# G6 — Independent Adversarial Challenge Round 1

Status: CHALLENGE COMPLETE — MATERIAL CORRECTIONS REQUIRED
Gate: G6 — Metering / Wallet
Artifacts attacked:
- `34_G6_USAGE_LEDGER_METERING_MODEL_DRAFT.md`
- `35_G6_PREPAID_WALLET_CAPACITY_AUTHORIZATION_AND_CUSTOMER_TRANSPARENCY_DRAFT.md`
- `36_G6_SPECIALIST_REVIEW.md`

Independent role: Architecture Audit / Adversarial Challenge
Final Approver: Boss only

## 1. Attack Method

Attempt to cause:
- duplicate or fabricated charge;
- missed charge converted into unsecured consumption;
- cross-Tenant charge attribution;
- wallet double-spend/negative balance;
- rule/version mismatch;
- Cell-move duplicate evidence;
- customer surprise or misleading forecast;
- historical rewrite;
- platform defect charged to customer;
- accounting/operational ledger confusion;
- data/privacy leakage;
- service-integrity failure at wallet exhaustion.

## 2. Challenge Findings

| ID | Severity | Attack / Failure Mode | Required correction |
|---|---|---|---|
| CH-01 | CRITICAL | Compromised producer emits synthetic usage with valid Tenant ID. | Meter promotion must trust only authorized producer identities plus source-domain evidence; producer identity alone is insufficient for financial promotion. |
| CH-02 | CRITICAL | System claims exactly-once delivery and still duplicates after retry/failover. | Never depend on transport exactly-once; require idempotent economic-event identity and deterministic dedupe/reconciliation. |
| CH-03 | CRITICAL | Same workload is metered in old and new Cell during movement/replay. | Canonical Tenant + economic event identity survives placement; Placement Epoch is lineage and stale-authority events are rejected/reconciled. |
| CH-04 | HIGH | Failed/reversed business action is still charged because compute occurred. | Commercial rule must state whether unit is attempt-based, committed-output-based, retained-storage-based or third-party-incurred; default cannot silently charge failed internal work. |
| CH-05 | CRITICAL | Work completes, reservation exists, settlement event is lost. | Reservation/job/usage reconciliation must detect orphaned HELD/EXECUTING states and require outcome proof before settle/release. |
| CH-06 | CRITICAL | Wallet debit succeeds but statement line fails, or statement line exists without debit. | Require one reconciliation identity linking charge decision, wallet settlement and statement line; partial publication remains recoverable/held, never silently divergent. |
| CH-07 | CRITICAL | Duplicate payment callback credits wallet twice. | Funding confirmation requires idempotent payment/funding identity and reconciliation to external settlement reference. |
| CH-08 | HIGH | Worker crash strands reservation forever, reducing customer balance. | Reservation lease/expiry recovery requires workload outcome check; expiry cannot blindly release if consumption may have occurred. |
| CH-09 | HIGH | Customer fragments heavy work into micro-jobs below reservation threshold. | Pre-authorization must consider aggregate Tenant/window exposure and canonical parent workload, not only individual request size. |
| CH-10 | CRITICAL | Many concurrent reservations each see same Available Balance. | Freeze atomic/fencing-equivalent Tenant+currency authorization and reservation serialization invariant. |
| CH-11 | HIGH | Actual usage exceeds reserve after non-interruptible job finishes, creating negative wallet. | Non-interruptible chargeable work must have bounded maximum exposure reserved; unbounded work cannot start without checkpoints/re-authorization. |
| CH-12 | HIGH | Package allowance resets while late events arrive and the same usage is counted in two periods. | Period assignment is by trusted occurrence-time policy; late event has one canonical period and correction lineage; counters/materializations cannot independently choose periods. |
| CH-13 | HIGH | Package/rate changes mid-job and settlement uses new price. | Reservation binds applicable commercial rule/version and maximum exposure for its authorization lease unless customer explicitly re-authorizes. |
| CH-14 | HIGH | Rule/rate is edited in place, making old charge unreconstructable. | Commercial rule versions are immutable/time-effective; corrections create new versions, never edit historical rule truth. |
| CH-15 | HIGH | Per-event rounding systematically overcharges high-frequency micro-usage. | Define canonical quantity precision and rounding stage; aggregate before monetary rounding where unit semantics require it; preserve raw normalized quantity. |
| CH-16 | CRITICAL | Platform retry storm becomes customer usage because request count increased. | Platform-defect/retry amplification exclusion remains mandatory; retry lineage and causal classification are part of charge eligibility. |
| CH-17 | HIGH | Customer sends false byte count/duration/unit to reduce or inflate metered quantity. | Quantity/unit must come from platform-controlled measurement or independently verified source, not client assertion. |
| CH-18 | HIGH | External vendor delayed event arrives after customer statement closed. | Third-party evidence has explicit late-arrival/adjustment rule and cannot silently rewrite closed statement; future adjustment requires contracted policy. |
| CH-19 | HIGH | Pending top-up is shown as Available Balance before funds settle. | Customer dashboard and authorization distinguish Pending Funding from Confirmed Spendable Funding. |
| CH-20 | HIGH | Chargeback/refund deletes prior usage or makes history inconsistent. | Use compensating wallet funding/adjustment entries; settled usage remains immutable; future authorization reflects revised spendable balance/risk status. |
| CH-21 | HIGH | Wallet balance mixes THB and another currency. | Wallet is currency-scoped; any FX is an explicit, evidenced conversion event with its own rule/version. |
| CH-22 | CRITICAL | One admin can change rate, inject usage and grant wallet credit. | Segregation-of-duties and audit controls must separate high-risk commercial rule changes, manual usage correction and wallet adjustments; no silent super-admin path. |
| CH-23 | HIGH | Metering outage causes critical ERP shutdown or optional free usage. | Degraded mode must separate evidence capture, entitlement, financial auth and workload criticality; optional new chargeable work fails closed while already-authorized integrity work preserves correctness where safe. |
| CH-24 | HIGH | Dashboard cache shows stale available balance and customer starts a job that later fails. | Display data freshness/as-of time; execution authorization always uses authoritative current state, never dashboard cache. |
| CH-25 | HIGH | 30-day forecast ignores active reservations/upcoming base rental and overstates runway. | Forecast basis includes available balance after reservations plus known scheduled obligations; disclose assumptions/confidence. |
| CH-26 | MEDIUM | One unusual burst drives misleading depletion date and alert spam. | Forecast must expose confidence and support evidence-based smoothing/range; notification engine needs dedupe/cooldown/escalation semantics, values remain later evidence. |
| CH-27 | HIGH | Statement exposes raw infrastructure telemetry or another Tenant's evidence during drill-down. | Customer drill-down uses Tenant-filtered customer-safe evidence; internal telemetry remains separately authorized. |
| CH-28 | HIGH | Usage ledger retains full payload/PII unnecessarily. | Enforce minimum metering facts + references; sensitive payload retention requires explicit need/access/retention policy. |
| CH-29 | CRITICAL | Wallet operational ledger is treated as accounting revenue/cash truth without reconciliation. | Define explicit accounting handoff/reconciliation obligation; G6 wallet remains operational authorization evidence only. |
| CH-30 | CRITICAL | Service credit transferred between unrelated Tenants, bypassing financial/customer boundary. | Cross-Tenant wallet transfer/pooling prohibited unless a separately approved legal/commercial settlement process exists; no implicit transfer. |
| CH-31 | HIGH | Company/Branch sub-allocation is mistaken for independent wallet ownership. | Freeze Tenant ownership; lower-level budgets/sub-wallets are future design and cannot alter current authorization boundary. |
| CH-32 | HIGH | Base subscription reservation consumes all wallet unexpectedly and hides variable spend capacity. | Dashboard must separately expose scheduled fixed obligations/reservations and variable usage reservations; reservation priority/order is explicit commercial policy, not hidden behavior. |
| CH-33 | HIGH | Customer exit after wallet depletion either gets unlimited free heavy export or loses basic data rights. | Separate bounded data-access/exit rights from expensive processing/export workload; contract/capacity policy required and visible. |
| CH-34 | HIGH | Enterprise reserved-capacity customer bypasses usage evidence because billing is fixed. | Same Usage Evidence lineage remains for capacity governance, Cost-to-Serve and reserved-envelope proof even where no per-unit wallet deduction occurs. |
| CH-35 | CRITICAL | Standard->Enterprise cutover resets usage/wallet period or double-settles events. | Tenant, wallet, usage IDs, period lineage and cutover boundary remain continuous; no double charge across mobility. |
| CH-36 | HIGH | Adjustment changes closed-period totals without traceable customer explanation. | Closed period is immutable; adjustment links original event, reason, approval and customer statement presentation. |

## 3. Architecture Verdict

No fatal contradiction with G1–G5 was found. However the drafts are not ready to pass until CH-01 through CH-36 and SR-01 through SR-22 are materially incorporated into one corrected G6 candidate.

Recommended architecture remains:
- immutable normalized Usage Evidence Ledger + derived aggregates;
- immutable operational Wallet Ledger + derived Tenant/currency balances;
- explicit economic-event idempotency;
- prepaid/secured pre-authorization for additional material usage;
- reservation + checkpoint + actual settlement/release;
- append-only correction/adjustment lineage;
- customer-safe transparency with freshness/provisional/final states;
- explicit Accounting handoff, not wallet-as-GL.

## 4. Numerical / Mechanism Freeze Veto

G6 MUST NOT freeze:
- customer meter unit taxonomy or weights;
- THB prices/rates;
- wallet minimum balance/reserve;
- auto-top-up threshold;
- exact 30/14/7-day reminder cadence beyond the existing 30-day primary requirement;
- grace/read-only/suspension duration;
- DB locking/isolation implementation;
- message broker/event store/billing provider;
- rounding scale/currency list/FX source;
- retention duration.

## 5. Round-1 Disposition

`REWORK REQUIRED — CREATE CORRECTED G6 FREEZE CANDIDATE AND RE-CHALLENGE`.

Build / Merge / Production remain HOLD.
Boss remains sole Final Approver.
