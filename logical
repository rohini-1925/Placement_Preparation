string='1C0C1C1A0B1'
res=int(string[0])
for i in range(len(string)):
    if string[i]=='A':
        res=res and int(string[i+1])
    elif string[i]=='B':
        res=res or int(string[i+1])
    elif string[i]=='C':
        res=res ^ int(string[i+1])
print(res)
