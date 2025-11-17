a,b,c=map(int,input().split())
a2=pow(a,2)
b2=pow(b,2)
c2=pow(c,2)
if a2+b2==c2 or b2+c2==a2 or a2+c2==b2:
    print('ROST')
else:
    print("YOLG'ON")