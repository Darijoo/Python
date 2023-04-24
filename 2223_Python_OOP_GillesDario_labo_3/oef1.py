import math


def zijde_berekenen(zijde1, zijde2):
    schuine_zijde = round(math.sqrt((zijde1**2)+(zijde2**2)),2)
    return schuine_zijde
    print(f"De schuine_zijde is {schuine_zijde}cm")

def main():
    zijde1 = float(input("Geef de eerste zijde "))
    zijde2 = float(input("Geef de tweede zijde "))
    zijde_berekenen(zijde1, zijde2)
    print(f"De schuine_zijde is {zijde_berekenen(zijde1, zijde2)}cm")
if __name__ == "__main__":
    main()
