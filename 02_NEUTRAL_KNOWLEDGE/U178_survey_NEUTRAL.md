# U178 — survey: Survey Creation, Response Lifecycle, Scoring, and Email/Portal Delivery
**Unit**: U178 | **Module**: survey | **Group**: G14 | **P2**
**Date**: 2026-10-02 | **Status**: GATE-PASS

## Survey Model Architecture

The `survey.survey` model mixes in both the thread and activity frameworks, enabling full chatter, follower tracking, and scheduled activity support directly on survey records. The model does not use a lifecycle state field for the survey itself; surveys are enabled or disabled through an active toggle. A separate session-state selection, with values for ready and in-progress, is used exclusively for live broadcast sessions. Responsible-user and restricted-user assignments are both audit-tracked through the chatter.

Survey access is controlled by an access-mode field with two values: open to anyone holding the link, or restricted to people who received an invitation token. A separate login-required toggle can overlay authentication on top of either mode. The survey carries its own globally unique access token (a UUID4), which forms the base of all public-facing URLs.

## Question Model

Questions and section pages share the same model, distinguished by an is-page flag. A database constraint prevents page records from carrying a question type. The question-type selection has nine values: single-choice (one answer), multiple-choice (many answers), multi-line text, single-line text, numeric value, scale (integer range), date, datetime, and matrix. Sections that lack a description are excluded from the page-per-question navigation sequence; questions that are conditioned on answers that were never triggered are similarly excluded.

The mandatory-answer flag on a question causes the answer-submission flow to store a skipped marker when the respondent bypasses the question. A navigation helper then routes the respondent back to the earliest unanswered mandatory question before allowing final submission.

## Response Lifecycle

A `survey.user_input` record begins in the "new" state at creation. When the respondent clicks begin, a begin-session endpoint writes the in-progress state and records the start timestamp. On final submission, the mark-done method writes the done state and the end timestamp, triggers completion notifications, and initiates certification and badge processing.

Each response carries three identity tokens: a unique access token for that specific response, an invite token that groups all attempts from the same invitation (without a uniqueness constraint), and an optional partner reference for authenticated respondents.

Individual answers are stored as `survey.user_input.line` records with a type selector and a matching typed value column for each type: character text, free text, numeric float, scale integer, date, datetime, and suggested-answer reference. Matrix answers additionally reference a row record. A mutual-exclusivity constraint prevents a line from being simultaneously skipped and typed.

## Invitation Wizard

The invitation wizard processes both partner records and free-form email addresses. For each unique recipient not yet having a response, it calls the survey's answer-creation helper, which creates the `survey.user_input` with tokens assigned. In resend mode, the most-recent existing response for each recipient is reused rather than creating a duplicate. An individual email is then composed per response, rendering the template in the recipient's language with the answer-specific token embedded, and dispatched as an outgoing mail record.

When attempt limiting is active on a non-public survey, the answer-creation helper auto-generates an invite token for the new response to group the attempt pool under that invitation.

## Scoring and Certification

Scoring percentage and total are both stored computed fields on the response, recomputed when any answer-line score changes. The percentage is the sum of earned scores divided by total possible score across predefined questions. The pass/fail determination compares the percentage to the survey's required-score threshold, which defaults to 80 percent.

On completion, for a certification survey where the respondent passed and the survey has a certification email template, the certification document is sent automatically (not for test entries). If the survey is configured to award a badge, the gamification challenge cron is invoked synchronously to grant the badge.

The certification badge integration creates a goal definition scoped to successful responses on that survey, wrapped in a real-time challenge with a category of "certification" and a period of "once". The challenge is created or recreated when the give-badge toggle is enabled on the survey.

## Portal Access

The public-facing entry route for surveys uses an authentication level of "public", meaning unauthenticated users can reach and begin a survey without logging in. When login is required, the controller builds a redirect back to the survey after authentication. The answer token is stored in a browser cookie for resumption on reconnect. The survey's short URL is formed from the first six characters of the access token.

## Completion Notifications

On marking a response done, the survey's follower list is checked for the response-completed subtype. For surveys that have such followers, a chatter message is posted on the response record identifying the participant by name (or as "Someone" for anonymous responses). Both the survey model and the response model inherit the thread framework, so each has an independent follower list and message log.

## Statistics and Answer Distribution

Answer distribution statistics are computed at render time, not stored on the model. The per-question statistics method produces table data and graph data in a structure suitable for frontend charting: for choice questions, a vote count per option; for matrix questions, a count grid of row-by-column intersections; for scale questions, a count per integer step in the defined range. Survey-level aggregate statistics (total responses, completed count, average score, success rate) are computed fields on the survey record, reading grouped data from the response table.
