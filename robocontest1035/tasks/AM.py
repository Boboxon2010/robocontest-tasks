n=int(input())
x=float(input())
s=x
k=1
for i in range(n):
    
    s+=(2*i-1)*(pow(x,2*i+1))/(2*i)*(2*i+1)
    
print(f"{s:.8f}")
