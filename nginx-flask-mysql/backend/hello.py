import os
from flask import Flask
import mysql.connector

class DBManager:
    def __init__(self, database='example', host="db-service", user="root", password_file=None):
        if password_file:
            with open(password_file, 'r') as pf:
                password = pf.read().strip()
        else:
            # Manejar el caso en el que el archivo de contraseña no se proporciona
            password = None

        self.connection = mysql.connector.connect(
            user=user,
            password=password,
            host=host,
            database=database,
            auth_plugin='mysql_native_password'
        )
        self.cursor = self.connection.cursor()

    def populate_db(self):
        self.cursor.execute('DROP TABLE IF EXISTS blog')
        self.cursor.execute('CREATE TABLE blog (id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255))')
        self.cursor.executemany('INSERT INTO blog (id, title) VALUES (%s, %s);', [(i, 'Blog post #%d' % i) for i in range(1, 5)])
        self.connection.commit()

    def query_titles(self):
        self.cursor.execute('SELECT title FROM blog')
        rec = []
        for c in self.cursor:
            rec.append(c[0])
        return rec

app = Flask(__name__)
conn = None

@app.route('/')
def listBlog():
    global conn
    if not conn:
        conn = DBManager(password_file='/mnt/secrets/db-password/password.txt')
        conn.populate_db()
    rec = conn.query_titles()

    response = ''
    for c in rec:
        response = response + '<div>Hello ' + c + '</div>'
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)