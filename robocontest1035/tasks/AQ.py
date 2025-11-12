n = int(input())
A, B = map(float, input().split())
x = (B - A) / n
for i in range(n + 1):
    print(f"{A + i * x:.5f}",end=' ')
