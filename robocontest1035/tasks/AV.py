n=int(input())
a1=1
a2=2
print(f"{a1:.6f}",f"{a2:.6f}",end=' ')
for i in range(3,n+1):
    a3=(a1+2*a2)/3
    a1=a2
    a2=a3
    print(f"{a3:.6f}",end=' ')