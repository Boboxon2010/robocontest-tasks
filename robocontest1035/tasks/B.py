A, B = map(int, input().split())
k = 0
for i in range(A, B + 1):
    k += 1
    print(i, end=" ")

print()
print(k)
