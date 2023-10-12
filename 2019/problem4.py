num_rows, num_cols = [int(i) for i in input().split(' ')]
grid = [list(input()) for _ in range(num_rows)]
num_words = int(input())
words = [input() for _ in range(num_words)]
found = set()

for r, row in enumerate(grid):
  if len(found) == len(words):
      break
  for c, char in enumerate(row):
    if len(found) == len(words):
      break
    for word in words:
      if word in found:
        continue
      if word[0] == char:
        if num_cols >= c + len(word):
          # Check if word is written horizontally forwards.
          i = 1
          while row[c + i] == word[i]:
            i += 1
            if i == len(word):
              found.add(word)
              break
        # Check if word is written horizontally backwards.
        if word in found:
          continue
        if c >= len(word) - 1:
          i = 1
          while row[c - i] == word[i]:
            i += 1
            if i == len(word):
              found.add(word)
              break
        # Check if word is written vertically downwards.
        if word in found:
          continue
        if num_rows > r + len(word):
          i = 1
          while grid[r + i][c] == word[i]:
            i += 1
            if i == len(word):
              found.add(word)
              break
        # Check if word is written vertically upwards.
        if word in found:
          continue
        if r >= len(word) - 1:
          i = 1
          while grid[r - i][c] == word[i]:
            i += 1
            if i == len(word):
              found.add(word)
              break
        # Check if word is written diagonally top-left to bottom-right
        if word in found:
          continue
        if num_rows >= r + len(word) and num_cols >= c + len(word):
          i = 1
          while grid[r + i][c + i] == word[i]:
            i += 1
            if i == len(word):
              found.add(word)
              break
        # Check if word is written diagonally bottom-right to top-left
        if word in found:
          continue
        if r >= len(word) - 1 and c >= len(word) - 1:
          i = 1
          while grid[r - i][c - i] == word[i]:
            i += 1
            if i == len(word):
              found.add(word)
              break
        # Check if word is written diagonally bottom-left to top-right
        if word in found:
          continue
        if r >= len(word) - 1 and num_cols >= c + len(word):
          i = 1
          while grid[r - i][c + i] == word[i]:
            i += 1
            if i == len(word):
              found.add(word)
              break
        # Check if word is written diagonally top-right to bottom-left
        if word in found:
          continue
        if num_rows >= r + len(word) and c >= len(word) - 1:
          i = 1
          while grid[r + i][c - i] == word[i]:
            i += 1
            if i == len(word):
              found.add(word)
              break

for word in words:
  if word in found:
    print(f"{word} FOUND")
  else:
    print(f"{word} NOT FOUND")
