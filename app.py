from flask import Flask, render_template, jsonify, request
import pymysql
import yaml

try:
    with open('database.yaml', 'r') as file:
        db = yaml.load(file, Loader=yaml.FullLoader)
except FileNotFoundError:
    print("Error: The file 'database.yaml' was not found.")
    db = None
except yaml.YAMLError as e:
    print(f"Error loading YAML file: {e}")
    db = None
app = Flask(__name__)

if db:
    app.config['MYSQL_HOST'] = db['mysql_host']
    app.config['MYSQL_USER'] = db['mysql_user']
    app.config['MYSQL_PASSWORD'] = db['mysql_password']
    app.config['MYSQL_DB'] = db['mysql_db']
else:
    raise ValueError("Database configuration is missing or invalid.")

# Route to test database connection
@app.route('/test_connection')
def test_connection():
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT VERSION()")
        version = cur.fetchone()
        cur.close()
        return jsonify({"version": version[0]})
    except Exception as e:
        return jsonify({"error": str(e)})

# Job listings
JOBS = [
    {
        'id': 1,
        'title': 'Machine Operator',
        'salary': "Rs. 12,500/m",
    },
    {
        'id': 2,
        'title': 'Delivery Agent',
        'salary': "Rs. 10,000/m",
    },
    {
        'id': 3,
        'title': 'Engineer',
        'salary': "Rs. 11,000/m",
    }
]
@app.route('/')
def hello_world(): 
    return render_template('index.html', jobs=JOBS)
@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
