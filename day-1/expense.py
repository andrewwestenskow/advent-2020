with open('expense.txt', 'r') as file:
  num_1 = 0
  num_2 = 0
  num_3 = 0
  data = []
  for l in file:
    data.append(int(l.strip()))
  for i in range(0, len(data) - 1):
    for j in range(i + 1, len(data ) - 1):
      for f in range(j + 1, len(data) - 1):
        if data[i] + data[j] + data[f] == 2020:
          print('FOUND')
          num_1 = data[i]
          num_2 = data[j]
          num_3 = data[f]
          break
  print(num_1 * num_2 * num_3)
