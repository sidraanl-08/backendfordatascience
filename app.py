from flask import Flask, render_template, request, jsonify
import mysql.connector

app = Flask(__name__)


#this is home route

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/addScore', methods=['POST'])
def score():
    data = request.get_json()
    name = data.get('name')
    score_value = data.get('score')

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
        'INSERT INTO scores(name, score) VALUES (%s,%s)',
        (name, score_value)
    )

    con.commit()

    cursor.close()
    con.close()

    return jsonify({'message': "score sent to database! :)"}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
