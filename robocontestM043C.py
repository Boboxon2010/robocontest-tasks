t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    if len(a)==len(set(a)):
        print("YES")
    else:
        print("NO")           
