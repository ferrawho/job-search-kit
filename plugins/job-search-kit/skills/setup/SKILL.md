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
4. **Copy the workspace.** Copy everything under `PLUGIN/templates/workspace/` into the current folder. Rename `gitignore` to `.gitignore`. Don't copy `.gitkeep` files; just create the empty `profile/projects/` and `applications/` folders. Skip any file that already exists and list what was skipped.
   - If `CLAUDE.md` already existed, offer to append the kit's sections from `PLUGIN/templates/workspace/CLAUDE.md` (Writing rules, Files, Resume markdown format, Cover letter markdown format) to the end of it. The skills depend on them. Append only with a yes.
5. **Optional: LibreOffice.** If `--check` reported it missing, tell the user it's optional: without it they get .docx files and a page estimate. With it they also get PDFs and exact page counts.
6. **Optional: git.** Ask whether they want this folder in git for history. If yes, `git init` and make one commit. Remind them never to push it to a public repo: it will hold personal data.
7. **Finish.** Show the folder tree and tell them the next step: `/job-search-kit:intake`. Mention that an existing resume or LinkedIn PDF dropped into the folder makes intake faster.
