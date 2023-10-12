def main():
  n = int(input())
  a1 = 1
  max_h = 0
  max_h_a2_val = None
  for a2 in range(1, n + 2):
    h = ((n + 1 - a2) + 1) * a2 + (n - (n + 1 - a2 + 1))
    # print(h, a2)
    if h > max_h:
      max_h = h
      max_h_a2_val = a2
  print(max_h)
  print(str(a1) + " " + str(max_h_a2_val))
    # Your code for Problem 7 goes here,
    # press the >Run button to execute

    
# Include a call to your main function.
main()
