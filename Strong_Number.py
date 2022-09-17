num=int(input())
p=num
s=0
while num>0:
    tmp=1
    res=num%10
    for i in range(1, res+1):
        tmp = tmp*i
    s+=tmp
    num=num//10
if s==p:
    print("The number",p,"is a strong number")
else:
    print("The number",p,"is not a strong number")