# Weekly Ops Reporting Automation

- Company and dates: Northwind Freight, 2021 to 2022

## Problem
The weekly operations report was built by hand every Monday from four spreadsheet exports. It took 6 hours and often went out late or with copy-paste errors.

## Why it mattered
Terminal managers made staffing decisions for the week from this report. Late or wrong numbers meant decisions made on guesses.

## What I did
- Wrote SQL views against the transportation and warehouse databases for volume, dock dwell time, on-time pickups, and cost per shipment.
- Rebuilt the report as a Tableau dashboard that refreshes overnight, with an Excel export for finance.
- Agreed metric definitions with the Director of Operations and the terminal managers so every terminal measured the same way.

## Who else was involved
The Director of Operations (metric definitions), the 4 terminal managers (feedback), and IT (database access). Sam built the queries and the dashboard alone.

## Tools
SQL (SQL Server), Tableau, Excel.

## Result
- Weekly preparation time fell from 6 hours to 45 minutes.
- The report now goes out every Monday morning. Error rate: no metric.

## What I'd do differently
Document the metric definitions in one shared place from day one.
