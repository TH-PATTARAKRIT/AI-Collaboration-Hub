# U92 Neutral Knowledge — Website Content Platform
> NEUTRAL LAYER — no source paths, no class/method names, no file extensions, no snake_case, no backticks

| NR-ID | Statement |
|---|---|
| NR-U92-001 | The blog container record inherits thread, multi-website, SEO metadata, and cover-properties capabilities. |
| NR-U92-002 | A blog post inherits thread, SEO metadata, multi-website publication mixin, and cover-properties mixin. |
| NR-U92-003 | Blog posts carry a many-to-many relationship to a dedicated tag model. |
| NR-U92-004 | Blog posts track a view count that is read-only, not copied on duplication, and defaults to zero. |
| NR-U92-005 | The website association on a blog post is derived indirectly through the owning blog record, not stored directly on the post. |
| NR-U92-006 | SEO metadata for blog posts populates Open Graph type as "article" and includes published time, modified time, and tag names. |
| NR-U92-007 | Website designer users may filter posts by published or unpublished state; ordinary visitors only see posts whose publish date is in the past. |
| NR-U92-008 | The tag model for blogs has a name, an optional grouping category, a color index, and a reverse many-to-many to its associated posts. |
| NR-U92-009 | Tag categories group blog tags and enforce a uniqueness constraint on the category name. |
| NR-U92-010 | When a blog post is set to published, the system sends a notification message to blog followers using a dedicated subtype. |
| NR-U92-011 | Archiving a blog post automatically removes its published status. |
| NR-U92-012 | The forum post record inherits thread, SEO metadata, and website searchable capabilities. |
| NR-U92-013 | A forum post may be in one of five states: active, pending validation, closed, offensive, or flagged. |
| NR-U92-014 | Forum posts aggregate votes through a child vote record collection; the total vote count is stored for performance. |
| NR-U92-015 | Forum answers are represented as child posts linked to their parent question through a self-referential relationship; deletion of the question cascades to answers. |
| NR-U92-016 | Each vote record links one user to one post with a value of upvote, downvote, or neutral, enforced as unique per user-post pair. |
| NR-U92-017 | Non-administrator users cannot forge the vote owner; the system strips any user identity override on vote creation. Voting for one's own post raises an error. |
| NR-U92-018 | Whether a user can ask a new question is determined by comparing the user's karma score to the forum's configurable ask threshold (default 3). |
| NR-U92-019 | Upvote permission requires karma above the forum upvote threshold or an existing downvote on the post. Downvote permission is symmetric. |
| NR-U92-020 | A post is viewable when the user can close it, or when the post is active and its author has positive karma or is the current user. |
| NR-U92-021 | Each forum defines configurable karma amounts granted or deducted for: asking a question (default +2), question upvoted (+5), question downvoted (−2), answer upvoted (+10), answer downvoted (−2), accepting an answer (+15 to answerer, +2 to acceptor), post flagged as offensive (−100). |
| NR-U92-022 | Each forum defines configurable karma thresholds required for: asking (3), answering (3), editing own post (1), editing all posts (300), closing own post (100), closing all posts (500), deleting own post (500), deleting all posts (1000), upvoting (5), downvoting (50), posting without validation (100), moderating (1000). |
| NR-U92-023 | A newly created question from a user below the "post without validation" threshold is automatically placed into pending state and requires moderator approval. |
| NR-U92-024 | The slide channel record represents a course; it inherits rating, activity, image, website publication, and website searchable capabilities. |
| NR-U92-025 | A slide channel has a type of either training or documentation (default training). |
| NR-U92-026 | A slide channel's enrollment policy is either open to all (public) or by invitation only; the system automatically forces invitation-only when channel visibility is restricted to members. |
| NR-U92-027 | Slide channel visibility has four options: visible to everyone (public), visible to signed-in users, visible only to enrolled members, or accessible via a direct link. |
| NR-U92-028 | A database-level constraint prevents setting visibility to members-only unless enrollment is simultaneously set to invitation-only. |
| NR-U92-029 | The slide record inherits thread, image, SEO metadata, and website publication capabilities. |
| NR-U92-030 | A slide must belong to one of five content categories: image, article, document, video, or quiz. |
| NR-U92-031 | A slide may be individually marked as a preview, granting public access to that slide even when the surrounding course requires enrollment. |
| NR-U92-032 | A course is visible to a user when the course is publicly visible, or when the user is enrolled, or when the course is set for signed-in users and the user is authenticated. |
| NR-U92-033 | Publishing a slide within a course is restricted to the course responsible user or users belonging to the slides-manager group. |
| NR-U92-034 | Each enrollment record linking a partner to a course carries one of four statuses: invitation sent, joined, ongoing, or completed. |
| NR-U92-035 | Completing a course awards the attendee configurable karma points; the default is 10 for finishing and 5 for ranking. |
| NR-U92-036 | Completing a quiz within a course awards karma that decreases with each attempt: 10 for the first, 7 for the second, 5 for the third, and 2 for every subsequent attempt. |
