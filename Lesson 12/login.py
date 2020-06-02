from flask import Flask, render_template, request, redirect,url_for,session
from pymongo import MongoClient
from bson import ObjectId
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField,DateField
from wtforms.validators import InputRequired, Email, DataRequired

client = MongoClient('mongodb://localhost:27017/')
db = client['c4e']
kpop_collection = db['kpop']

app = Flask(__name__)
app.secret_key = 'someone that you know'

class LoginForm(FlaskForm):
  username = StringField(u'Ten dang nhap', validators=[DataRequired()])
  password = PasswordField(u'Mat khau', validators=[DataRequired()])
  submit = SubmitField(u'Dang nhap')
class LogoutForm(FlaskForm):
  submit = SubmitField("Log Out")

@app.route('/',methods = ['GET', 'POST'])
def index():
  if session.get('username') is None:
    return redirect(url_for('login'))
  else:
    idols = kpop_collection.find({})
    return render_template('kpop.html', idols=idols)

#============================ CREATE ======================================
class CreateForm(FlaskForm):
  stagename = StringField(u'Stage Name', validators=[DataRequired()])
  koreanname = StringField(u'Korean Name', validators=[DataRequired()])
  dateofbirth = StringField(u'DOB', validators=[DataRequired()])
  group = StringField(u'Group', validators=[DataRequired()])
  submit = SubmitField(u'Create')

@app.route('/create',methods = ['GET', 'POST'])
def create():
  form = CreateForm(request.form)
  if request.method == "POST":
    if form.validate_on_submit():
      stagename = request.form.get('stagename','',type=str)
      koreanname = request.form.get('koreanname','',type=str)
      dateofbirth = request.form.get('dateofbirth','',type=str)
      group = request.form.get('group','',type=str)
      kpop_collection.insert_one({
        "Stage name": stagename,
        "Korean name": koreanname,
        "DOB": dateofbirth,
        "Group": group
      })
      return redirect(url_for("index"))
  return render_template("create.html",form=form)

#============================ READ =======================================
@app.route('/idol/<stagename>')
def detail(stagename):
  idol = kpop_collection.find_one({'Stage name': stagename})
  return render_template('detail.html', idol=idol)

#============================ UPDATE =====================================
class EditForm(FlaskForm):
    edit_stage_name = StringField(u'Stage Name', validators=[DataRequired()])
    edit_korean_name = StringField(u'Korean Name', validators=[DataRequired()])
    edit_DOB = StringField(u'DOB', validators=[DataRequired()])
    edit_group = StringField(u'Group', validators=[DataRequired()])
    submit = SubmitField(u'Edit')

@app.route('/edit/<stage_name>', methods = ['GET', 'POST'])
def edit(stage_name):
  form = EditForm(request.form)
  if request.method == "POST":
    if form.validate_on_submit():
      edit_stage_name = request.form.get('edit_stage_name','',type=str)
      edit_korean_name = request.form.get('edit_korean_name','',type=str)
      edit_DOB = request.form.get('edit_DOB','',type=str) 
      edit_group = request.form.get('edit_group','',type=str)
      kpop_collection.find_one_and_replace({"Stage name": stage_name},
      {
        'Stage name': edit_stage_name,
        'Korean name': edit_korean_name,
        'DOB': edit_DOB,
        'Group': edit_group
      })
      return redirect(url_for("index"))
  return render_template("edit.html",form=form,stage_name = stage_name)

#============================ DELETE =====================================
@app.route('/delete/<stagename>')
def delete(stagename):
  kpop_collection.delete_one({'Stage name': stagename})
  return redirect('/')

#============================ LOGIN ======================================
@app.route('/login', methods = ['GET', 'POST'])
def login():
  form = LoginForm(request.form)
  if request.method == 'POST':
    if form.validate_on_submit():
      username = request.form.get('username','',type=str)
      password = request.form.get('password','',type=str)
      if (username == "admin" and password == "hihihi"):
        session['username'] = username
        return redirect(url_for('index'))
  return render_template('login.html',form=form)


#============================ LOGOUT =====================================
@app.route('/logout')
def logout():
  session.pop('username',None)
  return redirect(url_for('create'))

if __name__ == '__main__':
  app.run(debug = True, port=3000)