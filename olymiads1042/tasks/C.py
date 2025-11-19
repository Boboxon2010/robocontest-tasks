n,k=map(int,input().split())
s=0
while n>=k:
    n=n-k
    s+=1
print(s,n)