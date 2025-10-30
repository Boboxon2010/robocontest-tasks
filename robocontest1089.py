def number_to_uzbek_latin(n):
    birlik = ["", "bir", "ikki", "uch", "to'rt", "besh", "olti", "yetti", "sakkiz", "to'qqiz"]
    onlik = ["", "o'n", "yigirma", "o'ttiz", "qirq", "ellik", "oltmish", "yetmish", "sakson", "to'qson"]
    
    if n <= 0 or n > 1000:
        return "Noto'g'ri son! 1-1000 oralig'ida bo'lishi kerak"
    
    if n < 10:
        return birlik[n]
    
    elif n < 100:
        if n % 10 == 0:
            return onlik[n // 10]
        else:
            return onlik[n // 10] + " " + birlik[n % 10]
    
    elif n < 1000:
        if n == 100:
            return "bir yuz"
        elif n % 100 == 0:
            return birlik[n // 100] + " yuz"
        else:
            return birlik[n // 100] + " yuz " + number_to_uzbek_latin(n % 100)
    
    else:  # n == 1000
        return "bir ming"

# Asosiy dastur
son = int(input())
natija = number_to_uzbek_latin(son)
print(natija)