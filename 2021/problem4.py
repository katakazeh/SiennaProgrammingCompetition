from math import pow
def find_numbers(min_n, max_n):
  numbers = []
  for i in range(min_n, max_n+1):
    string_num = str(i)
    sums = 0
    power = len(string_num)
    for digit in string_num:
      sums += pow(int(digit), power)
    if sums == i:
      numbers.append(i)
  return numbers

bounds = input().split(' ')
min_n = int(bounds[0])
max_n = int(bounds[1])

print(min_n, max_n)
numbers = find_numbers(min_n, max_n)
print(len(numbers))
for number in numbers:
  print(number)
