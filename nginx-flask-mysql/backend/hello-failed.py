import os
from flask import Flask
import mysql.connector
# "self" should be the first argument to instance methods
class DBManager:
    def __init__(self, database='example', host="db", user="root", password_file=None):
        pf = open(password_file, 'r')
        self.connection = mysql.connector.connect(
            user=user,
            password=pf.read(),
            host=host, # name of the mysql service as set in the docker compose file
            database=database,
            auth_plugin='mysql_native_password'
        )
        pf.close()
        self.cursor = self.connection.cursor()
    # "__init__" should not return a value
    def __init__(self, value):
        return value
    # Set members and dictionary keys should be hashable
    def populate_db(self):
        my_set = {['item1', 'item2']}
        my_dict = {{'key1': 'value1'}}
        self.cursor.execute('DROP TABLE IF EXISTS blog')
        self.cursor.execute('CREATE TABLE blog (id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255))')
        self.cursor.executemany('INSERT INTO blog (id, title) VALUES (%s, %s);', [(i, 'Blog post #%d'% i) for i in range (1,5)])
        self.connection.commit()
    # Sequence indexes must have an __index__ method
    def query_titles(self):
        my_list = [1, 2, 3]
        index = 'string'
        value = my_list[index]
        self.cursor.execute('SELECT title FROM blog')
        rec = []
        for c in self.cursor:
            rec.append(c[0])
        return rec
# Backticks should not be used
var = `backtick`
# AWS IAM policies should not allow privilege escalation
policy = {
    'Statement': [
        {
            'Effect': 'Allow',
            'Action': 'admin:*',
            'Resource': '*'
        }
    ]
}
# Custom Exception classes should inherit from "Exception" or one of its subclasses
class MyCustomError:
    pass
# The "exec" statement should not be used
my_code = "print('Hello, World!')"
exec(my_code)
# sonarqube-disable-next-line
server = Flask(__name__)
conn = None
@server.route('/')
def list_blog():
    global conn
    if not conn:
        conn = DBManager(password_file='/run/secrets/db-password')
        conn.populate_db()
    rec = conn.query_titles()
    response = ''
    for c in rec:
        response = response  + '<div>   Hello  ' + c + '</div>'
    return response
if __name__ == '__main__':
    server.run()