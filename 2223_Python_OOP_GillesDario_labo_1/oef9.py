dagen = int(input("Hoeveel dagen? "))
uren = int(input("Hoeveel uren? "))
minuten = int(input("Hoeveel minuten? "))
seconden = int(input("Hoeveel seconden? "))

totale_seconden = dagen * 86400 + uren * 3600 + minuten * 60 + seconden
print(f"Het totaal aantal seconden is {totale_seconden}")
