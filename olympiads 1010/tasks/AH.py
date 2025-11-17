x,y=map(int,input().split())
if x%2!=0 and y%2==0:
    print("ROST")
elif x%2==0 and y%2!=0:
    print("ROST")
elif x==0 or y==0:
    print("YOLG'ON")
else:
    print("YOLG'ON")
