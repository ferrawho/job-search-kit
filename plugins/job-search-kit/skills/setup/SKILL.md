---
name: setup
description: Use when starting a job search with job-search-kit, or when the current folder has no profile/ or applications/ folder. Creates the workspace and checks Python dependencies.
---

# Setup

Set up the current folder as a job search workspace.

## Steps

1. **Find the plugin root.** It is two levels above this skill's base directory. Call it `PLUGIN`.
2. **Check the folder.** If the current folder already has `profile/` or `CLAUDE.md`, say so and ask before changing anything. Never overwrite an existing file.
3. **Check Python.**
   - Run `python --version`. If that fails, try `python3 --version`. Need 3.9+. Use whichever command worked for every later python step.
   - Run `python "PLUGIN/scripts/build_docx.py" --check`. It reports Python, python-docx and LibreOffice.
   - If Python or python-docx is missing, show the user the fix (`python -m pip install python-docx`, or the python.org installer link) and ask whether to run it. Do not install anything without a yes.
4. **Copy the workspace.** Copy everything under `PLUGIN/templates/workspace/` into the current folder. Rename `gitignore` to `.gitignore`. Don't copy `.gitkeep` files; just create the empty `profile/projects/`, `applications/` and `imports/` folders. Skip any file that already exists and list what was skipped.
   - If `.gitignore` already existed, show the kit's lines from `PLUGIN/templates/workspace/gitignore` that it doesn't have yet and offer to append them. Append only with a yes.
   - If `CLAUDE.md` already existed, offer to append the kit's sections from `PLUGIN/templates/workspace/CLAUDE.md` (Writing rules, Privacy, Files, Resume markdown format, Cover letter markdown format) to the end of it. The skills depend on them. Append only with a yes.
5. **Optional: LibreOffice.** If `--check` reported it missing, tell the user it's optional: without it they get .docx files and a page estimate. With it they also get PDFs and exact page counts.
6. **Optional: git.** Ask whether they want this folder in git for history. If yes:
   - First run `git rev-parse --is-inside-work-tree` and `git remote -v`. An error from the first means the folder isn't in a repo yet.
   - If the folder is already inside a repo, don't run `git init`. Show any remote. If a remote is on GitHub or another public host, warn that the repo could be public and ask them to check it's private before committing.
   - Otherwise run `git init`.
   - Before the first commit, list the files that would be committed (`git status --short`) and commit only with a yes.
   - Tell them the only acceptable options are a private remote or no remote at all. Never push it to a public repo: it will hold contact details, compensation and interview notes.
7. **Finish.** Show the folder tree and tell them the next step: `/job-search-kit:intake`. Mention that an existing resume, LinkedIn PDF or performance review put in `imports/` makes intake faster.
