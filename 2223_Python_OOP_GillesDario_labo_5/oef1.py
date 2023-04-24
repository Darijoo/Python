import sys

AANTAL_REGELS = 10

if len(sys.argv) != 2:
    print("Geef de naam van het bestand mee als command-line argument.")
    quit() # programma stopt meteen na gebruik van de quit-functie

try:
    with open(sys.argv[1], "r") as mijn_bestand:
        regel = mijn_bestand.readline()
        teller = 0
        while teller < AANTAL_REGELS and regel != "":
            regel = mijn_bestand.readline 
            