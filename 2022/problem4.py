def main():
  answer = list(input())

  guess_count = int(input())

  for i in range(guess_count):
    answer_copy = answer[:]
    
    guess = list(input())
    result = ['D','D','D','D','D']
    
    for g in range(len(guess)):
        if guess[g] == answer_copy[g]:
          result[g] = 'G'
          answer_copy[g] = 1

    for g in range(len(guess)):
      for a in range(len(answer_copy)):
        if guess[g] == answer_copy[a]:
          if result[g] != 'G':
            result[g] = 'Y'
            answer_copy[a] = 1
            break

    print("".join(result))
          
  # Your code for Problem 4 goes here,
    # press the >Run button to execute

    
# Include a call to your main function.
main()
