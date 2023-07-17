n=int(2147483647)
lst=list("{:032b}".format(n))
print(lst)
binary=''
for i in range(len(lst)):
    if lst[i]=='0':
        binary=binary+''.join('1')
    else:
        binary=binary+''.join('0')
print(int(binary,2))
