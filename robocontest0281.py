n=int(input())
a=list(map(int,input().split()))
x=a.count(0)
for i in a:
    if a.count(i)>x:
        x=a.count(i)

print(n-x)
