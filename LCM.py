x,y=map(int,input().split())
if x>y:
    gre=x
else:
    gre=y
while True:
    if gre%x==0 and gre%y==0:
        lcm=gre
        break
    gre+=1
print(lcm)