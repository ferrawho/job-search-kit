---
name: score-jd
description: Use when the user shares a job description (pasted text, file, or URL) and wants to know how well they fit, whether to apply, or what the gaps are.
---

# Score a Job Description

## Steps
1. **Check the profile.** If `profile/master-resume.md` still has placeholder text, tell them to run `/job-search-kit:intake` first and stop.
2. **Get the JD.** Pasted text, a file path, or a URL (fetch it if a web tool is available; otherwise ask them to paste it).
3. **Create the application folder:** `applications/<company>-<role>/` in lowercase-hyphenated form, e.g. `applications/acme-ops-analyst/`. Save the JD verbatim to `jd.md` with the source URL and date at the top.
4. **Read** `profile/profile.md`, `profile/master-resume.md`, `profile/projects/*.md`, and the rubric at `PLUGIN/references/jd-scoring-rubric.md` (plugin root is two levels above this skill's base directory).
5. **Score** using the rubric. Every point cites the profile file and fact. Be honest: an inflated score wastes the user's time on bad applications.
6. **Write `score.md`** in the rubric's output format.
7. **Write `notes.md`:**
   ```
   Status: Scored
   Updated: <today>
   Score: <n>
   Next: <apply / skip / decide by date>

   ## Log
   - <today>: Scored <n>
   ```
8. **Report** the score, the verdict, the top gaps, and the red flags in chat. If the recommendation is apply, offer `/job-search-kit:tailor`.
