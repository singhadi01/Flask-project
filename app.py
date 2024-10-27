from flask import Flask,render_template,jsonify
app=Flask(__name__)
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