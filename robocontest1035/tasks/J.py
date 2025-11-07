A,B=map(int,input().split())
k=0
for i in range(A,B+1):
    s=pow(i,2)
    k+=s
print(k)
