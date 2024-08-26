from math import sqrt
#d AB² = (xB – xA)² + (yB – yA)²

xa=float(input())
ya=float(input())
xb=float(input())
yb=float(input())

dab= sqrt(pow(xb-xa, 2) + pow(yb-ya, 2))

print("{:.2f}".format(dab))
