
from fastapi import FastAPI, Form
from fastapi.responses import RedirectResponse
from psycopg2.extensions import connection

from const.path import PATH_API_USER_VERIFY_EMAIL, PATH_PAGE_GUEST_LOGIN

class ApiUserVerifyEmail:
    def __init__(self, app: FastAPI, db: connection):
        self.app = app
        self.db = db
        self.path = PATH_API_USER_VERIFY_EMAIL
        self.user_id = int
        self.email_key = str
        
    def mount(self):
        @self.app.get(self.path + '/{email_key}')
        async def controller(email_key: str):
            self.email_key = email_key
            err = self.find_user_by_email_key()
            if err != None:
                print('couldnt find user by email key')
            self.activate_user_by_id()
            return RedirectResponse(
            	f"{PATH_PAGE_GUEST_LOGIN}",
            	302,
        	)
            
    def find_user_by_email_key(self):
        cursor = self.db.cursor()
        query = """
            SELECT id FROM "user" WHERE email_key = %s
        """
        cursor.execute(query, (self.email_key,))
        user_id = cursor.fetchone()[0]
        cursor.close()
        self.user_id = user_id
        if self.user_id == None:
            return 'no user associated with email key'
        return None
    
    def activate_user_by_id(self):
        if self.user_id is not None:
            cursor = self.db.cursor()
            query = """
                UPDATE "user" SET active = true WHERE id = %s
            """
            cursor.execute(query, (self.user_id,))
            self.db.commit()
            cursor.close()
            print(f"User with ID {self.user_id} has been activated.")
        else:
            print("No user ID provided to activate_user_by_id.")