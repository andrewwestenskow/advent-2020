import re
from validators import validate_birth_year, validate_issue_year, validate_expiration_year, validate_height, validate_hair_color, validate_eye_color, validate_passport_id

required_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

def process_fields(file):
  input = open(file).read().split("\n\n")
  data = []
  for line in input:
    to_return = set()
    split_line = re.split('[: \n]', line)
    for char in split_line:
      if char in required_fields:
        to_return.add(char)
      else:
        pass
    data.append(to_return)
    
  return data

  

def process_values(file):
  input = open(file).read().split("\n\n")
  data = []
  for line in input:
    split_line = list(filter(lambda stat: ("cid" not in stat), re.split('[ \n]', line)))
    if len(split_line) == 7:
      d = {}
      for line in split_line:
        key_value = line.split(':')
        d[key_value[0]] = key_value[1]
      data.append(d)
    else:
      pass
  return data

data = process_fields('data.txt')

values = process_values('data.txt')

def find_approved_passports():
  count = 0
  for passport in data:
    if len(required_fields.difference(passport)) == 0:
      count += 1
    else:
      pass
  return count

def validate_passport_data():
  count = 0
  for passport in values:
    validated = True
    for key in passport:
      allowed = {
        'byr': validate_birth_year,
        'iyr': validate_issue_year,
        'eyr': validate_expiration_year,
        'hgt': validate_height,
        'hcl': validate_hair_color,
        'ecl': validate_eye_color,
        'pid': validate_passport_id
      }.get(key, lambda val: False)(passport[key])
      if allowed == True:
        pass
      else:
        validated = False
        break
    if validated == True:
      count += 1
    else:
      pass
  return count
      

#PART 1
approved_count = find_approved_passports()
print("The number of approved passports is {} out of {}".format(approved_count, len(data)))

#PART 2
validated_count = validate_passport_data()
print("The number of validated passports is {} out of {}".format(validated_count, len(data)))