from psycopg2 import connect

cnx = connect(user='postgres', password='postgres', host='localhost', database='chatroom_db')
cnx.autocommit = True
cursor = cnx.cursor()

class User:

    def __init__(self, username, hashed_password):
        self._id = -1
        self.username = username
        self._hashed_password = hashed_password

    def change_password(self, hashed_old_password, hashed_new_password):
        if hashed_old_password == self._hashed_password:
            self._hashed_password = hashed_new_password
            return self._hashed_password
        elif hashed_old_password != self._hashed_password:
            print("Wrong password")

    # def save_to_db(self, func):
    #     cnx = connect(user='postgres', password='postgres', host='localhost', database='chatroom_db')
    #     cnx.autocommit = True
    #     cursor = cnx.cursor()
    #     cursor.execute(func)

    def load_all_users(self):
        user_data = cursor.execute("SELECT id, username FROM Users")
        print(user_data)

    def load_user_by_id(self, id_):
        user_data = cursor.execute(f"SELECT username FROM Users WHERE id = {id_}")
        print(user_data)

    def load_user_by_username(self, name):
        user_data = cursor.execute(f"SELECT username FROM Users WHERE username = {name}")
        print(user_data)


class Messages:

    def __init__(self, from_id, to_id, text):
        self._id = -1
        self.from_id = from_id
        self.to_id = to_id
        self.text = text
        self.creation_date = None

    def save_to_db(self):
        cursor.execute(f"""INSERT INTO Messages (from_id, to_id, text)
        VALUES ({self.from_id}, {self.to_id}, {self.text});""")

    def load_all_messages(self):
        message_history = cursor.execute("SELECT text FROM Messages")
        print(message_history)


# Udostępnij _id i _hashed_password do odczytu na zewnątrz.

