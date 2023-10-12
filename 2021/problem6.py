target = int(input())

def evaluate_solution(solution):
  sum_ = 0
  nextsign = 1
  smushsum = 0
  for val in solution:
    if (isinstance(val, int)):
      smushsum *= 10
      smushsum += val
    else:
      if val != '/':
        sum_ += nextsign * smushsum
        if val == '-':
          nextsign = -1
        else:
          nextsign = 1
        smushsum = 0 

  sum_ += nextsign * smushsum       
  return sum_


# print(evaluate_solution([1, "+", 2, "/", 3, "-", 4, "+", 5, "/", 6]))

solutions = []

for i1 in ['+','-','/']:
  for i2 in ['+', '-', '/']:
    for i3 in ['+', '-', '/']:
      for i4 in ['+', '-', '/']:
        for i5 in ['+', '-', '/']:
          for i6 in ['+', '-', '/']:
            for i7 in ['+', '-', '/']:
              for i8 in ['+', '-', '/']:
                possible_solution = [1,i1,2,i2,3,i3,4,i4,5,i5,6,i6,7,i7,8,i8,9]
                if evaluate_solution(possible_solution) == target:
                  solutions.append(possible_solution)


def make_human(solutions):
  newsolutions = []
  for solution in solutions:
    newsolution = [0 for i in range(len(solution))]
    
    i = 0
    x = 0

    while i < len(solution):
      if solution[i] == '/':
        newsolution[x - 1] *= 10
        newsolution[x - 1] += solution[i + 1]
        i += 1
        x -= 1
      elif (isinstance(solution[i], int)):
        newsolution[x] += solution[i]
      else:
        newsolution[x] = solution[i]
      
      i += 1
      x += 1

    i = len(newsolution) - 1
    while i > 0:
      if (newsolution[i] == 0):
        newsolution.pop()
      else:
        break
      i -= 1

    newsolutions.append(newsolution)

  return newsolutions


def cmp_to_key(mycmp):
  class K:
    def __init__(self, obj, *args):
        self.obj = obj
    def __lt__(self, other):
        return mycmp(self.obj, other.obj) < 0
    def __gt__(self, other):
        return mycmp(self.obj, other.obj) > 0
    def __eq__(self, other):
        return mycmp(self.obj, other.obj) == 0
    def __le__(self, other):
        return mycmp(self.obj, other.obj) <= 0
    def __ge__(self, other):
        return mycmp(self.obj, other.obj) >= 0
    def __ne__(self, other):
        return mycmp(self.obj, other.obj) != 0
  return K


def compare(s1, s2):
  for i in range(len(s1)):
    if (isinstance(s1[i], int)):
      if (s1[i] < s2[i]):
        return -1
      elif (s1[i] > s2[i]):
        return 1

  for i in range(len(s1)):
    if(s1[i] == "-" and s2[i] == "+"):
      return 1
    elif (s1[i] == "+" and s2[i] == "-"):
      return -1

  return 0

  # if s1 < s2:
  #   return -1
  # elif s1 > s2:
  #   return 1
  # else:
  #   return 0
  
# print(solutions)
# print(make_human(solutions))

nsolutions = sorted(make_human(solutions), key=cmp_to_key(compare))


if len(nsolutions) == 0:
  print("NO SOLUTIONS FOUND")
else:
   for solution in nsolutions:
      for digit in solution:
        print(digit, end="")
      print()
