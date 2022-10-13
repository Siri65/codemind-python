num=int(input())
lst=list(str(num))
l=len(lst)
f=lst[0]
if f==0 or l<10:
    print("Invalid")
else:
    print("Valid")