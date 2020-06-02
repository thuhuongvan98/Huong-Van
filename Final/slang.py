from flask import Flask, render_template, request, redirect,url_for,session
from pymongo import MongoClient, aggregation
from bson import ObjectId
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField,DateField
from wtforms.validators import InputRequired, Email, DataRequired
import random

client = MongoClient('mongodb://localhost:27017/')
db = client['c4e']
slang_dict = db['slang']
user_collection = db['user']

app = Flask(__name__)
app.secret_key = 'hahaha'

check_login = ""
code_login = ""
welcome = ""

#====================LogIn & LogOut=========================
class LoginForm(FlaskForm):
  username = StringField(u'Username', validators=[DataRequired()])
  password = PasswordField(u'Password', validators=[DataRequired()])
  submit = SubmitField(u'Log In')
class LogoutForm(FlaskForm):
  submit = SubmitField("Log Out")

@app.route('/login', methods = ['GET', 'POST'])
def login():
  form = LoginForm(request.form)
  warning = ""
  if request.method == 'POST':
    if form.validate_on_submit():
        username = request.form.get('username','',type=str)
        password = request.form.get('password','',type=str)
        check_user = user_collection.find_one({'username': username})
        if check_user == None:
            warning = "*User Not Found"
            return render_template('login.html',form=form,warning=warning)
        else:
            if password == check_user['password']:
              session['username'] = username
              return redirect(url_for('homepage'))
            else:
              warning = "*Incorrect Password"
              return render_template('login.html',form=form,warning=warning)
  return render_template('login.html',form=form)

@app.route('/logout')
def logout():
  session.pop('username',None)
  return redirect(url_for('homepage'))

#=====================Homepage=====================
class SearchForm(FlaskForm):
    search = StringField("Find your word")
    submit = SubmitField("Search")
@app.route('/', methods = ['GET', 'POST'])
def homepage():
  form = SearchForm(request.form)
  if session.get('username') == None:
    check_login = "Log In"
    code_login = "login"
    welcome = ""
  else:
    check_login = "Log Out"
    code_login = "logout"
    welcome = f"Welcome, {session.get('username')}"
  check_word = ""
  add_word = ""
  count = int(slang_dict.estimated_document_count())
  randomn_number = random.randrange(1,count,1)
  random_dict = slang_dict.find().limit(-1).skip(randomn_number).next()
  if form.validate_on_submit():
      word = request.form.get('search','',type=str)
      find_word = slang_dict.find_one({'word': word})
      if find_word == None:
        check_word = "*Word not found"
        add_word = "Add new word?"
        return render_template('homepage.html', form = form,random_dict=random_dict,check_word=check_word, add_word=add_word)
      else:
          return redirect(url_for('define', word = word))
  return render_template('homepage.html', form = form,random_dict=random_dict,check_word=check_word,check_login=check_login,code_login=code_login,welcome=welcome)

#=====================Definition terms=================
@app.route('/define/<word>')
def define(word):
  if session.get('username') == None:
    check_login = "Log In"
    code_login = "login"
  else:
    check_login = "Log Out"
    code_login = "logout"
  define = slang_dict.find_one({'word': word})
  return render_template('definition.html',define = define,check_login=check_login,code_login=code_login)

# ======================== Sign Up ===========================
class SignupForm(FlaskForm):
    username = StringField(u'Username', validators=[DataRequired()])
    password = PasswordField(u'Password', validators=[DataRequired()])
    repassword = PasswordField(u'Confirm Password', validators=[DataRequired()])
    firstname = StringField('First Name')
    lastname = StringField('Last Name')
    dateofbirth = StringField('Date of Birth')
    submit = SubmitField(u'Sign Up')

@app.route('/signup',methods = ['GET', 'POST'])
def signup():
    form = SignupForm(request.form)
    warning = ""
    if request.method == 'POST':
        if form.validate_on_submit():
            username = request.form.get('username','',type=str)
            password = request.form.get('password','',type=str)
            repassword = request.form.get('repassword','',type=str)
            firstname = request.form.get('firstname','',type=str)
            lastname = request.form.get('lastname','',type=str)
            dateofbirth = request.form.get('dateofbirth','')
            check_user = user_collection.find_one({'username': username})
            if check_user == None:
                if password == repassword:
                    user_collection.insert_one({
                        'username': username,
                        'password': password,
                        'firstname': firstname,
                        'lastname': lastname,
                        'dateofbirth': dateofbirth
                    })
                    return redirect(url_for('homepage'))
                else:
                    warning = "*The password you typed do not match. Please retype the new password in both boxes."
                    return render_template('signup.html',form=form,warning=warning)              
            else:
                warning = "*User has already existed"
                return render_template('signup.html',form=form,warning=warning)       
    return render_template('signup.html',form=form)

# ======================= Add new word =====================
class AddForm(FlaskForm):
  word = StringField(u'Word', validators=[DataRequired()])
  definition = StringField(u'Definition', validators=[DataRequired()])
  example = StringField(u'Example', validators=[DataRequired()])
  tag = StringField(u'Tag')
  submit = SubmitField(u'Add to UrDict')

@app.route('/add',methods = ['GET', 'POST'])
def create():
  form = AddForm(request.form)
  if request.method == "POST":
    if form.validate_on_submit():
      word = request.form.get('word','',type=str)
      definition = request.form.get('definition','',type=str)
      example = request.form.get('example','',type=str)
      tag = request.form.get('tag','',type=str)
      slang_dict.insert_one({
        "word": word,
        "definition": definition,
        "example": example,
        "tag": tag
      })
      define = slang_dict.find_one({'word': word})
      return redirect(url_for("define"),word=word)
  return render_template("add.html",form=form)

# =================== Delete ===================
@app.route('/delete/<word>')
def delete(word):
    delete = slang_dict.delete_one({'word': word})
    return redirect(url_for('homepage'))

# ================== Edit ======================
class EditForm(FlaskForm):
  word = StringField(u'Word', validators=[DataRequired()])
  definition = StringField(u'Definition', validators=[DataRequired()])
  example = StringField(u'Example', validators=[DataRequired()])
  tag = StringField(u'Tag')
  submit = SubmitField(u'Save')

@app.route('/edit/<word>',methods = ['GET', 'POST'])
def edit(word):
  form = EditForm(request.form)
  if request.method == "POST":
    if form.validate_on_submit():
      term = request.form.get('word','',type=str)
      definition = request.form.get('definition','',type=str)
      example = request.form.get('example','',type=str)
      tag = request.form.get('tag','',type=str)
      slang_dict.find_one_and_replace({"word": word},
      {
        "word": term,
        "definition": definition,
        "example": example,
        "tag": tag
      })
      return redirect('/')
  return render_template("edit.html",form=form)


# ================== List =======================
@app.route('/list')
def listing():
  alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
  return render_template("list.html",alphabet=alphabet)

listing = []
for i in slang_dict.find():
  word = i['word']
  listing.append(word)
a = len(listing)
print(a)

@app.route('/list/<y>')
def letter_listing(y):
  alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
  letter_list = []
  for x in range(1000):
    if listing[x][0] == y:
      letter_list.append(listing[x])
  return render_template('letter_list.html',letter_list=letter_list,alphabet=alphabet)
#================== General ====================

if __name__ == '__main__':
  app.run(debug = True, port=3000)


  


