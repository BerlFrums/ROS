#predmet.py
import random  # Importuje modul pro práci s náhodnými čísly.

class Predmet:  # Definuje třídu s názvem Predmet.
    def __init__(self, nazev, min_cena, max_cena):  # Konstruktor třídy pro inicializaci atributů.
        self.nazev = nazev  # #Inicializuje atribut pro název předmětu.
        self.min_cena = min_cena  # #Inicializuje atribut pro minimální cenu.
        self.max_cena = max_cena  # #Inicializuje atribut pro maximální cenu.
        self.aktualni_cena = random.randint(min_cena, max_cena)  # Nastaví aktuální cenu na náhodnou hodnotu v rozmezí min_cena a max_cena.

    def aktualizovat_cenu(self):  # Definuje metodu pro aktualizaci ceny.
        zmena = random.randint(-5, 5)  # Vygeneruje náhodnou změnu ceny v rozsahu -5 až 5.
        self.aktualni_cena = max(self.min_cena, min(self.max_cena, self.aktualni_cena + zmena))  
        # #Aktualizuje aktuální cenu o náhodnou změnu, zároveň zajišťuje, že zůstane v rozmezí min_cena a max_cena.

  #lokace.py
  class Lokace:  # Definuje třídu s názvem Lokace.
    def __init__(self, nazev, predmety):  # Konstruktor třídy pro inicializaci atributů.
        self.nazev = nazev  # #Inicializuje atribut pro název lokace.
        self.predmety = predmety  # #Inicializuje atribut pro předměty jako slovník {nazev_predmetu: objekt Predmet}.

    def zobrazit_predmety(self):  # Definuje metodu pro zobrazení předmětů v lokaci.
        print(f"Předměty dostupné v lokaci {self.nazev}:")  # #Vypíše název lokace.
        for predmet in self.predmety.values():  # Iteruje přes všechny objekty Predmet ve slovníku predmety.
            print(f"{predmet.nazev}: {predmet.aktualni_cena} Kč")  # #Vypíše název a aktuální cenu každého předmětu.

    def aktualizovat_ceny(self):  # Definuje metodu pro aktualizaci cen všech předmětů v lokaci.
        for predmet in self.predmety.values():  # Iteruje přes všechny objekty Predmet ve slovníku predmety.
            predmet.aktualizovat_cenu()  # #Volá metodu aktualizovat_cenu pro každý předmět.

#osoba.py
class Osoba:  # Definuje třídu s názvem Osoba.
    def __init__(self, jmeno):  # Konstruktor třídy pro inicializaci atributů.
        self.jmeno = jmeno  # #Inicializuje atribut pro jméno osoby.
        self.penize = 100  # #Inicializuje atribut peníze na hodnotu 100.
        self.inventar = {}  # #Inicializuje atribut inventář jako prázdný slovník.
        self.max_velikost_inventare = 2  # #Inicializuje maximální kapacitu inventáře na 2.

    def koupit_predmet(self, nazev_predmetu, lokace):  # Definuje metodu pro koupi předmětu.
        if nazev_predmetu in lokace.predmety:  # #Zkontroluje, zda předmět existuje v lokaci.
            predmet = lokace.predmety[nazev_predmetu]  # #Získá objekt předmětu ze slovníku.
            if self.penize >= predmet.aktualni_cena and len(self.inventar) < self.max_velikost_inventare:  
                # #Zkontroluje, zda má dost peněz a volné místo v inventáři.
                self.penize -= predmet.aktualni_cena  # #Odečte cenu předmětu z peněz.
                self.inventar[nazev_predmetu] = self.inventar.get(nazev_predmetu, 0) + 1  
                # #Přidá předmět do inventáře nebo zvýší jeho počet, pokud již existuje.
                print(f"Koupil jsi {nazev_predmetu} za {predmet.aktualni_cena} Kč.")  # #Vypíše potvrzení nákupu.
            else:
                print("Nemáš dost peněz nebo místo v inventáři!")  # #Vypíše chybovou zprávu.

    def prodat_predmet(self, nazev_predmetu, lokace):  # Definuje metodu pro prodej předmětu.
        if nazev_predmetu in self.inventar and self.inventar[nazev_predmetu] > 0:  
            # #Zkontroluje, zda předmět existuje v inventáři a má nenulové množství.
            predmet = lokace.predmety[nazev_predmetu]  # #Získá objekt předmětu z lokace.
            self.penize += predmet.aktualni_cena  # #Přičte cenu předmětu k penězům.
            self.inventar[nazev_predmetu] -= 1  # #Sníží počet prodaného předmětu v inventáři.
            if self.inventar[nazev_predmetu] == 0:  
                del self.inventar[nazev_predmetu]  # #Odstraní předmět z inventáře, pokud jeho počet klesne na nulu.
            print(f"Prodal jsi {nazev_predmetu} za {predmet.aktualni_cena} Kč.")  # #Vypíše potvrzení prodeje.
        else:
            print(f"Nemáš žádný {nazev_predmetu} na prodej.")  # #Vypíše chybovou zprávu.

    def koupit_vylepseni(self, typ_vylepseni, cena):  # Definuje metodu pro koupi vylepšení.
        if self.penize >= cena:  # #Zkontroluje, zda má osoba dost peněz na vylepšení.
            self.penize -= cena  # #Odečte cenu vylepšení z peněz.
            if typ_vylepseni == "kabát":  # #Zkontroluje typ vylepšení.
                self.max_velikost_inventare += 2  # #Zvýší kapacitu inventáře o 2.
            elif typ_vylepseni == "batoh":  # #Další kontrola pro jiný typ vylepšení.
                self.max_velikost_inventare += 3  # #Zvýší kapacitu inventáře o 3.
            print(f"Koupil jsi {typ_vylepseni}. Kapacita inventáře zvětšena!")  # #Vypíše potvrzení koupi vylepšení.
        else:
            print("Nemáš dost peněz na toto vylepšení.")  # #Vypíše chybovou zprávu.

