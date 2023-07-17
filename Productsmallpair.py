sum1=int(input())
arr=list(map(int,input().split()))
arr.sort()
if len(arr)<2:
    print('-1')
elif sum(arr[-2:])<=sum1:
    print(arr[-1]*arr[-2])
else: 
    print('0')
