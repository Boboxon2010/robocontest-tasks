a, b, c = map(int, input().split())

# Uchburchak bo'lish sharti
if a + b > c and a + c > b and b + c > a:
    # Teng yonli sharti (kamida ikki tomon teng)
    if a == b or a == c or b == c:
        print('ROST')
    else:
        print("YOLG'ON")
else:
    print("YOLG'ON")