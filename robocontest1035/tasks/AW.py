n=int(input())
a1=1
a2=2
a3=3
print(1,2,3,end=' ')
for i in range(4,n+1):
    s=a3+a2-2*a1
    a4=s
    a1=a2
    a2=a3
    a3=a4
    print(s,end=' ')