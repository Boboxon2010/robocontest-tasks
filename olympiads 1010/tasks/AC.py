# Nuqtaning koordinatalari
x, y = map(int, input().split())

# To'rtburchakning ikki qarama-qarshi burchaklari
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

# Chegaralarni aniqlaymiz
xmin = min(x1, x2)
xmax = max(x1, x2)
ymin = min(y1, y2)
ymax = max(y1, y2)

# Ichkarida bo'lish sharti (chegaraga tegmasdan)
if xmin < x < xmax and ymin < y < ymax:
    print("ROST")
else:
    print("YOLG'ON")