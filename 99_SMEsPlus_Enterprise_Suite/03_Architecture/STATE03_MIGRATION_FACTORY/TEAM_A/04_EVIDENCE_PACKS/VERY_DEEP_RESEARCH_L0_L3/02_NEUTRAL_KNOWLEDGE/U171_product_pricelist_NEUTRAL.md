# U171 — Neutral Knowledge: Product Pricelists and Price Rule Computation
**Unit:** U171 | **Scope:** Pricing list rule selection, computation, and price override chain
**Audience:** Non-technical reviewers, migration planners, business analysts

---

## What Is a Pricelist?

A pricelist is a named price schedule that determines how much a customer pays for a product. Instead of quoting the same price to every customer, the business can maintain multiple pricelists — one for retail customers, one for wholesale buyers, one for a seasonal promotion, and so on. Each pricelist specifies its own currency and contains a set of rules.

---

## How a Price Is Calculated

When the system needs to price a product for a customer, it follows this sequence:

1. **Identify the pricelist.** If the customer has a pricelist assigned, that one is used. Otherwise the system falls back to a country-based default, a company-level default, or the first active pricelist it finds.
2. **Gather matching rules.** From all the rules in that pricelist, the system filters out any that do not apply to this product or category, or whose date window has expired, or whose minimum quantity is not met.
3. **Pick the best-matching rule.** Rules are ranked from most specific to least specific: a rule written for an exact product variant beats a rule for a product template, which beats a rule for a product category, which beats a catch-all rule. Within the same specificity tier, higher minimum quantities rank above lower ones.
4. **Compute the price.** The winning rule calculates the final price using one of three methods described below.
5. **Convert currency.** If the base price and the pricelist are in different currencies, the system converts using the exchange rate for the pricing date.

---

## The Three Pricing Methods

| Method | Plain-Language Description |
|--------|---------------------------|
| Fixed Price | The rule states an explicit amount. The customer pays exactly that number, regardless of the product's standard sales price. |
| Discount (Percentage) | The rule applies a percentage reduction to a base price (usually the standard sales price or another pricelist's price). A negative discount creates a mark-up. |
| Formula | The rule applies a percentage discount to a base price, then optionally rounds the result, then adds or subtracts a fixed surcharge, and finally enforces minimum and maximum margin limits. |

---

## Rule Components (plain language)

| Component | Meaning |
|-----------|---------|
| Apply On | Which products this rule covers: all products, a product category, a specific product, or a specific variant. |
| Base Price | Where the starting amount comes from: the product's standard sales price, its cost, or the result from another pricelist (chaining). |
| Min. Quantity | The rule only activates when the ordered quantity is at least this many units. Used to offer bulk discounts. |
| Start / End Date | The rule is only active within this date window. Both ends are optional; an empty end date means the rule never expires. |
| Price Discount | Percentage taken off the base price. Used in the Formula method. |
| Rounding | The discounted amount is rounded to the nearest multiple of this value before the surcharge is added. |
| Extra Fee | A fixed amount added (positive) or subtracted (negative) after rounding. |
| Min. Margin / Max. Margin | Guardrails: the final price cannot fall below base + min. margin, or rise above base + max. margin. |

---

## Pricelist Chaining

A pricelist rule can use another pricelist as its base. This is called chaining. For example, a "Gold Customer" pricelist may take its base prices from the "Standard Retail" pricelist and then apply a 10% discount on top. The system follows the chain recursively, and a built-in safeguard prevents circular references (a pricelist pointing back to itself through a chain).

---

## Who Gets Which Pricelist

The system determines a customer's pricelist in this priority order:

1. A pricelist explicitly saved on the customer's contact record.
2. A pricelist configured for the customer's country group.
3. A company-level default pricelist stored in system settings.
4. A global default, also in system settings.
5. The first available active pricelist.

On a sales order, the pricelist is pre-filled from the customer and can be manually changed while the order is still in draft. Once the order is confirmed, the pricelist is locked.

---

## Pricelist and Currency

Every pricelist has exactly one currency. All prices computed under that pricelist are expressed in that currency. If a product's base price is stored in a different currency (for example, the cost price is in USD and the pricelist is in EUR), the system automatically converts the amount using the daily exchange rate.

---

## Pricelist at the Point of Sale

The Point of Sale configuration has a default pricelist (used when no customer is identified) and a list of available pricelists that the cashier can switch to during a session. All available pricelists must share the same currency as the point of sale to avoid currency mismatches at checkout.

---

## Multi-Company Behaviour

A pricelist can be restricted to a single company or shared across all companies (by leaving the company field empty). Rules within a pricelist inherit the pricelist's company. When searching for a suitable pricelist, the system only considers pricelists belonging to the current company or those with no company restriction.
