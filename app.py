from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)


#this is home route

@app.route('/')
def home():
    return 'flask server is running! :)'

@app.route('/addScore', methods=['POST'])
def score():
    data = request.json()
    name = data['name']
    score = data['score']

    con = mysql.connect.connect(
        host = 'localhost',
        user = 'root',
        password = 'admin',
        database = 'mini game'
    )

    cursor = con.cursor()
    cursor.execute(
        'INSERT INTO scores(name, score) VALUES (%s,%s)'
    )

    con.commit()

    cursor.close()
    con.close()

    return jsonify({'message': "score sent to database! :)"}), 200

if __name__ == '__main__':
    app.run(debug=True)
