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

## First time? Start here

You only do this once. It takes about 15 minutes. You need a paid Claude plan (Pro or Max) to use Claude Code.

**1. Open a terminal**
- **Windows:** press the Start key, type `PowerShell`, and open it.
- **Mac:** press Cmd+Space, type `Terminal`, and open it.

**2. Install Claude Code.** Paste this line into the terminal and press Enter:
- **Windows:** `irm https://claude.ai/install.ps1 | iex`
- **Mac:** `curl -fsSL https://claude.ai/install.sh | bash`

Close the terminal and open a new one. Type `claude` and press Enter, then follow the steps to log in with your Claude account. Type `/exit` when you're done. If anything goes wrong, the official guide is at [docs.claude.com/en/docs/claude-code/setup](https://docs.claude.com/en/docs/claude-code/setup).

**3. Install Python.** Download it from [python.org/downloads](https://www.python.org/downloads/) and run the installer.
- **Windows:** on the first screen, tick **"Add python.exe to PATH"** before clicking Install. This is the step people most often miss.
- **Mac:** use the default options.

**4. Install the Word file library.** In a new terminal:
- **Windows:** `python -m pip install python-docx`
- **Mac:** `python3 -m pip install python-docx`

**5. Install Git.** It's needed to download the plugin. Windows: [git-scm.com/download/win](https://git-scm.com/download/win), default options. Mac: type `git --version` in the terminal and accept the prompt to install the developer tools.

**6. Private repo only: sign in to GitHub.** If this repo was shared with you privately, install the GitHub CLI from [cli.github.com](https://cli.github.com/), then run `gh auth login` and choose GitHub.com, HTTPS, and "Login with a web browser". Also run `gh auth setup-git` so downloads use that login.

**7. Make a folder for your job search**, for example `Documents\job-search`. Open a terminal in it:
- **Windows:** open the folder in File Explorer, click the address bar, type `powershell`, press Enter.
- **Mac:** right-click the folder in Finder, then Services, then New Terminal at Folder.

Then follow **Install** and **Quick start** below.

## Requirements

- [Claude Code](https://claude.com/claude-code)
- Python 3.9 or newer, with python-docx: `python -m pip install python-docx`
- Optional: [LibreOffice](https://www.libreoffice.org/) for PDF export and exact page counts

## Install

Run `claude` in any terminal, then type this line inside Claude Code (2.1.275 or later):

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

Every time after that: open a terminal in your job search folder and run `claude`. The skills are already installed.

## A typical week

| When | Run | What you get |
|---|---|---|
| Once, at the start | `/job-search-kit:intake` | Your profile, master resume, and interview stories. Rerun it when something changes (new project, new result). |
| You find a posting | Paste it, then `/job-search-kit:score-jd` | A fit score and an apply/skip call. Takes a minute. Do this for every posting before spending time on it. |
| It's worth applying | `/job-search-kit:tailor` | A tailored resume and cover letter as Word files in `applications/<company>-<role>/`. Read them once before sending. |
| You applied | Tell Claude "I applied to Acme" | The tracker updates and sets a follow-up date. |
| An interview is booked | `/job-search-kit:interview-prep` | Likely questions, answers built from your real stories, and questions to ask them. Ask for a mock interview to practise. |
| After each interview | "Debrief my Acme interview" | Notes saved, stories improved, thank-you note drafted. |
| You get a take-home | `/job-search-kit:take-home` | A scoped plan, a draft, and tough-question prep. |
| You get an offer | `/job-search-kit:offer-review` | What's missing from the contract, clauses to ask about, and a negotiation plan. |
| Monday mornings | `/job-search-kit:tracker` | Your whole pipeline and what needs a follow-up. |

You don't have to remember exact command names. Asking in plain words ("score this job", "prep me for my interview tomorrow") works too.

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