#hra.py
print()  # #Vypíše prázdný řádek.
input("Pro spuštění tutorialu stiskni ENTER")  # #Čeká na uživatele, aby stiskl ENTER.
print()  # #Vypíše další prázdný řádek.
print("Lokace vybíráš pomocí čísel 1 až 4.")  # #Instrukce pro výběr lokace.
print()  # #Další prázdný řádek.
print("Pokud budeš chtít zakoupit předmět, tak zadej písmeno: K")  # #Instrukce pro nákup.
print("Pokud budeš chtít prodat předmět, tak zadej písmeno: P")  # #Instrukce pro prodej.
print("Pokud chceš jít dál, tak zadej písmeno: J")  # #Instrukce pro posun dál.
print()  # #Prázdný řádek.
print("V inventáři máš místo pouze pro 2 předměty.")  # #Informace o omezení inventáře.
print("Jméno předmětu, který chceš zakoupit nebo prodat musíš napsat přesně tak, jak je uvedeno na skladě.")  # #Pokyny pro zadávání jména předmětu.
print("Stejně tak můžeš nakupovat ve večerce vylepšení, jako je kabát a batoh.")  # #Informace o vylepšeních.
print("Kabát ti rozšíří inventář o 2 předměty a batoh o 3.")  # #Detailní popis vylepšení.
print("Cena kabátu je 150 Kč a batohu 400 Kč.")  # #Ceny vylepšení.
print()  # #Prázdný řádek.
input("Pro spuštění hry stiskni ENTER")  # #Čeká na uživatele, aby stiskl ENTER pro začátek hry.

from lokace import Lokace  # #Importuje třídu Lokace z jiného souboru.
from predmet import Predmet  # #Importuje třídu Predmet z jiného souboru.
from osoba import Osoba  # #Importuje třídu Osoba z jiného souboru.

# Inicializace lokací a předmětů
predmety = {  # #Vytváří slovník s instancemi předmětů.
    "Utopenec": Predmet("Utopenec", 50, 100),  # #Vytvoří předmět s cenovým rozmezím.
    "Med": Predmet("Med", 100, 200),  # #Další předmět.
    "Láhev Pálavy": Predmet("Láhev Pálavy", 200, 500),  # #Další předmět.
}

lokace = [  # #Vytváří seznam lokací s kopiemi slovníku předmětů.
    Lokace("Hradčany", predmety.copy()),  # #Lokace Hradčany.
    Lokace("Václavák", predmety.copy()),  # #Lokace Václavák.
    Lokace("Holešovice", predmety.copy()),  # #Lokace Holešovice.
    Lokace("Večerka", {}),  # #Lokace Večerka bez předmětů, slouží pro vylepšení.
]

