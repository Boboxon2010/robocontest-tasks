from math import sin
n=int(input())
A,B=map(float,input().split())
x=(B-A)/n
for i in range(n+1):
    s=A+i*x
    print(f"{1-sin(s):.5f}",end=' ')
