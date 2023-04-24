##
# Oefening 15
# Is een string een palindroom? https://nl.wikipedia.org/wiki/
# Palindroom. Een string is een palindroom als het identiek is gelezen
# van links en rechts en van rechts naar links. Zo zijn “meetsysteem” en
# “stormrots” voorbeelden van palindromen. Schrijf een programma dat een
# string vraagt aan een gebruiker en een loop gebruikt om te bepalen of
# het woord al dan niet een palindroom is. Gebruik print om met een
# betekenisvol bericht eventueel te bevestigen of dat het geval is.
# Tip:
# Je kunt bvb positie 5 van een string opvragen met mijnstring[4]... De
# aantal karakters in een string krijg je met len(mijnstring)...

woord = input("Geef een string: ")
is_palindroom = True

i = 0
while (
    i < len(woord) / 2 and is_palindroom
):  # je hoeft slechts de eerste helft van het woord te testen, bij oneven aantal karakters maakt de middelste letter niet uit om te bepalen of een woord een palindroom is of niet
    # bvb bij stormrots...
    # stel i=0 - je vergelijkt dan s (positie 0) met de eind-s (positie 9 - 0 - 1 = 8)
    # stel i=1 - je vergelijkt dan t (positie 1) met de eind-t (positie 0 - 1 - 1 = 7)
    if woord[i] != woord[len(woord) - i - 1]:
        is_palindroom = False
    i = i + 1
if is_palindroom:
    print(f"De string '{woord}' is een palindroom")
else:
    print(f"De string '{woord}' is GEEN palindroom")