def main():  # #Hlavní funkce hry.
    hrac = Osoba("")  # #Vytváří instanci hráče.
    dny = 0  # #Inicializuje počet dnů na 0.

    while dny < 14:  # #Hra trvá 14 dnů.
        print()  # #Oddělovač mezi dny.
        inventar_obsah = " a v inventáři nic" if not hrac.inventar else " a v inventáři " + " a ".join(hrac.inventar.keys())  
        # #Popis inventáře hráče.
        print(f"Den {dny + 1}. Máš {hrac.penize} Kč{inventar_obsah}.")  # #Vypíše aktuální stav dne, peněz a inventáře.
        print("Lokace: 1. Hradčany  2. Václavák  3. Holešovice  4. Večerka")  # #Nabídka lokací.

        while True:  # #Cyklus pro výběr lokace.
            try:
                volba = int(input("Vyber lokaci (1-4): ")) - 1  # #Požádá uživatele o výběr lokace.
                if volba in range(4):  # #Zkontroluje platnost výběru.
                    break
                else:
                    print("Zadej číslo mezi 1 a 4.")  # #Chybová zpráva.
            except ValueError:
                print("Zadej platné číslo.")  # #Chybová zpráva.

        if volba in range(3):  # #Pokud je volba mezi prvními třemi lokacemi.
            aktualni_lokace = lokace[volba]  # #Vybere aktuální lokaci.
            aktualni_lokace.aktualizovat_ceny()  # #Aktualizuje ceny předmětů v lokaci.
            aktualni_lokace.zobrazit_predmety()  # #Zobrazí dostupné předměty.

            while True:  # #Cyklus pro volbu akce v lokaci.
                akce = input("Chceš (K)oupit, (P)rodat nebo (J)ít dál? ").lower()  
                # #Čeká na vstup uživatele.
                if akce in ["k", "p", "j"]:  # #Zkontroluje platnost volby.
                    break
                else:
                    print("Neplatná volba! Zadej 'K', 'P' nebo 'J'.")  # #Chybová zpráva.

            if akce == "k":  # #Akce koupit.
                while True:
                    nazev_predmetu = input("Zadej název předmětu k nákupu: ")  
                    if nazev_predmetu in aktualni_lokace.predmety:  # #Kontrola existence předmětu.
                        hrac.koupit_predmet(nazev_predmetu, aktualni_lokace)  # #Provede nákup.
                        break
                    else:
                        print("Neplatný název předmětu! Zkus to znovu.")  # #Chybová zpráva.
            elif akce == "p":  # #Akce prodat.
                while True:
                    nazev_predmetu = input("Zadej název předmětu k prodeji: ")  
                    if nazev_predmetu in hrac.inventar:  # #Kontrola existence v inventáři.
                        hrac.prodat_predmet(nazev_predmetu, aktualni_lokace)  # #Provede prodej.
                        break
                    else:
                        print("Nevlastníš tento předmět!")  # #Chybová zpráva.

        elif volba == 3:  # #Pokud hráč zvolí Večerku.
            print("Vylepšení k dispozici: Kabát (150 Kč), Batoh (400 Kč)")  # #Zobrazí dostupná vylepšení.
            while True:  # #Cyklus pro výběr vylepšení.
                vylepseni = input("Chceš koupit Kabát nebo Batoh? ").lower()  
                if vylepseni in ["kabát", "batoh"]:  # #Kontrola platnosti vstupu.
                    break
                else:
                    print("Neplatná volba! Zadej 'Kabát' nebo 'Batoh'.")  # #Chybová zpráva.
            if vylepseni == "kabát":  # #Koupě kabátu.
                hrac.koupit_vylepseni("kabát", 150)
            elif vylepseni == "batoh":  # #Koupě batohu.
                hrac.koupit_vylepseni("batoh", 400)

        dny += 1  # #Přidá den.

    jmeno_hrace = input("Zadej své jméno: ")  # #Požádá uživatele o zadání jména.
    hrac.jmeno = jmeno_hrace  # #Nastaví jméno hráče.
    print("Konec hry!")  # #Oznámí konec hry.
    print(f"Konečný počet peněz: {hrac.penize} Kč.")  # #Zobrazí konečný stav peněz.

    with open("highscores.txt", "a", encoding="utf-8") as soubor:  # #Otevře soubor s výsledky pro přidání.
        soubor.write(f"{hrac.jmeno}: {hrac.penize} Kč\n")  # #Zapíše jméno a peníze hráče.

    print("Nejlepší výsledky:")  # #Zobrazí žebříček.
    with open("highscores.txt", "r", encoding="utf-8") as soubor:  # #Otevře soubor s výsledky pro čtení.
        print(soubor.read())  # #Vypíše obsah souboru.

if __name__ == "__main__":  # #Kontrola, zda je soubor spuštěn přímo.
    main()  # #Spustí hlavní funkci.

