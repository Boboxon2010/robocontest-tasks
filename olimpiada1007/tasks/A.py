n=int(input())
toq=[]
k=1
for i in range(1,n+1):
    
    toq.append(k)
    k=k+2
for i in toq:
    print(i,end=' ')