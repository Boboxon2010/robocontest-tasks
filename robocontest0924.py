from itertools import combinations

a = list(map(int, input().split()))

total = sum(a)
if total % 2 == 1:
    print("NO")
else:
    half = total // 2
    possible = False
    
    for comb in combinations(a, 3):
        if sum(comb) == half:
            possible = True
            break
    print("YES" if possible else "NO")