A, B = map(int, input().split())

summa = 0  # umumiy yig‘indi

for i in range(A, B + 1):
    # i*i ni hisoblash (faqat qo‘shish bilan)
    kvadrat = 0
    j = 0
    while j < i:
        kvadrat += i
        j += 1

    # yig‘indiga qo‘shish (faqat 1 birlik orqali)
    k = 0
    while k < kvadrat:
        summa += 1
        k += 1

print(summa)
