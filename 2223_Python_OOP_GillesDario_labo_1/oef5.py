statiegeld_kleine = 0.12
statiegeld_grote = 0.25
aantal_kleine = float(input("Hoeveel kleine flessen worden er ingeleverd?"))
aantal_grote = float(input("Hoeveel grote flessen worden er ingeleverd?"))
teruggave = statiegeld_kleine * aantal_kleine + statiegeld_grote * aantal_grote
teruggave_afgerond = round(teruggave, 2)
print(f"Je krijgt {teruggave_afgerond} euro terug.")