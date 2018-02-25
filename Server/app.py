from flask import Flask,flash,redirect,render_template
from flask import request,session,abort
import os
app=Flask(__name__)


app.config['MONGO_DBNAME'] = 'restdb'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/restdb'

#mongo = PyMongo(app)

@app.route('/')
def home():
	if not session.get('logged_in'):
		return render_template('login.html')
	else:
		return "Welcome"


@app.route('/login',methods=['GET','POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		login_user(user)
		flask.flash('Logged in !')
		next = flask.request.args.get('next')
		if not is_safe_url(next):
			return flask.abort(400)
		return flask.redirect(next or flask.url_for('index'))
	return flask.render_template('login.html',form=form)

if __name__=="__main__":
	app.secret_key = os.urandom(12)
	app.run(debug=True,host='localhost',port=4000)
	