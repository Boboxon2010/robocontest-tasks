n=int(input())
list=list(map(int,input().split()))
z=-1
for i in range(1,n-1):
    if list[i]>list[i-1] and list[i]>list[i+1]:
        if z==-1 or list[i]<z:
            z=list[i]
print(z)

