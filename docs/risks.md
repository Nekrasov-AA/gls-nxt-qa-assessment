# Quality Risks (Risk-Based View)

Legend:
- P0 = high impact / high likelihood (must cover)
- P1 = high impact or medium likelihood (should cover)
- P2 = lower impact/likelihood (nice to cover)

## P0 (must)
1) Pricing calculation wrong (destination / size / option)
- Impact: revenue loss, refunds, trust damage
- Coverage: UI checks for price displayed & change when switching delivery options; monitoring of pricing anomalies

2) Delivery option selection not applied (UI shows A, backend uses B)
- Impact: wrong fulfillment, support workload, trust
- Coverage: UI regression checks, cart summary verification, server-side logs/metrics (in real setup)

3) Add-to-cart failure (button does nothing / cart not updated)
- Impact: conversion drop immediately
- Coverage: UI smoke (add-to-cart + cart contains item), synthetic monitoring

4) Recipient validation broken (missing required fields accepted / invalid data allowed)
- Impact: failed deliveries, returns, extra costs
- Coverage: UI validation tests, exploratory charters for invalid inputs (postcode, city, street)

5) Wrong destination constraints (unsupported country allowed / supported blocked)
- Impact: orders impossible to fulfill or lost orders
- Coverage: exploratory + parameterized checks for top destinations; contract with product rules

## P1 (should)
6) Localization / language inconsistencies (DE/EN copy changes break flows)
- Impact: UX issues, increased drop-off; brittle tests
- Coverage: prefer stable selectors where possible; smoke checks for key sections; translation review process

7) Performance degradation on configuration page
- Impact: drop-off, conversion loss
- Coverage: basic timing budgets, synthetic checks, monitoring

8) Accessibility regressions (labels, focus order, error messaging)
- Impact: compliance risk + usability
- Coverage: quick a11y spot-checks, keyboard-only exploration; later: automated a11y scanning

## P2 (nice)
9) Visual/layout regressions (misaligned sections, overlapping modals)
- Impact: usability
- Coverage: basic visual spot checks; later: visual regression tool on stable env

10) Analytics/telemetry missing on critical events (option change, add-to-cart)
- Impact: inability to detect issues quickly
- Coverage: event tracking review + dashboards in monitoring
