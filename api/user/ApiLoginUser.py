from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse

from psycopg2.extensions import connection

class ApiLoginUser:
    def __init__(self, app: FastAPI, db_conection: connection):
        self.app = app
        self.db
        

def api_login_user(app: FastAPI, db_connection: connection):
    @app.post("/login")
    async def controller(
        request: Request, email=Form(None), password=Form(None)
    ):
        return RedirectResponse("/login", 302)
    