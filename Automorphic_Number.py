num=int(input())
l=len(str(num))
sq=num**2
last=sq%pow(10,l)
if last==num:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")