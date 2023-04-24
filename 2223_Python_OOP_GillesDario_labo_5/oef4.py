aantal_zijden = int(input("Hoeveel zijden heeft de veelhoek? "))
if aantal_zijden < 3 or aantal_zijden > 10:
        print("Deze veelhoek heeft niet tussen 3 en 10 zijden.")
else:
        if aantal_zijden == 3:
            print("Dit is een driehoek.")
        elif aantal_zijden == 4:
            print("Dit is een vierhoek.")
        elif aantal_zijden == 5:
            print("Dit is een vijfhoek.")
        elif aantal_zijden == 6:
            print("Dit is een zeshoek.")
        elif aantal_zijden == 7:
            print("Dit is een zeventhoek.")
        elif aantal_zijden == 8:
            print("Dit is een achthoek.")
        elif aantal_zijden == 9:
            print("Dit is een negenhoek.")
        elif aantal_zijden == 10:
            print("Dit is een tienhoek.")
