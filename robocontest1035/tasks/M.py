N = int(input())

S = 0
for i in range(N, 2*N + 1):
    S += i * i  # i^2
print(S)
