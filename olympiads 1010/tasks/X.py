#a,b,c bir satrda  sonlar berilgan a noldan farqli, dekiminatdan foydalanib "Ax^2+Bx+C=0" kvadrat tenglamaning ild`izlarini nechta.`
import math 
a,b,c=map(int,input().split())
D=b**2-4*a*c
if D<0:
    print("YOLG'ON")
elif D==0:
    print('ROST')
else:
    print("ROST")
