from typing import Union

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from random import randrange

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")


@app.get("/")
def read_root():
    return {"I serve gremlins"}


@app.get("/gremlins", response_class=HTMLResponse)
async def read_item(request: Request):
    gremlin_image = f"gremlin{randrange(1,5)}.jpg"
    return templates.TemplateResponse("gremlin.html",{"request": request, "gremlin_image": gremlin_image})