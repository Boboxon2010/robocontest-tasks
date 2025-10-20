A,B,C=map(int,input().split())
if abs(A-C)<abs(B-C):
    print("1-mushuk")
elif abs(A-C)>abs(B-C):
    print("2-mushuk")
else:
    print("sichqon")