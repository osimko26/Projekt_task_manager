# Testovacie prípady – Správca úloh

Projekt: Správca úloh (`task_manager_ondrej.py`)
Zadanie č. 2 – návrh testovacích prípadov (TC) pre funkcie `hlavne_menu()`, `pridat_ulohu()`, `zobrazit_ulohy()` a `odstranit_ulohu()`.

## Prehľad

| Funkcia | Testovacie prípady | Pozitívne | Negatívne | Hraničné |
|---|---|---|---|---|
| `hlavne_menu()` | TC01 – TC11 | 5 | 5 | 1 |
| `pridat_ulohu()` | TC12 – TC20 | 2 | 4 | 3 |
| `zobrazit_ulohy()` | TC21 – TC25 | 3 | 0 | 2 |
| `odstranit_ulohu()` | TC26 – TC35 | 2 | 4 | 4 |
| **Spolu** | **35** | **12** | **13** | **10** |

**Typy testov:**
- **Pozitívny** – funkcia je použitá správne s platnými vstupmi.
- **Negatívny** – používateľ zadá neplatné alebo neúplné údaje.
- **Hraničný** – okrajové situácie (prvá úloha, prázdny zoznam, posledná úloha a pod.).

**Testovacie prostredie:** Python 3, spustenie príkazom `python task_manager_ondrej.py` v termináli.

> Poznámka: Text `[MENU]` v očakávaných výsledkoch znamená opätovné zobrazenie hlavného menu:
>
> ```
> Správca úloh - hlavné menu
> 1. Pridať novú úlohu
> 2. Zobraziť všetky úlohy
> 3. Odstrániť úlohu
> 4. Koniec programu
> Vyberte jednu z možností (1-4):
> ```

---

## 1. Funkcia `hlavne_menu()`

### TC01: Zobrazenie hlavného menu po spustení programu
- **Typ:** Pozitívny
- **Popis:** Overenie, že po spustení programu sa zobrazí hlavné menu so všetkými štyrmi voľbami a výzvou na zadanie voľby.
- **Vstupné podmienky:** Program nie je spustený.
- **Kroky testu:**
  1. Spustite program príkazom `python task_manager_ondrej.py`.
  2. Skontrolujte text zobrazený v konzole.
- **Očakávaný výsledok:** Zobrazí sa nadpis „Správca úloh - hlavné menu“, voľby 1 až 4 a výzva „Vyberte jednu z možností (1-4):“.
- **Skutočný výsledok:** Zobrazilo sa hlavné menu s nadpisom, štyrmi voľbami a výzvou na zadanie voľby.
- **Stav:** Pass
- **Poznámky:** Základný test – bez funkčného menu nie je možné použiť žiadnu inú funkciu programu.

### TC02: Voľba 1 spustí pridanie úlohy
- **Typ:** Pozitívny
- **Popis:** Overenie, že voľba čísla 1 v hlavnom menu správne spustí funkciu `pridat_ulohu()`.
- **Vstupné podmienky:** Program zobrazuje hlavné menu.
- **Kroky testu:**
  1. Spustite program.
  2. Zadajte `1` a potvrďte klávesom Enter.
- **Očakávaný výsledok:** Program spustí funkciu `pridat_ulohu()` a zobrazí výzvu „Zadajte názov úlohy:“.
- **Skutočný výsledok:** Zobrazila sa výzva „Zadajte názov úlohy:“.
- **Stav:** Pass
- **Poznámky:** Overuje navigáciu z menu na jednu z kľúčových funkcií programu.

### TC03: Voľba 2 spustí zobrazenie úloh
- **Typ:** Pozitívny
- **Popis:** Overenie, že voľba čísla 2 spustí funkciu `zobrazit_ulohy()`.
- **Vstupné podmienky:** Program zobrazuje hlavné menu, zoznam úloh je prázdny.
- **Kroky testu:**
  1. Zadajte `2` a potvrďte klávesom Enter.
- **Očakávaný výsledok:** Program spustí funkciu `zobrazit_ulohy()`, vypíše „Zoznam úloh je prázdny.“ a znova zobrazí `[MENU]`.
- **Skutočný výsledok:** Vypísalo sa „Zoznam úloh je prázdny.“ a znova sa zobrazilo hlavné menu.
- **Stav:** Pass
- **Poznámky:** Overuje navigáciu na zobrazenie úloh a návrat do menu.

