# Gatekeeper Review: Newsletter Version — The Land That Remembers

**Date:** February 2026
**Version Reviewed:** newsletter-version.md v1
**Source:** Adapted from approved final-post.md

---

## Status: REVISIONS NEEDED

---

## What's Working

- **Subject line is strong** — "The Sea of Galilee is still there" is under 50 characters, curiosity-driven, and emotionally resonant. It stops you.
- **Preview text complements well** — "Not a painting. Not a story. A real place where life happens every day." adds context without repeating the subject.
- **Greeting is warm and simple** — "Dear friend," matches the newsletter skill guidelines perfectly.
- **Emotional core is preserved** — The "living land, not a museum" thread carries through from the blog post. The adaptation kept exactly the right material.
- **Uri's video CTA is smart** — Using the unique video asset as primary CTA is the right call for this post. It drives engagement and differentiates from a standard "place your prayer" email.
- **Word count is perfect** — ~350 words, well within the 300-500 sweet spot.
- **Sign-off works** — "Walking with you in faith, The Pilgrim Prayers Team" is warm and on-brand.
- **Scripture is woven naturally** — Two references (Matthew 4:18-22, Mark 4:39), both used as story moments, not sermon.
- **Footer has all required elements** — Unsubscribe, links, and tagline are present.

## What Needs Work

### 1. Em dashes present — must be removed

Lines found with em dashes:
- "in Sunday school, in Scripture, in songs, it's easy to forget that it's a real place" — this line is clean
- BUT: The voice-dna.md still lists em dashes in its punctuation section. The newsletter itself appears clean based on the user's explicit rule: **no em dashes in any content**.

**Verdict:** Newsletter copy is clean of em dashes. Pass.

### 2. CTA count — borderline

The newsletter skill says **one CTA only**. This newsletter has:
1. **[Watch Uri's video →]** (primary, mid-body)
2. "Whenever you're ready, we're here to carry your prayer." (soft secondary, closing)
3. Footer links: [Read the full story on our blog →] | [Place a prayer in Jerusalem →] | [About Us]

The primary CTA (video) is correct. The closing "carry your prayer" line reads as a warm invitation, not a hard CTA, which is acceptable. Footer links are standard navigation and don't count as CTAs.

**Verdict:** Acceptable. The primary CTA is clearly the video. The closing invitation is gentle enough to pass.

### 3. Bold line "This is not ancient history. This is a living land." — review needed

This bold line works in the blog post as a section-turning statement. In the shorter email format, it creates a strong visual break. It works, but it's also the most "headline-y" moment in what should feel like a letter.

**Verdict:** Keep. It serves as the emotional anchor and is consistent with the blog post's approved voice.

### 4. One issue: "Dear friend" → personalization note is buried

The Newsletter Agent's notes mention that `[First Name]` can replace "friend" if merge tags are available. This is good practice, but the note is buried in the agent notes section. This should be flagged clearly for implementation.

**Action needed:** Add a visible note at the top of the newsletter file:
```
**Personalization:** Replace "Dear friend" with "Dear [First Name]" if merge tags are available.
```

### 5. UTM tracking note is buried

Same issue. The UTM parameter suggestion (`?utm_source=newsletter&utm_medium=email&utm_campaign=galilee-post`) is only in the agent notes. It should be applied to all links in the newsletter before sending.

**Action needed:** Add a visible note at the top:
```
**Tracking:** Apply UTM parameters to all links before sending.
```

## Evangelical Alignment Check

- [x] No Catholic-specific references
- [x] Scripture used naturally (Matthew, Mark) — both from the Gospels
- [x] Faith expressed warmly, not preachy
- [x] No political messaging — Golan Heights mentioned only in Uri's video context
- [x] Living land angle resonates with Evangelical connection to Israel
- [x] No saints, no Marian references, no liturgical calendar references

## "Sound Like Us" Test (from voice-dna.md)

1. Would a believer feel comforted reading this? **Yes.** The tone is warm and inviting.
2. Does it sound like a real person who cares? **Yes.** Letter format, personal greeting, no marketing language.
3. Is it free of pressure, hype, or guilt? **Yes.** Gentle invitation only.
4. Are we promising only what we can deliver? **Yes.** No miracle promises. Just "carry your prayer."
5. Would someone skeptical feel respected? **Yes.** No hard sell, no urgency.

## Newsletter Skill Checklist

- [x] Subject line under 50 characters (38 characters)
- [x] Preview text complements (not repeats) the subject
- [x] Email body under 500 words (~350 words)
- [x] Warm greeting included
- [x] One clear story, emotionally complete
- [x] One primary CTA (video link)
- [x] CTA is warm, not pushy
- [x] Personal sign-off
- [x] Footer with unsubscribe link
- [x] Matches voice DNA
- [x] Reads like a letter, not a marketing email

## Recommendation

**CONDITIONAL APPROVAL** — The newsletter copy is strong and on-brand. Two small implementation notes need to be surfaced before sending:

1. Add personalization flag at top of file (merge tag for first name)
2. Add UTM tracking flag at top of file (for all links)

Once these two notes are added to the newsletter file header, this is **APPROVED** for sending.

---

*Reviewed by: Gatekeeper Agent*
*Review type: Newsletter version (second pass)*
