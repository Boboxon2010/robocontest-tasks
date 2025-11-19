n=int(input())
a=list(map(int,input().split()))
x=a.count(0)
for i in a:
    if i>x:
        x=