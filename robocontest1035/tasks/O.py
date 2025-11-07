n = int(input())  
s = 1.0           

for i in range(1, n + 1):
    k = 1 + i / 10   
    s *= k

print(s)
