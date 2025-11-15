a=int(input())
birlar=a%10
onlar=(a//10)%10
yuzlar=a//100
if yuzlar<onlar and onlar<birlar:
    print("ROST")
elif yuzlar>onlar and onlar>birlar:
    print("ROST")
else:
    print("YOLG'ON")