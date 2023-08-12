import time
import os

from fastapi import FastAPI, Form
from fastapi.responses import RedirectResponse

from psycopg2.extensions import connection

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from util.validate import is_email
from util.security import hash_value, get_random_characters
from const.path import (
    PATH_API_USER_SIGNUP,
    PATH_PAGE_GUEST_LOGIN,
    PATH_API_USER_VERIFY_EMAIL,
)


class ApiUserSignup:
    def __init__(self, app: FastAPI, db: connection):
        self.app = app
        self.db = db
        self.path = PATH_API_USER_SIGNUP
        self.email = ""
        self.password = ""
        self.hashed_password = ""
        self.email_key = ""

    def mount(self):
        @self.app.post(self.path)
        async def endpoint(email=Form(""), password=Form("")):
            self.consume_form_data(email, password)
            redirect = self.validate_form_values()
            if redirect != None:
                return redirect
            self.hash_password()
            self.generate_email_key()
            self.insert_user()
            err = self.send_account_verification_email()
            if err != None:
                print(err)
                # return self.server_error_redirect()
            return self.success_redirect()

    def form_err_redirect(self, form_err: str):
        return RedirectResponse(
            f"{self.path}?form_err={form_err}&email={self.email}&password={self.password}",
            302,
        )

    def success_redirect(self):
        return RedirectResponse(
            f"{PATH_PAGE_GUEST_LOGIN}?email={self.email}&password={self.password}", 302
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
            return self.form_err_redirect("email is required")
        if is_email(self.email) == False:
            return self.form_err_redirect("email must be valid")
        if len(self.email) > 64:
            return self.form_err_redirect("email too long")
        if len(self.email) < 5:
            return self.form_err_redirect("email too short")
        return None

    def validate_password(self):
        if self.password == "":
            return self.form_err_redirect("password is required")
        if len(self.password) > 64:
            return self.form_err_redirect("password too long")
        if len(self.password) < 8:
            return self.form_err_redirect("password too short")
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

    def send_account_verification_email(self):
        try:
            verification_link = ""
            if os.getenv("PYTHON_ENV") == "dev":
                verification_link = (
                    f'{os.getenv("DEV_URL")}{PATH_API_USER_VERIFY_EMAIL}'
                )
            else:
                verification_link = (
                    f'{os.getenv("PROD_URL")}{PATH_API_USER_VERIFY_EMAIL}'
                )
            message = Mail(
                from_email=os.environ.get("APP_EMAIL"),
                to_emails=self.email,
                subject="CFA Suite | Account Verification",
                html_content=f"""
                    <p>Click this link to verify your account</p>
                    <p>{verification_link}</p>
                """,
            )
            sg = SendGridAPIClient(os.environ.get("SENDGRID_API_KEY"))
            sg.send(message)
            return None
        except Exception as e:
            return e
