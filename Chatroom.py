import create_db
from psycopg2 import connect, OperationalError
from psycopg2.errors import UndefinedColumnError
import argparse


# create_db()
cnx = connect(user='postgres', password='postgres', host='localhost', database='chatroom_db')
cnx.autocommit = True
cursor = cnx.cursor()

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--username", help="username")
parser.add_argument("-p", "--password", help="password (min 8 characters)")
parser.add_argument("-n", "--new_pass", help="new password (min 8 characters)", action="store_true")
parser.add_argument("-l", "--list", help="user list", action="store_true")
parser.add_argument("-d", "--delete", help="delete your username from the database", action="store_true")
parser.add_argument("-e", "--edit", help="edit", action="store_true")

args = parser.parse_args()

if args.username == None:
    print("""Access denied. Log in using the following command:
python3 Chatroom.py -u <username> -p <password>""")
else:
    try:
        cursor.execute(f"SELECT username FROM Users WHERE username = {args.username}")
    except UndefinedColumn:






