from flask import Flask, render_template, request, jsonify
import mysql.connector
from datetime import datetime

app = Flask(__name__)


#this is home route

@app.route('/')
def home():
    return render_template('index.html')


#this is post route to add scores

@app.route('/addScore', methods=['POST'])
def score():
    data = request.get_json()
    name = data.get('name')
    score_value = data.get('score')

    created_at = datetime.now() #this sends date and time to database 

    if not name or score_value is None:
        return jsonify({'error': "Missing 'name' or 'score'"}), 400


    con = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'admin',
        database = 'game'
    )

    cursor = con.cursor()
    cursor.execute(
        'INSERT INTO scores(name, score, created_at) VALUES (%s,%s, %s)', #%s should be according to number fo columns
        (name, score_value, created_at)
    )

    con.commit()


    cursor.close()
    con.close() #each route has its own connection that must be closed

    return jsonify({'message': "score sent to database! :)"}), 200


#this is get route to show highscore table on game 

@app.route('/highscores', methods=['GET'])
def get_highscores():
    con = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'admin',
        database = 'game'
    )

    cursor = con.cursor(dictionary=True) #we use python object dictionary to visualize data from database through json
    cursor.execute(
        'SELECT name, score, created_at FROM scores ORDER BY score DESC LIMIT 5'
    )

    scores = cursor.fetchall()
    cursor.close()
    con.close()

    return jsonify(scores)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

