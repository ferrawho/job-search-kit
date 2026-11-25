---
name: take-home
description: Use when the user has a take-home assignment, case study, or presentation to prepare as part of an interview process.
---

# Take-Home Assignments

## Ground rules
- Read the workspace `CLAUDE.md` first if you haven't read it this session, and follow its writing rules.
- Every fact, number, title, date, tool, motive and company fact must come from the user, `profile/`, `jd.md`, or research done this session with a cited source. If it isn't there, ask or leave it out.

## Check inputs
- If `profile/master-resume.md` is missing or still has template placeholder text (such as "FIRST LAST" or "Filled in by intake"), stop and tell the user to run `/job-search-kit:setup` (if there's no `profile/` folder) or `/job-search-kit:intake`.
- If the application folder or its `jd.md` is missing, ask for the job description and create the folder the way score-jd does: `applications/<company>-<role>/` in lowercase-hyphenated form, with the JD saved verbatim to `jd.md` and the source URL and date at the top. If `notes.md` is missing, create it in score-jd's format with `Score: not scored` and the status this skill sets.

## Steps
1. **Save the brief** to `applications/<folder>/take-home/brief.md`.
2. **Scope it.** Confirm: deadline, suggested time budget, format (doc, slides, live presentation), audience, and how it will be judged. Write down unstated assumptions; they become an "Assumptions" section in the deliverable.
3. **Outline first.** Propose a structure, check it with the user before drafting. Lead with the answer or recommendation, then support it.
4. **Draft** in `applications/<folder>/take-home/draft.md`. Use the user's real experience from `profile/` as proof points where relevant. Label every assumption and estimate as such in the text. External facts (market sizes, competitor details, benchmarks) need a cited source; if there isn't one, mark them "(verify)". Same in `qa.md`.
5. **Format.**
   - Document: produce markdown, and a .docx if they want one (a pptx/docx skill may be available; otherwise keep it in markdown and tell them to paste it into their tool).
   - Presentation: slide-by-slide outline with a headline per slide, speaker notes, and a timing plan. Use a slides/pptx skill if one is available.
6. **Pressure-test.** Write `applications/<folder>/take-home/qa.md`: the 10 toughest questions a panel could ask about the work, with answers. Include "what would you do with more time or data?"
7. **Respect the time budget.** If the work is going far past what the company asked for, say so. Unpaid work should be scoped to what they asked.
8. Update `applications/<folder>/notes.md`: `Status: Take-home`, today's date, log line. Status only moves forward: Scored < Tailored < Applied < Screen < Interviewing or Take-home (same rank) < Offer. Change `Status:` only to a later one; otherwise keep it and just add the log line. Set Accepted, Rejected, Withdrawn or Skipped only when the user says so.
