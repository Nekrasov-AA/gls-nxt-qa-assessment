# Test Strategy (Minimal, Risk-Based)

## Goal
Build confidence in a production parcel-shipping flow under limited time and incomplete system knowledge.

## Approach
### 1) Exploratory testing (highest ROI first)
- Critical path: configure parcel -> recipient -> delivery option -> add to cart -> verify cart summary
- Charters:
  - validation: required fields, invalid postcode/city formats, special characters
  - pricing: option toggles, destination changes, size changes
  - usability: error messages, field hints, recovery from mistakes

### 2) Automation (small and stable)
- UI smoke (pytest + Selenium) focused on “page renders” and “CTA available”.
- Keep the automated set minimal to reduce flakiness on production UI and to fit the timebox.

### 3) CI/CD integration
- CI runs:
  - stable baseline checks (sanity / non-UI)
  - UI smoke headless as best-effort (public production may block headless)
- On UI failures, store artifacts (screenshot + HTML) for debugging.

## Quality signals / metrics (what I would track)
- Smoke pass rate (headed on controlled env / staging)
- Flake rate (re-runs required / intermittent failures)
- Defect leakage (issues found in prod vs pre-prod)
- Time to detect (MTTD) and time to recover (MTTR) for checkout incidents
- Conversion funnel drop-offs around config -> cart

## Observability / monitoring
- Synthetic monitoring for critical path endpoints/pages (if allowed)
- Dashboards:
  - errors on config/cart endpoints
  - latency for config page
  - add-to-cart failures / cart error rates
- Alerts:
  - spikes in 4xx/5xx
  - significant conversion drop around add-to-cart

## Notes about production constraints
- Public production is protected by Cloudflare/Turnstile which may block headless automation. The reliable long-term solution is to run E2E against staging/internal environments or allowlisted CI runners.
