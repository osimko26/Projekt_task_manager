"""
Projekt číslo 1: Správca úloh
Zadanie č. 1: konzolová aplikácia na pridávanie, zobrazovanie a odstraňovanie úloh.
"""

# Zoznam, do ktorého sa ukladajú úlohy (každá úloha je slovník s názvom a popisom)
ulohy = []

# Zobrazí hlavné menu a podľa voľby používateľa spustí príslušnú funkciu.
def hlavne_menu():
     while True:
        print("\nSprávca úloh - hlavné menu")
        print("1. Pridať novú úlohu")
        print("2. Zobraziť všetky úlohy")
        print("3. Odstrániť úlohu")
        print("4. Koniec programu")

        volba = input("Vyberte jednu z možností (1-4): ").strip()

        if volba == "1":
            pridat_ulohu()
        elif volba == "2":
            zobrazit_ulohy()
        elif volba == "3":
            odstranit_ulohu()
        elif volba == "4":
            print("\nKoniec programu.")
            break
        else:
            print("Neplatná voľba, zadajte prosím číslo od 1 do 4.")

# Načíta názov a popis úlohy a uloží ju do zoznamu. Prázdny vstup nie je povolený.
def pridat_ulohu():
    while True:
        nazov = input("\nZadajte názov úlohy: ").strip()
        popis = input("Zadajte popis úlohy: ").strip()
 
        if not nazov or not popis:
            print("Názov ani popis úlohy nemôže byť prázdny. Zadajte ich prosím znova.")
            continue
 
        ulohy.append({"nazov": nazov, "popis": popis})
        print(f"Úloha '{nazov}' bola pridaná.")
        return


# Vypíše všetky uložené úlohy. Vráti False, ak je zoznam prázdny.
def zobrazit_ulohy():
    if not ulohy:
        print("\nZoznam úloh je prázdny.")
        return False

    print("\nZoznam úloh:")
    for poradie, uloha in enumerate(ulohy, start=1):
        print(f"{poradie}. {uloha['nazov']} - {uloha['popis']}")
    return True

# Zobrazí úlohy a odstráni tú, ktorej číslo používateľ zadá.
def odstranit_ulohu():
    if not zobrazit_ulohy():
        print("Nie je čo odstrániť.")
        return

    while True:
        vstup = input("\nZadajte číslo úlohy, ktorú chcete odstrániť: ").strip()

        if not vstup.isdigit() or not 1 <= int(vstup) <= len(ulohy):
            print(f"Úloha s číslom '{vstup}' neexistuje. Zadajte číslo od 1 do {len(ulohy)}.")
            continue

        odstranena = ulohy.pop(int(vstup) - 1)
        print(f"Úloha '{odstranena['nazov']}' bola odstránená.")
        return


if __name__ == "__main__":
    hlavne_menu()
