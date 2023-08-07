

from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse

from util.validate import is_email

def api_login_user(app: FastAPI, db_connection):
	@app.post("/login")
	async def api_login_user_controller(request: Request, email=Form(None), password=Form(None)):
		print(email, password)
		return RedirectResponse("/login", 302)

def api_signup_user(app: FastAPI, db_connection):
	@app.post("/signup")
	async def api_login_user_controller(request: Request, email=Form(''), password=Form('')):
		if email == '':
			return RedirectResponse(f"/signup?form_err=email is required&email={email}&password={password}", 302)
		if password == '':
			return RedirectResponse(f"/signup?form_err=password is required&email={email}&password={password}", 302)
		return RedirectResponse("/login", 302)