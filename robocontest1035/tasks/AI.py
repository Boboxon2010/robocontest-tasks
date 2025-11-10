n=int(input())
x=float(input())
s=0
for i in range(1,n+1):
    s+=pow((-1),i-1)*pow(x,i)/i
print(f"{s:.8f}")