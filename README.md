# GLS/NXT QA Assessment

Quality Engineering exercise: risk-based test strategy + a small, stable UI automation POC (pytest + Selenium) for GLS parcel configuration flow.

## Scope
- Target page: https://www.gls-pakete.de/en/private-customers/parcel-shipping/parcel-configuration
- Focus: critical user journey to add a parcel configuration to shopping cart (no payment).

## What's inside
- `docs/test-strategy.md` — testing approach, quality standards, CI/CD, metrics, monitoring ideas
- `docs/risks.md` — top product risks + mitigation ideas
- `tests/ui` — Selenium smoke tests (minimal and stable)

## How to run locally
1. Create venv
2. Install deps: `pip install -r requirements.txt`
3. Run smoke: `pytest -m smoke`

## Notes
- Selenium chosen for speed-to-delivery and reliability.
- If this were a long-term project: consider migrating to Playwright for better auto-waits and debugging.
