N,A,B=map(int,input().split())
list=[A,B]
for i in range(N-1):
    C=A+B
    A=B
    B=C
    list.append(C)
for i in list:
    print(i,end=' ')