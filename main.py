from flask import Flask, render_template, request, jsonify
import pymongo

mongo_url='mongodb+srv://wnstjrdlrj:dkagh1025!@cluster0-7nxpj.mongodb.net/test?retryWrites=true'
client = pymongo.MongoClient(mongo_url)
db = pymongo.database.Database(client, 'Cluster0')
users = pymongo.collection.Collection(db, 'Books')

app=Flask(__name__)

@app.route('/')
def hello_world():
	return render_template('book.html')

@app.route('/register')
def test():
	return render_template('bookAdd.html')

@app.route('/books', methods=['GET','POST'])
def post():
	if request.method == 'GET':
#		results = users.find_one()
		books = users.find()
		return render_template('bookList.html', books = books)
	elif request.method == 'POST':
		data = request.form.to_dict()
		users.insert_one({"book_name":data['test'],"book_price":data['test1'],"book_writer":data['test2'], "book_pub":data['test3']})
#		return jsonify(request.form)		
#		data = request.form.to_dict()
		books = users.find()
		return render_template('bookList.html', books = books)		

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
