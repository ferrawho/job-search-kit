---
name: tailor
description: Use when writing a tailored resume and/or cover letter for a specific job, after the JD has been saved to an applications/ folder. Produces markdown and formatted .docx files.
---

# Tailor Resume and Cover Letter

## Inputs
- `applications/<folder>/jd.md` (if missing, run the score-jd steps first)
- `applications/<folder>/score.md` if present
- `profile/` (master resume, projects, profile)
- Writing rules in the workspace `CLAUDE.md`. Follow all of them.

## Steps
1. **Keyword map.** List the 10 to 15 most important terms and requirements in the JD. For each, find the profile evidence or mark it as a GAP. Show this to the user briefly.
2. **Gaps.** Ask the user about each GAP: "Have you done anything like X that isn't in your profile?" If yes, add it to the profile (with their words) first, then use it. If no, leave it out of the resume. The cover letter may address one important gap honestly (adjacent experience, how fast they'd learn it).
3. **Write `resume.md`** in the resume markdown format:
   - Summary rewritten for this role, 3 to 4 sentences.
   - Skills grouped and ordered by what the JD emphasizes.
   - Bullets selected, reordered, and reworded from the master resume using the JD's language where it is accurate. **Rewording is allowed, new facts are not.**
   - Most relevant role gets the most bullets. Cut what doesn't serve this job.
   - Target 2 pages max (1 for early career).
4. **Write `cover.md`** in the cover format (`# Name`, contact line, then one paragraph per line):
   - Date line and greeting (use the hiring manager's name if known).
   - Paragraph 1: why this role, tied to something specific in the JD.
   - Paragraph 2 to 3: proof. One or two concrete results from the profile that match the job's biggest needs.
   - Paragraph 4: why this company (something real from the JD or company research) and a short close.
   - Under 400 words.
5. **Self-check before building.** Read both files and fix: em dashes, banned phrases, any claim not traceable to `profile/`, numbers not in the profile, typos.
6. **Build.** With `PLUGIN` = two levels above this skill's base directory, and the name from the profile:
   ```
   python "PLUGIN/scripts/build_docx.py" resume "applications/<folder>/resume.md" -o "applications/<folder>/<First>-<Last>-Resume-<Company>.docx"
   python "PLUGIN/scripts/build_docx.py" cover "applications/<folder>/cover.md" -o "applications/<folder>/<First>-<Last>-Cover-Letter-<Company>.docx"
   ```
   Fix every WARNING the script prints and rebuild. If the resume runs over the page target, propose specific bullets to cut and rebuild after the user agrees.
7. **Update `notes.md`:** `Status: Tailored`, today's date, log line.
8. **Report:** file paths, page count, gaps that remain, and a reminder to read it once out loud before sending.
