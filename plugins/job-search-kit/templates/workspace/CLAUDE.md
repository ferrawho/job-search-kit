# Job Search Workspace

This folder is a job search workspace run with the job-search-kit plugin.

## Workflow
1. `/job-search-kit:intake` builds `profile/`. Run once, rerun any time to update.
2. Paste a job description and run `/job-search-kit:score-jd`.
3. `/job-search-kit:tailor` for roles worth applying to.
4. `/job-search-kit:interview-prep`, `/job-search-kit:take-home`, `/job-search-kit:offer-review` as the process moves.
5. `/job-search-kit:tracker` to see the whole pipeline.

## Writing rules (apply to everything written in this folder)
- **Never invent.** Experience, metrics, titles, dates, tools, and employers must trace to a file in `profile/`. If a job asks for something the profile doesn't show, list it as a gap and ask. Never write around it.
- **No em dashes.** Use periods, commas, colons, or rephrase.
- **Banned phrases:** spearheaded, leveraged, synergy, passionate about, results-driven, dynamic, proven track record, go-getter, think outside the box, detail-oriented, team player, hit the ground running, fast-paced environment, delve, tapestry, testament to, seamless, robust.
- **Specifics over adjectives.** Every resume bullet carries a number or a concrete outcome when the profile supports one. Never make up a number. Numbers marked "approx" in the profile may be written as "~" or "roughly".
- **Sound like a person.** Cover letters read like the candidate talking, not a template.

## Privacy
- Web searches and fetches contain only public things: the company, the role title, level, location, and an interviewer's name with their company. Never put my name, contact details, my current employer's internal numbers, compensation, salary floor, or any text from an offer or contract into a search query, URL or web form.
- Never upload or send files from this folder to any outside service, connector or email unless I ask for that specific file to be sent.
- Files in `applications/*/offer/` are never quoted outside that folder.
- If a number or detail is confidential to an employer, ask whether it can appear on a resume. If not, mark it "(confidential, don't publish)" in the profile and keep it out of resumes, cover letters and interview answers.

## Personal style notes
<!-- Add your own rules here. Examples: "Spell it e-commerce", "Don't mention the 2019 contract role". -->

## Files
- `profile/profile.md`: who I am, day-to-day, goals, constraints
- `profile/master-resume.md`: everything, uncut. Tailored resumes are cut from this.
- `profile/projects/*.md`: one file per standout project
- `profile/stories.md`: STAR story bank for interviews
- `profile/intake-progress.md`: which intake topics are done
- `applications/<company>-<role>/`: one folder per application (jd, score, resume, cover, prep, notes)
- `tracker.md`: pipeline summary written by the tracker skill
- `imports/`: existing resumes, LinkedIn exports and reviews you bring in (git-ignored)

## Resume markdown format (used by the .docx builder)
- `# Name`, then the contact line on the next line
- `## SECTION HEADER`
- `### Company | short description`
- `**Job Title** | Month Year - Month Year`
- `#### Subheader`
- `- bullet` (inline `**bold**` works)
- Anything else is a plain paragraph.

## Cover letter markdown format
- `# Name`, then the contact line on the next line
- Every other non-empty line is one paragraph (date, greeting, body paragraphs, sign-off)
- Inline `**bold**` works. No other headings.
