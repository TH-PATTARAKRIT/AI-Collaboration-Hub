# U61 neutral knowledge — website portal: forum, recruitment, eLearning, live chat, short links, profile, payment, project portal

> Neutral knowledge layer. DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION.
> Date: 2026-10-02
> Scope: website_forum, website_google_map, website_hr_recruitment, website_hr_recruitment_livechat, website_links, website_livechat, website_mail, website_partner, website_payment, website_profile, website_project, website_slides, website_slides_forum, website_sms, website_timesheet

---

## Forum

[N-U61-001] A community forum system on a public website lets visitors post questions, provide answers, vote on content, and earn reputation points that unlock posting privileges.

[N-U61-002] A forum can operate in one of two modes: a questions mode where each topic may have only one accepted answer, or a discussions mode where multiple answers are allowed and none is treated as definitive.

[N-U61-003] Forum access can be configured at three levels of openness: fully public for all visitors, restricted to signed-in users only, or limited to members of a specific user group.

[N-U61-004] The forum uses a karma (reputation) economy. Specific activities generate or deduct points for the author: asking a question, receiving upvotes or downvotes, having an answer accepted, and having a post flagged as offensive all change the author's karma balance.

[N-U61-005] Karma thresholds govern what a user may do in a forum. Actions such as asking questions, answering, editing other users' posts, closing posts, deleting posts, creating tags, upvoting, downvoting, flagging, and moderating each require a minimum karma level that can be configured per forum.

[N-U61-006] When a user's karma is below the threshold required to post without review, newly submitted questions are placed in a pending state awaiting moderator approval rather than appearing immediately.

[N-U61-007] Forum posts carry a computed website address combining the forum and post slugs. Answer posts append a fragment identifier to the parent question's address so that a direct link scrolls the page to the relevant answer.

[N-U61-008] A relevancy score is computed for each post from the number of votes it has received and the number of days since it was created, using configurable exponent parameters. This score is used as a sort order option in the forum.

[N-U61-009] Votes are cast as upvote, downvote, or retraction. A user cannot vote more than once per post and cannot vote on their own post. Attempting either raises an error. The system stores one vote record per user per post enforced at the database level.

[N-U61-010] Forum tags help categorise questions. Tags are unique within a forum. Creating new tags requires a minimum karma level.

[N-U61-011] The forum module adds a link to the gamification system so users can be redirected to the forum from achievement notifications.

---

## Google Maps integration

[N-U61-012] A website page builder snippet can embed an interactive map showing the locations of published partner or customer records. The map is rendered in a sub-frame and loads partner location data from the database. Only partners that have been explicitly published on the website and have geographic coordinates are shown. A default limit of eighty partners applies.

[N-U61-013] Displaying the map requires a Google Maps application programming key configured in the website settings. Without this key the map cannot be rendered.

---

## Job posting and online recruitment

[N-U61-014] HR job positions can be published to the public website so that visitors can browse open roles. Publishing a job records the publication date. Re-opening a filled position removes the website publication. Archiving a job also removes the website publication. Each job has a computed public web address following a consistent slug-based pattern.

[N-U61-015] Visitors can apply for a job through an online form. When an application is submitted, the system validates that the target job is still open and assigns the application to the first appropriate stage in the recruitment pipeline. Closed jobs are rejected with a user-visible error.

[N-U61-016] Each combination of job and marketing source generates a tracking link containing campaign, medium, and source tags so that the origin of incoming candidates can be measured.

[N-U61-017] Department names are readable by portal users without requiring full access to the HR department model, so that job listings can display department information correctly.

---

## Recruitment live chat chatbot

[N-U61-018] An optional chatbot can be configured to guide visitors on the jobs page through the recruitment process and direct them to the most relevant job listings. This chatbot relies on the live chat infrastructure and is activated by installing a dedicated bridge module.

---

## Short-link tracking

[N-U61-019] Any website link can be shortened into a brief code-based address. Clicking a short link redirects the visitor to the original destination, and each click is counted. A statistics page for each short link is available by appending a special suffix to the short address. Short links can be given custom codes. The host portion of the short address uses the current website's base address rather than a fixed server address.

---

## Live chat on website

[N-U61-020] Each website can be assigned a dedicated live chat channel. When a visitor opens a page on that website, the live chat button and configuration for that channel are served. This assignment is configurable from the website settings panel. When a new channel is created from the website context, a welcome chatbot rule is automatically attached.

[N-U61-021] The website records anonymous visitor sessions. When a visitor starts a live chat conversation, the conversation is linked to the visitor record, and the assigned operator is stored on the visitor so their current status is visible to support staff.

[N-U61-022] An operator can proactively send a chat request to a visitor who is currently browsing. The chat session is created in a pending state until the visitor opens it. If the operator closes an empty chat without sending any message, the system deletes the pending session automatically to allow a fresh request.

---

## Email follow subscriptions

