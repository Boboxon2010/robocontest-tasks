t=int(input())
for g in range(t):
    k,q,n = map(int, input().split())
    barcha_olmalar= q
    for i in range(n):
    	barcha_olmalar = (barcha_olmalar + k) * 2
    print(barcha_olmalar)