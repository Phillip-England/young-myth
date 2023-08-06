from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse

def api_login_user(app: FastAPI):
	@app.post("/login")
	async def api_login_user_controller(request: Request, email=Form(...), password=Form(...)):
		print(email, password)
		return RedirectResponse("/login", 302)
	
def api_signup_user(app: FastAPI):
	@app.post("/signup")
	async def api_login_user_controller(request: Request, email=Form(...), password=Form(...)):
		print(email, password)
		return RedirectResponse("/login", 302)