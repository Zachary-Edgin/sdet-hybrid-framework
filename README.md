# sdet-hybrid-framework

A small, portfolio-grade SDET project demonstrating a maintainable automation framework in Python:
- FastAPI app (UI + JSON API)
- API tests (pytest + requests)
- UI tests (pytest + Playwright)
- Docker Compose for consistent local + CI execution
- CI evidence: HTML report + JUnit XML + screenshots on UI failures

## CI Proof
- ✅ Latest report (GitHub Pages):  
  (add your Pages URL here)

- ✅ CI workflow runs + downloadable artifacts:  
  (add your Actions workflow URL here)

## What it includes
- Local FastAPI app with a real login UI + JSON API
- API tests (pytest + requests)
- UI tests (pytest + Playwright)
- Docker Compose for consistent local + CI runs
- CI artifacts (HTML report + JUnit XML)
- UI failure evidence (auto-screenshots saved on failure)
## Run locally

Start the app:
```bash
docker compose up -d --build app

## Design Decisions
- **Docker Compose parity:** app + tests run the same locally and in CI to reduce “works on my machine” drift.
- **API + UI coverage:** API tests validate behavior quickly; UI tests validate critical user flows end-to-end.
- **pytest fixtures for reuse:** shared setup/teardown keeps tests maintainable and consistent.
- **Actionable failure evidence:** HTML report + JUnit XML + screenshot on UI failures makes debugging fast.
- **Artifacts are generated, not committed:** reports/screenshots live in CI artifacts (and optionally Pages), keeping the repo clean.
