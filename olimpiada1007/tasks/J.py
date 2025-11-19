# n=int(input())
# a=list(map(int,input().split()))
# juft=[]
# toq=[]
# for i in range(0,n,2):
#     juft.append(a[i])
# for i in range(1,n+1,2):
#     toq.append(a[i])    
# teskari_toq=[]
# for i in juft:
#     print(i,end=' ')
# for i in toq:
#     teskari_toq.insert(0,i)
# for i in teskari_toq:
#     print(i,end=' ')

n = int(input())
a = list(map(int, input().split()))

# Juft indekslar
for i in range(0, n, 2):
    print(a[i], end=' ')

# Toq indekslar teskari
for i in range(n-1 if n % 2 == 0 else n-2, 0, -2):
    print(a[i], end=' ')
