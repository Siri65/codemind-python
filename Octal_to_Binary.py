t=int(input())
for i in range(t):
    num=input()
    t=int(num,8)
    r=bin(t)
    print(r[2:])