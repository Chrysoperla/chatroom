from psycopg2 import connect
from psycopg2 import OperationalError

try:
    cnx = connect(user='postgres', password='postgres', host='localhost', database='chatroom_db')
    cnx.autocommit = True
    cursor = cnx.cursor()
except OperationalError:
    pass


def create_db():
    try:
        cnx = connect(user='postgres', password='postgres', host='localhost', database='chatroom_db')
        print("Connected")
    except OperationalError:
        cnx = connect(user='postgres', password='postgres', host='localhost')
        cnx.autocommit = True
        cursor = cnx.cursor()
        cursor.execute("CREATE DATABASE chatroom_db;")
        print("Database chatroom_db has been successfully created!")


def create_user_table():
    try:
        cursor.execute("""CREATE TABLE Users(
        id serial,
        username varchar(255),
        hashed_password varchar(80),
        PRIMARY KEY(id)
        );""")
        print("Table Users has been successfully created")
    except OperationalError:
        print("Encountered error while creating table Users.")


def create_message_table():
    try:
        cursor.execute("""CREATE TABLE Messages(
        id serial,
        creation_date timestamp,
        from_id int unique,
        to_id int unique,
        text varchar(255),
        PRIMARY KEY(id),
        FOREIGN KEY(from_id) REFERENCES Users(id),
        FOREIGN KEY(to_id) REFERENCES Users(id)
        );""")
        print("Table Users has been successfully created")
    except OperationalError:
        print("Encountered error while creating table Users.")



