from fastapi import FastAPI, Query, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from const.path import PATH_PAGE_GUEST_SIGNUP
from cmp.banner import guest_banner
from cmp.overlay import guest_nav_overlay
from cmp.form import signup_form
from cmp.meta import metadata
from cmp.nav import guest_nav_menu
from cmp.loader import big_loader
from cmp.footer import guest_footer


class PageGuestSignup:
    def __init__(self, app: FastAPI, templates: Jinja2Templates):
        self.app = app
        self.templates = templates
        self.path = PATH_PAGE_GUEST_SIGNUP
        self.components = {}
        self.doc = 'signup.html'

    def mount(self):
        @self.app.get(self.path, response_class=HTMLResponse)
        async def controller(request: Request, form_err = Query(''), email = Query(''), password = Query('')):
            self.register_components(form_err, email, password)
            return self.templates.TemplateResponse(
                self.doc,
                {
                    "request": request,
                    "components": self.components,
                },
            )
        
    def register_components(self, form_err, email, password):
        self.components = {
            "signup_form": signup_form(form_err, email, password),
            "guest_banner": guest_banner(),
            "guest_nav_overlay": guest_nav_overlay(),
            "metadata": metadata(),
            "guest_nav_menu": guest_nav_menu(path=self.path),
            "big_loader": big_loader(),
            "guest_footer": guest_footer(),
        }

