n=int(input())
a=n//100000
b=(n//10000)%10
c=(n//1000)%10
d=(n//100)%10
e=(n//10)%10
f=n%10
if (a+b+c)==(d+e+f):
    print("YES")
else:
    print("NO")