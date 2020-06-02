from flask import *

app = Flask(__name__)

@app.route('/')
def homepage():
  return "Hello me!"

users = {
    'thuhuongvan98': {
      "Name": "Van Nguyet Thu Huong",
      "Age": 21,
      "Address": "Hahaha"
    },
    'baohoa96' : {
      "Name": "Hoa Hoang Bao Hoa",
      "Age": 23,
      "Address": "Complicated"
    },
    'htkl172' : {
      "Name": "Hoang Tran Khanh Linh",
      "Age": 21,
      "Address": "Huhuhu"
    }
  }

@app.route('/about-me')
def about_me(): 
  return render_template('about_me.html',users = users)
  #ten bien trong html va trong python co the khac nhau
  #render_template không render đc ảnh

@app.route('/school')
def school():
  return redirect("https://mindx.edu.vn/", code=302)

@app.route('/bmi/<weight>/<height>')
def bmi(weight,height):
  bmi_calculation = int(weight)/((int(height)/100)**2)
  if bmi_calculation < 16:
    evaluate = "Severely underweight"
  elif bmi_calculation <18.5:
    evaluate = "Underweight"
  elif bmi_calculation < 25:
    evaluate = "Normal"
  elif bmi_calculation < 30:
    evaluate = "Overweight"
  elif bmi_calculation >= 30:
    evaluate = "Obsese"
  return render_template('bmi.html',bmi_calculation = bmi_calculation, evaluate = evaluate)

# @app.route('/user/<username>')
# def user(username):
#   users = {
#     'thuhuongvan98': {
#       "Name": "Van Nguyet Thu Huong",
#       "Age": 21,
#       "Relationship_Status": "Married"
#     },
#     'baohoa96' : {
#       "Name": "Hoa Hoang Bao Hoa",
#       "Age": 23,
#       "Relationship_Status": "Complicated"
#     },
#     'htkl172' : {
#       "Name": "Hoang Tran Khanh Linh",
#       "Age": 21,
#       "Relationship_Status": "Married"
#     }
#   }
#   if username in users:
#     return f'{users[username]["Name"]}, {users[username]["Age"]}'
#   else:
#     return "User not found"

app.run(debug=True, port=3000)
#trong html co the lay data tu dict & list: {{users.htkl172.Age}}