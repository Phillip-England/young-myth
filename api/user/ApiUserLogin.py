from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse
from psycopg2.extensions import connection

from const.path import PATH_API_USER_LOGIN


class ApiUserLogin:
    def __init__(self, app: FastAPI, db: connection):
        self.app = app
        self.db = db
        self.path = PATH_API_USER_LOGIN

    def mount(self):
        @self.app.post("/login")
        async def controller(request: Request, email=Form(None), password=Form(None)):
            print(email, password)
            return RedirectResponse(PATH_API_USER_LOGIN, 302)
