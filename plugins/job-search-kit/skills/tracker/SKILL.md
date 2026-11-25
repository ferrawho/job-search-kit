---
name: tracker
description: Use when the user wants to see their job search pipeline, update an application's status, or know what needs follow-up.
---

# Tracker

Statuses: Scored, Skipped, Tailored, Applied, Screen, Interviewing, Take-home, Offer, Accepted, Rejected, Withdrawn.

Status only moves forward: Scored < Tailored < Applied < Screen < Interviewing or Take-home (same rank) < Offer. Change `Status:` only to a later one; otherwise keep it and just add the log line. Set Accepted, Rejected, Withdrawn or Skipped only when the user says so.

## Show the pipeline
1. Read the header lines (`Status:`, `Updated:`, `Score:`, `Next:`) of every `applications/*/notes.md`. A folder with no notes.md shows as "Unknown".
2. Write `tracker.md` in the workspace root and show it in chat:
   - Table: Company / role (folder), score, status, last updated, next step.
   - Sorted: active stages first (Offer, Interviewing, Take-home, Screen, Applied, Tailored), then Scored, then closed.
   - **Needs attention:** Applied more than 7 days ago with no update, a `Next:` date in the past, interviews in the next 3 days.
   - Totals: applied, active, offers, response rate.

## Update a status
When the user says something like "I applied to Acme" or "got rejected by Beta", find the folder (if none matches, list the folders and ask; for a new application, ask for the JD and create `applications/<company>-<role>/` with `jd.md` and `notes.md` the way score-jd does), update `Status:` and `Updated:`, follow the order above (a user statement like "got rejected" is what sets a closed status), set a sensible `Next:` (e.g. follow up in 7 days after applying), and add a log line. Confirm the change in one line.
