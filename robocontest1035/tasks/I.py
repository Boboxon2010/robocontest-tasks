A,B=map(int,input().split())


# Ko'paytma boshlang'ich qiymati 1
product = 1

# Oddiy ko'paytirish funksiyasi (faqat qo'shish orqali)
def multiply(x, y):
    result = 0
    for _ in range(y):
        result += x
    return result

for i in range(A, B + 1):
    product = multiply(product, i)

print(product)