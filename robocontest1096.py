from collections import Counter

n = int(input())
sizes = list(map(int, input().split()))

# O'lchamlarni sanash
count = Counter(sizes)

# Juftliklar sonini hisoblash
pairs = sum(c * (c - 1) // 2 for c in count.values())

print(pairs)
