num=int(input())
lst=list(str(num))
lst.sort()
u=list(set(lst))
u.sort()
if u==lst:
    print("Unique Number")
else:
    print("Not Unique Number")