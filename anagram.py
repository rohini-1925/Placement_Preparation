string1=str(input())
string2=str(input())
s1=''.join(sorted(string1))
s2=''.join(sorted(string2))
if s1==s2:
    print("Yes")
else:
    print("No")
