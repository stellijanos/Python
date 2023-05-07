from litere.litere import *
from logik_1.logik import *



def menu():
    return '''
    Turtle Paint v1.0

    1. Textnachricht zeichnen
    2. Neues Wort hinzufugen
    0. Exit
    '''


def main():
    while True:
        print(menu())
        opt = int(input("Wahlen sie ein Option aus: "))
        if opt == 1:
            dictionar = dict()
            string = read_zeichenfolge()
            durchfuhren(string, dictionar)
        if opt == 2:
            charakter=read_charakter()
            uberprufen(charakter)
        if opt == 0:
            break