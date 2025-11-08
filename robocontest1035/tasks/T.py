n=int(input())
a=float(input())
k=1
for i in range(1,n+1):
    k+=pow(a,i)
print(f"{k:.2f}")