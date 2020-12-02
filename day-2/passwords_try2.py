import re

def process(file):
  with open(file) as inputs:
    data = []
    for line in inputs:
      split = re.split('[- :]', line)
      data.append((int(split[0]), int(split[1]), split[2], split[4].strip()))
    return data

data = process('data.txt')
# [(min, max, letter, pw)]

def count_correct_passwords(data):
  ok = 0
  for(min, max, letter, pw) in data:
    count = pw.count(letter)
    if count >= min and count <= max:
      ok+=1
    else:
      pass
  return ok

def find_correct_position(data):
  
  new_data = [(first -1, second -1, letter, pw) for (first, second, letter, pw) in data]
  
  ok = 0
  for(first, second, letter, pw) in new_data:
    if (pw[first] == letter and pw[second] != letter) or (pw[first] != letter and pw[second] == letter):
      ok+=1
    else:
      pass
  return ok

# PART 1
part_one_count = count_correct_passwords(data)
print("The answer to the first part is {}".format(part_one_count))

# PART 2
part_two_count = find_correct_position(data)
print("The answer to the second part is {}".format(part_two_count))