### TC04: Voľba 3 spustí odstránenie úlohy
- **Typ:** Pozitívny
- **Popis:** Overenie, že voľba čísla 3 spustí funkciu `odstranit_ulohu()`.
- **Vstupné podmienky:** Program zobrazuje hlavné menu, zoznam úloh je prázdny.
- **Kroky testu:**
  1. Zadajte `3` a potvrďte klávesom Enter.
- **Očakávaný výsledok:** Program spustí funkciu `odstranit_ulohu()`, vypíše „Zoznam úloh je prázdny.“ a „Nie je čo odstrániť.“ a znova zobrazí `[MENU]`.
- **Skutočný výsledok:** Vypísali sa obe hlášky a znova sa zobrazilo hlavné menu.
- **Stav:** Pass
- **Poznámky:** Overuje navigáciu na odstránenie úlohy.

### TC05: Voľba 4 ukončí program
- **Typ:** Pozitívny
- **Popis:** Overenie, že voľba čísla 4 korektne ukončí program.
- **Vstupné podmienky:** Program zobrazuje hlavné menu.
- **Kroky testu:**
  1. Zadajte `4` a potvrďte klávesom Enter.
- **Očakávaný výsledok:** Program vypíše „Koniec programu.“ a ukončí sa bez chyby.
- **Skutočný výsledok:** Vypísalo sa „Koniec programu.“ a program sa ukončil (návratový kód 0).
- **Stav:** Pass
- **Poznámky:** Jediný riadny spôsob ukončenia programu.

### TC06: Zadanie čísla mimo rozsahu (0 a 5)
- **Typ:** Negatívny
- **Popis:** Overenie, že číslo mimo rozsahu 1 až 4 je odmietnuté.
- **Vstupné podmienky:** Program zobrazuje hlavné menu.
- **Kroky testu:**
  1. Zadajte `0` a potvrďte klávesom Enter.
  2. Zadajte `5` a potvrďte klávesom Enter.
- **Očakávaný výsledok:** Po každom vstupe program vypíše „Neplatná voľba, zadajte prosím číslo od 1 do 4.“ a znova zobrazí `[MENU]`.
- **Skutočný výsledok:** Po oboch vstupoch sa vypísalo upozornenie a znova sa zobrazilo hlavné menu.
- **Stav:** Pass
- **Poznámky:** Testuje hodnoty tesne pod a tesne nad platným rozsahom.

### TC07: Zadanie písmena namiesto čísla
- **Typ:** Negatívny
- **Popis:** Overenie, že textový vstup je odmietnutý. Zahŕňa aj častú zámenu malého písmena `l` za číslicu `1`.
- **Vstupné podmienky:** Program zobrazuje hlavné menu.
- **Kroky testu:**
  1. Zadajte `l` (malé písmeno L) a potvrďte klávesom Enter.
  2. Zadajte `a` a potvrďte klávesom Enter.
- **Očakávaný výsledok:** Po každom vstupe program vypíše upozornenie o neplatnej voľbe a znova zobrazí `[MENU]`. Program nespadne.
- **Skutočný výsledok:** Po oboch vstupoch sa vypísalo upozornenie a znova sa zobrazilo hlavné menu.
- **Stav:** Pass
- **Poznámky:** Program nesmie pri textovom vstupe skončiť chybou (napr. `ValueError`).

### TC08: Prázdny vstup v menu
- **Typ:** Negatívny
- **Popis:** Overenie reakcie na stlačenie klávesu Enter bez zadania voľby.
- **Vstupné podmienky:** Program zobrazuje hlavné menu.
- **Kroky testu:**
  1. Bez zadania hodnoty stlačte Enter.
- **Očakávaný výsledok:** Program vypíše upozornenie o neplatnej voľbe a znova zobrazí `[MENU]`.
- **Skutočný výsledok:** Vypísalo sa upozornenie a znova sa zobrazilo hlavné menu.
- **Stav:** Pass
- **Poznámky:** Častá situácia pri náhodnom stlačení klávesu Enter.

