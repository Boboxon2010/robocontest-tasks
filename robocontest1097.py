n = input().strip()

# Sonni string sifatida qabul qilamiz
s = list(n)

# Birinchi 9 emas raqamni topamiz va uni 9 ga o'zgartiramiz
for i in range(len(s)):
    if s[i] != '9':
        s[i] = '9'
        break

# Natijani chiqaramiz
print(''.join(s))