# Carrier Scorecard

- Company and dates: Northwind Freight, 2023 to 2024

## Problem
Carrier relations judged the 40 partner carriers on anecdotes. There was no shared measure of on-time pickup, damage claims, or tender acceptance.

## Why it mattered
Late pickups at origin pushed freight past cross-dock cutoffs and caused missed deliveries. Without data, carrier relations could not hold carriers to their commitments.

## What I did
- Defined the scorecard metrics with carrier relations: on-time pickup, tender acceptance, and damage claims per 1,000 shipments.
- Built the scorecard in SQL and Tableau, refreshed weekly.
- Set up a weekly review where carrier relations walks through the bottom five carriers.
- Handled pushback from one carrier that disputed its on-time numbers by walking their account manager through the raw timestamps.

## Who else was involved
The carrier relations team (3 people) ran the carrier conversations. Sam built the scorecard and joined the weekly reviews.

## Tools
SQL (SQL Server), Tableau, Excel.

## Result
- On-time pickup rate across the 40 carriers rose from 84% to 93% over 12 months.
- Damage claims: no metric yet (data too sparse).

## What I'd do differently
Share each carrier's own scorecard with them directly from the start instead of only in reviews.
