from flask import Flask, render_template, jsonify

jobs_list = [
  {
    "id": 1,
    "role": "Software Engineer",
    "location": "Bengaluru, India",
    "salary": 120000,
    "currency": "INR",
  },
  {
    "id": 2,
    "role": "Game Developer",
    "location": "Hyderabad, India",
    "salary": 100000,
    "currency": "INR",
  },
  {
    "id": 3,
    "role": "Cloud Engineer",
    "location": "San Francisco, USA",
    "salary": 1200,
    "currency": "USD",
  },
]

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html', jobs = jobs_list)


@app.route('/auth/login')
def login():
    return render_template('login.html')


@app.route('/api/jobs')
def jobs():
    return jsonify(jobs_list)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)