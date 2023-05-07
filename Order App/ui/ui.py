from controller.controller import print_gekochterGericht, add_gekochterGericht, delete_gekochterGericht, print_getrank, \
    add_getrank, delete_getrank, print_customer, search_customer, add_customer, update_customer_name, \
    update_customer_address, delete_customer, make_an_order
from tests.test_1 import test_add_gekochterGericht, test_add_getrank
from tests.test_2 import test_suchenKunde_name
from tests.test_3 import test_suchenKunde_adresse
from tests.test_4 import test_aktualisieren_kunde_name
from tests.test_5 import test_anzeigeRechnung
from tests.test_6 import test_order_repo_save
from tests.test_7 import test_order_repo_load


def menu():
    return '''
    Restaurant app Version 1.0

    Mogliche Optionen:

    0 - Exit
    1 - Bestellung machen 
    2 - Speisekarte Optionen
    3 - Kunden Optionen 
    4 - Funktionen testen
    
    '''


def subMenu1():
    make_an_order()


def subMenu2():
    while True:
        print('''

    0 - Exit/Back
    Gekochter Gerichte Optionen:             Getranke Optionen:
    1 - anzeigen                             4 - anzeigen
    2 - hinzufugen                           5 - hinzufugen
    3 - loschen                              6 - loschen
    ''')
        opt = int(input("Wahlen Sie bitte ein Option aus: "))
        if opt == 0: break
        if opt == 1: print_gekochterGericht()
        if opt == 2: add_gekochterGericht()
        if opt == 3: delete_gekochterGericht()
        if opt == 4: print_getrank()
        if opt == 5: add_getrank()
        if opt == 6: delete_getrank()


def subMenu3():
    while True:
        print('''
            0 - Exit/Back 
            1 - Kunden anzeigen 
            2 - Kunde suchen
            3 - Kunde hinzufugen 
            4 - Kunde Name aktualisieren
            5 - Kunde Adresse aktualisieren
            6 - Kunde loschen 
            ''')
        opt = int(input('Geben Sie bitte ein Option ein: '))
        if opt == 0: break
        if opt == 1: print_customer()
        if opt == 2: search_customer()
        if opt == 3: add_customer()
        if opt == 4: update_customer_name()
        if opt == 5: update_customer_address()
        if opt == 6: delete_customer()

def subMenu4():
    print('\n1. Hinzufügen eines Gerichts:')
    test_add_gekochterGericht()
    test_add_getrank()
    print('\n2. Suche nach einem Kunden anhand seines Teilnamens testen: ')
    test_suchenKunde_name()
    print('\n3. Suche nach einem Kunden anhand seiner Teiladresse testen: ')
    test_suchenKunde_adresse()
    print('\n4. Aktualisieren eines Kundennamens testen:')
    test_aktualisieren_kunde_name()
    print('\n5. Generierung des Strings, der die Rechnung darstellt')
    test_anzeigeRechnung()
    print('\n6. Konvertierung und Speicherung einer Bestellunginstanz in einer Datei')
    test_order_repo_save()
    print('\n7. Einlesen und Konvertieren einer Bestellunginstanz aus einer Datei')
    test_order_repo_load()
    print('\nEnd of tests')

def main():
    while True:
        print(menu())
        opt = int(input('Geben Sie von der Tastatur die Nummer der Option an: '))
        if opt == 0: break
        if opt == 1: subMenu1()
        if opt == 2: subMenu2()
        if opt == 3: subMenu3()
        if opt == 4: subMenu4()