from flask import Flask, request, redirect, render_template
import cgi
from helper_functions import text_len, no_spaces, special_chars

app = Flask(__name__)

app.config['DEBUG'] = True  

def username_validation(username):

  if text_len(username) and no_spaces(username) == True:
      
    return True
  else:

    return False

def password_validation(password):

  if text_len(password) and no_spaces(password) == True:
    return True

  else:
    return False

def password_match(password, passwordConfirmation):
    if passwordConfirmation == '':
        return False 
    
    elif password == passwordConfirmation:
        return True   

    else:
        return False 

def email_validation(userEmail):

  if userEmail == '':
      return True
  
  elif text_len(userEmail) and no_spaces(userEmail) and special_chars(userEmail) ==  True:
      return True
  
  else:
    return False

@app.route("/", methods=['GET'])
def index():
    return render_template('signup.html')


@app.route("/", methods=['POST'])
def validate_signup():
    usernameField = request.form['username']
    passwordField = request.form['password']
    passwordConfirmationField = request.form['passwordConfirmation']
    emailField = request.form['email']
    error = "That is not a valid input"

    usernameError = " "
    passwordError = " "
    passwordConfirmationError = " "
    emailError = " "

    if not username_validation(usernameField):
        usernameError = error

    if not password_validation(passwordField):
        passwordError = error

    if not password_match(passwordField,passwordConfirmationField):
        passwordConfirmationError = error 

    if not email_validation(emailField):
        emailError = error  
  

    if username_validation(usernameField) is True and password_validation(passwordField) is True and password_match(passwordField, passwordConfirmationField) is True and email_validation(emailField) is True:
        return redirect('/welcome?username={0}'.format(usernameField))
    
    else:        
        #this loads the data the user entered into the form after the error
        if not username_validation(usernameField):
            return render_template('signup.html', username=usernameField,email=emailField, 
            usernameError=usernameError, passwordError=passwordError,
            passwordConfirmationError=passwordConfirmationError, emailError=emailError,)
  
#got the error message to appear next to one field. how
#can i make it appear on multiple? right now the code
#will stop at the first return. should i nest a function
#within this one?


@app.route("/welcome")
def welcome():
    username = request.args.get('username')
    return render_template('welcome.html', username=username)
    #return '<h1> Welcome {0}</h1>'.format(username)



app.run()    


#validate data functions
#def validate_data():
#if statements return a redirect to the 
# homepage with error as a query parameter
#if successful, return render.template