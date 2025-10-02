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


@app.route("/mssql_query")
def python_mssql_query():
    try:
        # server = 'sql.bsite.net\\MSSQL2016'
        # database = 'saiasamazingaspsite_SampleDB'
        # username = 'saiasamazingaspsite_SampleDB'
        # password = 'DBSamplePW'

        server = request.args.get("server")
        database = request.args.get("database")
        username = request.args.get("username")
        password = request.args.get("password")
        query = request.args.get("query")

        connection = pymssql.connect(server, username, password, database)

        cursor = connection.cursor()
        # cursor.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE'")
        cursor.execute(query)
        rows = cursor.fetchall()

        data = "<style>body{margin:0;padding:0;}p{margin:0;}#row-container{display:flex;flex-direction:column;}</style><div id='row-container'>"

        for row in rows:
            data += "<p>" + str(row)[2:-3] + "</p>"

        data += "</div>"

        connection.close()

        return data
    except:
        return "Connection broken. Please check your parameters again."