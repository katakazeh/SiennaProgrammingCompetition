from math import factorial


bounds = input().split(' ')
min_n = int(bounds[0])
max_n = int(bounds[1])

bottom = factorial(min_n-1)/(factorial(max_n-1)*factorial(min_n-max_n))
bottom *= min_n
print("1/" + str(int(bottom)))
