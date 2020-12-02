with open('data.txt') as file:
  data = []
  for i in file:
    in_half = i.split(':')
    rule = in_half[0].split('-')
    rest = rule[1].split(' ')
    # @line (min, max, letter, pw)
    data.append((int(rule[0]), int(rest[0]), rest[1], in_half[1].strip()))
  
  ok_pw = 0
  more_ok_pw = 0

  for (min, max, letter, pw) in data:
    count = pw.count(letter)
    if count >= min and count <= max:
      ok_pw+= 1
    else:
      pass

    if (pw[min - 1] == letter and pw[max-1] != letter) or (pw[min-1] != letter and pw[max-1] == letter):
      more_ok_pw += 1
  
  print('The solution to part 1 is {}'.format(ok_pw))
  print('The solution to part 2 is {}'.format(more_ok_pw))