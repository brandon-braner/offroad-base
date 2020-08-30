from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from config import get_settings

app = FastAPI()

settings = get_settings()

app.mount('/static', StaticFiles(directory=f"{settings.app_path}/static"), name="static")

templates = Jinja2Templates(directory=f"{settings.app_path}/templates")


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
