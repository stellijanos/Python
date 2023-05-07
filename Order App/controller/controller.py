import hashlib
from modelle.Bestellung import Bestellung
from modelle.GekochterGericht import GekochterGericht
from modelle.Getrank import Getrank
from modelle.Kunde import Kunde
from repository.CookedDishRepo import CookedDishRepo
from repository.CustomerRepo import CustomerRepo
from repository.DrinkRepo import DrinkRepo
from repository.OrderRepo import OrderRepo


def suchenKunde(Kundenliste, query):  # query=interogare
    query = query.lower()
    return list(filter(lambda kunde: query in kunde.name.lower() or query in kunde.adresse.lower(), Kundenliste))


def loschen_kunde(kundenListe, loschen):
    return list(filter(lambda kunde: (kunde.name != loschen.name) or (kunde.adresse != loschen.adresse), kundenListe))


def loschen(jsonList, index):
    return list(filter(lambda x: jsonList.index(x) != index, jsonList))  # using filter
    # return [jsonList[i] for i in range(len(jsonList)) if i != value] -using list comprehension


def aktualisieren_kunde_name(lista, kunde_infos, neue_name):
    for i in range(len(lista)):
        if (lista[i].name == kunde_infos.name) and (lista[i].adresse == kunde_infos.adresse):
            lista[i].name = neue_name
    return lista


def aktualisieren_kunde_adresse(lista, kunde_infos, neue_adresse):
    for i in range(len(lista)):
        if (lista[i].name == kunde_infos.name) and (lista[i].adresse == kunde_infos.adresse):
            lista[i].adresse = neue_adresse
    return lista


def anzeigen_kunde(lista):
    for elem in range(len(lista)):
        print(f'{elem}. ID: {lista[elem].id} | Name: {lista[elem].name} | Adresse: {lista[elem].adresse}')


def anzeigen_gericht(lista):
    print('Gekochte Gerichten:')
    for elem in range(len(lista)):
        print(
            f'{elem}. Name: {lista[elem].id} | Portionsgrosse: {lista[elem].portionsgrosse}g |Preis: {lista[elem].preis} Euro | Zubereitungszeit: {lista[elem].zubereitungszeit} mins.')


def anzeigen_getrank(lista):
    print('Getranke:')
    for elem in range(len(lista)):
        print(
            f'{elem}. Name: {lista[elem].id} | Portionsgrosse: {lista[elem].portionsgrosse}ml |Preis: {lista[elem].preis} Euro | Alkoholgehalt: {lista[elem].alkoholgehalt}%')


# Informationen uber neue gekocher Gerichte einlesen
def infoGekochterGericht():
    name = input('Name: ')
    portionsgrosse = int(input('Portionsgrosse: '))
    preis = int(input('Preis: '))
    zubereitungszeit = int(input('Zubereitungszeit: '))
    return name, portionsgrosse, preis, zubereitungszeit


# Infomationen uber neue Getrank einlesen
def infoGetrank():
    name = input('Name: ')
    portionsgrosse = int(input('Portionsgrosse: '))
    preis = int(input('Preis: '))
    alkoholgehalt = int(input('Alkoholgehalt: '))
    return name, portionsgrosse, preis, alkoholgehalt


def bestellungGekochterGericht(gerichteMenu, lista_gericht):
    while True:
        print('\nHier ist der Menu Liste der gekochter Gerichten:\n')
        anzeigen_gericht(gerichteMenu)
        dish = int(input('\nWahlen Sie bitte ein gekochter Gericht: '))
        print('Sie haben folgendes gewahlt:')
        anzeigen_gericht([gerichteMenu[dish]])
        dishBestellung = GekochterGericht(gerichteMenu[dish].id, gerichteMenu[dish].portionsgrosse,
                                          gerichteMenu[dish].preis, gerichteMenu[dish].zubereitungszeit)
        lista_gericht.append(dishBestellung)
        print('''
        0 - Exit (Kein mehr gekochter Gericht wahlen)
        1 - Noch ein gekochter Gericht wahlen
        ''')
        opt = int(input('Wahlen Sie bitte ein Option aus: '))
        if opt == 0:
            break
        if opt == 1: pass
    return lista_gericht


def bestellungGetrank(getrankeMenu, lista_getrank):
    while True:
        print('\nHier ist der Menu Liste der Getranke:\n')
        anzeigen_getrank(getrankeMenu)
        drink = int(input('\nWahlen Sie bitte ein Getrank: '))
        anzeigen_getrank([getrankeMenu[drink]])
        drinkBestellung = Getrank(getrankeMenu[drink].id, getrankeMenu[drink].portionsgrosse,
                                  getrankeMenu[drink].preis, getrankeMenu[drink].alkoholgehalt)
        lista_getrank.append(drinkBestellung)
        print('''
            0 - Exit 
            1 - Noch ein Getrank wahlen
                ''')
        opt = int(input('Wahlen Sie bitte ein Option aus: '))
        if opt == 0: break
        if opt == 1: pass

    return lista_getrank


