from math import factorial,exp
n=int(input())
x=float(input())
s=1
for i in range(1,n+1):
    s+=pow(x,i)/factorial(i)
print(f"{s:.8f}")