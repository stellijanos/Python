# 6. Konvertierung und Speicherung einer Bestellunginstanz in einer Datei

import json
from repository.OrderRepo import OrderRepo
from modelle.Bestellung import Bestellung


def test_order_repo_save():
    # Create a Bestellung instance with sample data
    bestellung = Bestellung("0", "1", ['Pizza', 'Pasta'], ['Coke', 'Water'], [20, 15, 5, 7])

    # Create an OrderRepo instance
    repo = OrderRepo('tests/test.txt')

    # Save the Bestellung instance to the file
    repo.save([bestellung])

    # Read the contents of the file
    with open('tests/test.txt', 'r') as f:
        file_contents = f.read()

    # Assert that the file contains the expected data
    expected_data = [
        {
            "ID": "0",
            "Kunden ID": "1",
            "Name Gericht": [
                "Pizza",
                "Pasta"
            ],
            "Name Getrank": [
                "Coke",
                "Water"
            ],
            "Gesamtkosten": 47
        }
    ]
    try:
        assert json.loads(file_contents) == expected_data
    except AssertionError:
        print('Test 6 failed!')
    else:
        print('Test 6 succeded!')
