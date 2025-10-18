# masala: Sizga ikkita natural son beriladi. Sizning vazifangiz shu sonlar orasidagi 3ga bo'linadigan ammo 7 bo'linmaydigan sonlar yigindisini topish. Bunda ikkala chegara ham kiradi. Time limit (test 101) xatoliki chiqmasin
a,b=map(int,input().split())
if a>b:
    a,b = b,a

def sum_of_multiples(k, L, R):
    """Return sum of multiples of k in [L, R] using arithmetic progression."""
    if L>R:
        return 0
    # first multiple of k >= L
    first = ((L + k - 1) // k) * k
    # last multiple of k <= R
    last = (R // k) * k
    if first>last:
        return 0
    n = (last - first) // k + 1
    return n * (first + last) // 2

# Sum multiples of 3 but exclude those divisible by 7 (i.e., divisible by lcm(3,7)=21)
sum3 = sum_of_multiples(3, a, b)
sum21 = sum_of_multiples(21, a, b)
print(sum3 - sum21)

