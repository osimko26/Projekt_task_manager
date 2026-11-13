"""
Automatické testy pre projekt Správca úloh.
Testy zodpovedajú testovacím prípadom TC01 až TC35 v súbore test_cases_ondrej.md.
"""
import pytest
import task_manager_ondrej as tm  # ak sa tvoj súbor volá inak, zmeň názov modulu tu

MENU_NADPIS = "Správca úloh - hlavné menu"
NEPLATNA_VOLBA = "Neplatná voľba, zadajte prosím číslo od 1 do 4."
PRAZDNY_VSTUP = "Názov ani popis úlohy nemôže byť prázdny. Zadajte ich prosím znova."
PRAZDNY_ZOZNAM = "Zoznam úloh je prázdny."

# ---------------------------------------------------------------------------
# Pomocné fixtures
# ---------------------------------------------------------------------------

@pytest.fixture(autouse=True)
def prazdny_zoznam():
    """Pred každým testom aj po ňom vyprázdni zoznam úloh, aby boli testy nezávislé."""
    tm.ulohy.clear()
    yield
    tm.ulohy.clear()


@pytest.fixture
def vstupy(monkeypatch):
    """
    Nahradí funkciu input() zoznamom pripravených vstupov.
    Ak program žiada viac vstupov, než test pripravil, test zlyhá
    (namiesto toho, aby sa program zasekol v nekonečnom cykle).
    """
    def nastav(*hodnoty):
        zostavajuce = list(hodnoty)

        def falosny_input(vyzva=""):
            print(vyzva, end="")
            if not zostavajuce:
                raise AssertionError(f"Program žiadal ďalší vstup navyše: {vyzva!r}")
            return zostavajuce.pop(0)

        monkeypatch.setattr("builtins.input", falosny_input)
        return zostavajuce

    return nastav


def pridaj(*ulohy):
    """Priamo naplní zoznam úloh (vstupná podmienka testu)."""
    for nazov, popis in ulohy:
        tm.ulohy.append({"nazov": nazov, "popis": popis})


def nazvy():
    """Vráti názvy úloh v aktuálnom poradí."""
    return [u["nazov"] for u in tm.ulohy]


# ---------------------------------------------------------------------------
# 1. hlavne_menu()
# ---------------------------------------------------------------------------

def test_tc01_zobrazenie_menu(vstupy, capsys):
    vstupy("4")
    tm.hlavne_menu()
    vystup = capsys.readouterr().out
    assert MENU_NADPIS in vystup
    for riadok in ("1. Pridať novú úlohu", "2. Zobraziť všetky úlohy",
                   "3. Odstrániť úlohu", "4. Koniec programu",
                   "Vyberte jednu z možností (1-4):"):
        assert riadok in vystup


def test_tc02_volba_1_spusti_pridanie(vstupy, capsys):
    vstupy("1", "Úloha", "Popis", "4")
    tm.hlavne_menu()
    assert "Zadajte názov úlohy:" in capsys.readouterr().out
    assert nazvy() == ["Úloha"]


def test_tc03_volba_2_spusti_zobrazenie(vstupy, capsys):
    vstupy("2", "4")
    tm.hlavne_menu()
    vystup = capsys.readouterr().out
    assert PRAZDNY_ZOZNAM in vystup
    assert vystup.count(MENU_NADPIS) == 2  # menu sa po zobrazení znova ukázalo


def test_tc04_volba_3_spusti_odstranenie(vstupy, capsys):
    vstupy("3", "4")
    tm.hlavne_menu()
    vystup = capsys.readouterr().out
    assert "Nie je čo odstrániť." in vystup
    assert vystup.count(MENU_NADPIS) == 2


def test_tc05_volba_4_ukonci_program(vstupy, capsys):
    zostavajuce = vstupy("4")
    tm.hlavne_menu()  # funkcia sa musí vrátiť, nie zaseknúť
    assert "Koniec programu." in capsys.readouterr().out
    assert zostavajuce == []


@pytest.mark.parametrize("volba", ["0", "5"])
def test_tc06_cislo_mimo_rozsahu(vstupy, capsys, volba):
    vstupy(volba, "4")
    tm.hlavne_menu()
    assert NEPLATNA_VOLBA in capsys.readouterr().out


@pytest.mark.parametrize("volba", ["l", "a"])
def test_tc07_pismeno_namiesto_cisla(vstupy, capsys, volba):
    vstupy(volba, "4")
    tm.hlavne_menu()
    assert NEPLATNA_VOLBA in capsys.readouterr().out


