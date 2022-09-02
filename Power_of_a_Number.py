import math
x,y,z=map(int,input().split())
res=int(math.pow(x,y))
r=res%z
print(r)