n = int(input())
x = float(input())

S = 0.0
odd_fact = 1.0   # 1*3*5*...
even_fact = 1.0  # 2*4*6*...

for i in range(0, n + 1):
    if i > 0:
        odd_fact *= (2 * i - 1)
        even_fact *= (2 * i)
    term = odd_fact * x**(2 * i + 1) / (even_fact * (2 * i + 1))
    S += term

print(f"{S:.8f}")
