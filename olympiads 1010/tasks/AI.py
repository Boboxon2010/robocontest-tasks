x, y = map(int, input().split())
x1, y1 = map(int, input().split())

if (x + y) % 2 == (x1 + y1) % 2:
    print("ROST")  # same color
else:
    print("YOLG'ON")  # different color
