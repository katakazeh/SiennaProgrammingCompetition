itemskey = {"HAT":0, "SHIRT":1, "PANTS":2, "SOCKS":3}
COLORS = ["GREEN","RED", "BLUE", "YELLOW"]

def checkCombo(c1, i1, c2, i2, restriction):
  if restriction[itemskey[i1]] == c1 and restriction[itemskey[i2]] == c2:
    return False
  return True

def main():
    # Your code for Problem 5 goes here,
    # press the >Run button to execute
  x = 256
  
  n = int(input())

  restrictions = []
  for i in range(n):
    restrictions.append(input().split())
  
  for hat in COLORS:
    for shirt in COLORS:
      for pants in COLORS:
        for socks in COLORS:
          hasFailed = False
          for r in restrictions:
            if not checkCombo(r[0], r[1], r[2], r[3], [hat, shirt, pants, socks]):
              hasFailed = True

          if hasFailed:
            x -= 1

  print(x)
# Include a call to your main function.
main()
