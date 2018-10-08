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
