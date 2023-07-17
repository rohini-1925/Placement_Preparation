from itertools import permutations
string,k=input().split()
lst=list(string)
string=''.join(sorted(lst))
k=int(k)
lst=list(permutations(string,k))
for i in lst:
    print(*i,sep='')