### TC09: Záporné a desatinné číslo
- **Typ:** Negatívny
- **Popis:** Overenie, že záporné a desatinné čísla sú odmietnuté.
- **Vstupné podmienky:** Program zobrazuje hlavné menu.
- **Kroky testu:**
  1. Zadajte `-1` a potvrďte klávesom Enter.
  2. Zadajte `1.0` a potvrďte klávesom Enter.
- **Očakávaný výsledok:** Po každom vstupe program vypíše upozornenie o neplatnej voľbe a znova zobrazí `[MENU]`.
- **Skutočný výsledok:** Po oboch vstupoch sa vypísalo upozornenie a znova sa zobrazilo hlavné menu.
- **Stav:** Pass
- **Poznámky:** Program akceptuje iba presné hodnoty `1`, `2`, `3`, `4`.

### TC10: Opakované neplatné voľby a následne platná voľba
- **Typ:** Negatívny
- **Popis:** Overenie, že po viacerých neplatných pokusoch program stále funguje a akceptuje platnú voľbu.
- **Vstupné podmienky:** Program zobrazuje hlavné menu.
- **Kroky testu:**
  1. Zadajte postupne `0`, `abc`, `5`.
  2. Zadajte `4`.
- **Očakávaný výsledok:** Po každom neplatnom vstupe sa zobrazí upozornenie a menu. Po zadaní `4` sa program ukončí.
- **Skutočný výsledok:** Po neplatných vstupoch sa zobrazilo upozornenie a menu, voľba `4` program ukončila.
- **Stav:** Pass
- **Poznámky:** Overuje, že program sa po chybe nezasekne a nemá obmedzený počet pokusov.

### TC11: Voľba s medzerami okolo čísla
- **Typ:** Hraničný
- **Popis:** Overenie, že medzery pred a za číslom sú ignorované.
- **Vstupné podmienky:** Program zobrazuje hlavné menu.
- **Kroky testu:**
  1. Zadajte ` 2 ` (medzera, číslo 2, medzera) a potvrďte klávesom Enter.
- **Očakávaný výsledok:** Program vstup akceptuje ako voľbu 2 a spustí `zobrazit_ulohy()`.
- **Skutočný výsledok:** Spustilo sa zobrazenie úloh („Zoznam úloh je prázdny.“).
- **Stav:** Pass
- **Poznámky:** Program odstraňuje medzery metódou `.strip()`. Zvyšuje to používateľskú prívetivosť.

---

## 2. Funkcia `pridat_ulohu()`

### TC12: Pridanie prvej úlohy do prázdneho zoznamu
- **Typ:** Hraničný
- **Popis:** Overenie, že do prázdneho zoznamu je možné pridať prvú úlohu s platným názvom a popisom.
- **Vstupné podmienky:** Zoznam úloh je prázdny, program zobrazuje hlavné menu.
- **Kroky testu:**
  1. Zadajte `1`.
  2. Zadajte názov `Nákup`.
  3. Zadajte popis `mlieko`.
  4. V menu zadajte `2` na overenie.
- **Očakávaný výsledok:** Program vypíše „Úloha 'Nákup' bola pridaná.“, vráti sa do menu a pri zobrazení sa vypíše `1. Nákup - mlieko`.
- **Skutočný výsledok:** Úloha bola pridaná a v zozname sa zobrazila ako `1. Nákup - mlieko`.
- **Stav:** Pass
- **Poznámky:** Hraničný prípad – zoznam prechádza zo stavu „prázdny“ do stavu „obsahuje úlohy“.

### TC13: Pridanie ďalších úloh do neprázdneho zoznamu
- **Typ:** Pozitívny
- **Popis:** Overenie, že nové úlohy sa pridávajú na koniec zoznamu a poradie sa zachová.
- **Vstupné podmienky:** Zoznam úloh je prázdny.
- **Kroky testu:**
  1. Pridajte úlohy `A` (popis `a`), `B` (popis `b`), `C` (popis `c`).
  2. V menu zadajte `2`.
- **Očakávaný výsledok:** Zobrazia sa tri úlohy v poradí pridania: `1. A - a`, `2. B - b`, `3. C - c`.
- **Skutočný výsledok:** Zobrazili sa tri úlohy v správnom poradí.
- **Stav:** Pass
- **Poznámky:** Overuje, že pridanie novej úlohy neprepíše existujúce úlohy.

