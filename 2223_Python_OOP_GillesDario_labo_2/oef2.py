mensen_jaren = int(input("Hoeveel mensenjaren oud is de hond? "))
if mensen_jaren < 0:
    print("Ongeldige invoer: het aantal jaren moet positief zijn.")
elif mensen_jaren <= 2:
    honden_jaren = mensen_jaren * 10.5
else:
    honden_jaren = 21 + (mensen_jaren - 2) * 4
print("De hond is ongeveer", honden_jaren, "hondenjaren oud.")
