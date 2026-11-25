---
name: tracker
description: Use when the user wants to see their job search pipeline, update an application's status, or know what needs follow-up.
---

# Tracker

Statuses: Scored, Skipped, Tailored, Applied, Screen, Interviewing, Take-home, Offer, Accepted, Rejected, Withdrawn.

## Show the pipeline
1. Read the header lines (`Status:`, `Updated:`, `Score:`, `Next:`) of every `applications/*/notes.md`. A folder with no notes.md shows as "Unknown".
2. Write `tracker.md` in the workspace root and show it in chat:
   - Table: Company / role (folder), score, status, last updated, next step.
   - Sorted: active stages first (Offer, Interviewing, Take-home, Screen, Applied, Tailored), then Scored, then closed.
   - **Needs attention:** Applied more than 7 days ago with no update, a `Next:` date in the past, interviews in the next 3 days.
   - Totals: applied, active, offers, response rate.

## Update a status
When the user says something like "I applied to Acme" or "got rejected by Beta", find the folder, update `Status:` and `Updated:`, set a sensible `Next:` (e.g. follow up in 7 days after applying), and add a log line. Confirm the change in one line.
