n=int(input ())
a=list(map(int,input().split()))
empty=[]
for i in a:
    if i%2!=0:
        empty.append(i)
son=len(empty)
for i in empty:
    print(i,end=' ')
print()
print(son)