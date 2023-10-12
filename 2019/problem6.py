strings = input()
addend1, addend2, sum = strings.split(" ")
letters = []
for letter in strings:
  if letter == " ":
    continue
  if letter not in letters:
    letters.append(letter)

for letter in letters:
  exec(letter + "= -1")
print(letters)
