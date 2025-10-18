# masala: Sizga ikkita natural son beriladi. Sizning vazifangiz shu sonlar orasidagi 3ga bo'linadigan ammo 7 bo'linmaydigan sonlar yigindisini topish. Bunda ikkala chegara ham kiradi. Time limit (test 101) xatoliki chiqmasin
a,b=map(int,input().split())
s=0
for i in range(a,b+1):
    if i%3==0 and i%7!=0:
        s+=i    
print(s)

