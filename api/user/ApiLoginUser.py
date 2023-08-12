from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse

from psycopg2.extensions import connection

class ApiLoginUser:
    def __init__(self, app: FastAPI, db: connection):
        self.app = app
        self.db = db

    def mount(self):
        @self.app.post("/login")
        async def controller(
            request: Request, email=Form(None), password=Form(None)
        ):
            print(email, password)
            return RedirectResponse("/login", 302)
        
        
        
