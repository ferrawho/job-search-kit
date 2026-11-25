# End-to-End Checklist

Run the skills headlessly against the fictional Sam Rivera fixture (`plugins/job-search-kit/tests/fixtures/sam-rivera/`) in a fresh scratch folder, then check every item below against the files the skills wrote. Never run this from inside the kit repo.

## How to run

From an empty scratch folder (`$WS`), with `KIT` set to this repo:

```bash
FLAGS=(--plugin-dir "$KIT/plugins/job-search-kit"
  --setting-sources local --strict-mcp-config
  --permission-mode acceptEdits --permission-prompts none
  --allowedTools "Read" "Glob" "Grep" "Skill" "Bash(python:*)" "Bash(cp:*)" "Bash(mkdir:*)" "Bash(ls:*)" "Bash(soffice --version)"
  --disallowedTools "PowerShell"
  --output-format json)
cd "$WS"
claude "${FLAGS[@]}" -p "/job-search-kit:setup Skip the optional git step."
cp -r "$KIT/plugins/job-search-kit/tests/fixtures/sam-rivera/profile/"* profile/
claude "${FLAGS[@]}" -p "/job-search-kit:score-jd $(cat "$KIT/plugins/job-search-kit/tests/fixtures/sam-rivera/jd-acme-ops-manager.md")"
claude "${FLAGS[@]}" -p "/job-search-kit:tailor for applications/<folder>. Skip gap questions: treat all gaps as not in profile."
claude "${FLAGS[@]}" -p "/job-search-kit:interview-prep for applications/<folder>, hiring manager stage, interviewer unknown. Skip questions and use defaults."
claude "${FLAGS[@]}" -p "/job-search-kit:tracker"
```

Why these flags: `acceptEdits` lets the session write files only inside the working folder, `--permission-prompts none` denies anything else instead of hanging, `--setting-sources local` keeps the user's own allow rules out, and PowerShell is disabled so shell calls go through the narrow Bash allowlist. Slash commands (`/job-search-kit:<skill>`) trigger the plugin skills in `-p` mode.

## Checklist

| # | Check | Result (2026-11-25) | Evidence |
|---|---|---|---|
| 1 | setup created `CLAUDE.md`, `.gitignore`, `profile/` tree, `applications/` | PASS | All present; each file identical to `templates/workspace/` (`diff --strip-trailing-cr`). `gitignore` renamed to `.gitignore`, `profile/projects/` and `applications/` created empty, no `.gitkeep` copied. Python 3.10.9 and python-docx detected, LibreOffice reported missing (optional). |
| 2 | `score.md` exists | PASS | `applications/acme-distribution-operations-manager/score.md`, plus `jd.md` (verbatim, source and date header) and `notes.md` (`Status: Scored`, `Score: 56`). |
| 3 | Score is plausibly 55 to 75 | PASS | 56/100. Must-have 20/35, Core 13/25, Seniority 5/15, Domain 6/10, Tools 7/10, Logistics 5/5. Recommendation: Skip. |
| 4 | Flags people management as a must-have gap | PASS | "3+ yrs people management, supervising supervisors: 0/7." Must-have gap 1: "3+ years managing people, including supervisors. Sam has zero, and it's the core of the job." |
| 5 | Cites profile files | PASS | Every table row cites a file, e.g. "(profile.md, Tools and skills)", "(projects/dock-scheduling.md)", "(projects/carrier-scorecard.md)". |
| 6 | `resume.md` and `cover.md`: no em dashes | PASS | U+2014 count 0 in both (U+2013 also 0). |
| 7 | `resume.md` and `cover.md`: no banned phrases | PASS | Case-insensitive search for all 18 phrases in the workspace `CLAUDE.md`: none found. |
| 8 | `resume.md` and `cover.md`: no people-management claims | PASS | Searched for manag*, supervis*, direct report, team of, hired/hiring, coach*, mentor*, performance review, people, leadership, lead*/led. Every hit is a non-claim: "mapped the inbound process with dock supervisors" (fixture fact), "Led rollout meetings" (fixture fact), "KPI reporting to leadership" (subheader), "Dear Hiring Manager", and the cover letter's honest disclosure: "I'll be direct about the gap: I have not had direct reports." |
| 9 | `resume.md` and `cover.md`: no numbers absent from the fixture | PASS | Every number in both files appears in the fixture profile or JD. Only exception: `2026` in the cover letter date line. |
| 10 | Both .docx files exist | PASS | `Sam-Rivera-Resume-Acme-Distribution.docx`, `Sam-Rivera-Cover-Letter-Acme-Distribution.docx`. |
| 11 | Both .docx files open | PASS | Both open with python-docx: resume 32 non-empty paragraphs starting "SAM RIVERA", cover 11 starting "Sam Rivera". Rebuilding both with `build_docx.py --no-pdf` printed no WARNING lines (resume about 1.1 pages, cover about 0.5). Not opened in Word itself in this headless run. |
| 12 | Prep file has a 60-second intro | PASS | `prep-hiring-manager.md` section 1, "60-second intro". |
| 13 | Prep file has 10+ questions | PASS | 17 likely questions (Q1 to Q17), behavioral ones naming the story used. |
| 14 | Prep file has gap questions about people management | PASS | Section 4, Gap 1: "No people management. The role asks for 3+ years, including supervising supervisors." Answer opens "I haven't had direct reports or written a performance review." |
| 15 | Prep file has questions to ask | PASS | Section 5, 8 questions, including support for a first-time manager. |
| 16 | `tracker.md` lists the application with status Tailored or later | PASS | One row: `acme-distribution-operations-manager`, score 56, status "Interviewing (hiring manager)", updated 2026-11-25. |

## Observations (not failures)

- **setup:** compound shell commands (`cd ...; ls; find ...`) were denied by the narrow allowlist, so the session read each template and wrote identical copies instead of using `cp`. Result is correct.
- **interview-prep:** set `Status: Interviewing (hiring manager)` in `notes.md`. The skill only says to update status in debrief mode, and the value is not one of the tracker's canonical statuses. The tracker handled it, but sorting relies on the canonical names.
- **interview-prep:** the "Why are you leaving Northwind?" outline includes a sentence not in the profile ("Northwind's next step for me isn't a people-management role"), flagged in the file as "Check that this is true before saying the second sentence." Hedged, but it is a drafted claim.
- **interview-prep:** the two problems above (non-canonical status, drafted motive) were fixed in commit f23ac5a.
- **interview-prep:** web search was denied by the permission setup, so company research was skipped and marked as a to-do in the file.

## Timings (headless runs)

setup 32 s, score-jd 66 s, tailor 44 s, interview-prep 81 s, tracker 10 s. Total 233 s, plus one 31 s setup attempt rerun after adjusting flags.
