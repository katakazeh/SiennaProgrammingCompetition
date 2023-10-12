


one, sub1, two, sub2, three, sub3=input().split()


q=int(sub1)
w=int(sub2) 
e=int(sub3)
one=int(one)
two=int(two)
three=int(three)



q=100 - q #Runner 1's distance
w=100 - w #Runner 2's distance
e=100 - e #Runner 3's distance

a=q/one
s=w/two
d=e/three

speed_to_run_num = {a:1,s:2,d:3}
distance
speeds = [a,s,d]
speeds = sorted(speeds)
if (speeds[0] == speeds[1]) and (speeds[1] == speeds[2]):
  sorted([sub1,sub2,sub3])

if a != s and s != d and a != d:
 # max_time = 

  if (a>s) and (a>d):
    first=1
  if (s>a) and (s>d):
    first=2
  if (d>a) and (d>s):
    first=3


  if (a>s) and (a<d):
    second=1
  if (a<s) and (a>d):
   second=1
  if (s>a) and (s<d):
   second=2
  if (s<a) and (s>d):
   second=2
  if (d>a) and (d<s):
   second=3
  if (d<a) and (d>s):
   second=3




  if (a<s) and (a<d):
    last=1
  if (s<a) and (s<d):
    last=2
  if (d<a) and (d<s):
    last=3

  print(last, second, first)
if (a==s) | (a==d) | (d==s):
  if (a==s) and a < d:
    if sub1<sub2:
      print(1,2,3)
    else:
      print(2,1,3)
  if (a==s) and a > d:
    if sub1<sub2:
      print(3,1, 2)
    if sub1>sub2:
      print(3,2,1)
  if (s==d) and a < s:
    if sub2<sub3:
      print(1,2,3)
    else:
      print(1,3,2)
  if (s==d) and a > s:
    if sub2<sub3:
      print(2, 3,1)
    else:
      print(3,2,1)
  if (a==d) and a < s:
    if sub1<sub3:
      print(1, 3, 2)
    else:
      print(3, 1, 2)
  if (a==d) and a > s:
    if sub1<sub3:
      print(2, 1, 3)
    else:
      print(2, 3, 1)
  if (a==s) and (a==d) and (d==s):
    



  






