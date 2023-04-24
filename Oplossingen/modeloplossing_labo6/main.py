import sys
from modi import menu, cli
from checks import initialiseer


def main():
    """Deze functie start de applicatie op. Als er geen argumenten meegegeven worden, dan start de applicatie in de grafische modus. Als er argumenten meegegeven worden, dan start de applicatie in de command line modus.ls"""
    initialiseer()
    if len(sys.argv) > 1:
        cli(sys.argv)
    else:
        menu()


if __name__ == "__main__":
    main()
