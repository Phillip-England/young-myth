import time

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from cmp.banner import GuestBanner
from cmp.overlay import GuestNavOverlay

from cmp.form import LoginForm, SignupForm
from cmp.meta import MetaData
from cmp.nav import GuestNavMenu

class PageHome:
	def __init__(self, app: FastAPI, templates: Jinja2Templates):
		self.app = app
		self.templates = templates
	def mount(self):
		@self.app.get("/", response_class=HTMLResponse)
		async def read_page_home(request: Request):
			guest_banner = GuestBanner()
			guest_nav_overlay = GuestNavOverlay()
			metadata = MetaData()
			guest_nav_menu = GuestNavMenu(path="/")
			return self.templates.TemplateResponse("index.html", {"request": request, "components": {
				"guest_banner": guest_banner.HTML(),
				"main_overlay": guest_nav_overlay.HTML(),
				"metadata": metadata.HTML(),
				"guest_nav_menu": guest_nav_menu.HTML(),
			}})

class PageLogin:
	def __init__(self, app: FastAPI, templates: Jinja2Templates):
		self.app = app
		self.templates = templates
	def mount(self):
		@self.app.get("/login", response_class=HTMLResponse)
		async def read_page_login(request: Request):
			guest_banner = GuestBanner()
			guest_nav_overlay = GuestNavOverlay()
			login_form = LoginForm()
			metadata = MetaData()
			guest_nav_menu = GuestNavMenu(path="/")
			return self.templates.TemplateResponse("login.html", {"request": request, "components": {
				"login_form": login_form.HTML(),
				"guest_banner": guest_banner.HTML(),
				"main_overlay": guest_nav_overlay.HTML(),
				"metadata": metadata.HTML(),
				"guest_nav_menu": guest_nav_menu.HTML(),
			}})

class PageSignup:
	def __init__(self, app: FastAPI, templates: Jinja2Templates):
		self.app = app
		self.templates = templates
	def mount(self):
		@self.app.get("/signup", response_class=HTMLResponse)
		async def read_page_signup(request: Request):
			guest_banner = GuestBanner()
			guest_nav_overlay = GuestNavOverlay()
			signup_form = SignupForm()
			metadata = MetaData()
			guest_nav_menu = GuestNavMenu(path="/")
			return self.templates.TemplateResponse("signup.html", {"request": request, "components": {
				"signup_form": signup_form.HTML(),
				"guest_banner": guest_banner.HTML(),
				"main_overlay": guest_nav_overlay.HTML(),
				"metadata": metadata.HTML(),
				"guest_nav_menu": guest_nav_menu.HTML(),
			}})
