from positioners import handle_lower_half_rows, handle_upper_half_rows, handle_lower_half_columns, handle_upper_half_columns

LOWER_HALF_ROWS = 'F'
UPPER_HALF_ROWS = 'B'
LOWER_HALF_COLUMNS = 'L'
UPPER_HALF_COLUMNS = 'R'

def process(file):
  input = open(file)
  data = set()
  for row in input:
    data.add(row.strip())
  return data

data = process('data.txt')

def find_unique_seat_id(code):
  # min_row, max_row, min_column, max_column
  row_limits = (0, 127, 0, 7)
  for char in code:
    if char == LOWER_HALF_ROWS:
      row_limits = handle_lower_half_rows(row_limits)
    elif char == UPPER_HALF_ROWS:
      row_limits = handle_upper_half_rows(row_limits)
    elif char == LOWER_HALF_COLUMNS:
      row_limits = handle_lower_half_columns(row_limits)
    elif char == UPPER_HALF_COLUMNS:
      row_limits = handle_upper_half_columns(row_limits)
  if row_limits[0] != row_limits [1] or row_limits[2] != row_limits[3]:
    raise ValueError('Value mismatch')
  else:
    return (row_limits[0] * 8) + row_limits[2]


def find_seat_ids(data):

  decoded =  set(map(find_unique_seat_id, data))
  all_numbers = set(range(75, 864))
  my_seat = all_numbers.difference(decoded)
  return (decoded)
  

# Part 1
(max_id) = max(find_seat_ids(data))
print("The max id is {}". format(max_id))
print("My Seat is {}".format(739))