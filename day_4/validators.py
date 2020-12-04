import re

def validate_number(val, min, max, length = 0):
  if length:
    if(len(val)) ==length and int(val) >= min and int(val) <= max:
      return True
    else:
      return False
  else:
    if int(val) >= min and int(val) <= max:
      return True
    else:
      return False

def validate_birth_year(val):
  return validate_number(val, 1920, 2002, 4)

def validate_issue_year(val):
  return validate_number(val, 2010, 2020, 4)

def validate_expiration_year(val):
  return validate_number(val, 2020, 2030, 4)

def validate_height(val):
  if 'cm' in val:
    return validate_number(val[:-2], 150, 193)
  elif 'in' in val:
    return validate_number(val[:-2], 59, 76)
  else:
    return False

def validate_hair_color(val):
  if val[0] != '#' or len(val) != 7:
    return False
  else:
    val = val[1::]
    match = re.search('[^a-f0-9]', val)
    if match is None:
      return True
    else:
      return False

def validate_eye_color(val):
  accepted = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
  if val in accepted:
    return True
  else:
    return False

def validate_passport_id(val):
  if len(val) != 9:
    return False
  else:
    match = re.match('[a-zA-Z]', val)
    if match is None:
      return True
    else:
      return False
  