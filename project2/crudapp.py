from flask import Flask, request, jsonify #request is to receive data sent by client #jsonify send data back to flask using dicts
import mysql.connector #to connect flask with mysql database, we can use SQL queries within flask 


#here Flask(__name__) is called flask application object
#__name__ The current Python file is the main app
#__name__ Helps Flask know where to look for templates, static files, etc.
#app is the variable in which we store the flask application object FAO
#we use same app variable to create routes, and run the server

app = Flask(__name__)


#this is mysql connection
#it opens connection between flask and mysql
#it helps flask read, fetch, retrieve data from database and send data into it

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'admin',
    database = 'flaskcrud'
)

#cursor is a tool that flask uses to run SQL queries
#it talks to the database and works per the flask requests being made (CREATE, READ, UPDATE, DELETE)
#apis use json to work with data, so here dictionary = True means return data in form of a dictionary in json

cursor = db.cursor(dictionary=True)

#this is a test route to check whether flask app is working or not

@app.route('/')
def Index():
    return "<h1> Hello Flask Application </h1>"


#CREATE Route:::: make a new user 
#request.json reads data sent by client (postman) in json 
#request.json is used when client sends data to flask (eg: in CREATE & UPDATE of CRUD)
#cursor.execute performs SQL commands and follows flask instructions
#db.commit will store the data changes 
#jsonify will return the response to flask 
#200, 201 are HTTP status codes, they tell us whether our request was successful or not


@app.route('/user', methods=['POST'])
def create_user():
    data = request.json
    cursor.execute(
        "INSERT INTO users(name, email, phone) VALUES ( %s, %s, %s)",
        (data['name'], data['email'], data['phone'])
    )
    db.commit()
    return jsonify({"message" : "user created :)"}), 201



#READ Route:::: read one user with fetchone()
#<int:id> is a URL param where it picks data per given id converted into integer
#(id,) is used coz SQL placeholders use a tuple so in python tuple is made with a comma
#%s is a safe and reliable for safe value insertion and prevents SQL injection
#fetchone gets only one record given through the URL param


@app.route('/user/<int:id>', methods=['GET'])
def get_user(id):
    cursor.execute("SELECT * FROM users WHERE id=%s", (id,))
    user = cursor.fetchone()
    return jsonify(user)



#UPDATE Route:::: update user by id
#similar like CREATE Route 
#only SQL operation is different, here users are being updated 


@app.route('/user/<int:id>', methods=['PUT'])
def update_user(id):
    data = request.json
    cursor.execute(
        "UPDATE users SET name=%s, email=%s, phone=%s WHERE id=%s",
        (data['name'], data['email'], data['phone'], id)
    )
    db.commit()
    return jsonify({'message' : 'user updated :)'})



#DELETE Route:::: delete user by id
#this is same as GET Route
#SQL Operation is different, here users are being deleted


@app.route('/user/<int:id>', methods=['DELETE'])
def delete_user(id):
    cursor.execute("DELETE FROM users WHERE id=%s", (id,))
    db.commit()
    return jsonify ({'message': "user deleted :("})


#read all users with fetchall()
#fetchall() is responsible to read/get/fetch all users from database

@app.route('/users', methods=['GET'])
def get_users():
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    return jsonify(users)



#if line ensures that file is run directly and is not imported as module
#once its made sure, only then it runs the flask server
#app.run will start the flask's built-in development server
#debug=True will show errors in console
#debug=True also reloads the server if any code changes made 

if __name__ == '__main__':
    app.run(debug=True)

