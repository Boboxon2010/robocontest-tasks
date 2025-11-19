n=int(input())
i=1
if n==0:
    print("\"3 ning darajasi emas\"")
else:
    while n>i:
        i*=3
        
    if n==i:
        print("\"3 ning darajasi\"")
    else:
        print("\"3 ning darajasi emas\"")
