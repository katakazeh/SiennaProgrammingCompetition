from itertools import permutations
from string import ascii_uppercase


def print_board(board):
  for row in board:
    row_str = ""
    for char in row:
      if char == "":
        row_str += " "
      else:
        row_str += char
    print(row_str)


def get_full(board):
  for row in board:
    if "" in row:
      return False
  return True


def get_col(board, col):
  return [row[col] for row in board]


def get_possible_letters(board, loc, col_clues, row_clues, a_loc):
  row = loc // 5
  col = loc % 5
  used_letters = {char for row in board for char in row}
  unused_letters = set(ascii_uppercase[:-1]).difference(used_letters)

  if loc == a_loc:
    return "A"

  row_possible_letters = set()
  # Get set of letters valid by row clues
  if col > 0:
    if row_clues[row][0] in board[row]:
      if row_clues[row][1] in used_letters:
          return set()
      if col == 4:
        # One possible letter.
        row_possible_letters.add(row_clues[row][1])
      else:
        row_possible_letters = unused_letters
    else:
      if row_clues[row][0] in used_letters:
        return set()
      if col == 3:
        # One possible letter.
        row_possible_letters.add(row_clues[row][0])
      elif col == 4:
        return set()
      else:
        row_possible_letters = unused_letters
  else:
    row_possible_letters = unused_letters

  # Get set of letters to be valid by col clues.
  col_possible_letters = set()
  if row > 0:
    if col_clues[col][0] in get_col(board, col):
      if col_clues[col][1] in used_letters:
        return set()
      if row == 4:
        # One possible letter.
        col_possible_letters.add(col_clues[col][1])
      else:
        col_possible_letters = unused_letters
    else:
      if col_clues[col][0] in used_letters:
        return set()
      if row == 3:
        # One possible letter.
        col_possible_letters.add(col_clues[col][0])
      elif row == 4:
        return set()
      else:
        col_possible_letters = unused_letters
  else:
    col_possible_letters = unused_letters

  return row_possible_letters.intersection(col_possible_letters)


def solve_board(board, loc, col_clues, row_clues, a_loc):
  for letter in get_possible_letters(board, loc, col_clues, row_clues, a_loc):
    next_board = [row[:] for row in board]
    next_board[loc // 5][loc % 5] = letter
    if get_full(next_board):
      return next_board
    else:
      solution = solve_board(next_board, loc + 1, col_clues, row_clues, a_loc)
      if solution:
        return solution
  return False


def main():
  col_clues = []
  row_clues = []
  a_loc = []

  col_clues.append(input())
  for _ in range(5):
    row_clues.append(input())
  col_clues.append(input())
  a_loc_str = input()
  a_loc = 5 * int(a_loc_str[0]) + int(a_loc_str[-1])

  transposed_col_clues = []
  for c in range(len(col_clues[0])):
    transposed_col_clues.append([col_clues[0][c], col_clues[1][c]])

  start_board = [["" for _ in range(5)] for _ in range(5)]
  print_board(solve_board(start_board, 0, transposed_col_clues, row_clues, a_loc))

main()
