#demonstrating GET method (can be accessed by chrome and postman both)

from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)


@app.route('/')
def home():
    return "Flask server is running!"


@app.route('/getTable', methods=['GET'])
def get_tables():
    con = mysql.connector.connect(
        host='localhost',
        user='root',
        password='admin',
        database='mydatabase'
    )

    cursor = con.cursor()
    cursor.execute('SHOW TABLES;')
    tables = cursor.fetchall()
    cursor.close()
    con.close()

    table_names = [table[0] for table in tables]
    return jsonify({'tables': table_names}), 200


#demonstrating POST method (can only be done by postman)

@app.route('/addStudent', methods=['POST'])
def add_student():
    data = request.get_json()
    name = data.get('name')
    mark = data.get('mark')

    con = mysql.connector.connect(
        host='localhost',
        user='root',
        password='admin',
        database='mydatabase'
    )
    cursor = con.cursor()
    cursor.execute('INSERT INTO students (name, mark) VALUES (%s, %s)', (name, mark))
    con.commit()
    cursor.close()
    con.close()

    return jsonify({"message": "Student added successfully"}), 200

if __name__ == "__main__":
    print("connecting to DB.....")
    app.run(debug=True)
