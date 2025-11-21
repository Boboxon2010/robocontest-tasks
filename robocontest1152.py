Q, B, K = map(int, input().split())

# x -- chetga yuboriladigan qizlar soni
# y = K - x -- chetga yuboriladigan o‘g‘illar soni
# Cheklovlar:
L = max(0, K - B)      # y <= B
R = min(Q, K)          # x <= Q

if K == 0:
    print(min(Q // 2, B))
    exit()

def teams(x):
    Q2 = Q - x
    B2 = B - (K - x)
    if Q2 < 0 or B2 < 0:
        return 0
    return min(Q2 // 2, B2)

# Optimal x* nuqta
x_star = (Q - 2*B + 2*K) // 3

candidates = set([L, R, x_star, x_star-1, x_star+1])

ans = 0
for x in candidates:
    if L <= x <= R:
        ans = max(ans, teams(x))

print(ans)