### TC14: Prázdny názov úlohy
- **Typ:** Negatívny
- **Popis:** Overenie, že úlohu nie je možné uložiť bez názvu.
- **Vstupné podmienky:** Zoznam úloh je prázdny, program zobrazuje hlavné menu.
- **Kroky testu:**
  1. Zadajte `1`.
  2. Pri názve iba stlačte Enter.
  3. Zadajte popis `popis`.
  4. Zadajte platný názov `N` a popis `P`.
- **Očakávaný výsledok:** Po kroku 3 program vypíše „Názov ani popis úlohy nemôže byť prázdny. Zadajte ich prosím znova.“ a znova si vyžiada názov aj popis. Úloha s prázdnym názvom sa neuloží. Po kroku 4 sa uloží úloha `N - P`.
- **Skutočný výsledok:** Zobrazilo sa upozornenie, program si vyžiadal oba údaje znova a uložila sa iba úloha `N - P`.
- **Stav:** Pass
- **Poznámky:** Požiadavka zo zadania – pri prázdnom vstupe sa zadáva znova názov aj popis.

### TC15: Prázdny popis úlohy
- **Typ:** Negatívny
- **Popis:** Overenie, že úlohu nie je možné uložiť bez popisu.
- **Vstupné podmienky:** Program zobrazuje hlavné menu.
- **Kroky testu:**
  1. Zadajte `1`.
  2. Zadajte názov `N`.
  3. Pri popise iba stlačte Enter.
  4. Zadajte platný názov `N` a popis `P`.
- **Očakávaný výsledok:** Po kroku 3 sa zobrazí upozornenie na prázdny vstup a program si vyžiada názov aj popis znova. Po kroku 4 sa úloha uloží.
- **Skutočný výsledok:** Zobrazilo sa upozornenie, po opakovanom zadaní sa úloha uložila.
- **Stav:** Pass
- **Poznámky:** Popis je povinný údaj rovnako ako názov.

### TC16: Prázdny názov aj popis
- **Typ:** Negatívny
- **Popis:** Overenie správania, keď používateľ nezadá ani názov, ani popis.
- **Vstupné podmienky:** Program zobrazuje hlavné menu.
- **Kroky testu:**
  1. Zadajte `1`.
  2. Pri názve aj popise iba stlačte Enter.
  3. Zadajte platný názov `N` a popis `P`.
- **Očakávaný výsledok:** Zobrazí sa jedno upozornenie na prázdny vstup a program si vyžiada oba údaje znova. Po kroku 3 sa úloha uloží.
- **Skutočný výsledok:** Zobrazilo sa upozornenie, po opakovanom zadaní sa úloha uložila.
- **Stav:** Pass
- **Poznámky:** Kombinácia oboch chybových stavov naraz.

### TC17: Názov tvorený iba medzerami
- **Typ:** Negatívny
- **Popis:** Overenie, že názov obsahujúci iba medzery sa považuje za prázdny.
- **Vstupné podmienky:** Program zobrazuje hlavné menu.
- **Kroky testu:**
  1. Zadajte `1`.
  2. Ako názov zadajte tri medzery `   `.
  3. Zadajte popis `P`.
  4. Zadajte platný názov `N` a popis `P`.
- **Očakávaný výsledok:** Po kroku 3 sa zobrazí upozornenie na prázdny vstup. Úloha s „neviditeľným“ názvom sa neuloží.
- **Skutočný výsledok:** Zobrazilo sa upozornenie, uložila sa iba úloha `N - P`.
- **Stav:** Pass
- **Poznámky:** Bez kontroly by v zozname vznikla úloha, ktorá vyzerá ako bez názvu. Program to rieši metódou `.strip()`.

### TC18: Názov a popis s diakritikou a špeciálnymi znakmi
- **Typ:** Pozitívny
- **Popis:** Overenie, že program správne uloží a zobrazí slovenskú diakritiku a špeciálne znaky.
- **Vstupné podmienky:** Zoznam úloh je prázdny.
- **Kroky testu:**
  1. Zadajte `1`.
  2. Ako názov zadajte `Žltý kôň @#&`.
  3. Ako popis zadajte `Ďaľší úpis 100% "ok"`.
  4. V menu zadajte `2`.
