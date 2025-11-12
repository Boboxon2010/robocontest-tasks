n=int(input())
f1=1
f2=1
print(1,1,end=' ')
for i in range(3,n+1):
    s=f1+f2
    f1=f2
    f2=s
    print(s,end=' ')