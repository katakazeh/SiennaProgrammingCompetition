from copy import deepcopy


def print_matrix(matrix):
  for row in matrix:
    print("".join(row))


def backtrack(board):
  solutions = get_neighbors(board)
  for solution in solutions:
    if (get_final(solution)):
      return solution
    return backtrack(solution)


def get_neighbors(board):
  next_state_boards = []
  test_board = board
  for r, row in enumerate(board):
    for s, square in enumerate(row):
      if square == "O":
        for char in ["B", "W"]:
          test_board[r][s] = char
          if get_valid(test_board):
            next_state_boards.append(deepcopy(test_board))
        test_board[r][s] = "O"
  return next_state_boards


def get_final(board):
  for i in range(len(board)):
    for j in range(len(board[i])):
      if (board[i][j] == "O"):
        return False
  return True


def check_array(arr):
  dim = len(arr)
  for i in range(dim - 2):
    arr_slice = arr[i:i+3]
    if (len(set(arr_slice)) == 1 and arr_slice[0] != "O"):
      return False
  return True


def get_valid(board):
  for i in range(len(board)):
    if not check_array(board[i]):
      return False
    if not check_array([board[r][i] for r in range(len(board))]):
      return False
  return True
  

dim = int(input())
board = []

for i in range(dim):
  board.append(list(input()))

print(backtrack(board))
# print_matrix(backtrack(board))
