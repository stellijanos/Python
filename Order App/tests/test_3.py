from controller.controller import suchenKunde, aktualisieren_kunde_name
from modelle.Kunde import Kunde


# 3. Suche nach einem Kunden anhand seiner Teiladresse
def test_suchenKunde_adresse():
    # Test with empty list
    Kundenliste = []
    query = "Str. Ploiesti"
    expected = []
    result = suchenKunde(Kundenliste, query)
    try:
        assert result == expected
    except AssertionError:
        print("Test 3 case 1 failed!")
    else:
        print("Test 3 case 1 succeeded!")

    # Test with non-empty list and no matches
    Kundenliste = [
        Kunde("1", "Janos", "Caminul 16 Hasdeu"),
        Kunde("2", "Dorian", "Cluj Str. Manastur")
    ]
    query = "const"
    expected = []
    result = suchenKunde(Kundenliste, query)
    try:
        assert result == expected
    except AssertionError:
        print("Test 3 case 2 failed!")
    else:
        print("Test 3 case 2 succeeded!")

    # Test with non-empty list and one match
    Kundenliste = [
        Kunde("1", "Janos", "Caminul 16 Hasdeu"),
        Kunde("2", "Dorian", "Cluj Str. Manastur")
    ]
    query = "hasd"
    expected = [Kunde("1", "Janos", "Caminul 16 Hasdeu")]
    result = suchenKunde(Kundenliste, query)
    try:
        assert result == expected
    except AssertionError:
        print("Test 3 case 3 failed!")
    else:
        print("Test 3 case 3 succeeded!")

    # Test with non-empty list and multiple matches
    Kundenliste = [
        Kunde("1", "Janos", "Caminul 16 Hasdeu"),
        Kunde("2", "Dorian", "Cluj Str. Manastur"),
        Kunde("3", "Janos", "Str. Manastur")
    ]
    query = "Manastur"
    expected = [Kunde("2", "Dorian", "Cluj Str. Manastur"), Kunde("3", "Janos", "Str. Manastur")]
    result = suchenKunde(Kundenliste, query)
    try:
        assert result == expected
    except AssertionError:
        print("Test 3 case 4 failed!")
    else:
        print("Test 3 case 4 succeeded!")

    # Test with non-empty list and multiple matches, but case-insensitive
    Kundenliste = [
        Kunde("1", "Janos", "Caminul 16 Hasdeu"),
        Kunde("2", "Dorian", "Cluj Str. Manastur"),
        Kunde("3", "Ion", "Str. Hasdeu")
    ]
    query = "sDeU"
    expected = [Kunde("1", "Janos", "Caminul 16 Hasdeu"), Kunde("3", "Ion", "Str. Hasdeu")]
    result = suchenKunde(Kundenliste, query)
    try:
        assert result == expected
    except AssertionError:
        print("Test 3 case 5 failed!")
    else:
        print("Test 3 case 5 succeeded!")
