n=int(input())
s=0
while True:
    s=0
    while n>0:
        res=n%10
        s=s+res
        n=n//10
    if s<=9:
        print(s)
        break
    else:
        n=s