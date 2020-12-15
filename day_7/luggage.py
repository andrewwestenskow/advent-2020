import re

def process(file):
  input = open(file).read().split('\n')
  def process_bag(bag):
    parent, contents = bag.split(' bags contain ')
    
    def clean_list(str):
      if str in {'', ' ', '.', 's', 's.'}:
        return False
      else:
        return True

    contains = set(map(lambda str: str.strip('.'), list(filter(clean_list ,re.split('[0-9,] | bag', contents)))))
    return {"parent": parent, "contents": contains}
  
  rules = list(map(process_bag, input))
  return rules

rules = process('data.txt')

for rule in rules:
  print(rule)