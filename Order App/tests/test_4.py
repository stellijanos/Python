from controller.controller import suchenKunde, aktualisieren_kunde_name
from modelle.Kunde import Kunde


# 4. Aktualisieren eines Kundennamens


def test_aktualisieren_kunde_name():
    # Test with empty list
    lista = []
    kunde_infos = Kunde("1", "Janos", "Caminul 16 Hasdeu")
    neue_name = "Peter"
    expected = []
    result = aktualisieren_kunde_name(lista, kunde_infos, neue_name)
    try:
        assert result == expected
    except AssertionError:
        print("Test 4 case 1 failed!")
    else:
        print("Test 4 case 1 succeeded!")

    # Test with non-empty list and no matching entries
    lista = [
        Kunde("2", "Dorian", "Cluj Str. Manastur")
    ]
    kunde_infos = Kunde("1", "Janos", "Caminul 16 Hasdeu")
    neue_name = "Popescu"
    expected = [Kunde("2", "Dorian", "Cluj Str. Manastur")]
    result = aktualisieren_kunde_name(lista, kunde_infos, neue_name)
    try:
        assert result == expected
    except AssertionError:
        print("Test 4 case 2 failed!")
    else:
        print("Test 4 case 2 succeeded!")

    # Test with non-empty list and one matching entry
    lista = [
        Kunde("1", "Janos", "Caminul 16 Hasdeu"),
        Kunde("2", "Dorian", "Cluj Str. Manastur"),
        Kunde("3", "Janos", "Str. Hasdeu")
    ]
    kunde_infos = Kunde("1", "Janos", "Caminul 16 Hasdeu")
    neue_name = "Alexandru"
    expected = [Kunde("1", "Alexandru", "Caminul 16 Hasdeu"), Kunde("2", "Dorian", "Cluj Str. Manastur"),
                Kunde("3", "Janos", "Str. Hasdeu")]
    result = aktualisieren_kunde_name(lista, kunde_infos, neue_name)
    try:
        assert result == expected
    except AssertionError:
        print("Test 4 case 3 failed!")
    else:
        print("Test 4 case 3 succeeded!")
