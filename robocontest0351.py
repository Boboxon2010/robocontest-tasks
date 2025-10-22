# Uchta o’quvchiga savatdagi N ta olmani necha xil usulda bo’lib berish mumkin? Savatda olma qolmasligi va har bir o’quvchida kamida ikkita olma bo’lishi kerak
from math import comb
N=int(input())
if N<6:
    print(0)
else:
    print(comb(N-1-2*3,3-1))