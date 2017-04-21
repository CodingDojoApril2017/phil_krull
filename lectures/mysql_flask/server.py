from flask import Flask, render_template
from mysqlconnection import MySQLConnector

app = Flask(__name__)
mysql = MySQLConnector(app, 'april_demo')
query = 'SELECT * FROM states'

result = mysql.query_db(query)
for x in result:
    print x['name']

app.run(debug = True)
