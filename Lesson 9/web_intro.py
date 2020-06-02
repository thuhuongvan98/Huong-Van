from flask import *
from pymongo import MongoClient
from bson import ObjectId

client = MongoClient('localhost:27017')
db = client['c4e']
kpop_collection = db['Kpop']

app = Flask(__name__)

@app.route('/')
def homepage(): 
  idols = kpop_collection.find({})
  return render_template('homepage.html', idols_data=idols)


@app.route('/idol/<id>')
def detail(id):
  idol = kpop_collection.find_one({'_id': ObjectId(id)})
  return render_template('detail.html', idol=idol)


@app.route('/delete/<id>')
def delete(id):
  kpop_collection.delete_one({'_id': ObjectId(id)})
  return redirect('/')

@app.route('/goback')
def goback():

  return redirect('/')
app.run(debug=True, port=3000)