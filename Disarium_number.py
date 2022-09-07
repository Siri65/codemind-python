n=input()
l=len(n)
n=int(n)
c=n
res=0
while n!=0:
    rem=n%10
    res=res+pow(rem,l)
    n=n//10
    l-=1
if c==res:
    print("True")
else:
    print("False")