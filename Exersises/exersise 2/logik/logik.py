def offnen_lesen():
    return open('meine_datei.txt', 'r')


def offnen_schreiben():
    return open('meine_datei.txt', 'w')


def schliessen(f):
    f.close()
    return f


def einlesen():
    ersetzen = input('Wort zu ersetzen: ')
    ersatzwort = input('Ersatzwort: ')
    return ersetzen, ersatzwort, 0


def durchfuhren(ersetzen, ersatzwort, anzahl, f):
    inhalt = f.read()
    anzahl += inhalt.count(ersetzen)
    inhalt = inhalt.replace(ersetzen, ersatzwort)
    f = offnen_schreiben()
    f.write(inhalt)
    return anzahl, f


def ausdrucken(ersetzen, ersatzwort, anzahl):
    print("Ersetzt '", ersetzen, "' duch '", ersatzwort, "' an ", anzahl, " Stellen")