- **Očakávaný výsledok:** Úloha sa uloží a zobrazí ako `1. Žltý kôň @#& - Ďaľší úpis 100% "ok"` bez poškodených znakov.
- **Skutočný výsledok:** Úloha sa zobrazila presne v zadanom tvare.
- **Stav:** Pass
- **Poznámky:** Dôležité pre slovenských používateľov. Na Windowse môže zobrazenie závisieť od kódovania konzoly.

### TC19: Pridanie duplicitnej úlohy
- **Typ:** Hraničný
- **Popis:** Overenie správania pri pridaní úlohy s rovnakým názvom a popisom, aké už v zozname existujú.
- **Vstupné podmienky:** Zoznam úloh je prázdny.
- **Kroky testu:**
  1. Pridajte úlohu `A` s popisom `B`.
  2. Znova pridajte úlohu `A` s popisom `B`.
  3. V menu zadajte `2`.
- **Očakávaný výsledok:** Zadanie duplicity nezakazuje, preto sa uložia obe úlohy: `1. A - B` a `2. A - B`.
- **Skutočný výsledok:** Zobrazili sa dve rovnaké úlohy s číslami 1 a 2.
- **Stav:** Pass
- **Poznámky:** Správanie zodpovedá zadaniu. Ak by sa v budúcnosti duplicity zakazovali, test treba upraviť.

### TC20: Veľmi dlhý názov úlohy
- **Typ:** Hraničný
- **Popis:** Overenie, že program zvládne veľmi dlhý vstup.
- **Vstupné podmienky:** Program zobrazuje hlavné menu.
- **Kroky testu:**
  1. Zadajte `1`.
  2. Ako názov zadajte reťazec s dĺžkou 1000 znakov.
  3. Zadajte popis `B`.
- **Očakávaný výsledok:** Úloha sa uloží a program pokračuje hlavným menu bez chyby.
- **Skutočný výsledok:** Úloha s 1000-znakovým názvom bola pridaná, program pokračoval hlavným menu.
- **Stav:** Pass
- **Poznámky:** Zadanie neurčuje maximálnu dĺžku. Test overuje, že program pri dlhom vstupe nespadne.

---

## 3. Funkcia `zobrazit_ulohy()`

### TC21: Zobrazenie prázdneho zoznamu
- **Typ:** Hraničný
- **Popis:** Overenie, že pri prázdnom zozname program zobrazí zrozumiteľnú správu.
- **Vstupné podmienky:** Zoznam úloh je prázdny.
- **Kroky testu:**
  1. Zadajte `2`.
- **Očakávaný výsledok:** Program vypíše „Zoznam úloh je prázdny.“ a znova zobrazí `[MENU]`.
- **Skutočný výsledok:** Vypísalo sa „Zoznam úloh je prázdny.“ a zobrazilo sa hlavné menu.
- **Stav:** Pass
- **Poznámky:** Používateľ nesmie dostať prázdny výstup bez vysvetlenia.

### TC22: Zobrazenie jednej úlohy
- **Typ:** Pozitívny
- **Popis:** Overenie formátu výpisu pri jednej úlohe.
- **Vstupné podmienky:** V zozname je jedna úloha `Nákup – mlieko`.
- **Kroky testu:**
  1. Zadajte `2`.
- **Očakávaný výsledok:** Vypíše sa „Zoznam úloh:“ a riadok `1. Nákup - mlieko`.
- **Skutočný výsledok:** Vypísalo sa „Zoznam úloh:“ a `1. Nákup - mlieko`.
- **Stav:** Pass
- **Poznámky:** Overuje formát „číslo. názov - popis“.

### TC23: Zobrazenie viacerých úloh s číslovaním
- **Typ:** Pozitívny
- **Popis:** Overenie, že všetky úlohy sa zobrazia v poradí pridania a číslujú sa od 1.
- **Vstupné podmienky:** V zozname sú úlohy `A - a`, `B - b`, `C - c`.
- **Kroky testu:**
  1. Zadajte `2`.
