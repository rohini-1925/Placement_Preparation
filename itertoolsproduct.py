from itertools import product
A=list(map(int,input().split()))
B=list(map(int,input().split()))
lst=list(product(A,B))
print(*lst,sep=' ')
