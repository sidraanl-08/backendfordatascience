from flask import Flask
import mysql.connector

app = Flask(__name__)


@app.route('/')
def Index():
    return "<h1> Hello Flask Application </h1>"



#run ur server

if __name__ == '__main__':
    app.run(debug=True)