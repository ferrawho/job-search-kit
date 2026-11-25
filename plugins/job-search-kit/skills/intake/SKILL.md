---
name: intake
description: "Use when building or updating the job seeker's profile in profile/: their role, day-to-day work, standout projects, metrics, skills, and story bank. Run after setup, before scoring or tailoring."
---

# Intake

Interview the user to build a complete, truthful profile. Everything later (scores, resumes, interview answers) is only as good as this.

## Ground rules
- Read the workspace `CLAUDE.md` first if you haven't read it this session, and follow its writing rules.
- Every fact, number, title, date, tool, motive and company fact must come from the user, `profile/`, `jd.md`, or research done this session with a cited source. If it isn't there, ask or leave it out.

## Before starting
- If `profile/` doesn't exist, tell them to run `/job-search-kit:setup` and stop.
- Read `profile/intake-progress.md`. If some topics are checked, say what's done and continue from the first unchecked topic. The user can also name a topic to redo.
- Ask if they have an existing resume, LinkedIn PDF export, performance review, or portfolio. If so, read it first. PDFs can be read directly. For a .docx, extract the text with `python` (or `python3`, whichever worked in setup): `python -c "import docx,sys; print(chr(10).join(p.text for p in docx.Document(sys.argv[1]).paragraphs))" "<file>.docx"`.
- Before prefilling, ask once how recent the document is and what has changed since (new job, title, or big result). Old documents often list a past job as "present".
- Show the user what you would prefill, topic by topic, and save it only after they confirm or correct it. Then only ask questions that fill gaps or dig for specifics.

## How to interview
- **One question per message.** Multiple choice when the answer space is predictable. Open questions for stories.
- **Dig for numbers.** For every accomplishment ask: how many, how much, how long before vs. after, what would have happened without it. If they don't know, write "no metric". If they estimate, write the number with "(approx)". Never supply a number yourself.
- **Dig for "I".** Ask what *they* personally did versus the team.
- **Get the day-to-day.** Ask them to walk through a typical week. This is often where the best resume material hides.
- Keep it moving. If an answer is thin, ask one follow-up, then move on and note it as a weak spot.
- After each topic, **write the files immediately** and check the box in `intake-progress.md`. If the session ends, nothing is lost.

## Topics
1. **Basics and goals:** name, location, contact line, links, target roles and level, remote preference, current compensation (optional), salary floor, timeline, dealbreakers. Write `profile/profile.md` Basics.
2. **Current role:** title, company, what the company does, size, who they report to and work with. Write `profile/profile.md` Current role.
3. **Day-to-day:** typical week, recurring responsibilities, tools touched daily. Write `profile/profile.md` Day-to-day.
4. **Standout projects (aim for 3 to 6):** for each, ask: the problem, why it mattered, what they did, who else was involved, tools, the result in numbers, what they'd do differently. Write one file per project in `profile/projects/<short-slug>.md` with those headings.
5. **Previous roles:** title, company, dates, top 2 to 4 accomplishments each (same digging, lighter touch). Write `profile/profile.md` Previous roles.
6. **Skills, tools, certifications, education.** Write `profile/profile.md` Tools and skills (certifications and education go there too).
7. **Known for:** what colleagues come to them for, feedback from reviews, awards. Write `profile/profile.md` Known for, and fill in "What I want next" if it came up.
8. **Story bank:** turn projects and accomplishments into STAR stories in `profile/stories.md` using `PLUGIN/references/star-guide.md` (plugin root is two levels above this skill's base directory). Tag competencies. Stories only restate what the user told you: don't add actions, results or numbers they didn't give. If a STAR part is missing, ask for it; if they don't know, write "unknown". Point out which common competencies have no story yet and ask for one example for each.
9. **Master resume:** write `profile/master-resume.md` in the resume markdown format from the workspace `CLAUDE.md`. Include **everything**, uncut. Follow every writing rule in `CLAUDE.md`.

## Finish
- Summarize the profile in 5 lines.
- List weak spots: accomplishments with no metric, missing competencies, unclear dates.
- Next step: paste a job description and run `/job-search-kit:score-jd`.