- **Očakávaný výsledok:** Vypíšu sa riadky `1. A - a`, `2. B - b`, `3. C - c`.
- **Skutočný výsledok:** Zobrazili sa všetky tri úlohy so správnym číslovaním.
- **Stav:** Pass
- **Poznámky:** Číslovanie začína od 1 (nie od 0), aby bolo prirodzené pre používateľa.

### TC24: Prečíslovanie po odstránení úlohy
- **Typ:** Hraničný
- **Popis:** Overenie, že po odstránení úlohy zo stredu zoznamu sa ostatné úlohy prečíslujú bez medzier.
- **Vstupné podmienky:** V zozname sú úlohy `A - a`, `B - b`, `C - c`.
- **Kroky testu:**
  1. Zadajte `3` a odstráňte úlohu číslo `2`.
  2. Zadajte `2`.
- **Očakávaný výsledok:** Vypíšu sa riadky `1. A - a` a `2. C - c` (bez medzery v číslovaní).
- **Skutočný výsledok:** Zobrazilo sa `1. A - a` a `2. C - c`.
- **Stav:** Pass
- **Poznámky:** Číslovanie musí zodpovedať aktuálnemu stavu, inak by používateľ pri ďalšom odstraňovaní zadal nesprávne číslo.

### TC25: Návrat do hlavného menu po zobrazení
- **Typ:** Pozitívny
- **Popis:** Overenie, že po zobrazení úloh program pokračuje hlavným menu a zoznam ostane nezmenený.
- **Vstupné podmienky:** V zozname je aspoň jedna úloha.
- **Kroky testu:**
  1. Zadajte `2`.
  2. Znova zadajte `2`.
- **Očakávaný výsledok:** Po každom zobrazení sa objaví `[MENU]`. Oba výpisy sú zhodné – zobrazenie nemení obsah zoznamu.
- **Skutočný výsledok:** Po zobrazení sa vrátilo hlavné menu, oba výpisy boli zhodné.
- **Stav:** Pass
- **Poznámky:** Zobrazenie je operácia iba na čítanie a nesmie meniť dáta.

---

## 4. Funkcia `odstranit_ulohu()`

### TC26: Odstránenie z prázdneho zoznamu
- **Typ:** Hraničný
- **Popis:** Overenie správania, keď používateľ chce odstrániť úlohu a zoznam je prázdny.
- **Vstupné podmienky:** Zoznam úloh je prázdny.
- **Kroky testu:**
  1. Zadajte `3`.
- **Očakávaný výsledok:** Program vypíše „Zoznam úloh je prázdny.“ a „Nie je čo odstrániť.“ a vráti sa do `[MENU]` bez výzvy na zadanie čísla.
- **Skutočný výsledok:** Vypísali sa obe hlášky a zobrazilo sa hlavné menu.
- **Stav:** Pass
- **Poznámky:** Bez tejto kontroly by sa používateľ dostal do nekonečnej výzvy na zadanie čísla, ktoré nemôže existovať.

### TC27: Zobrazenie úloh pred odstránením
- **Typ:** Pozitívny
- **Popis:** Overenie, že pred výberom čísla sa používateľovi zobrazia všetky uložené úlohy.
- **Vstupné podmienky:** V zozname sú úlohy `A - a`, `B - b`, `C - c`.
- **Kroky testu:**
  1. Zadajte `3`.
- **Očakávaný výsledok:** Vypíše sa „Zoznam úloh:“ so všetkými tromi úlohami a výzva „Zadajte číslo úlohy, ktorú chcete odstrániť:“.
- **Skutočný výsledok:** Zobrazili sa všetky tri úlohy a výzva na zadanie čísla.
- **Stav:** Pass
- **Poznámky:** Požiadavka zo zadania – používateľ musí vidieť všetky uložené úlohy.

### TC28: Odstránenie úlohy zo stredu zoznamu
- **Typ:** Pozitívny
- **Popis:** Overenie, že sa odstráni práve vybraná úloha a ostatné zostanú.
- **Vstupné podmienky:** V zozname sú úlohy `A - a`, `B - b`, `C - c`.
- **Kroky testu:**
  1. Zadajte `3`.
  2. Zadajte číslo `2`.
  3. V menu zadajte `2`.
