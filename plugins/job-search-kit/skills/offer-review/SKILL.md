---
name: offer-review
description: Use when the user receives a job offer or employment contract and wants it reviewed, compared to the offer letter, valued, or negotiated.
---

# Offer Review

Start by saying once: this is a structured review, not legal advice. For termination, restrictive covenants, or significant equity, a short paid review by a local employment lawyer is worth it.

## Ground rules
- Read the workspace `CLAUDE.md` first if you haven't read it this session, and follow its writing rules.
- Every fact, number, title, date, tool, motive and company fact must come from the user, `profile/`, `jd.md`, or research done this session with a cited source. If it isn't there, ask or leave it out.

## Check inputs
- If `profile/master-resume.md` is missing or still has template placeholder text (such as "FIRST LAST" or "Filled in by intake"), stop and tell the user to run `/job-search-kit:setup` (if there's no `profile/` folder) or `/job-search-kit:intake`.
- If the application folder or its `jd.md` is missing, ask for the job description and create the folder the way score-jd does: `applications/<company>-<role>/` in lowercase-hyphenated form, with the JD saved verbatim to `jd.md` and the source URL and date at the top. If `notes.md` is missing, create it in score-jd's format with `Score: not scored` and the status this skill sets.

## Steps
1. **Collect** the offer letter, contract, benefits summary, equity docs, and any recruiter emails with promises. Save them to `applications/<folder>/offer/` (git-ignored).
2. **Read** `PLUGIN/references/offer-checklist.md` (plugin root two levels above this skill's base directory) and go through every item.
3. **Write `offer/offer-review.md`:**
   - **Promised vs. written:** table of every term in the offer letter or emails, with where (or whether) the contract covers it. Flag anything missing, especially when there's an entire agreement clause.
   - **Clauses to watch:** quote the clause, explain it in plain language, rate it (fine / worth asking / important).
   - **Total compensation:** calculation with assumptions stated, compared with the current job and the salary floor from `profile/profile.md`. If the profile's "Current compensation" line is empty, ask the user for it (base, bonus, equity, benefits) and save it there.
   - **Negotiation plan:** prioritized asks, suggested wording, and the walk-away point. Use market data only with a cited source (never a figure from memory). Mention a competing offer only if the user has told you they have one, and never word an ask to imply one.
   - **Questions to send:** a ready-to-send email asking for clarifications and getting missing terms in writing.
   - **Before you resign:** conditions that must clear first.
4. Update `notes.md`: `Status: Offer`, today's date, log line. Status only moves forward: Scored < Tailored < Applied < Screen < Interviewing or Take-home (same rank) < Offer. Change `Status:` only to a later one; otherwise keep it and just add the log line. Set Accepted, Rejected, Withdrawn or Skipped only when the user says so.
