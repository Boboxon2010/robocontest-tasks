from math import*
n=int(input())
s=1
for i in range(1,n+1):
    s+=1/factorial(i)
print(f"{s:.8f}")