- **Očakávaný výsledok:** Program vypíše „Úloha 'B' bola odstránená.“ a vráti sa do menu. V zozname zostanú `1. A - a` a `2. C - c`.
- **Skutočný výsledok:** Úloha `B` bola odstránená, zostali úlohy `A` a `C`.
- **Stav:** Pass
- **Poznámky:** Overuje, že sa neodstráni nesprávna úloha (napr. posun indexu o 1).

### TC29: Odstránenie jedinej (poslednej zostávajúcej) úlohy
- **Typ:** Hraničný
- **Popis:** Overenie, že po odstránení jedinej úlohy je zoznam prázdny.
- **Vstupné podmienky:** V zozname je jedna úloha `A - a`.
- **Kroky testu:**
  1. Zadajte `3`.
  2. Zadajte číslo `1`.
  3. V menu zadajte `2`.
- **Očakávaný výsledok:** Program vypíše „Úloha 'A' bola odstránená.“. Pri zobrazení sa vypíše „Zoznam úloh je prázdny.“.
- **Skutočný výsledok:** Úloha bola odstránená a zoznam bol prázdny.
- **Stav:** Pass
- **Poznámky:** Hraničný prípad – zoznam prechádza zo stavu „obsahuje úlohy“ do stavu „prázdny“.

### TC30: Odstránenie prvej a poslednej úlohy v zozname
- **Typ:** Hraničný
- **Popis:** Overenie odstránenia úloh na okrajoch zoznamu (najnižšie a najvyššie číslo).
- **Vstupné podmienky:** V zozname sú úlohy `A - a`, `B - b`, `C - c`.
- **Kroky testu:**
  1. Zadajte `3` a odstráňte úlohu číslo `3`.
  2. Zadajte `3` a odstráňte úlohu číslo `1`.
  3. V menu zadajte `2`.
- **Očakávaný výsledok:** Najprv sa odstráni úloha `C`, potom úloha `A`. V zozname zostane iba `1. B - b`.
- **Skutočný výsledok:** Odstránili sa úlohy `C` a `A`, zostala úloha `1. B - b`.
- **Stav:** Pass
- **Poznámky:** Okraje zoznamu sú typické miesto chýb pri práci s indexmi.

### TC31: Zadanie neexistujúceho čísla úlohy
- **Typ:** Negatívny
- **Popis:** Overenie, že pri zadaní čísla väčšieho ako počet úloh je používateľ upozornený.
- **Vstupné podmienky:** V zozname je jedna úloha `A - a`.
- **Kroky testu:**
  1. Zadajte `3`.
  2. Zadajte číslo `5`.
  3. Zadajte číslo `1`.
- **Očakávaný výsledok:** Po kroku 2 program vypíše „Úloha s číslom '5' neexistuje. Zadajte číslo od 1 do 1.“ a vyžiada si číslo znova. Žiadna úloha sa neodstráni. Po kroku 3 sa úloha `A` odstráni.
- **Skutočný výsledok:** Zobrazilo sa upozornenie, po zadaní `1` sa úloha odstránila.
- **Stav:** Pass
- **Poznámky:** Požiadavka zo zadania – upozornenie pri výbere neexistujúcej úlohy. Program nesmie spadnúť na `IndexError`.

### TC32: Zadanie čísla 0 a záporného čísla
- **Typ:** Negatívny
- **Popis:** Overenie, že čísla menšie ako 1 sú odmietnuté.
- **Vstupné podmienky:** V zozname je jedna úloha `A - a`.
- **Kroky testu:**
  1. Zadajte `3`.
  2. Zadajte `0`.
  3. Zadajte `-1`.
  4. Zadajte `1`.
- **Očakávaný výsledok:** Po krokoch 2 a 3 sa zobrazí upozornenie, že úloha neexistuje, a žiadna úloha sa neodstráni.
- **Skutočný výsledok:** Po oboch vstupoch sa zobrazilo upozornenie, úloha `A` sa odstránila až po zadaní `1`.
- **Stav:** Pass
- **Poznámky:** Dôležitý test – v Pythone index `-1` znamená poslednú položku zoznamu. Bez kontroly by sa omylom odstránila posledná úloha.

