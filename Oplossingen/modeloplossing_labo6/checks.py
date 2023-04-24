from datetime import datetime
from rich.table import Table
from rich import box
from bestanden import lezen_bestand, schrijven_bestand, schrijven_naar_html

CHECKS_BESTAND = "data/checks.json"
LOGS_BESTAND = "data/logs.json"


def initialiseer():
    """Deze functie initialiseert de applicatie. Ze leest de checks en logs uit de json-bestanden en geeft ze terug als list. Ze wordt aangeroepen in main.py. Ze heeft geen parameters. Ze heeft geen returnwaarde."""
    global checks_list
    global logs_list
    checks_list = lezen_bestand(CHECKS_BESTAND)
    logs_list = lezen_bestand(LOGS_BESTAND)


def toevoegen_check(soort_check, parameters_check):
    """Deze functie faciliteert het toevoegen van een check aan het systeem. Ze neemt een soort check en een list met parameters als parameters. Ze heeft geen returnwaarde."""
    checks_list.append([soort_check, parameters_check])
    schrijven_bestand(CHECKS_BESTAND, checks_list)


def oplijsten_checks():
    """Deze functie faciliteert het oplijsten van de checks in het systeem. Ze heeft geen parameters. Ze geeft een rich.table.Table terug. Deze kan gebruikt worden om de checks in een tabel weer te geven. De tabel wordt aangemaakt met de rich.table.Table klasse. De tabel wordt opgemaakt met de rich.box.Box klasse. De tabel wordt gevuld met de rich.table.Table.add_row methode. De tabel wordt gereturned met de rich.table.Table klasse."""
    table = Table(box=box.ASCII2)
    table.add_column("No", justify="center", style="cyan", no_wrap=True)
    table.add_column("Type", justify="center", style="cyan", no_wrap=True)
    table.add_column("Naam", justify="center", style="magenta", no_wrap=True)
    table.add_column("IP/host", justify="center", style="green", no_wrap=True)
    table.add_column("Aantal checks", justify="center", style="cyan", no_wrap=True)
    table.add_column("Succes", justify="center", style="cyan", no_wrap=True)
    for id, check in enumerate(checks_list):
        table.add_row(
            str(id + 1),
            check[0],
            check[1][0],
            check[1][1],
            check[1][2],
            check[1][3],
        )
    return table


def verwijderen_check(index_getal_check):
    """Deze functie faciliteert het verwijderen van een check uit het systeem. Ze neemt een index_getal_check als parameter. Ze heeft geen returnwaarde. De index_getal_check is een string. Deze wordt eerst omgezet naar een integer. De integer wordt gebruikt om de check uit de checks_list te verwijderen. De checks_list wordt opnieuw weggeschreven naar het checks.json bestand."""
    del checks_list[int(index_getal_check)]
    schrijven_bestand(CHECKS_BESTAND, checks_list)


def uitvoeren_checks():
    """Deze functie faciliteert het uitvoeren van de checks. Ze heeft geen parameters. Ze heeft geen returnwaarde. Ze importeert de module ping.py. Ze gebruikt de getattr() functie om de run() functie uit de module ping.py te halen. Ze gebruikt de run() functie om de check uit te voeren. Ze gebruikt de datetime.now() functie om de datum en tijd op te halen. Ze gebruikt de datetime.strftime() functie om de datum en tijd om te zetten naar een string. Ze gebruikt de append() functie om de check_resultaat toe te voegen aan de logs_list. De logs_list wordt opnieuw weggeschreven naar het logs.json bestand. De logs_list wordt doorgegeven aan de schrijven_naar_html() functie. De schrijven_naar_html() functie schrijft de logs_list weg naar het logs.html bestand."""
    for check in checks_list:
        # Ik kon hier ook een if gebruiken, maar ben voor algemene oplossing gegaan
        # Ik gebruik getattr() om de run() functie uit de module ping.py te halen
        module = __import__(check[0].lower())
        functie = getattr(module, "run")
        resultaat = functie(
            check[1][1], check[1][2]
        )  # hier runnen we run() uit de module ping.py
        datum_tijd = datetime.now()
        datum_tijd_clean = datum_tijd.strftime("%Y-%m-%d %X")
        datum = datum_tijd.strftime("%d-%m-%Y")
        tijd = datum_tijd.strftime("%X")
        check_resultaat = [
            str(datum_tijd_clean),
            str(datum),
            str(tijd),
            "ping",
            check[1][0],
            resultaat,
        ]
        logs_list.append(check_resultaat)
    schrijven_bestand(LOGS_BESTAND, logs_list)
    schrijven_naar_html(logs_list)
