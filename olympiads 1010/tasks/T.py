a=int(input())
birlar=a%10
onlar=(a//10)%10
yuzlar=a//100
if birlar==onlar and onlar==yuzlar:
    print('ROST')
else:
    print("YOLG'ON")