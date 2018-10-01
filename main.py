from flask import Flask, request, redirect, render_template
import cgi
import helper_functions

app = Flask(__name__)

app.config['DEBUG'] = True  

def input_validation(userEmail, userName, password, passwordConfirmation):
  if email_validation(userEmail) and username_validation(userName) and password_validation(password) and password_match(password,passwordConfirmation) == True:
      return True
  
  else:
      return False


@app.route("/", methods=['GET'])
def index():
    return render_template('signup.html')


@app.route("/", methods=['POST'])
userInput = request.args.get('userEmail', 'userName', 'password', 'passwordConfirmation')

if input_validation(userEmail, userName, password, passwordConfirmation) == True:
    return "pass" #redirect to welcome page

else:

@app.route("/signup", methods=['POST'])
def signup():


@app.route("/welcome", methods=['POST'])
def welcome():
    greeting = request.form('userName')
    return '<h2>Welcome, ' + userName + '</h2>'   

app.run()    


#validate data functions
#def validate_data():
#if statements return a redirect to the 
# homepage with error as a query parameter
#if successful, return render.template