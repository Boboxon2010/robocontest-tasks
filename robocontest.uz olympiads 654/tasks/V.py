a = int(input())
birlar = a % 10           
onlar = (a // 10) % 10   
yuzlar = (a // 100) % 10 
minglar = a // 1000       
if birlar == minglar and onlar == yuzlar:
    print('yes')
else:
    print('no')