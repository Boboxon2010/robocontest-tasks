n = int(input())
a = list(map(int, input().split()))
m = int(input())

s = []
for i in a:
    s.append((i % m + m) % m)

k = sorted(set(s))   # set() -> list() va sort bir qatorda

for i in k:
    print(i, end=' ')
