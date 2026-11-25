# Story Bank

## Cutting truck wait time with dock appointments
- Competencies: ambiguity, influence, technical depth, customer focus
- Situation: At Northwind Freight, inbound trucks at the Joliet and Gary terminals waited an average of 52 minutes to unload, and carriers billed detention for long waits.
- Task: The Director of Operations asked me to find out why and propose a fix the terminal managers would accept.
- Action: I pulled 6 months of gate and unload timestamps with SQL and found arrivals clustered between 7 and 10 a.m. I ran time studies on the dock floor to size unload times by trailer type, mapped the process with the dock supervisors, and proposed fixed appointment windows. I built the Tableau dashboard to track arrivals against appointments and led the rollout meetings at Joliet first, then Gary.
- Result (with numbers): Average truck wait fell from 52 to 19 minutes across both terminals. The project won the 2023 Operations Impact award. Lesson: two large carriers pushed back because carrier relations told them late, so next time I would bring that team in earlier.
- Source: profile/projects/dock-scheduling.md

## Automating the weekly operations report
- Competencies: technical depth, prioritization
- Situation: The weekly operations report at Northwind Freight took 6 hours to build by hand from four spreadsheet exports and often went out late or with errors.
- Task: Terminal managers needed the report on Monday morning to plan staffing. I owned the report.
- Action: I wrote SQL views for volume, dock dwell time, on-time pickups, and cost per shipment, rebuilt the report as a Tableau dashboard that refreshes overnight, and got the Director of Operations and the 4 terminal managers to agree on one set of metric definitions.
- Result (with numbers): Preparation time fell from 6 hours to 45 minutes a week, and the report now goes out every Monday morning.
- Source: profile/projects/ops-reporting-automation.md

## Getting a disputing carrier to accept the scorecard
- Competencies: conflict, influence, customer focus
- Situation: After I built the carrier scorecard for 40 partner carriers, one carrier disputed its on-time pickup numbers and asked carrier relations to drop it from the weekly review.
- Task: Keep the scorecard credible without damaging the carrier relationship.
- Action: I met with the carrier's account manager and walked through the raw gate timestamps for their late pickups, shipment by shipment, and offered to fix any record they could show was wrong. None were wrong. We agreed they would get a copy of their own numbers each week.
- Result (with numbers): The carrier stayed in the review and its numbers improved. Across all 40 carriers, on-time pickup rose from 84% to 93% over 12 months.
- Source: profile/projects/carrier-scorecard.md

<!-- Competencies with no story yet: leadership (no direct reports), failure. -->
