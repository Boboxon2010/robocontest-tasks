n=int(input())
A0=1
for i in range(1,n+1):
    s=(A0+1)/i
    A0=s
    print(f"{s:.6f}",end=' ')