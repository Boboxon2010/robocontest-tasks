n,a,q=map(int,input().split())
list=[]
for i in range(n):
    list.append(a)
    a=a*q
for i in list:
    print(i,end=' ')
