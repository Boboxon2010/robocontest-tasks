from math import*
a,b=map(int,input().split())
if ((a+b)/2)>sqrt(a*b):
    print(">")
elif ((a+b)/2)<sqrt(a*b):
    print("<")
else:
    print("=")