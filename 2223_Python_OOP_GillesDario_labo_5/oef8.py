import math
straal = float(input("Geef de straal: "))
hoogte = float(input("Geef de hoogte: "))

volume = round((math.pi * (straal**2) * hoogte),1)

print(f"Het volume is {volume} kubieke meter")