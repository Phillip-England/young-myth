import time

from fastapi import FastAPI, Form
from fastapi.responses import RedirectResponse

from psycopg2.extensions import connection

from util.validate import is_email
from util.security import hash_value, get_random_characters

class ApiSignupUser:
    def __init__(self, app: FastAPI, db: connection):
        self.app = app
        self.db = db
        self.path = '/signup'
        self.email = ''
        self.password = ''
        self.hashed_password = ''
        self.email_key = ''

    def mount(self):
        @self.app.post(self.path)
        async def endpoint(email=Form(""), password=Form("")):
            start = time.time()
            self.consume_form_data(email, password)
            redirect = self.validate_form_values()
            if redirect != None:
                return redirect
            self.hash_password()
            self.generate_email_key()
            self.insert_user()
            return RedirectResponse("/login", 302)
    
    async def controller(self, email=Form(''), password=Form('')):
        start = time.time()
        self.consume_form_data(email, password)
        redirect = self.validate_form_values()
        if redirect != None:
            return redirect
        self.hash_password()
        self.generate_email_key()
        self.insert_user()
        return RedirectResponse("/login", 302)
        
    def form_err_redirect(self, form_err: str):
        return RedirectResponse(
            f'/signup?form_err={form_err}&email={self.email}&password={self.password}',
            302,
        )
    
    def validate_form_values(self):
        redirect = self.validate_email()
        if redirect != None:
            return redirect
        redirect = self.validate_password()
        if redirect != None:
            return redirect
        return None

    def consume_form_data(self, email: str, password: str):
        self.email = email.lower()
        self.password = password

    def validate_email(self):
        if self.email == "":
            return self.form_err_redirect('email is required')
        if is_email(self.email) == False:
            return self.form_err_redirect('email must be valid')
        if len(self.email) > 64:
            return self.form_err_redirect('email too long')
        if len(self.email) < 5:
            return self.form_err_redirect('email too short')
        return None
    
    def validate_password(self):
        if self.password == "":
            return self.form_err_redirect('password is required')
        if len(self.password) > 64:
            return self.form_err_redirect('password too long')
        if len(self.password) < 8:
            return self.form_err_redirect('password too short')
        return None
    
    def hash_password(self):
        self.hashed_password = hash_value(self.password)

    def generate_email_key(self):
        self.email_key = get_random_characters(64)

    def insert_user(self):
        cursor = self.db.cursor()
        query = """
            INSERT INTO "user" (email, password, email_key)
            VALUES (%s, %s, %s)
            RETURNING id
        """
        values = (self.email, self.hashed_password, self.email_key)
        cursor.execute(query, values)
        self.db.commit()
        cursor.close()
