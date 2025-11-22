n=int(input())
a=str(n)
start=n//100000000
s=0
for i in a:
    i=int(i)
    if start!=0:
        s+=i
if s%2==1:
    print('yes')
else:
    print('no')