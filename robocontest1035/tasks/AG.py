from math import*
n=int(input())
x=float(input())
s=0
for i in range(n+1):
    s+=(pow((-1),i)*pow(x,2*i))/factorial(2*i)
print(f"{s:.8f}")