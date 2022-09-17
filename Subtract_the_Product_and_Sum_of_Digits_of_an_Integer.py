num=int(input())
s=0
p=1
while num>0:
    res=num % 10
    s += res
    p *= res
    num = num // 10
print(p-s)