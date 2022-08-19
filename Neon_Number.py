n=int(input())
sq=n**2
s=0
for i in str(sq):
    s=s+int(i)
r=s**2
if r==sq:
    print("Neon Number")
else:
    print("Not Neon Number")