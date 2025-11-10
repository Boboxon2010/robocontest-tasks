n=int(input())
a=float(input())
p=0
for i in range(n+1):
    p+=pow((-1),i)*pow(a,i)
p=int(p)
print(f"{p:.2f}")


