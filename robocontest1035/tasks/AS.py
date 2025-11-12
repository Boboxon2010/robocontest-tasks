n=int(input())
A0=2
for i in range(n):
    s=2+1/A0
    A0=s
    print(f"{s:.6f}",end=' ')