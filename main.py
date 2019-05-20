from flask import Flask, render_template, request, session, url_for, redirect
import pymongo
from datetime import timedelta

mongo_url='mongodb+srv://wnstjrdlrj:dkagh1025!@cluster0-7nxpj.mongodb.net/test?retryWrites=true'
client = pymongo.MongoClient(mongo_url)
db = pymongo.database.Database(client, 'Cluster0')
books = pymongo.collection.Collection(db, 'Books')
users = pymongo.collection.Collection(db, 'Users')

app=Flask(__name__)
app.secret_key = "hi"


@app.route('/')
def hello_world():
	if 'userEmail' in session:
		return render_template('book.html', info=session['userEmail'])
	return redirect(url_for('signin'))

@app.route('/register')
def register():
	if 'userEmail' in session:
		return render_template('bookAdd.html')
	return redirect(url_for('signin'))

@app.route('/books', methods=['GET','POST'])
def post():
	if request.method == 'GET':
#		results = users.find_one()
		if 'userEmail' in session:
#			books = books.find()
			return render_template('bookList.html', results = books.find({}))
		return redirect(url_for('signin'))
	elif request.method == 'POST':
		if 'userEmail' in session:
			data = request.form.to_dict(flat='true')
			books.insert_one(data)
		#	books = books.find()
			return render_template('bookList.html', results = books.find({}))		
		return render_template('bookList.html', results = books.find({}))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
	if request.method == 'GET':
		if not 'userEmail' in session:
			return render_template('signup.html')
		return render_template('book.html', info=session['userEmail'])

	elif request.method == 'POST':
		if not 'userEmail' in session:
			users.insert_one(request.form.to_dict(flat='true'))
			session['userEmail'] = request.form['userEmail']
			return render_template('book.html', info=session['userEmail'])
		return render_template('book.html', info=session['userEmail'])

@app.route('/signin', methods=['GET', 'POST'])
def signin():
	if request.method == 'GET':
		if 'userEmail' in session:
			return render_template('book.html', info=session['userEmail'])
		return render_template('signin.html')

	elif request.method == 'POST':
		if 'userEmail' in session:
			return render_template('book.html', info=session['userEmail'])

		elif users.find_one(request.form.to_dict(flat='true')) is not None:
			session['userEmail'] = request.form['userEmail']
			return render_template('book.html', info=session['userEmail'])
		return redirect(url_for('signin'))	

@app.route('/logout')
def logout():
	if 'userEmail' in session:
		session.pop('userEmail')
		return redirect(url_for('signin'))
	return redirect(url_for('signin'))

@app.before_request
def make_session_permanent():
	session.permanent=True
	app.permanent_session_lifetime=timedelta(minutes=60)


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
