A, B = map(int, input().split())
k = 0
for i in range(B - 1, A, -1):
    print(i, end=' ')
    k += 1
print()
print(k)
