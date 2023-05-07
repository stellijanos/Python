from controller.controller import suchenKunde, aktualisieren_kunde_name
from modelle.Kunde import Kunde


# 2. Suche nach einem Kunden anhand seines Teilnamens


def test_suchenKunde_name():
    # Test with empty list
    Kundenliste = []
    query = "Janos"
    expected = []
    result = suchenKunde(Kundenliste, query)
    try:
        assert result == expected
    except AssertionError:
        print("Test 2 case 1 failed!")
    else:
        print("Test 2 case 1 succeeded!")

    # Test with non-empty list and no matches
    Kundenliste = [
        Kunde("1", "Janos", "Caminul 16 Hasdeu"),
        Kunde("2", "Dorian", "Cluj Str. Manastur")
    ]
    query = "Alex"
    expected = []
    result = suchenKunde(Kundenliste, query)
    try:
        assert result == expected
    except AssertionError:
        print("Test 2 case 2 failed!")
    else:
        print("Test 2 case 2 succeeded!")

    # Test with non-empty list and one match
    Kundenliste = [
        Kunde("1", "Janos", "Caminul 16 Hasdeu"),
        Kunde("2", "Dorian", "Cluj Str. Manastur")
    ]
    query = "jan"
    expected = [Kunde("1", "Janos", "Caminul 16 Hasdeu")]
    result = suchenKunde(Kundenliste, query)
    try:
        assert result == expected
    except AssertionError:
        print("Test 2 case 3 failed!")
    else:
        print("Test 2 case 3 succeeded!")

    # Test with non-empty list and multiple matches
    Kundenliste = [
        Kunde("1", "Janos", "Caminul 16 Hasdeu"),
        Kunde("2", "Dorian", "Cluj Str. Manastur"),
        Kunde("3", "Janos", "Str. Ploiesti")
    ]
    query = "Janos"
    expected = [Kunde("1", "Janos", "Caminul 16 Hasdeu"), Kunde("3", "Janos", "Str. Ploiesti")]
    result = suchenKunde(Kundenliste, query)
    try:
        assert result == expected
    except AssertionError:
        print("Test 2 case 4 failed!")
    else:
        print("Test 2 case 4 succeeded!")

    # Test with non-empty list and multiple matches, but case-insensitive
    Kundenliste = [
        Kunde("1", "Janos", "Caminul 16 Hasdeu"),
        Kunde("2", "Dorian", "Cluj Str. Manastur"),
        Kunde("3", "Janos", "Str. Ploiesti")
    ]
    query = "jaN"
    expected = [Kunde("1", "Janos", "Caminul 16 Hasdeu"), Kunde("3", "Janos", "Str. Ploiesti")]
    result = suchenKunde(Kundenliste, query)
    try:
        assert result == expected
    except AssertionError:
        print("Test 2 case 5 failed!")
    else:
        print("Test 2 case 5 succeeded!")
