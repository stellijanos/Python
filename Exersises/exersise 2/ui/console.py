from logik.logik import *

def menu():
    return '''
        Pfad zur Datei: meine_datei.txt
        1-Programm beginnen 
        0-Exit
    '''

def main():
    while True:
        print(menu())
        option=int(input('Whalen Sie ein Option aus: '))
        if option == 1:
            f = offnen_lesen()
            ersetzen, ersatzwort, anzahl = einlesen()
            anzahl, f = durchfuhren(ersetzen, ersatzwort, anzahl, f)
            ausdrucken(ersetzen, ersatzwort, anzahl)
            f = schliessen(f)
        if option == 0:
            break





