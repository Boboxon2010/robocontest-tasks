a=int(input())
if a%3==0:
    print(3)
elif a%3!=0 and a%5==0:
    print(5)
elif a%5!=0 and a%7==0:
    print(7)
elif a%7!=0:
    print(-1)