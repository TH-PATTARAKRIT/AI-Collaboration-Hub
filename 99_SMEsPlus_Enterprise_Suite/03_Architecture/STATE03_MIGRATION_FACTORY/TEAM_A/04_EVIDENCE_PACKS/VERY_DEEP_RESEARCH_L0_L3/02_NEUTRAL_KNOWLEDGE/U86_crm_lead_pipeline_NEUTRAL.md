# U86 Neutral Knowledge — CRM Lead Pipeline
> NEUTRAL LAYER — no source paths, no class/method names, no file extensions, no snake_case, no backticks

| NR-ID | Statement |
|---|---|
| NR-U86-001 | The CRM module defines a lead record model that manages both pre-qualified leads and qualified sales opportunities within a single model. |
| NR-U86-002 | Each lead record carries a type discriminator with two values: one for early-stage unqualified leads and one for qualified pipeline opportunities. The system default depends on whether the group for using leads is active for the current user. |
| NR-U86-003 | Each lead is associated with a pipeline stage via a many-to-one relationship. Stage availability on a lead is optionally restricted to the stages associated with the lead's sales team. |
| NR-U86-004 | A probability score (0–100) represents the estimated likelihood of winning a lead. It is computed automatically by the predictive lead scoring engine but can be manually overridden. |
| NR-U86-005 | An automated probability score is maintained separately and represents the system-computed value; it is read-only. When a user has not overridden the probability, both values are equal. |
| NR-U86-006 | A computed won/lost status field with three values — won, lost, and pending — summarises the lead's outcome state and is stored for efficient filtering. |
| NR-U86-007 | The won/lost status is derived from three inputs: whether the record is active, the numeric probability value, and whether the current stage is designated as a won stage. |
| NR-U86-008 | A lead is considered won when its probability equals 100 and its stage is marked as a won stage. |
| NR-U86-009 | A lead is considered lost when it is archived (deactivated) and its probability is zero. |
| NR-U86-010 | All leads not meeting the won or lost criteria are in a pending state, representing active pipeline records. |
| NR-U86-011 | The lost action sets a lead to the lost state by archiving the record and resetting both the probability and automated probability to zero. Optional additional field values (such as a lost reason) may be passed when calling the action. |
| NR-U86-012 | The won action first restores a lead to active status, then selects the nearest won stage by sequence relative to the current stage, and finally writes that stage and a probability of 100 to the record. |
| NR-U86-013 | Winning a lead selects the won stage whose sequence is closest to but greater than the current stage sequence; if none exists, the last won stage by sequence is used. |
| NR-U86-014 | Lead-to-opportunity conversion writes the opportunity type value and records a conversion timestamp. An initial stage is assigned if the lead had no stage. |
| NR-U86-015 | The conversion process skips any lead that is archived or already won. |
| NR-U86-016 | The salesperson field links to a user record; the sales team field links to a CRM team record and is automatically computed from the salesperson assignment but can be overridden. |
| NR-U86-017 | Expected revenue is a monetary amount tracking the anticipated deal value; it supports tracking and defaults to zero. The contact field links to a partner record with company-aware access control. |
| NR-U86-018 | When a write operation moves a lead into a won stage, the system automatically forces active to true, probability to 100, and automated probability to 100 in the same write call. |
| NR-U86-019 | The closed date is automatically set when a lead is won (probability reaches 100) or lost (record is deactivated), and cleared when the lead returns to an active pipeline state. |
| NR-U86-020 | A pipeline stage model carries an "is won stage" flag. When a stage's won flag changes, all leads in that stage have their probabilities automatically updated. |
| NR-U86-021 | The sale CRM integration module extends the lead model by adding a one-to-many relationship to sale order records, linking them via the opportunity reference on the sale order. |
| NR-U86-022 | The sale order model gains an opportunity reference field — a many-to-one link to the lead/opportunity model — added by the sale CRM integration module. The domain on this field restricts selection to records of the opportunity type only. |
| NR-U86-023 | A new quotation can be created from a lead using a dedicated action. If the lead has no associated contact, a partner selection dialog is shown first. The new quotation is pre-populated with the opportunity reference, partner, UTM source and campaign, origin name, and team assignment from the lead. |
| NR-U86-024 | When a sale order linked to an opportunity is confirmed, the system checks whether the confirmed order's untaxed amount exceeds the opportunity's current expected revenue. If so, and if the currencies match, the expected revenue on the opportunity is updated to match the order amount. |
| NR-U86-025 | The predictive lead scoring system uses a naive Bayes classifier trained on historical win and loss frequencies. The fields used as scoring inputs are configurable via a system parameter; the model always includes stage and team as inputs. |
| NR-U86-026 | A frequency table stores historical won and lost counts per field value, enabling the probabilistic scoring to update automatically as deals are won or lost. |
| NR-U86-027 | The lead model inherits full chatter, activity, blacklist, phone validation, and UTM tracking capabilities. |
| NR-U86-028 | The conversion date is recorded as a read-only timestamp at the moment a lead record transitions from lead type to opportunity type. |
| NR-U86-029 | UTM tracking fields on the lead (campaign, medium, source) are configured so that deleting the linked UTM record sets the field to null rather than preventing deletion. |
| NR-U86-030 | A database-level constraint enforces that the probability value is always between 0 and 100 inclusive. A model-level constraint prevents a lead in a won stage from having a probability other than 100. |
| NR-U86-031 | The lost reason field links to a lost reason record; it is indexed and prevents deletion of a reason record that is still in use. |
| NR-U86-032 | No analytic account field exists on the lead or opportunity model in the Community edition of the CRM or sale CRM modules; analytic propagation from CRM to sale orders is not present in Community. |
| NR-U86-033 | The sale CRM module computes aggregate statistics on each lead: total untaxed value of confirmed sale orders, count of open quotations, and count of confirmed orders. These are computed from the linked order records. |
