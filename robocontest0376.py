x=int(input())
if x<=12:
    if x<=2 or x==12:
        print("Winter")
    elif x<=5:
        print("Spring")
    elif x<=8:
        print("Summer")
    else:
        print("Autumn")
else:
    print("Error")