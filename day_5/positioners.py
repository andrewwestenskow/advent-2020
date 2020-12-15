from math import floor, ceil

def handle_lower_half_rows(row_limits):
  # F - MIN STAYS THE SAME
  min_row, max_row, min_column, max_column = row_limits
  new_max = max_row - ceil((max_row - min_row) / 2)
  return (min_row, new_max, min_column, max_column)

# 0 - 127
# F = 0 - 63
# B = 32 - 63
# F = 32 - 47
# B = 40 - 47
# B = 44 - 47
# F = 44 - 45
# F = 44 - 44

def handle_upper_half_rows(row_limits):
  # B - MAX STAYS THE SAME
  min_row, max_row, min_column, max_column = row_limits
  new_min = max_row - floor((max_row - min_row) / 2)
  return (new_min, max_row, min_column, max_column)

def handle_lower_half_columns(row_limits):
  min_row, max_row, min_column, max_column = row_limits
  new_max = max_column - ceil((max_column - min_column) / 2)
  return (min_row, max_row, min_column, new_max)


def handle_upper_half_columns(row_limits):
  min_row, max_row, min_column, max_column = row_limits
  new_min = max_column - floor((max_column - min_column) / 2)
  return (min_row, max_row, new_min, max_column)