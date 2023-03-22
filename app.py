from flask import Flask, render_template, jsonify, request
from database import load_jobs_from_db, load_job_from_db

app = Flask(__name__)

# hard coded data
# JOBS = [
# 	{
# 	'id': '1',
# 	'title': 'Data analyst',
# 	'location' : 'Bangalore, India',
# 	'salary': 'Rs. 10,00,000',
# 	},
# 	{
# 	'id': '2',
# 	'title': 'Data Scientist',
# 	'location' : 'Delhi, India',
# 	'salary': 'Rs. 12,00,000'
# 	},
# 	{
# 	'id': '3',
# 	'title': 'Data Engineer',
# 	'location' : 'California, USA',
# 	'salary': '$ 150,000'
# 	},
# 	{
# 	'id': '4',
# 	'title': 'Machine Learning Engineer',
# 	'location' : 'Remote, USA',
# 	'salary': '$ 180,000'
# 	},
# 	{
# 	'id': '5',
# 	'title': 'Full Stack Engineer',
# 	'location' : 'Remote',
# 	'salary': '$ 120,000'
# 	}
# ]



@app.route("/")
@app.route("/index")
def index():
	jobs = load_jobs_from_db()
	return render_template("home.html", jobs=jobs)


@app.route('/view/<id>')
def view_details(id):
	job = load_job_from_db(id)
	if not job:
		return "Not none", 404
	return render_template('job-detail.html', job=job)


@app.route('/apply')
def apply():
	return render_template('form-apply.html')


@app.route('/submit', methods=['post'])
def submitForm():
	data = request.form
	return render_template('application_submitted.html', application = data)


@app.route("/api/jobs")
def jobs():
	jobs = load_jobs_from_db() # loads the job from the db
	return jsonify(jobs)


if __name__ == '__main__':
	app.run(debug=True)