n=int(input())
r=n**2
rev=0
while n>0:
    rem=n%10
    rev=(rev*10)+rem
    n=n//10
t=rev**2
tmp=0
while t>0:
    remi=t%10
    tmp=(tmp*10)+remi
    t=t//10
if r==tmp:
    print("True")
else:
    print("False")