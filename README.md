# GLS/NXT QA Assessment

Small QA assessment repo with Selenium smoke checks for GLS parcel configuration.
Target URL: https://www.gls-pakete.de/en/private-customers/parcel-shipping/parcel-configuration

Install dependencies:
```
pip install -r requirements.txt
```
Run smoke:
```
pytest -m smoke
```

Docs: [docs/assessment.md](docs/assessment.md), [docs/risks.md](docs/risks.md), [docs/test-strategy.md](docs/test-strategy.md)
Public production site uses Cloudflare/Turnstile; headless automation may be blocked. Smoke tests are intended for local headed demonstration.
