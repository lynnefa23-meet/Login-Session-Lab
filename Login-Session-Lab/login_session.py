from flask import Flask, render_template, request, url_for, redirect
from flask import session as login_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret-key'

@app.route('/', methods = ["POST", "GET"]) # What methods are needed?
def home():
	if request.method == "POST":
		try:
			name= request.form["author's name"]
			age= request.form["author's age"]
			quote= request.form["enter a quote"]
			login_session["author's name"]=name
			login_session["author's age"]=age
			login_session["enter a quote"]=quote
			return render_template("thanks.html", quote=login_session["enter a quote"], name=login_session["author's name"], age=login_session["author's age"])
		except: 
			return render_template("error.html")

	else: 
		return render_template('home.html')
		

@app.route('/error')
def error():

	return render_template('error.html')


@app.route('/display')
def display():

	return render_template('display.html', quote=login_session["enter a quote"], name=login_session["author's name"], age=login_session["author's age"]) # What variables are needed?


@app.route('/thanks')
def thanks():

	return render_template('thanks.html')


if __name__ == '__main__':
	app.run(debug=True)