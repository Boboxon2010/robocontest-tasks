n=int(input())
x=float(input())
s=0
for i in range(n+1):
    s+=(pow(-1,i)*pow(x,2*i+1))/(2*i+1)
print(f"{s:.8f}")