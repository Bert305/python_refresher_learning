from flask import Flask, request, jsonify
from flask_cors import CORS
import pymysql

app = Flask(__name__)

# add environment variable for MySQL password
import os
import dotenv
dotenv.load_dotenv()
import pymysql.cursors
os.environ['MYSQL_PASSWORD'] = 'your_mysql_password'
os.environ['MYSQL_USER'] = 'your_mysql_user'
CORS(app)


# MySQL connection function
def get_db_connection():
    return pymysql.connect(
        host='localhost',
        user=os.environ['MYSQL_USER'],
        password=os.environ['MYSQL_PASSWORD'],
        port=3306,
        db='flask_api',
        cursorclass=pymysql.cursors.DictCursor
    )


# Create a new user
@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    first_name = data['first_name']
    last_name = data['last_name']
    phone = data['phone']
    email = data['email']

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO users (first_name, last_name, phone, email)
        VALUES (%s, %s, %s, %s)
    """, (first_name, last_name, phone, email))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'message': 'User created successfully'}), 201

# Read all users
@app.route('/users', methods=['GET'])
def get_users():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(users)

# Read single user
@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE id = %s", (id,))
    user = cur.fetchone()
    cur.close()
    conn.close()
    if user:
        return jsonify(user)
    else:
        return jsonify({'message': 'User not found'}), 404

# Update a user
@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    data = request.get_json()
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        UPDATE users SET first_name=%s, last_name=%s, phone=%s, email=%s
        WHERE id = %s
    """, (data['first_name'], data['last_name'], data['phone'], data['email'], id))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'message': 'User updated successfully'})

# Delete a user
@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM users WHERE id = %s", (id,))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'message': 'User deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)

