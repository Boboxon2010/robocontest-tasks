n=int(input())
for _ in range(n):
    h,d,g=map(int,input().split())
    if 200<=h and h<=300 and d>=50 and g>=150:
        print('Yes')
    else:
        print('No')