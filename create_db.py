from psycopg2 import connect
from psycopg2 import OperationalError


def create_db():
    try:
        cnx = connect(user='postgres', password='postgres', host='localhost', database='chatroom_db')
        print("Connected")
        cnx.close()
    except OperationalError:
        cnx = connect(user='postgres', password='postgres', host='localhost')
        cnx.autocommit = True
        cursor = cnx.cursor()
        cursor.execute("CREATE DATABASE chatroom_db;")
        print("Database: chatroom_db has been successfully created!")
        cnx.close()


create_db()
