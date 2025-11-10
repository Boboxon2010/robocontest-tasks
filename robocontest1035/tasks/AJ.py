n=int(input())
x=float(input())
s=0
k=-1
p=1
for i in range(1,n+1):
    k=k*(-1)
    p=p*x
    s+=k*(p/i)
print(f"{s:.8f}")