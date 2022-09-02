x,y=map(int,input().split())
s=0
if x>y:
    s=y
else:
    s=x
for i in range(1,s+1):
    if x%i==0 and y%i==0:
        hcf=i
print(hcf)