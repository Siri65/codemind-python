n=int(input())
m=int(input())
add=0
s=0
for i in range(1,n):
    if n%i==0:
        add+=i
for j in range(1,m):
    if m%j==0:
       s+=j 
if add==m and s==n:
    print("Amicable")
else:
    print("Not Amicable")