[N-U61-023] Visitors can subscribe to or unsubscribe from email updates for individual records on the website, such as a blog post or forum topic. Subscribers receive notifications when the record is updated. Subscribing as an anonymous visitor requires a security verification step. The system provides a public interface to check which records a user already follows.

---

## Partner directory

[N-U61-024] Partners and contacts can be given a long-form and a short-form description for display on the public website. Partners can be individually published or unpublished, and the system tracks publication changes in the activity log. The public partner detail page is accessible only when the partner is published, unless the viewer is a website editor. Each partner has a predictable web address based on its name.

---

## Payment integration

[N-U61-025] Payment providers can optionally be restricted to a specific website so that only the providers assigned to the current website are offered to visitors. When a provider has no website restriction it is available on all websites. The provider's return address for payment confirmation uses the active website's web address rather than a generic server address.

[N-U61-026] A donation widget can be placed on any website page. Visitors can choose an amount (with a configurable minimum and optional preset amounts), fill in their name, email and country, and complete payment. On success, a confirmation email is sent to the donor and a notification email is sent to an internal recipient. Anonymous visitors do not receive the option to save payment details for future use.

[N-U61-027] A snippet displays the payment methods accepted on the website for informational purposes. The list is derived from the payment providers configured for the current website. For public visitors the list is cached in the browser for seven days.

---

## User profile pages

[N-U61-028] Signed-in users with karma points and a published profile can be found and viewed on the website. Viewing another user's profile requires a minimum karma level, configurable per website with a default of one hundred and fifty points. Users with unpublished profiles cannot be viewed by others. Users can update certain profile fields for themselves including their location, personal website link, description, and publication status.

[N-U61-029] A new user who verifies their email address through a profile validation link is awarded three karma points, provided they currently have zero karma. The validation token is a daily-expiring hash derived from a secret identifier stored in system settings.

[N-U61-030] Achievement badges earned through gamification can be published on the website so they appear on user profile pages.

---

## Project task submission portal

[N-U61-031] A contact or feedback form on a website page can be configured to create project tasks directly. When a known visitor is recognised, their contact details are pre-filled. The submitted task is not assigned to any user by default. The task submission confirmation page bypasses the page cache so visitors always see a fresh confirmation. Submitted tasks can carry the submitter's name, company, and phone number for later use by the project team.

---

## eLearning channels and slides

[N-U61-032] An eLearning platform lets website administrators create courses, each classified as either a training course for interactive guided learning or a documentation repository for reference material. Courses can be tagged and grouped. The platform supports optional add-on features including an embedded forum, certifications via surveys, and integration with a mailing list, each controlled by a separate installation setting.

[N-U61-033] Enrolment in a course can be open to all visitors or by invitation only. Access to view course content can be restricted to the public, signed-in users, enrolled members only, or anyone who has the invitation link. Certain user groups can be configured for automatic enrolment. When a new user is created or assigned to a group that is linked to a course, they are enrolled automatically. An enrolled learner progresses through statuses from invited, to joined, to ongoing, and finally to completed. Invitation links include a security hash to prevent forgery.

[N-U61-034] Completing and rating courses earns karma points. The default awards are five points for ranking a course and ten for finishing it. Slides within a course can also be voted on, and karma thresholds apply for commenting and voting. Quiz slides offer decreasing rewards for later attempts: ten points on the first attempt, seven on the second, five on the third, and two for each subsequent attempt.

[N-U61-035] Individual lessons within a course (called slides) can be articles, images, documents, videos, or quizzes. Videos can be sourced from YouTube, Google Drive, or Vimeo. Documents and slides can be uploaded as files or linked from Google Drive. A Google Docs API key stored in system settings is required for Google Drive integration. Slides can be embedded on third-party websites, and each embedding site is tracked with a view count.

[N-U61-036] Quiz slides contain one or more multiple-choice questions, each with several answer options. At least one option must be correct and at least one incorrect. An explanatory comment can be attached to each answer option and is shown to the learner after they select it.

[N-U61-037] When a course slide is embedded on a third-party website, the system records the embedding site's address and counts the number of times it has been viewed from that site.

---

## Forum inside eLearning

[N-U61-038] A discussion forum can be embedded inside an eLearning course. The forum and course are linked one-to-one: a single forum can belong to at most one course. The forum's visibility level is automatically inherited from the course's own visibility setting. When a forum is assigned to a course, it becomes publicly accessible. When a forum is detached from a course, it is automatically restricted to slides administrators. Course images are automatically shared with the linked forum if the forum has no image of its own.

---

## SMS contact from visitor

[N-U61-039] A support agent can send an SMS message directly to a website visitor from the visitor record in the back office, provided the visitor is linked to a contact that has a phone number recorded. Opening the action presents a message composition interface pre-populated with the contact's phone number.

---

## Timesheet portal visibility

[N-U61-040] Whether timesheet entries are visible to customers in the customer portal is controlled by whether a specific portal view is active in the system. The check inspects the view by its internal key and returns whether that view is currently enabled, allowing administrators to toggle timesheet portal visibility by activating or deactivating the view.
