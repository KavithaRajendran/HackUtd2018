from flask import Flask,flash,redirect,render_template
from flask import request,session,abort,url_for
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
		return render_template('home.html')



@app.route('/login',methods=['GET','POST'])
def login():
	if request.method =='POST':
		username = request.form['username']
		password = request.form['password']
		if username == 'user' and password =='password':
			flash('Logged in !')
			session['logged_in'] = True
			return redirect(url_for('home'))
	
	
if __name__=="__main__":
	app.secret_key = os.urandom(12)
	app.run(debug=True,host='localhost',port=4000)