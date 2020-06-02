from flask import Flask, render_template, request, redirect, url_for, session, escape
from pymongo import MongoClient
from bson import ObjectId
from flask_wtf import FlaskForm
from wtforms            import StringField, SubmitField, PasswordField
from wtforms.validators import InputRequired, DataRequired

app = Flask(__name__)

#########################################################################################
# Các bạn tự thay đổi cấu hình theo như máy của mình #
#########################################################################################
client = MongoClient("mongodb://localhost:27017/")
db = client["Kpop"]
app.secret_key = 'someone that you know'
#########################################################################################

#########################################################################################
class LoginForm(FlaskForm):
    username = StringField(u'Tên đăng nhập', validators=[DataRequired()])
    password = PasswordField(u'Mật khẩu', validators=[DataRequired()])
    submit = SubmitField(u'Đăng nhập')

class CreateForm(FlaskForm):
    stage_name = StringField(u'Stage Name', validators=[DataRequired()])
    full_name = StringField(u'Full Name', validators=[DataRequired()])
    k_name = StringField(u'Korean Name', validators=[DataRequired()])
    submit = SubmitField(u'Create')

class EditForm(FlaskForm):
###### Thêm code vào đoạn này
    pass
#########################################################################################

#########################################################################################
@app.route('/')
def index():
    if session.get('username') is None:
        return redirect(url_for('login'))
    
    artist_list = list(db.Kpop.find({}))

    return render_template('index.html', artist_list = artist_list)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            username = request.form.get('username', '', type=str)
            password = request.form.get('password', '', type=str)
            if (username == 'admin' and password == 'MindX'):
                session['username'] = username
                return redirect(url_for('index'))
    return render_template('login.html', form = form)

@app.route('/detail/<stage_name>')
def detail(stage_name):
    if session.get('username') is None:
        return redirect(url_for('login'))
    artist = db.Kpop.find_one({"stage_name": stage_name})
    return render_template('detail.html', artist = artist)

@app.route('/delete/<stage_name>')
def delete(stage_name):
    if session.get('username') is None:
        return redirect(url_for('login'))
    
    db.Kpop.delete_one({'stage_name': stage_name})
    return redirect(url_for('index'))

@app.route('/create', methods = ['GET', 'POST'])
def create():
    form = CreateForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            stage_name = request.form.get('stage_name', '', type=str)
            full_name = request.form.get('full_name', '', type=str)
            k_name = request.form.get('k_name', '', type=str)
            artist = {'stage_name': stage_name, 'full_name': full_name, 'k_name': k_name}
            db.Kpop.insert_one(artist)
            return redirect(url_for('index'))
    return render_template('create_idol.html', form = form)

@app.route('/edit', methods = ['GET', 'POST'])
def edit():
###### Thêm code vào đoạn này    
    pass

# Đăng xuất người dùng
@app.route('/logout')
def logout():
   session.pop('username', None)
   return redirect(url_for('login'))
#########################################################################################

if __name__ == '__main__':
    app.run(debug = True)