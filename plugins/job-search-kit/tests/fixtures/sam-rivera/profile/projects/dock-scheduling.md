# Dock Scheduling Redesign

- Company and dates: Northwind Freight, Joliet and Gary terminals, 2022 to 2023

## Problem
Inbound trucks arrived on a first-come, first-served basis. Average truck wait before unloading was 52 minutes, and carriers were billing detention fees for long waits.

## Why it mattered
Long waits meant detention charges, unhappy carriers, and dock crews that sat idle in the morning and were overloaded in the afternoon.

## What I did
- Pulled 6 months of gate and unload timestamps with SQL and found that most of the wait came from arrivals clustered between 7 and 10 a.m.
- Ran time studies on the dock floor to measure real unload times by trailer type.
- Mapped the inbound process with the dock supervisors and both terminal managers.
- Proposed fixed appointment windows sized by trailer type, and built the Tableau dashboard that tracks arrivals against appointments.
- Rolled out the new schedule at Joliet first, then Gary.

## Who else was involved
Two terminal managers, the dock supervisors at both terminals, and the carrier relations team, who told carriers about the appointment windows. The terminal managers approved the change; Sam did the analysis and design and led the rollout meetings.

## Tools
SQL (SQL Server), Excel, Tableau, time studies, process mapping.

## Result
- Average truck wait fell from 52 to 19 minutes across both terminals.
- Detention fees: no metric (finance did not break them out).
- Won the 2023 Northwind Freight Operations Impact award.

## What I'd do differently
Bring carrier relations in earlier. Two large carriers pushed back on the windows during the first month because they heard about them late.
