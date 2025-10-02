from flask import Flask, request
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
        # server = 'sql.bsite.net\\MSSQL2016'
        # database = 'saiasamazingaspsite_SampleDB'
        # username = 'saiasamazingaspsite_SampleDB'
        # password = 'DBSamplePW'

        server = request.args.get("server")
        database = request.args.get("database")
        username = request.args.get("username")
        password = request.args.get("password")

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
        return "Connection broken. Please check your parameters again."