# ------------------------------

#submenu1()
def make_an_order():
    while True:
        # create the objects
        cookedDish_repo = CookedDishRepo('Database/ha5_gekochterGerichte.txt')
        drink_repo = DrinkRepo('Database/ha5_getranke.txt')
        customer_repo = CustomerRepo('Database/ha5_kunden.txt')
        order_repo = OrderRepo('Database/ha5_bestellungen.txt')
        # load the content/data of these
        cookedDishes = cookedDish_repo.load()
        drinks = drink_repo.load()
        kunden = customer_repo.load()
        bestellungen = order_repo.load()
        # load the food and drink menus
        gerichteFile = CookedDishRepo('Database/ha5_menu_gekochterGericht.txt')
        getrankeFile = DrinkRepo('Database/ha5_menu_getranke.txt')
        gerichteMenu = gerichteFile.load()
        getrankeMenu = getrankeFile.load()

        # print cooked dishes and choose one
        lista_gericht = bestellungGekochterGericht(gerichteMenu, [])
        cookedDishes += lista_gericht

        # print drinks and choose one
        lista_getrank = bestellungGetrank(getrankeMenu, [])
        drinks += lista_getrank
        while True:
            option = int(input("""
            1-neue Kunde hinzufugen
            2-Kunde Suchen
            
            Wahlen Sie bitte ein Option aus: """))

            if option == 1:
                #
                #
                nameKunde = input('\nGeben Sie bitte die Name der Kunde an: ')
                adresseKunde = input('\nGeben Sie bitte die Adresse der Kunde an: ')
                kunden_info = nameKunde + adresseKunde
                kunden_id = hashlib.sha256(kunden_info.encode()).hexdigest()
                neue_kunde = Kunde(kunden_id, nameKunde, adresseKunde)
                kunden.append(neue_kunde)
                besteller = neue_kunde
                print('Kunde war succesfully hinzugefugt!\n')
                break
            if option == 2:
                wort = input('Suchen der Kunden nach Name/Adresse: ')
                gesucht = suchenKunde(kunden, wort)
                if len(gesucht) == 0:
                    print('\nKeine Kunde mit dieser Name/Adresse gefunden\n')
                else:
                    anzeigen_kunde(gesucht)
                    wahl = int(input('\nWahlen Sie bitte eine Kunde aus (nr.): '))
                    print('Sie haben diese Kunde gewahlt: ')
                    anzeigen_kunde([gesucht[wahl]])
                    besteller = gesucht[wahl]
                    break

        liste_id_gerichte = [lista_gericht[i].id for i in range(len(lista_gericht))]
        liste_id_getranke = [lista_getrank[i].id for i in range(len(lista_getrank))]
        gesamtpreis = [lista_gericht[i].preis for i in range(len(lista_gericht))] + [lista_getrank[i].preis for i in
                                                                                     range(len(lista_getrank))]
        # Bestellung machen
        bestellungInfo = Bestellung(len(bestellungen), besteller.id, liste_id_gerichte, liste_id_getranke,
                                    gesamtpreis)
        bestellungen.append(bestellungInfo)
        # speichern der Daten
        cookedDish_repo.save(cookedDishes)
        drink_repo.save(drinks)
        customer_repo.save(kunden)
        order_repo.save(bestellungen)
        print('Bestellung succesfully registiert! ')
        print('Wollen Sie die Rechnung (Bon fiscal) anschauen?:\n0 - Nein\n1 - Ja')
        opt = int(input("Wahlen Sie bitte ein Option aus: "))
        if opt == 1:
            bestellungInfo.anzeigeRechnung()
        break

# subMenu2() option 1
def print_gekochterGericht():
    gerichteFile = CookedDishRepo('Database/ha5_menu_gekochterGericht.txt')
    gerichteMenu = gerichteFile.load()
    anzeigen_gericht(gerichteMenu)
    gerichteFile.save(gerichteMenu)


# subMenu2() option 2
def add_gekochterGericht():
    gerichteFile = CookedDishRepo('Database/ha5_menu_gekochterGericht.txt')
    gerichteMenu = gerichteFile.load()
    name, portionsgrosse, preis, zubereitungszeit = infoGekochterGericht()
    gerichteMenu.append(GekochterGericht(name, portionsgrosse, preis, zubereitungszeit))
    anzeigen_gericht(gerichteMenu)
    gerichteFile.save(gerichteMenu)


# subMenu2() option 3
def delete_gekochterGericht():
    gerichteFile = CookedDishRepo('Database/ha5_menu_gekochterGericht.txt')
    gerichteMenu = gerichteFile.load()
    anzeigen_gericht(gerichteMenu)
    value = int(input('\nLoschen von Nummer: '))
    if value <= len(gerichteMenu):
        gerichteMenu = loschen(gerichteMenu, value)
        gerichteFile.save(gerichteMenu)
        print('\nGekochter Gericht successfully geloscht!\n')
    else:
        pass
    gerichteFile.save(gerichteMenu)


