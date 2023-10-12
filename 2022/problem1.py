rank = {
  "MARSHALL" : 1,
  "GENERAL" : 2,
  "COLONEL" : 3,
  "MAJOR" : 4,
  "CAPTAIN" : 5,
  "LIEUTENANT" : 6,
  "SERGEANT" : 7,
  "MINER" : 8,
  "SCOUT" : 9,
  "SPY" : 10
}


def main():
  attacking = input()
  defending = input()
  if defending == "FLAG":
    print("FLAG REMOVED")
  elif defending == "BOMB":
    if attacking == "MINER":
      print("BOMB REMOVED")
    else:
      print(attacking + " REMOVED")
  elif attacking == defending:
    print("BOTH REMOVED")
  elif attacking == "SPY" and defending == "MARSHAL":
    print("MARSHAL REMOVED")
  elif attacking > defending:
    print(attacking + " REMOVED")
  else:
    print(defending + " REMOVED")
    # Your code for Problem 1 goes here,
    # press the >Run button to execute

    
# Include a call to your main function.
main()
