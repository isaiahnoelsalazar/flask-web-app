from flask import Flask
import pymssql
import traceback
import sys

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello'

@app.route('/about')
def about():
    return sys.version

@app.route("/mssql")
def python_mssql():
    try:
        server = 'sql.bsite.net\\MSSQL2016'
        database = 'saiasamazingaspsite_SampleDB'
        username = 'saiasamazingaspsite_SampleDB'
        password = 'DBSamplePW'

        connection = pymssql.connect(server, username, password, database)

        cursor = connection.cursor()
        cursor.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE'")
        rows = cursor.fetchall()

        allstr = ""

        for row in rows:
            allstr += str(row)[2:-3] + "\n"

        connection.close()

        return allstr
    except:
        return traceback.format_exc()