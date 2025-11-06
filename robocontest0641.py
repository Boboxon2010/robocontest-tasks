n,m=map(int,input().split())
if n==m:
    n=n*100+55
    m=m*100+56
    print(n,m)
elif n-m==1:
    n=n*100
    m=m*100+99
    print(min(n,m),max(m,n))
elif m-n==1:
    m=m*100
    n=n*100+99
    print(n,m)
elif n==9 and m==1:
    print(9,10)
else:
    print(-1)
