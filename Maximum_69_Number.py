n = input()
count=0
ans=''
for i in n:
    if i == '6' and count != 1:
        count += 1
        ans = ans + '9'
    else:
        ans  = ans  + i
        
print(ans)