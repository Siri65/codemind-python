num=int(input())
f=0
for i in range(num):
    if i*(i+1)==num:
        f=1
        break
if f==1:
    print("YES")
else:
    print("NO")