### TC33: Zadanie textu namiesto čísla
- **Typ:** Negatívny
- **Popis:** Overenie, že textový vstup pri odstraňovaní nespôsobí pád programu.
- **Vstupné podmienky:** V zozname je jedna úloha `A - a`.
- **Kroky testu:**
  1. Zadajte `3`.
  2. Zadajte `abc`.
  3. Zadajte `1`.
- **Očakávaný výsledok:** Po kroku 2 sa zobrazí upozornenie, že úloha neexistuje, a program si vyžiada číslo znova.
- **Skutočný výsledok:** Zobrazilo sa upozornenie „Úloha s číslom 'abc' neexistuje. Zadajte číslo od 1 do 1.“, program pokračoval.
- **Stav:** Pass
- **Poznámky:** Program nesmie spadnúť na `ValueError` pri prevode textu na číslo.

### TC34: Prázdny vstup pri odstraňovaní
- **Typ:** Negatívny
- **Popis:** Overenie reakcie na stlačenie klávesu Enter bez zadania čísla.
- **Vstupné podmienky:** V zozname je jedna úloha `A - a`.
- **Kroky testu:**
  1. Zadajte `3`.
  2. Bez zadania hodnoty stlačte Enter.
  3. Zadajte `1`.
- **Očakávaný výsledok:** Po kroku 2 sa zobrazí upozornenie a program si vyžiada číslo znova. Žiadna úloha sa neodstráni.
- **Skutočný výsledok:** Zobrazilo sa upozornenie „Úloha s číslom '' neexistuje. Zadajte číslo od 1 do 1.“, program pokračoval.
- **Stav:** Pass
- **Poznámky:** Funkčne správne. Text hlášky s prázdnymi úvodzovkami `''` je menej zrozumiteľný – pozri zistenie Z2.

### TC35: Číslo zadané s úvodnou nulou (01)
- **Typ:** Hraničný
- **Popis:** Overenie, ako program interpretuje číslo s úvodnou nulou.
- **Vstupné podmienky:** V zozname sú úlohy `A - a` a `B - b`.
- **Kroky testu:**
  1. Zadajte `3`.
  2. Zadajte `01`.
  3. V menu zadajte `2`.
- **Očakávaný výsledok:** Vstup `01` sa interpretuje ako číslo 1, odstráni sa úloha `A`. V zozname zostane `1. B - b`.
- **Skutočný výsledok:** Odstránila sa úloha `A`, zostala úloha `1. B - b`.
- **Stav:** Pass
- **Poznámky:** Pozor na rozdiel oproti hlavnému menu, kde je `01` neplatná voľba (porovnáva sa text, nie číslo). Obe správania sú prijateľné, ale je dobré o nich vedieť.

---

## Zistenia a odporúčania

Nasledujúce body nie sú chybami podľa zadania, ale počas testovania sa ukázali ako možné vylepšenia.

| ID | Zistenie | Závažnosť | Odporúčanie |
|---|---|---|---|
| Z1 | Pri odstraňovaní nie je možné akciu zrušiť. Používateľ musí zadať platné číslo, inak sa nedostane späť do menu. | Nízka | Pridať možnosť zrušenia, napr. zadaním `0` alebo prázdneho vstupu. |
| Z2 | Pri prázdnom vstupe sa zobrazí hláška `Úloha s číslom '' neexistuje.` | Kozmetická | Pre prázdny vstup zobraziť samostatnú hlášku, napr. „Nezadali ste žiadne číslo.“ |
| Z3 | Ukončenie cez `Ctrl + C` alebo `Ctrl + Z` (koniec vstupu) skončí chybovým výpisom `KeyboardInterrupt` / `EOFError`. | Nízka | Ošetriť výnimky v `hlavne_menu()` a vypísať „Koniec programu.“ |
| Z4 | Úlohy sa ukladajú iba do pamäte, po ukončení programu sa stratia. | Informatívna | Zodpovedá zadaniu. Do budúcna možné ukladanie do súboru (JSON) alebo databázy. |

## Súhrn výsledkov

| Stav | Počet |
|---|---|
| Pass | 35 |
| Fail | 0 |
| **Spolu** | **35** |
