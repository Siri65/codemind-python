n=int(input())
c=0
n1=0
n2=1
res=0
if n==1:
    print(n1)
else:
    while c<n:
        print(n1,end=" ")
        res=n1+n2
        n2=n1
        n1=res
        c+=1
        