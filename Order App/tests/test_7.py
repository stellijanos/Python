# 7. Einlesen und Konvertieren einer Bestellunginstanz aus einer Datei

from repository.OrderRepo import OrderRepo
from modelle.Bestellung import Bestellung


def test_order_repo_load():
    # Create an OrderRepo instance
    repo = OrderRepo('tests/test.txt')

    # Load the contents of the file
    result = repo.load()

    # Create a Bestellung instance with sample data
    expected = [Bestellung("0", "1", ['Pizza', 'Pasta'], ['Coke', 'Water'], [20, 15, 5, 7])]

    # Assert that the file contains the expected data
    try:
        assert result == expected
    except AssertionError:
        print('Test 7 failed!')
    else:
        print('Test 7 succeded!')
