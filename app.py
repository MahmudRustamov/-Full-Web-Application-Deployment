from flask import Flask, jsonify, request
import psycopg2
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Database connection parameters
DB_HOST = 'db-mahmud.ct6ei6agkus4.ap-south-1.rds.amazonaws.com'
DB_NAME = 'postgres'
DB_USER = 'postgres'
DB_PASS = 'postgres'
DB_PORT = '5432'

def get_db_connection():
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        port=DB_PORT
    )
    return conn

# Endpoint to get all users
@app.route('/students', methods=['GET'])
def get_students():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM tbl_mahmud_data;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(rows)

# Endpoint to get a specific user by ID
@app.route('/students/<int:user_id>', methods=['GET'])
def get_student(user_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM tbl_mahmud_data WHERE UserID = %s", (user_id,))
    student = cur.fetchone()
    cur.close()
    conn.close()

    if student:
        student_dict = {
            "UserID": student[0],
            "Gender": student[1],
            "Age": student[2],
            "EstimatedSalary": student[3],
            "Purchased": student[4]
        }
        return jsonify(student_dict)
    return jsonify({"message": "Student not found"}), 404

# Endpoint to add a new user
@app.route('/students', methods=['POST'])
def add_student():
    data = request.get_json()
    user_id = data['UserID']
    gender = data['Gender']
    age = data['Age']
    estimated_salary = data['EstimatedSalary']
    purchased = data['Purchased']

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO tbl_mahmud_data (UserID, Gender, Age, EstimatedSalary, Purchased)
        VALUES (%s, %s, %s, %s, %s)
    """, (user_id, gender, age, estimated_salary, purchased))
    conn.commit()
    cur.close()
    conn.close()

    return jsonify({'message': 'User added successfully'})

# Endpoint to delete a user by ID
@app.route('/students/<int:user_id>', methods=['DELETE'])
def delete_student(user_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM tbl_mahmud_data WHERE UserID = %s", (user_id,))
    conn.commit()
    cur.close()
    conn.close()

    return jsonify({'message': 'User deleted successfully'})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)