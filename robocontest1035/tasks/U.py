n=int(input())
a=float(input())
k=1
p=1
for i in range(1,n+1):
    p=p*a
    k+=p
print(F"{k:.2f}")