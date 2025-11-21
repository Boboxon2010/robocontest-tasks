x,y=map(int,input().split())
n=x%100
b=y%100
x1=2022-x
y1=2022-y
if n<b:
    print(x1,y1)
else:
    print('NO')