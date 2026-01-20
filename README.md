![tests](https://github.com/Zachary-Edgin/sdet-hybrid-framework/actions/workflows/tests.yml/badge.svg)

# sdet-hybrid-framework

A small, portfolio-grade SDET project demonstrating a maintainable test automation framework in Python.

## CI Proof

- ✅ **Latest HTML test report (GitHub Pages):**  
  https://zachary-edgin.github.io/sdet-hybrid-framework/?sort=result
  
- ✅ **Latest passing CI run (Actions):**  
  [Open the latest passing run](https://github.com/Zachary-Edgin/sdet-hybrid-framework/actions/runs/21176303167)

- 📦 **Downloadable test artifacts (HTML report + JUnit XML):**  
  Open the run → **Artifacts** → `test-artifacts`
  Download `test-artifacts` → open `report.html` (human-friendly) or `junit.xml` (machine-readable).

- 🧪 **Intentional failure demo branch (shows screenshot evidence on UI failure):**  
  Branch: `demo-failure-artifacts`  
  PR: [Intentional failure demo](https://github.com/Zachary-Edgin/sdet-hybrid-framework/pull/1) 
  (This branch is intentionally failing — do not merge.)
  Run: https://github.com/Zachary-Edgin/sdet-hybrid-framework/actions/runs/21150925399

## What it includes
- Local FastAPI app with a real login UI + JSON API
- API tests (pytest + requests)
- UI tests (pytest + Playwright)
- Docker Compose for consistent local + CI runs
- Test artifacts (HTML report + JUnit XML)

## Run locally

1. Start the app:
```bash
docker compose up -d --build app
```

2. Run tests:
```bash
docker compose run --rm tests pytest -q
```

## Design Decisions
- **Docker Compose parity:** app + test runner execute identically locally and in CI to reduce “works on my machine” drift.
- **API + UI coverage:** API tests validate behavior quickly; UI tests validate critical user flows end-to-end.
- **pytest fixtures for reuse:** shared setup/teardown keeps tests maintainable and consistent.
- **Actionable failure evidence:** HTML report + JUnit XML + screenshots on UI failures makes debugging fast.
- **Artifacts are generated, not committed:** reports/screenshots are produced in CI and published via artifacts + Pages, keeping the repo clean.