# subMenu2() option 4
def print_getrank():
    getrankeFile = DrinkRepo('Database/ha5_menu_getranke.txt')
    getrankeMenu = getrankeFile.load()
    anzeigen_getrank(getrankeMenu)
    getrankeFile.save(getrankeMenu)


# subMenu2() option 5
def add_getrank():
    getrankeFile = DrinkRepo('Database/ha5_menu_getranke.txt')
    getrankeMenu = getrankeFile.load()
    name, portionsgrosse, preis, alkoholgehalt = infoGetrank()
    getrankeMenu.append(Getrank(name, portionsgrosse, preis, alkoholgehalt))
    anzeigen_getrank(getrankeMenu)
    getrankeFile.save(getrankeMenu)


# subMenu2() option 6
def delete_getrank():
    getrankeFile = DrinkRepo('Database/ha5_menu_getranke.txt')
    getrankeMenu = getrankeFile.load()
    anzeigen_getrank(getrankeMenu)
    value = int(input('\nLoschen von Nummer: '))
    if value <= len(getrankeMenu):
        getrankeMenu = loschen(getrankeMenu, value)
        getrankeFile.save(getrankeMenu)
        print('\nGetrank successfully geloscht!\n')
    else:
        pass
    getrankeFile.save(getrankeMenu)


# submenu3() option 1
def print_customer():
    customer_repo = CustomerRepo('Database/ha5_kunden.txt')
    kunden = customer_repo.load()
    anzeigen_kunde(kunden)
    customer_repo.save(kunden)


# submenu3() option 2
def search_customer():
    customer_repo = CustomerRepo('Database/ha5_kunden.txt')
    kunden = customer_repo.load()
    wort = input('Suchen der Kunden nach Name/Adresse: ')
    gesucht = suchenKunde(kunden, wort)
    if len(gesucht) == 0:
        print('\nKeine Kunde mit dieser Name/Adresse gefunden\n')
    else:
        anzeigen_kunde(gesucht)
    customer_repo.save(kunden)


# submenu3() option 3
def add_customer():
    customer_repo = CustomerRepo('Database/ha5_kunden.txt')
    kunden = customer_repo.load()
    nameKunde = input('\nGeben Sie bitte die Name der Kunde an: ')
    adresseKunde = input('\nGeben Sie bitte die Adresse der Kunde an: ')
    kunden_info = nameKunde + adresseKunde
    kunden_id = hashlib.sha256(kunden_info.encode()).hexdigest()
    neue_kunde = Kunde(kunden_id, nameKunde, adresseKunde)
    kunden.append(neue_kunde)
    print('Kunde war succesfully hinzugefugt!\n')
    customer_repo.save(kunden)


# submenu3() option 4
def update_customer_name():
    customer_repo = CustomerRepo('Database/ha5_kunden.txt')
    kunden = customer_repo.load()
    # --
    wort = input('Suchen der Name der Kunde: ')
    gesucht = suchenKunde(kunden, wort)
    if len(gesucht) == 0:
        print('\nKeine Kunde mit dieser Name gefunden\n')
    else:
        anzeigen_kunde(gesucht)
        zahl = int(input('Verandern der Name der Kunde Nr. (geben Sie ein Zahl ein): '))
        verandern = input('Geben Sie die Neue Name ein: ')
        kunden = aktualisieren_kunde_name(kunden, gesucht[zahl], verandern)
        print('Name der Kunde war successfully aktualisiert!\n')
    # --
    customer_repo.save(kunden)


# submenu3() option 5
def update_customer_address():
    customer_repo = CustomerRepo('Database/ha5_kunden.txt')
    kunden = customer_repo.load()
    # --
    wort = input('Suchen der Adresse der Kunde: ')
    gesucht = suchenKunde(kunden, wort)
    if len(gesucht) == 0:
        print('\nKeine Kunde mit dieser Adresse gefunden\n')
    else:
        anzeigen_kunde(gesucht)
        zahl = int(input('Verandern der Adresse der Kunde Nr. (geben Sie ein Zahl ein): '))
        verandern = input('Geben Sie die Neue Name ein: ')
        kunden = aktualisieren_kunde_adresse(kunden, gesucht[zahl], verandern)
        print('Adresse der Kunde war successfully aktualisiert!\n')
    # --
    customer_repo.save(kunden)


# submenu3() option 6
def delete_customer():
    customer_repo = CustomerRepo('Database/ha5_kunden.txt')
    kunden = customer_repo.load()
    # ------
    wort = input('Suchen der Name der Kunde: ')
    gesucht = suchenKunde(kunden, wort)
    if len(gesucht) == 0:
        print('\nKeine Kunde mit dieser Name gefunden\n')
    else:
        anzeigen_kunde(gesucht)
        value = int(input('\nLoschen von Nummer: '))
        if value <= len(gesucht):
            kunden = loschen_kunde(kunden, gesucht[value])
            customer_repo.save(kunden)
            print('\nKunde successfully geloscht!\n')
    # ------
    customer_repo.save(kunden)
