a,b,c=map(int,input().split())
if a%2==0:
    print(a,end=' ')
if b%2==0:
    print(b,end=' ')
if c%2==0:
    print(c,end=' ')
if a%2!=0 and b%2!=0 and c%2!=0:
    print(-1)