def test_tc08_prazdny_vstup_v_menu(vstupy, capsys):
    vstupy("", "4")
    tm.hlavne_menu()
    assert NEPLATNA_VOLBA in capsys.readouterr().out


@pytest.mark.parametrize("volba", ["-1", "1.0"])
def test_tc09_zaporne_a_desatinne_cislo(vstupy, capsys, volba):
    vstupy(volba, "4")
    tm.hlavne_menu()
    assert NEPLATNA_VOLBA in capsys.readouterr().out
    assert tm.ulohy == []  # "1.0" nesmie spustiť pridanie úlohy


def test_tc10_opakovane_neplatne_volby(vstupy, capsys):
    vstupy("0", "abc", "5", "4")
    tm.hlavne_menu()
    vystup = capsys.readouterr().out
    assert vystup.count(NEPLATNA_VOLBA) == 3
    assert "Koniec programu." in vystup


def test_tc11_volba_s_medzerami(vstupy, capsys):
    vstupy(" 2 ", "4")
    tm.hlavne_menu()
    vystup = capsys.readouterr().out
    assert PRAZDNY_ZOZNAM in vystup
    assert NEPLATNA_VOLBA not in vystup


# ---------------------------------------------------------------------------
# 2. pridat_ulohu()
# ---------------------------------------------------------------------------

def test_tc12_pridanie_prvej_ulohy(vstupy, capsys):
    vstupy("Nákup", "mlieko")
    tm.pridat_ulohu()
    assert tm.ulohy == [{"nazov": "Nákup", "popis": "mlieko"}]
    assert "Úloha 'Nákup' bola pridaná." in capsys.readouterr().out


def test_tc13_pridanie_dalsich_uloh_zachova_poradie(vstupy):
    vstupy("A", "a", "B", "b", "C", "c")
    tm.pridat_ulohu()
    tm.pridat_ulohu()
    tm.pridat_ulohu()
    assert nazvy() == ["A", "B", "C"]


def test_tc14_prazdny_nazov(vstupy, capsys):
    vstupy("", "popis", "N", "P")
    tm.pridat_ulohu()
    assert PRAZDNY_VSTUP in capsys.readouterr().out
    assert tm.ulohy == [{"nazov": "N", "popis": "P"}]


def test_tc15_prazdny_popis(vstupy, capsys):
    vstupy("N", "", "N", "P")
    tm.pridat_ulohu()
    assert PRAZDNY_VSTUP in capsys.readouterr().out
    assert tm.ulohy == [{"nazov": "N", "popis": "P"}]


def test_tc16_prazdny_nazov_aj_popis(vstupy, capsys):
    vstupy("", "", "N", "P")
    tm.pridat_ulohu()
    assert capsys.readouterr().out.count(PRAZDNY_VSTUP) == 1
    assert len(tm.ulohy) == 1


def test_tc17_nazov_iba_z_medzier(vstupy, capsys):
    vstupy("   ", "P", "N", "P")
    tm.pridat_ulohu()
    assert PRAZDNY_VSTUP in capsys.readouterr().out
    assert nazvy() == ["N"]


def test_tc18_diakritika_a_specialne_znaky(vstupy, capsys):
    vstupy("Žltý kôň @#&", 'Ďaľší úpis 100% "ok"')
    tm.pridat_ulohu()
    tm.zobrazit_ulohy()
    assert '1. Žltý kôň @#& - Ďaľší úpis 100% "ok"' in capsys.readouterr().out


def test_tc19_duplicitna_uloha(vstupy):
    vstupy("A", "B", "A", "B")
    tm.pridat_ulohu()
    tm.pridat_ulohu()
    assert tm.ulohy == [{"nazov": "A", "popis": "B"}, {"nazov": "A", "popis": "B"}]


def test_tc20_velmi_dlhy_nazov(vstupy):
    dlhy = "x" * 1000
    vstupy(dlhy, "B")
    tm.pridat_ulohu()
    assert tm.ulohy[0]["nazov"] == dlhy


# ---------------------------------------------------------------------------
# 3. zobrazit_ulohy()
# ---------------------------------------------------------------------------

def test_tc21_prazdny_zoznam(capsys):
    assert tm.zobrazit_ulohy() is False
    assert PRAZDNY_ZOZNAM in capsys.readouterr().out


def test_tc22_jedna_uloha(capsys):
    pridaj(("Nákup", "mlieko"))
    assert tm.zobrazit_ulohy() is True
    vystup = capsys.readouterr().out
    assert "Zoznam úloh:" in vystup
    assert "1. Nákup - mlieko" in vystup


