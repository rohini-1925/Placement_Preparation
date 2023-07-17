def sumOfMaximum(arr):
    odd=[]
    even=[]
    for i in range(len(arr)):
        if i%2==0:
            even.append(arr[i])
        else:
            odd.append(arr[i])
    even.sort()
    odd.sort()
    return even[-2]+odd[1]
n=int(input('Enter range : '))
lst=[]
for i in range(n):
    a=int(input())
    lst.append(a)
print("The sum is = ",end=" ")
print(sumOfMaximum(lst))
