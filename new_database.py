import psycopg2
from psycopg2 import connect, OperationalError
from psycopg2.errors import DuplicateDatabase, DuplicateTable
# new database in sql_server

new_database = "CREATE DATABASE workshop;"

DB_USER = "workshop"
DB_PASSWORD = "coderslab"
DB_HOST = "127.0.0.1"

try:
    cnx = connect(user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
    cnx.autocommit = True
    cursor = cnx.cursor()
    try:
        cursor.execute(CREATE_DB)
        print("Database created")
    except DuplicateDatabase as e:
        print("Database exists ", e)
    cnx.close()
except OperationalError as e:
    print("Connection Error: ", e)

# make table of user and table witch be used to messages

new_users_table = """CREATE TABLE users(
                        id serial PRIMARY KEY,
                        usename VARCHAR(300) UNIQUE,
                        hashed_password VARCHAR(40))"""

messages_table = """CREATE TABLE messages(
                        id SERIAL,
                        from_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
                        to_id INTEGER REFERENCES users(id) ON DELETE CASCADE, 
                        text varchar(255),
                        creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP)"""

# connection data with the postgres server

DB_PASSWORD = "coderslab"
HOST = "127.0.0.1"

try:
    _connect = psycopg2.connect(dbname="workshop", user="postgres", password=DB_PASSWORD)
    _connect.autocommit = True
    cursor = _connect.cursor()
# _connect.close()

    try:
     cursor.execute(new_users_table)
     print("Database created")
    except DuplicateDatabase as e:
     print("Database exists ", e)
    _connect.close()
except OperationalError as e:
    print("Connection Error: ", e)


try:
    _connect = connect(dbname="workshop", user="postgres", password=DB_PASSWORD, host=HOST)
    _connect.autocommit = True
    cursor = _connect.cursor()

    try:
        cursor.execute(messages_table)
        print("Messages table created")
    except DuplicateTable as e:
        print("Table exists ", e)

except OperationalError as e:
        print("Connection Error", e)
_connect.close()
# cursor.execute(messages_table)
