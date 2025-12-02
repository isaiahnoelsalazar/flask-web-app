from flask import Flask, request, render_template
import pymssql
import sys

app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello'


@app.route('/test')
def home():
    return render_template("test.html")


@app.route('/about')
def about():
    return sys.version


@app.route("/mssql_query")
def python_mssql_query():
    try:
        server = request.args.get("server")
        database = request.args.get("database")
        username = request.args.get("username")
        password = request.args.get("password")
        query = request.args.get("query")

        connection = pymssql.connect(server, username, password, database)

        cursor = connection.cursor()
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


@app.route("/mssql_execute")
def python_mssql_execute():
    try:
        server = request.args.get("server")
        database = request.args.get("database")
        username = request.args.get("username")
        password = request.args.get("password")
        execute = request.args.get("execute")

        connection = pymssql.connect(server, username, password, database)

        cursor = connection.cursor()
        cursor.execute(execute)
        connection.commit()
        connection.close()

        return "Command completed."
    except:
        return "Connection broken. Please check your parameters again."