def test_tc23_viac_uloh_s_cislovanim(capsys):
    pridaj(("A", "a"), ("B", "b"), ("C", "c"))
    tm.zobrazit_ulohy()
    vystup = capsys.readouterr().out
    assert "1. A - a\n2. B - b\n3. C - c" in vystup


def test_tc24_precislovanie_po_odstraneni(vstupy, capsys):
    pridaj(("A", "a"), ("B", "b"), ("C", "c"))
    vstupy("2")
    tm.odstranit_ulohu()
    capsys.readouterr()  # zahodí výstup z odstraňovania
    tm.zobrazit_ulohy()
    vystup = capsys.readouterr().out
    assert "1. A - a\n2. C - c" in vystup
    assert "3." not in vystup


def test_tc25_zobrazenie_nemeni_zoznam(vstupy, capsys):
    pridaj(("A", "a"))
    povodny = [dict(u) for u in tm.ulohy]
    vstupy("2", "2", "4")
    tm.hlavne_menu()
    vystup = capsys.readouterr().out
    assert vystup.count("1. A - a") == 2
    assert tm.ulohy == povodny


# ---------------------------------------------------------------------------
# 4. odstranit_ulohu()
# ---------------------------------------------------------------------------

def test_tc26_odstranenie_z_prazdneho_zoznamu(vstupy, capsys):
    vstupy()  # žiadny vstup – program sa nesmie pýtať na číslo
    tm.odstranit_ulohu()
    vystup = capsys.readouterr().out
    assert PRAZDNY_ZOZNAM in vystup
    assert "Nie je čo odstrániť." in vystup


def test_tc27_zobrazenie_uloh_pred_odstranenim(vstupy, capsys):
    pridaj(("A", "a"), ("B", "b"), ("C", "c"))
    vstupy("1")
    tm.odstranit_ulohu()
    vystup = capsys.readouterr().out
    zoznam = vystup.index("1. A - a\n2. B - b\n3. C - c")
    vyzva = vystup.index("Zadajte číslo úlohy, ktorú chcete odstrániť:")
    assert zoznam < vyzva  # úlohy sa zobrazia ešte pred výzvou


def test_tc28_odstranenie_zo_stredu(vstupy, capsys):
    pridaj(("A", "a"), ("B", "b"), ("C", "c"))
    vstupy("2")
    tm.odstranit_ulohu()
    assert "Úloha 'B' bola odstránená." in capsys.readouterr().out
    assert nazvy() == ["A", "C"]


def test_tc29_odstranenie_jedinej_ulohy(vstupy):
    pridaj(("A", "a"))
    vstupy("1")
    tm.odstranit_ulohu()
    assert tm.ulohy == []


def test_tc30_odstranenie_poslednej_a_prvej(vstupy):
    pridaj(("A", "a"), ("B", "b"), ("C", "c"))
    vstupy("3")
    tm.odstranit_ulohu()
    vstupy("1")
    tm.odstranit_ulohu()
    assert nazvy() == ["B"]


def test_tc31_neexistujuce_cislo(vstupy, capsys):
    pridaj(("A", "a"))
    vstupy("5", "1")
    tm.odstranit_ulohu()
    assert "Úloha s číslom '5' neexistuje. Zadajte číslo od 1 do 1." in capsys.readouterr().out
    assert tm.ulohy == []


@pytest.mark.parametrize("cislo", ["0", "-1"])
def test_tc32_nula_a_zaporne_cislo(vstupy, capsys, cislo):
    pridaj(("A", "a"), ("B", "b"))
    vstupy(cislo, "1")
    tm.odstranit_ulohu()
    assert f"Úloha s číslom '{cislo}' neexistuje." in capsys.readouterr().out
    # -1 nesmie zmazať poslednú úlohu; zmaže sa až úloha 1 (A)
    assert nazvy() == ["B"]


def test_tc33_text_namiesto_cisla(vstupy, capsys):
    pridaj(("A", "a"))
    vstupy("abc", "1")
    tm.odstranit_ulohu()
    assert "Úloha s číslom 'abc' neexistuje." in capsys.readouterr().out
    assert tm.ulohy == []


def test_tc34_prazdny_vstup_pri_odstranovani(vstupy, capsys):
    pridaj(("A", "a"))
    vstupy("", "1")
    tm.odstranit_ulohu()
    assert "neexistuje" in capsys.readouterr().out
    assert tm.ulohy == []


def test_tc35_cislo_s_uvodnou_nulou(vstupy):
    pridaj(("A", "a"), ("B", "b"))
    vstupy("01")
    tm.odstranit_ulohu()
    assert nazvy() == ["B"]
