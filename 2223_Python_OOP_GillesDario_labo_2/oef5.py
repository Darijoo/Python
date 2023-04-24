maand = input("Geef de naam van de maand: ")

if maand in ["januari", "maart", "mei", "juli", "augustus", "oktober", "december"]:
    aantal_dagen = 31
elif maand in ["april", "juni", "september", "november"]:
    aantal_dagen = 30
elif maand == "februari":
    aantal_dagen = "28 of 29"
else:
    print("Ongeldige invoer: dit is geen geldige maandnaam.")
    aantal_dagen = None

if aantal_dagen is not None:
    print(f"De maand", maand, "heeft", aantal_dagen, "dagen.")
