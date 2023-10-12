x, y = input().split()
array=[]
z=([])
x=int(x)
y=int(y)


while(x!=0):

  z=int(x%y)
  
  x=int(x/y)
  array.append(hex(z)[2:])
 
  print(str(x) + " " + str(z))

res = array[::-1]
print("".join([str(x) for x in res]))
