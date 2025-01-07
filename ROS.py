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

print("Vítej ve hře! Máš v kapse 100 Kč a můžeš cestovat mezi Hradčany, Václavákem a Holešovicemi.")
print(f"Začínáš na lokaci: {aktualni_lokace.nazev}\n")