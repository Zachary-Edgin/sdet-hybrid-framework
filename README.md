![tests](https://github.com/Zachary-Edgin/sdet-hybrid-framework/actions/workflows/tests.yml/badge.svg)

# sdet-hybrid-framework

A small, portfolio-grade SDET project demonstrating a maintainable test automation framework in Python.

## CI Proof

- ✅ **Latest passing CI run (Actions):**  
  <PASTE_ACTIONS_RUN_URL_HERE>

- 📦 **Downloadable test artifacts (HTML report + JUnit XML):**  
  Open the run → **Artifacts** → `test-artifacts`

- 🧪 **Intentional failure demo branch (shows screenshot evidence on UI failure):**  
  Branch: `demo-failure-artifacts`  
  PR: <PASTE_PR_URL_HERE>  
  (This branch is intentionally failing — do not merge.)

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
- **Docker Compose for stability:** app + test runner execute identically locally and in CI.
- **API + UI coverage:** API tests validate behavior quickly; UI tests validate critical user flows.
- **pytest fixtures for reuse:** shared setup/teardown keeps tests maintainable and consistent.
- **CI artifacts:** GitHub Actions uploads JUnit + HTML reports; UI failures capture screenshots for debugging.