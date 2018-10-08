from flask import Flask, request, redirect, render_template
import cgi
from helper_functions import text_len, no_spaces, special_chars

app = Flask(__name__)

app.config['DEBUG'] = True  

@app.route("/", methods=['GET'])
def index():
    return render_template('signup.html')


@app.route("/", methods=['POST'])
def validate_signup():

# here we are creating variables for the validation functions
# by requesting data from the form
        
    usernameField = request.form['username']
    passwordField = request.form['password']
    passwordConfirmationField = request.form['passwordConfirmation']
    emailField = request.form['email']
    error = "That is not a valid input"

#these functions validate the user input against the 
# standards of the assignment

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
    

# this section will trigger an error for each input field 
# if the user input does not meet validation

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

    # this redirects the user to the welcome page if all fields pass validation
    if username_validation(usernameField) is True and password_validation(passwordField) is True and password_match(passwordField, passwordConfirmationField) is True and email_validation(emailField) is True:
        return redirect('/welcome?username={0}'.format(usernameField))

    # this loads the data the user entered into the form after the error   
    else:        
        if not username_validation(usernameField):
            return render_template('signup.html', username=usernameField,email=emailField, 
            usernameError=usernameError, passwordError=passwordError,
            passwordConfirmationError=passwordConfirmationError, emailError=emailError,)
    

@app.route("/welcome")
def welcome():
    username = request.args.get('username')
    return render_template('welcome.html', username=username and cgi.escape(username, quote=True))

if __name__ == "__main__":
    app.run()
