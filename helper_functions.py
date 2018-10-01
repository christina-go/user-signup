def text_len(text):
  textLength = len(text)

  if textLength < 3 or textLength > 20:
    return False

  else:
    return True

def no_spaces(text):
  
  if ' ' in text:
    return False
  else:
    return True

def special_chars(userEmail):

  atSignCount = int(userEmail.count("@"))
  periodCount = int(userEmail.count("."))
  if atSignCount is 1 and periodCount is 1:
    return True
  else:
    return False  


def email_validation(userEmail):

  if text_len(userEmail) and no_spaces   (userEmail) and special_chars(userEmail) ==  True:
    return True
  else:
    return False

def username_validation(userName):

  if text_len(userName) and no_spaces(userName) == True:
    return True
  else:
    return False

def password_validation(password):

  if text_len(password) and no_spaces(password) == True:
    return True

  else:
    return False

def password_match(password, passwordConfirmation):
  if password == password_confirmation:
    return True

  else:
    return False 
    

