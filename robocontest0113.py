x=int(input())
if x>=38:
    for i in range(x,x+4):
        if i%5==0:
            if abs(i-x)<3:
                x=i
            break
print(x)