---
name: tailor
description: Use when writing a tailored resume and/or cover letter for a specific job, after the JD has been saved to an applications/ folder. Produces markdown and formatted .docx files.
---

# Tailor Resume and Cover Letter

## Ground rules
- Read the workspace `CLAUDE.md` first if you haven't read it this session, and follow its writing rules.
- Every fact, number, title, date, tool, motive and company fact must come from the user, `profile/`, `jd.md`, or research done this session with a cited source. If it isn't there, ask or leave it out.

## Check inputs
- If `profile/master-resume.md` is missing or still has template placeholder text (such as "FIRST LAST" or "Filled in by intake"), stop and tell the user to run `/job-search-kit:setup` (if there's no `profile/` folder) or `/job-search-kit:intake`.
- If the application folder or its `jd.md` is missing, ask for the job description and create the folder the way score-jd does: `applications/<company>-<role>/` in lowercase-hyphenated form, with the JD saved verbatim to `jd.md` and the source URL and date at the top. If `notes.md` is missing, create it in score-jd's format with `Score: not scored` and the status this skill sets.

## Inputs
- `applications/<folder>/jd.md`
- `applications/<folder>/score.md` if present
- `profile/` (master resume, projects, profile)

## Steps
1. **Keyword map.** List the 10 to 15 most important terms and requirements in the JD. For each, find the profile evidence or mark it as a GAP. Show this to the user briefly.
2. **Gaps.** Ask the user about each GAP: "Have you done anything like X that isn't in your profile?" If yes, add it in their words to both `profile/profile.md` (the matching section) and `profile/master-resume.md` first, then use it. If no, leave it out of the resume. The cover letter may address one important gap honestly, using adjacent experience from the profile only. No promises about how fast they'd learn it unless the user said so.
3. **Motives.** The cover letter's "why this role" and "why this company" come from the user's own reasons. If `profile/profile.md` "What I want next" doesn't cover this job, ask them why they want it.
4. **Write `resume.md`** in the resume markdown format:
   - Summary rewritten for this role, 3 to 4 sentences.
   - Skills grouped and ordered by what the JD emphasizes.
   - Before cutting, check that `master-resume.md` has every role and result in `profile.md` and `profile/projects/`. If it's missing some (it can lag behind the other files), add them to it first.
   - Bullets selected, reordered, and reworded from the master resume using the JD's language where it is accurate. **Rewording is allowed, new facts are not.**
   - Most relevant role gets the most bullets. Cut what doesn't serve this job.
   - Target 2 pages max (1 for early career).
5. **Write `cover.md`** in the cover format (`# Name`, contact line, then one paragraph per line):
   - Date line and greeting (use the hiring manager's name if known).
   - Paragraph 1: why this role, from the user's stated reasons, tied to something specific in the JD.
   - Paragraph 2 to 3: proof. One or two concrete results from the profile that match the job's biggest needs.
   - Paragraph 4: why this company (the user's reasons, plus facts from `jd.md` or sourced research) and a short close.
   - Under 400 words.
6. **Self-check before building.** Read both files and fix: em dashes, banned phrases, any claim not traceable to `profile/`, numbers not in the profile, motives the user didn't state, company facts without a source in `jd.md` or research, typos.
7. **Build.** With `PLUGIN` = two levels above this skill's base directory, the name from the profile, and `python` (or `python3`, whichever worked in setup):
   ```
   python "PLUGIN/scripts/build_docx.py" resume "applications/<folder>/resume.md" -o "applications/<folder>/<First>-<Last>-Resume-<Company>.docx"
   python "PLUGIN/scripts/build_docx.py" cover "applications/<folder>/cover.md" -o "applications/<folder>/<First>-<Last>-Cover-Letter-<Company>.docx"
   ```
   Fix every WARNING the script prints and rebuild. If the resume runs over the page target, propose specific bullets to cut and rebuild after the user agrees.
8. **Update `notes.md`:** `Status: Tailored`, today's date, log line. Status only moves forward: Scored < Tailored < Applied < Screen < Interviewing or Take-home (same rank) < Offer. Change `Status:` only to a later one; otherwise keep it and just add the log line. Set Accepted, Rejected, Withdrawn or Skipped only when the user says so.
9. **Report:** file paths, page count (without LibreOffice it's an estimate: tell the user to open the file to confirm), gaps that remain, and a reminder to read it once out loud before sending.
