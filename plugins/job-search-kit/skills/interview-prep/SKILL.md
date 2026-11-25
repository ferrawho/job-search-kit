---
name: interview-prep
description: Use when the user has an interview coming up (recruiter screen, hiring manager, panel, executive, technical, or case), wants likely questions and answers, wants a mock interview, or wants to debrief after one.
---

# Interview Prep

## Ground rules
- Read the workspace `CLAUDE.md` first if you haven't read it this session, and follow its writing rules.
- Every fact, number, title, date, tool, motive and company fact must come from the user, `profile/`, `jd.md`, or research done this session with a cited source. If it isn't there, ask or leave it out.

## Check inputs
- If `profile/master-resume.md` is missing or still has template placeholder text (such as "FIRST LAST" or "Filled in by intake"), stop and tell the user to run `/job-search-kit:setup` (if there's no `profile/` folder) or `/job-search-kit:intake`.
- If the application folder or its `jd.md` is missing, ask for the job description and create the folder the way score-jd does: `applications/<company>-<role>/` in lowercase-hyphenated form, with the JD saved verbatim to `jd.md` and the source URL and date at the top. If `notes.md` is missing, create it in score-jd's format with `Score: not scored` and the status this skill sets.

## Gather
Ask one at a time, skipping anything already in `applications/<folder>/notes.md`:
1. Which application (folder) and which stage?
2. Who are the interviewers (names, titles, LinkedIn if they have it)? What do they likely care about?
3. Date and format (video, onsite, length).
4. Anything the recruiter said about what to expect.

Research the company if a web tool is available: product, customers, recent news, funding, leadership. Cite sources.

## Write `applications/<folder>/prep-<stage>.md`
1. **60-second intro** ("tell me about yourself") built for this role. Present to past to why this job.
2. **Why this company / why this role:** specific, not flattering.
3. **Likely questions** (10 to 20), grouped by interviewer, each with an answer outline. Behavioral answers use stories from `profile/stories.md` in STAR form (`PLUGIN/references/star-guide.md`, plugin root two levels above this skill's base directory). Name which story each one uses.
4. **Gap questions:** the hard questions they'll ask about gaps in `score.md`, with honest answers.
5. **Questions to ask them:** 5 to 8, different per interviewer. Real questions whose answers help decide whether to take the job.
6. **Logistics checklist:** links, time zone, what to have open, salary answer if asked (from the profile floor and research).

Same writing rules as `CLAUDE.md`: never invent experience. That includes the user's motives, plans, and feelings: if an answer needs something the profile doesn't say (why they're leaving, what they want next), ask the user instead of drafting it.

Then update `applications/<folder>/notes.md`: `Status: Screen` for a recruiter screen, otherwise `Status: Interviewing` (use only the status names from the tracker skill; put the stage and date in `Next:`), today's date, and a log line. Status only moves forward: Scored < Tailored < Applied < Screen < Interviewing or Take-home (same rank) < Offer. Change `Status:` only to a later one; otherwise keep it and just add the log line. Set Accepted, Rejected, Withdrawn or Skipped only when the user says so.

## Mock interview mode
If the user asks for a mock: ask one question at a time and wait for the answer. After each, give short feedback: what landed, what was missing (numbers, "I" vs "we", length), and a tighter version. At the end, list the three weakest answers to practice.

## Debrief mode
After a real interview, ask what was asked, what went well, what was awkward, and any signals. Log it in `notes.md`, update `Status:` (tracker status names only, forward only as above), add new or improved stories to `profile/stories.md`, and draft a short thank-you note if wanted.
