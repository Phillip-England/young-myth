from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from cmp.banner import guest_banner
from cmp.overlay import guest_nav_overlay

from cmp.form import login_form, signup_form
from cmp.meta import metadata
from cmp.nav import guest_nav_menu
from cmp.loader import big_loader


def page_home(app: FastAPI, templates: Jinja2Templates):
	@app.get("/", response_class=HTMLResponse)
	async def read_page_home(request: Request):
		return templates.TemplateResponse("index.html", {"request": request, "components": {
			"guest_banner": guest_banner(),
			"guest_nav_overlay": guest_nav_overlay(),
			"metadata": metadata(),
			"guest_nav_menu": guest_nav_menu(path="/"),
			"big_loader": big_loader(),
		}})

def page_login(app: FastAPI, templates: Jinja2Templates):
	@app.get("/login", response_class=HTMLResponse)
	async def read_page_login(request: Request):
		return templates.TemplateResponse("login.html", {"request": request, "components": {
			"login_form": login_form(),
			"guest_banner": guest_banner(),
			"guest_nav_overlay": guest_nav_overlay(),
			"metadata": metadata(),
			"guest_nav_menu": guest_nav_menu(path="/login"),
			"big_loader": big_loader(),
		}})


def page_signup(app: FastAPI, templates: Jinja2Templates):
	@app.get("/signup", response_class=HTMLResponse)
	async def read_page_signup(request: Request):
		return templates.TemplateResponse("signup.html", {"request": request, "components": {
			"signup_form": signup_form(),
			"guest_banner": guest_banner(),
			"guest_nav_overlay": guest_nav_overlay(),
			"metadata": metadata(),
			"guest_nav_menu": guest_nav_menu(path="/signup"),
			"big_loader": big_loader(),
		}})
