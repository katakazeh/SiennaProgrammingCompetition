import math
def main():
  binstr = input()
  denom = int(math.pow(2, len(binstr)))-1
  num = 0
  for i in range(len(binstr)):
    if binstr[i] == "1":
      num += int(math.pow(2, len(binstr)-i-1))
  gcd = math.gcd(denom, num)
  num = int(num/gcd)
  denom = int(denom/gcd)
  print(str(num) + "/" + str(denom))
    # Your code for Problem 3 goes here,
    # press the >Run button to execute

    
# Include a call to your main function.
main()
