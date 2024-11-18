import sqlite3


def get_connection_products():
    connection = sqlite3.connect('initiate.db')
    cursor = connection.cursor()
    cursor.execute('DELETE FROM Products')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products(
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        description TEXT,
        price INTEGER NOT NULL
        )
        ''')

    for i in range(1, 5):
        cursor.execute(
            "INSERT INTO Products (title, description, price) VALUES (?, ?, ?)",
                   (f"Product{i}", f"Описание{i}", f"{i * 100}")
        )

    connection.commit()
    connection.close()
    return sqlite3.connect('initiate.db')

def get_connection_users():
    connection = sqlite3.connect('initiate.db')
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL, 
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL
    )
    ''')

    connection.commit()
    connection.close()
    return sqlite3.connect('initiate.db')


def add_user(username:str, email:str, age:int, balance = 1000):
    connection = get_connection_users()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
                   (f'{username}', f'{email}', f'{age}', f'{balance}')

    )
    connection.commit()

def is_included(username: str):
    connection = get_connection_users()
    cursor = connection.cursor()
    check_users = cursor.execute("SELECT * FROM Users WHERE username=?", (username,))
    if check_users.fetchone() is None:
        return True
    else:
        return False



def get_all_products():
    connection = get_connection_products()
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT title, description, price FROM Products")
        all_products = cursor.fetchall()
        return all_products
    finally:
        connection.close()

