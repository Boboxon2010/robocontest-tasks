a=int(input())
if a%3==0:
    print(3,end=' ')
if a%5==0:
    print(5,end=' ')
if a%7==0:
    print(7,end=' ')
if a%7!=0 and a%5!=0 and a%3!=0:    
    print(-1)