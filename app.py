from flask import Flask,render_template,jsonify,request
from flask_mysqldb import MySQl
import yaml
db = yaml.load(open('database.yaml'), Loader=yaml.FullLoader)
app=Flask(__name__)
db=yaml.load(open('database.yaml'))
app.config['MYSQL_HOST']=db['mysql_host']
app.config['MYSQL_USER']=db['mysql_user']
app.config['MYSQL_PASSWORD']=db['mysql_password']
app.config['MYSQL_DB']=db['mysql_db']
mysql=MySQl(app)
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
JOBS=[
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
  return render_template('index.html',jobs=JOBS)
@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)
if __name__=="__main__":
  app.run(host='0.0.0.0',debug=True)