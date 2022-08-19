t=int(input())
for i in range(t):
    count=0
    l,r=map(int,input().split())
    for j in range(l,r+1):
        if j%10==2 or j%10==3 or j%10==9:
            count+=1
    print(count)