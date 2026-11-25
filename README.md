# job-search-kit

A Claude Code plugin that runs your job search with you. It interviews you to build a truthful profile of your work, scores job descriptions against it, writes tailored resumes and cover letters as formatted Word files, preps you for interviews, helps with take-home assignments, and reviews offers.

It never invents experience. Every claim in a resume or answer has to trace back to your profile. When a job asks for something you don't have, it tells you it's a gap instead of writing around it.

## Skills

| Command | What it does |
|---|---|
| `/job-search-kit:setup` | Creates your workspace folder and checks Python. Run once. |
| `/job-search-kit:intake` | Interviews you about your role, day-to-day work, standout projects, and results. Builds your profile, master resume, and interview story bank. |
| `/job-search-kit:score-jd` | Scores a job description 0 to 100 against your profile, with gaps, red flags, and an apply/skip call. |
| `/job-search-kit:tailor` | Writes a resume and cover letter for one job and builds the .docx files. |
| `/job-search-kit:interview-prep` | Likely questions and answers per interviewer, questions to ask them, mock interviews, and debriefs. |
| `/job-search-kit:take-home` | Scopes and drafts take-home assignments and presentations. |
| `/job-search-kit:offer-review` | Compares the offer with the contract, flags gaps and risky clauses, and builds a negotiation plan. Not legal advice. |
| `/job-search-kit:tracker` | Shows your pipeline and what needs follow-up. |

## Requirements

- [Claude Code](https://claude.com/claude-code)
- Python 3.9 or newer, with python-docx: `python -m pip install python-docx`
- Optional: [LibreOffice](https://www.libreoffice.org/) for PDF export and exact page counts

## Install

In Claude Code (2.1.275 or later):

```
/plugin install job-search-kit --marketplace ferrawho/job-search-kit
```

On older versions, use two steps:

```
/plugin marketplace add ferrawho/job-search-kit
/plugin install job-search-kit@job-search-kit
```

## Quick start

1. Make an empty folder for your job search and open a terminal there.
2. Run `claude`.
3. Type `/job-search-kit:setup`.
4. Type `/job-search-kit:intake`. If you have an existing resume or a LinkedIn PDF export, drop it in the folder first. Intake reads it and only asks about what's missing.
5. Paste a job description and type `/job-search-kit:score-jd`.

The first time, Claude asks permission to read the plugin's files and run python. Approving is safe: the plugin only reads its own files and runs python to build and read Word files in your workspace.

Intake saves after every topic, so you can stop and pick it up later.

## Your data

Everything about you lives in your own workspace folder (`profile/` and `applications/`), never inside the plugin. If you put your workspace in git, keep that repo private: it holds your contact details and, later, offer letters. Offer documents are git-ignored by default.

## Updating

```
/plugin marketplace update job-search-kit
```

## Customizing

Your workspace `CLAUDE.md` holds the writing rules every skill follows: no em dashes, a list of banned buzzwords, numbers over adjectives. Edit it to add your own rules, such as spellings to use or roles to leave out.

## Resume format

Resumes are written in plain markdown and turned into Word files by `scripts/build_docx.py`:

```
# FIRST LAST
City, Region | email | phone | linkedin.com/in/handle

## EXPERIENCE
### Company | what the company does
**Job Title** | Jan 2022 - Present
#### Optional subheader
- Bullet with a **bold** phrase and a number
```

The script warns about anything it can't format. You don't need to learn this; the tailor skill writes it for you.

## For maintainers

Bump `version` in `plugins/job-search-kit/.claude-plugin/plugin.json` on every release. Installed users only receive an update when the version changes.

## License

MIT
