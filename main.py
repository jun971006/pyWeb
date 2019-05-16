from flask import Flask, render_template, request, session
import pymongo

mongo_url='mongodb+srv://wnstjrdlrj:dkagh1025!@cluster0-7nxpj.mongodb.net/test?retryWrites=true'
client = pymongo.MongoClient(mongo_url)
db = pymongo.database.Database(client, 'Cluster0')
books = pymongo.collection.Collection(db, 'Books')
users = pymongo.collection.Collection(db, 'Users')

app=Flask(__name__)
app.secret_key = "hi"


@app.route('/')
def hello_world():
	return render_template('book.html')

@app.route('/register')
def register():
	return render_template('bookAdd.html')

@app.route('/books', methods=['GET','POST'])
def post():
	if request.method == 'GET':
#		results = users.find_one()
		books = books.find()
		return render_template('bookList.html', books = books)
	elif request.method == 'POST':
		data = request.form.to_dict(flat='true')
#		users.insert_one({"book_name":data['test'],"book_price":data['test1'],"book_writer":data['test2'], "book_pub":data['test3']})
		books.insert_one(data)
#		return jsonify(request.form)		
#		data = request.form.to_dict()
		books = books.find()
		return render_template('bookList.html', books = books)		

@app.route('/signup', methods=['GET', 'POST'])
def signup():
	if request.method == 'GET':
		return render_template('signup.html')

	elif request.method == 'POST':
		users.insert_one(request.form.to_dict(flat='true'))
		session['userEmail'] = request.form['userEmail']
		return render_template('welcome.html', info=session['userEmail'])





if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
