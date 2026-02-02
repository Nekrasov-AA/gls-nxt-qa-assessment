# GLS/NXT QA Assessment

Minimal smoke checks for GLS parcel configuration.
Install dependencies:

pip install -r requirements.txt

Run smoke:

pytest -m smoke

Public production site uses Cloudflare/Turnstile; headless automation may be blocked. Smoke tests are intended for local headed demonstration.
