# new database in sql_server

new_database = "CREATE DATABASE workshop;"

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