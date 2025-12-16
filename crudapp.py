from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

#this is mysql connection

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'admin',
    database = 'flaskcrud'
)

cursor = db.cursor(dictionary=True)

@app.route('/')
def Index():
    return "<h1> Hello Flask Application </h1>"

#make a new user 

@app.route('/user', methods=['POST'])
def create_user():
    data = request.json
    cursor.execute(
        "INSERT INTO users(name, email, phone) VALUES ( %s, %s, %s)",
        (data['name'], data['email'], data['phone'])
    )
    db.commit()
    return jsonify({"message" : "user created :)"}), 201


#read one user with fetchone

@app.route('/user/<int:id>', methods=['GET'])
def get_user(id):
    cursor.execute("SELECT * FROM users WHERE id=%s", (id,))
    user = cursor.fetchone()
    return jsonify(user)


#update user by id

@app.route('/user/<int:id>', methods=['PUT'])
def update_user(id):
    data = request.json
    cursor.execute(
        "UPDATE users SET name=%s, email=%s, phone=%s WHERE id=%s",
        (data['name'], data['email'], data['phone'], id)
    )
    db.commit()
    return jsonify({'message' : 'user updated :)'})


#delete user by id

@app.route('/user/<int:id>', methods=['DELETE'])
def delete_user(id):
    cursor.execute("DELETE FROM users WHERE id=%s", (id,))
    db.commit()
    return jsonify ({'message': "user deleted :("})


#read all users with fetchall

@app.route('/users', methods=['GET'])
def get_users():
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    return jsonify(users)



#run ur server

if __name__ == '__main__':
    app.run(debug=True)

