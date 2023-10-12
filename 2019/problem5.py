string = input()
middle = len(string) // 2
# Find all letters in string. 
letters = []
for letter in string:
  if letter not in letters:
    letters.append(letter)
left_string = string[:middle]
if len(string) % 2 == 0:
  right_string = string[middle:]
else:
  right_string = string[middle+1:]
imperfect = False
status = 0
for letter in letters:
  if left_string.count(letter) > right_string.count(letter):
    status -= 1
    imperfect = True
  elif left_string.count(letter) < right_string.count(letter):
    status += 1
    imperfect = True

print(string)
if not imperfect:
  print("PERFECTLY BALANCED")  # As all things should be
elif status == 0:
  print("BALANCED")
elif status < 0:
  print("LEFT UNBALANCED")
else:
  print("RIGHT UNBALANCED")
