import os

import psycopg2
from psycopg2.extensions import connection



def connect_db():
    try:
        connection_string = os.getenv("POSTGRES_CONNECTION_STRING")
        connection = psycopg2.connect(connection_string)
        return (connection, None)
    except Exception as e:
        return (None, e)


def run_migrations(db_connection: connection):
    create_user_table(db_connection)


def create_user_table(db_connection: connection):
    cursor = db_connection.cursor()
    query = f"""
		CREATE TABLE IF NOT EXISTS "user" (
			id SERIAL PRIMARY KEY,
			email VARCHAR(255) NOT NULL,
			password VARCHAR(255) NOT NULL,
			email_key VARCHAR(255) NOT NULL
		)
	"""
    cursor.execute(query)
    db_connection.commit()
    cursor.close()
