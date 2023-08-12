from dotenv import load_dotenv

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from page.guest.PageGuestHome import PageGuestHome
from page.guest.PageGuestLogin import PageGuestLogin
from page.guest.PageGuestSignup import PageGuestSignup

from api.user.ApiUserLogin import ApiUserLogin
from api.user.ApiUserSignup import ApiUserSignup
from api.user.ApiUserVerfiyEmail import ApiUserVerifyEmail

from db.config import connect_db, run_migrations

load_dotenv()

db_connection, err = connect_db()
if err != None:
    raise err
run_migrations(db_connection)

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

PageGuestSignup(app, templates).mount()
PageGuestHome(app, templates).mount()
PageGuestLogin(app, templates).mount()

ApiUserSignup(app, db_connection).mount()
ApiUserLogin(app, db_connection).mount()
ApiUserVerifyEmail(app, db_connection).mount()
