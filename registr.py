import sqlite3


def initiate_db():
    connection = sqlite3.connect('users.db')
    c = connection.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS Users
                 (id INTEGER PRIMARY KEY, 
                 username TEXT NOT NULL, 
                 firstname TEXT NOT NULL, 
                 phone INTEGER NOT NULL)''')
    c.execute("CREATE INDEX IF NOT title on Users (title)")
    connection.commit()
    connection.close()
def add_user(username, firstname,phone):
    connection = sqlite3.connect('users.db')
    conn = connection.cursor()
    conn.execute("INSERT INTO Users (username, firstname, phone) VALUES (?, ?, ?)",
                    (username, firstname, phone))
    connection.commit()
    connection.close()

def is_included(username):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    check_user= c.execute("SELECT * FROM Users WHERE username=?", (username,))
    if check_user.fetchone() is None:
        c.close()
        return False
    else:
        c.close()
        return True

def initiate_db():
    connection = sqlite3.connect('products.db')
    c = connection.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS Products
                 (id INTEGER PRIMARY KEY,
                 title TEXT NOT NULL,
                 description TEXT,
                 phone INTEGER NOT NULL)''')
    c.execute("CREATE INDEX IF NOT title on Products (title)")
    connection.commit()
    connection.close()

def get_all_products():
    connection = sqlite3.connect('products.db')
    c = connection.cursor()
    c.execute("SELECT * FROM Products")
    rows = c.fetchall()
    c.close()
    return rows

def add_product(title, description,phone):
    connection = sqlite3.connect('products.db')
    conn = connection.cursor()
    conn.execute("INSERT INTO Products (title, description,phone) VALUES (?, ?,?)",
                 (title, description,phone))
    connection.commit()
    connection.close()



def get_phon_data(phone):
    connection = sqlite3.connect('products.db')
    c = connection.cursor()
    c.execute("SELECT * FROM Products WHERE phone=?", (phone,))
    user_data=c.fetchone()
    connection.commit()
    c.close()
    connection.close()
    return user_data


def get_user_data(phone):
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Users WHERE phone = ?", (phone,))
    user_data = cursor.fetchone()
    return user_data
