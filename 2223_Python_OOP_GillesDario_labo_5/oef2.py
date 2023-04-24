import sys

AANTAL_REGELS = 10
regels_list = []

if len(sys.argv) != 2:
    print("Geef de naam van het bestand mee als command-line argument.")
    quit() # programma stopt meteen na gebruik van de quit-functie

try:
    with open(sys.argv[1], "r") as mijn_bestand:
        for regel in mijn_bestand:
            regels_list.append(regel.rstrip())

            if len(regels_list) > AANTAL_REGELS:
                regels_list.pop(0)

except IOError:
    print("Er is iets fout gelopen bij het openen/lezen van het bestand.")

for
