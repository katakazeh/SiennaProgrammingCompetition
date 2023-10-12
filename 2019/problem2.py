from math import floor

def sum_square(x):
  sum_square_digits = 0
  power = 0
  x = str(x)

  for digit in x:
    digit = int(digit)
    sum_square_digits += pow(digit, 2)
    power += 1;

  return sum_square_digits



val = int(input())
iterations = 0

while (val != 1 and val != 89):
  val = sum_square(val)
  iterations += 1

print(str(val) + " " + str(iterations))
