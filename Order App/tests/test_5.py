# 5. Generierung des Strings, der die Rechnung darstellt

from modelle.Bestellung import Bestellung


def test_anzeigeRechnung():
    # Create an instance of the Bestellung class
    order = Bestellung("1", "134bdh", ['Schnitzel', 'Pizza'], ['Cola,Fanta'], [15, 20, 5, 5])
    result = order.returnRechnung()  # result will have the output returned

    # Assert that the anzeigeRechnung() method produced the expected output
    expected = "----------------------------\nRECHNUNG\n\nGerichte: Schnitzel, Pizza\nGetranke: Cola,Fanta\nGesamtkosten: 45 Euro\n----------------------------"

    try:
        assert result == expected
    except AssertionError:
        print('Test 5 failed!')
    else:
        print('Test 5 succeded!')
