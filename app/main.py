import os
from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

APP_USERNAME = os.getenv("APP_USERNAME", "demo")
APP_PASSWORD = os.getenv("APP_PASSWORD", "secret")

AUTH_COOKIE = "auth_token"
DEMO_TOKEN = "demo-token"


@app.get("/api/health")
def health():
    return {"status": "ok"}


@app.post("/api/login")
def login_api(payload: dict):
    username = payload.get("username")
    password = payload.get("password")
    if username == APP_USERNAME and password == APP_PASSWORD:
        return {"token": DEMO_TOKEN}
    raise HTTPException(status_code=401, detail="Invalid credentials")


@app.get("/", response_class=HTMLResponse)
def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request, "error": None})


@app.post("/ui/login")
def login_ui(
    request: Request,
    username: str = Form(...),
    password: str = Form(...)
):
    if username == APP_USERNAME and password == APP_PASSWORD:
        resp = RedirectResponse(url="/dashboard", status_code=303)
        resp.set_cookie(key=AUTH_COOKIE, value=DEMO_TOKEN, httponly=True)
        return resp

    return templates.TemplateResponse(
        "login.html",
        {"request": request, "error": "Invalid credentials", "username": username},
    )


@app.get("/dashboard", response_class=HTMLResponse)
def dashboard(request: Request):
    token = request.cookies.get(AUTH_COOKIE)
    if token != DEMO_TOKEN:
        return RedirectResponse(url="/", status_code=303)

    return templates.TemplateResponse("dashboard.html", {"request": request, "username": APP_USERNAME})