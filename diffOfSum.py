def diffOfSum(n,m):
    divid=0
    nodivid=0
    for i in range(1,m+1):
        if i%n==0:
            divid=divid+i
        else:
            nodivid=nodivid+i
    return abs(nodivid-divid)
a=int(input('Enter range : '))
b=int(input("Enter divisor : "))
print("The difference is = ",end=" ")
print(diffOfSum(b,a))
