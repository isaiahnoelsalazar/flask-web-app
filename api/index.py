from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello'

@app.route('/about')
def about():
    return 'About'

@app.route("/mssql")
def pymssql():
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
    except Exception as e:
        return str(e)