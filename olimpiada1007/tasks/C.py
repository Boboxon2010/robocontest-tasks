n,a,d=map(int,input().split())
list=[]
for i in range(n):
    list.append(a)
    a=a+d
for i in list:
    print(i,end=' ')
