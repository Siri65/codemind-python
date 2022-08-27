import math
n=int(input())
res=int(math.sqrt(n))
if int(res*res)==n:
    print("True")
else:
    print("False")