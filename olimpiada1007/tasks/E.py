n=int(input())
f0=1
f1=1
print(1,1,end=' ')
for i in range(2,n+1):
    f2=f1+f0
    f0=f1
    f1=f2
    print(f2,end=' ')