from rich.console import Console
from rich.prompt import Prompt
from checks import (
    toevoegen_check,
    oplijsten_checks,
    verwijderen_check,
    uitvoeren_checks,
)

console = Console()

PROMPT_START = "Welkom bij Server Check! Uw trouwe en betrouwbare netwerk, service en server check die uw leven een pak gemakkelijker maakt 😀"
PROMPT_EINDE = "Bedankt om Server Check te gebruiken. Tot snel! 😉"


def menu():
    """Deze functie faciliteert het menu van de applicatie. Het menu is een loop die de gebruiker telkens een keuze laat maken. De keuze wordt verwerkt in een switch-case constructie. De functie geeft geen waarde terug."""
    console.print(PROMPT_START)
    while True:
        prompt = Prompt.ask(
            "Server check: maak een keuze ('1' om check toe te voegen, '2' om checks op te lijsten, '3' om check te verwijderen, '4' om de checks uit te voeren, '0' om te stoppen)",
            choices=["1", "2", "3", "4", "0"],
            default="2",
        )
        match prompt:
            case "1":  # server toevoegen
                soort_check = Prompt.ask(
                    "Welk soort check wil je uitvoeren?",
                    choices=["Ping"],
                    default="Ping",
                )
                naam_check = Prompt.ask(
                    "Kies een naam voor je check",
                    default="Ping Google",
                )
                ip_check = Prompt.ask(
                    "Geef ip of hostnaam van de server", default="google.com"
                )
                aantal_check = Prompt.ask(
                    "Geef het aantal keer dat je de check wil uitvoeren",
                    choices=["1", "2", "3", "4", "5"],
                    default="1",
                )
                succes_check = Prompt.ask(
                    "Hoeveel percent succesvolle checks wil je?",
                    choices=["25", "50", "75", "100"],
                    default="100",
                )
                toevoegen_check(
                    soort_check, [naam_check, ip_check, aantal_check, succes_check]
                )
                console.clear()
                console.print("De check werd toegevoegd!")
            case "2":  # servers oplijsten
                console.print(oplijsten_checks())
            case "3":  # server verwijderen
                console.print(oplijsten_checks())
                te_verwijderen = input(
                    'Geef het nummer van de check die je wil verwijderen (bvb "1", "0" om terug te keren) '
                )
                if te_verwijderen != "0":
                    verwijderen_check(int(te_verwijderen) - 1)
                    console.clear()
                    console.print("De check werd verwijderd!")
            case "4":  # servers checken
                uitvoeren_checks()
            case "0":  # toepassing stoppen
                console.print(PROMPT_EINDE)
                quit()
            case _:
                console.print("Sorry, ik begrijp je niet. Probeer opnieuw.")


def cli(argumenten):
    """Deze functie laat de toepassing werken als een CLI-tool. De toepassing kan twee argumenten aanvaarden: 'check' en 'help'. Als het argument 'check' wordt meegegeven, worden de checks uitgevoerd. Als het argument 'help' wordt meegegeven, wordt de help-tekst weergegeven."""
    if argumenten[1] == "check":
        uitvoeren_checks()
        console.print("De checks werden uitgevoerd!")
    elif argumenten[1] == "help" or argumenten[1] == "--help":
        console.print(
            "Voer de toepassing uit met argument 'check' om de checks uit te voeren."
        )
    quit()
