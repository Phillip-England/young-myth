import time

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from page.guest import PageLogin, PageSignup, PageHome

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

PageHome(app, templates).mount()
PageLogin(app, templates).mount()
PageSignup(app, templates).mount()