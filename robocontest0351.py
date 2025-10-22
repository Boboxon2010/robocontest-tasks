import math

def olma_taqsimlash(N):
    if N < 6:
        return 0  # Agar N < 6 bo'lsa, hech qanday usul yo'q, chunki har bir o'quvchiga kamida 2 ta olma berish kerak
    
    # Kombinatorik hisoblash: C(N-4, 2)
    return math.comb(N - 4, 2)

# Kirish ma'lumotlarini olish
N = int(input())

# Javobni chiqarish
print(olma_taqsimlash(N))
