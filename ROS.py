import random

# Třída Lokace
class Lokace:
    def __init__(self, nazev):
        self.nazev = nazev


# Třída Osoba
class Osoba:
    def __init__(self, jmeno, pocet_penez):
        self.jmeno = jmeno
        self.pocet_penez = pocet_penez

# Lokace
lokace = [
    Lokace("Hradčany"),
    Lokace("Václavák"),
    Lokace("Holešovice")
]

# Osoba
hrac = Osoba("Hráč", 100)

# Dny
celkovy_pocet_dni = 14
den = 0
aktualni_lokace = random.choice(lokace)

print("Vítej ve hře! Máš v kapse 100 Kč a můžš cestovat mezi Hradčany, Václavákem a Holešovicemi.")
print(f"Začínáš na lokaci: {aktualni_lokace.nazev}\n")

while den < celkovy_pocet_dni:
    print(f"\nDen {den + 1} z 14")
    print(f"Jste v lokaci: {aktualni_lokace.nazev}")
    print(f"Máte {hrac.pocet_penez} Kč.")

    print("\nLokace na výběr:")
    for i, l in enumerate(lokace):
        print(f"{i + 1}. {l.nazev}")

    volba = input("Vyberte číslo lokace pro přesun (1-3). Stiskem Enter zůstanete na místě: ")

    if volba.isdigit():
        volba = int(volba)
        if 1 <= volba <= 3:
            nova_lokace = lokace[volba - 1]
            if nova_lokace != aktualni_lokace:
                aktualni_lokace = nova_lokace
                den += 1
                print(f"Přesunuli jste se do lokace {nova_lokace.nazev}.")
            else:
                print("Jste již v této lokaci, den nebyl spotřebován.")
        else:
            print("Neplatná volba.")
    else:
        print("Zůstáváte v aktuální lokaci.")
        den += 1

print(f"\nHra skončila po 14 dnech.")
print(f"Konečný počet peněz: {hrac.pocet_penez} Kč")
