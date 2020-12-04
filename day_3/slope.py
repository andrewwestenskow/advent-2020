def process(file):
  data = []
  input = open(file)
  for line in input:
    data.append(line.strip())
  return data

data = process('data.txt')

def handle_index_change(current, step, max = 31):
  if current < max - step:
    return current + step
  else:
    return (current + step) - max

def find_trees(data, step):
  index = 0
  count = 0
  for row in data:
    if row[index] == '#':
      count +=1
    else:
      pass
    index = handle_index_change(index, step)
  return count
  
# Part 1
tree_count = find_trees(data, 3)
print('The number of trees is {}'.format(tree_count))

# Part 2
tree_count_1 = find_trees(data, 1)
tree_count_3 = find_trees(data, 3)
tree_count_5 = find_trees(data, 5)
tree_count_7 = find_trees(data, 7)
tree_count_evens = find_trees(data[::2], 1)

print('Step 1: The number of trees is {}'.format(tree_count_1))
print('Step 3: The number of trees is {}'.format(tree_count_3))
print('Step 5: The number of trees is {}'.format(tree_count_5))
print('Step 7: The number of trees is {}'.format(tree_count_7))
print('Step evens: The number of trees is {}'.format(tree_count_evens))

print('The multiplied number is {}'.format(tree_count_1* tree_count_3 *tree_count_5 * tree_count_7 *tree_count_evens))