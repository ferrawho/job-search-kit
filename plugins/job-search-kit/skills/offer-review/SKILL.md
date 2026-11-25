---
name: offer-review
description: Use when the user receives a job offer or employment contract and wants it reviewed, compared to the offer letter, valued, or negotiated.
---

# Offer Review

Start by saying once: this is a structured review, not legal advice. For termination, restrictive covenants, or significant equity, a short paid review by a local employment lawyer is worth it.

1. **Collect** the offer letter, contract, benefits summary, equity docs, and any recruiter emails with promises. Save them to `applications/<folder>/offer/` (git-ignored).
2. **Read** `PLUGIN/references/offer-checklist.md` (plugin root two levels above this skill's base directory) and go through every item.
3. **Write `offer/offer-review.md`:**
   - **Promised vs. written:** table of every term in the offer letter or emails, with where (or whether) the contract covers it. Flag anything missing, especially when there's an entire agreement clause.
   - **Clauses to watch:** quote the clause, explain it in plain language, rate it (fine / worth asking / important).
   - **Total compensation:** calculation with assumptions stated, compared with the current job and the salary floor from `profile/profile.md`.
   - **Negotiation plan:** prioritized asks, suggested wording, and the walk-away point. Use market data if a web tool is available, with sources.
   - **Questions to send:** a ready-to-send email asking for clarifications and getting missing terms in writing.
   - **Before you resign:** conditions that must clear first.
4. Update `notes.md`: `Status: Offer`, log line.
