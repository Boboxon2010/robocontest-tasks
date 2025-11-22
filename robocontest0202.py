n=int(input())
a=str(n)
s=0
for i in a:
    i=int(i)
    if i==0:
        s+=6
    elif i==1:
        s+=2
    elif i==2:
        s+=5
    elif i==3:
        s+=5
    elif i==4:
        s+=4
    elif i==5:
        s+=5
    elif i==6:
        s+=6
    elif i==7:
        s+=3
    elif i==8:
        s+=7
    elif i==9:
        s+=6
print(s)
    