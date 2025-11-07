shohX, shohY = map(int, input("Shohning koordinatasini kiriting (x1 y1): ").split())
farzinX, farzinY = map(int, input("Farzinning koordinatasini kiriting (x2 y2): ").split())

if shohX == farzinX or shohY == farzinY or abs(shohX - farzinX) == abs(shohY - farzinY):
    print("game over")
else:
    print("game")
 