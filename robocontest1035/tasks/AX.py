n,k=map(int,input().split())
s=0
for i in range(1,n+1):
    s+=pow(i,k)
print(f"{s:.2f}")