# sdet-hybrid-framework

A small, portfolio-grade SDET project demonstrating a maintainable test automation framework in Python.

## What it includes
- Local FastAPI app with a real login UI + JSON API
- API tests (pytest + requests)
- UI tests (pytest + Playwright)
- Docker Compose for consistent local + CI runs
- Test artifacts (HTML report + JUnit XML)

## Run locally
1) Start the app:
```bash
docker compose up -d --build app# test
