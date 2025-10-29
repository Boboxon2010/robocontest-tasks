a,b,c=map(int,input().split())
s=0
if a%2==0:
    s+=a//2
else:
    a%2!=0
    s+=a//2+1
if b%2==0:
    s+=b//2
else:
    b%2!=0
    s+=b//2+1
if c%2==0:
    s+=c//2
else:
    c%2!=0
    s+=c//2+1
print(s)