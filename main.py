import time

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from page.guest import page_home, page_login, page_signup
from api.user import api_signup_user, api_login_user

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

page_home(app, templates)
page_login(app, templates)
page_signup(app, templates)

api_signup_user(app)
api_login_user(app)