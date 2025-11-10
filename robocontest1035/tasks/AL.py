n=int(input())
x=float(input())
s=0
k=-1
p=1
for i in range(n+1):
    k=k*(-1)
    p*=x
    s+=k*p/(2*i+1)
    p=p*x
print(f"{s:.8f}")

