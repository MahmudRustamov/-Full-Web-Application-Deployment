This project is a simple full-stack customer management system allowing users to add, search, and delete customer data using a PostgreSQL database.
# 👤 Customer Management System – Flask + PostgreSQL
A simple Customer Management System built with Flask. It uses a PostgreSQL database hosted on AWS RDS and runs on an EC2 instance. Users can be added or deleted through a web interface.

---

## 📌 Features

- Add and delete customer records
- Flask-based web backend
- PostgreSQL database hosted on AWS RDS
- Deployed on an AWS EC2 instance

---

## 🗃️ Database Schema

**Table Name:** `tbl_mahmud_data`

| Column Name     | Data Type |
|------------------|-----------|
| UserID           | SERIAL PRIMARY KEY |
| Gender           | VARCHAR |
| Age              | INTEGER |
| EstimatedSalary  | INTEGER |
| Purchased        | BOOLEAN |

---

## 📂 Project Structure
final_project/
├── app.py
├── frontend/ # Static frontend files (hosted in S3)

1. Set up EC2 Instance:

  Configure the security group to allow traffic on ports: 80, 22, 443, 5432, 8000, and all traffic.
  Set up RDS PostgreSQL:

  Make sure the RDS instance allows all traffic from the EC2 instance (public access).
  SSH into EC2:

2.Run:
```ssh -i "C:\your_key_2_ec2.pem" ubuntu@<EC2_Public_IP>```


3. Install dependencies:
    ```bash
    sudo apt update
    sudo apt install python3 python3-pip postgresql-client -y
    ```
    
4. Connect to the RDS instance using psql:
   ```psql -h <RDS_End_Point> -U <RDS_User> -d <RDS_Database_Name>```

5. Your PostgreSQL table `tbl_mahmud_data` should look like this:
```sql
CREATE TABLE tbl_mahmud_data (
    UserID INT PRIMARY KEY,
    Gender VARCHAR(10),
    Age INT,
    EstimatedSalary INT,
    Purchased INT
);
```
Exit

6.Create Project Directory and Flask Application:
  Create the project directory and Python file: 
```
mkdir final_project
cd final_project
touch app.py
```
Edit app.py and implement the Flask application with PostgreSQL connection.

7. Create index.html Template:
   Create and populate index.html to display the tbl_mahmud_data.

9. Install Python Dependencies:
   Install python3-venv (if not already installed)
```
cd final_project
sudo apt update
sudo apt install python3-venv
python3 -m venv venv
source venv/bin/activate
```

Install the necessary libraries:
```
pip3 install --upgrade pip
pip3 install flask psycopg2-binary
```

10. Run the server:
    ```bash
    cd final_project
    python app.py    
    ```

### 🔹 Frontend

The frontend is a static HTML page. You can:

- Open `index.html` directly
- Or upload it to an [AWS S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/WebsiteHosting.html)

11. Access the Application:
```Open the browser and access the web application on your EC2 instance at http://<EC2_Public_IP>:8000.```
This sequence now includes placeholders (<RDS_End_Point>, <RDS_User>, <RDS_Database_Name>, <EC2_Public_IP>) to replace with the actual connection details for your EC2 and RDS instances.



