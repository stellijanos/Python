from modelle.GekochterGericht import GekochterGericht
from modelle.Getrank import Getrank


# 1. Hinzufügen eines Gerichts

def test_add_gekochterGericht():
    result = [GekochterGericht('Schnitzel', 300, 10, 60), GekochterGericht('Fisch', 150, 5, 30)]
    expected = [GekochterGericht('Schnitzel', 300, 10, 60), GekochterGericht('Fisch', 150, 5, 30),
                GekochterGericht('Pizza', 500, 15, 40)]
    result.append(GekochterGericht('Pizza', 500, 15, 40))
    try:
        assert result == expected
    except AssertionError:
        print("Test 1 case 1 failed!")
    else:
        print("Test 1 case 1 succeded!")


def test_add_getrank():
    result = [Getrank('Wasser', 500, 5, 0), Getrank('Bier', 400, 10, 15)]
    expected = [Getrank('Wasser', 500, 5, 0), Getrank('Bier', 400, 10, 15), Getrank('Cola', 500, 7, 0)]
    result.append(Getrank('Cola', 500, 7, 0))
    try:
        assert result == expected
    except AssertionError:
        print("Test 1 case 2 failed!")
    else:
        print("Test 1 case 2 succeded!")
