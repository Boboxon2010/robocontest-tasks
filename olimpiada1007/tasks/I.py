n=int(input())
a=list(map(int,input().split()))
empty=[]
for i in a:
    if i%2==0:
        empty.append(i)
empty1=[]
for i in empty:
    empty1.insert(0,i)
for i in empty1:
    print(i,end=' ')
z=len(empty1)
print()
print(z)