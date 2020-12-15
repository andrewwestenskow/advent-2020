from functools import reduce

def process(file):
  input = open(file).read().split('\n\n')
  return input

input= process('data.txt')

def get_all_yes():
  formatted = list(map(lambda group: set(group.replace('\n', '')), input))
  sum = 0
  for group in formatted:
    sum += len(group)
  return sum

def get_everyone_yes():
  def to_sets(group):
    individuals = list(map(lambda person: set(person), group.split('\n')))
    return individuals
  
  def to_common(group):
    first_set = group.pop()
    common = first_set.intersection(*group)
    return len(common)

  formatted = list(map(to_sets, input))
  all_common = list(map(to_common, formatted))
  sum = reduce(lambda x,y: x+y, all_common)
  return sum


# Part 1
all_yes = get_all_yes()
print('The total number of yesess is {}'.format(all_yes))

# Part 2
everyone_yes = get_everyone_yes()
print('The updated count is {}'.format(everyone_yes))