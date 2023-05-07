import turtle
from litere.litere import *
import json


def read_zeichenfolge():
    string = input("Geben Sie eine Zeichenfolge, was der Turtle zeichnen wird: ")
    return string.upper()


def dict():
    dictionar = {'A': a, 'B': b, 'C': c, 'D': d, 'E': e, 'F': f, 'G': g, 'H': h, 'I': i, 'J': j, 'K': k,
                 'L': l, 'M': m, 'N': n, 'O': o, 'P': p, 'Q': q, 'R': r, 'S': s, 'T': t, 'U': u, 'V': v,
                 'X': x, 'Y': y, 'Z': z, '.': punkt, '?': 'frage', '!': ausrufe, ' ': spatiu}
    return dictionar


def zeichnen_fur_dict(liste):
    def key_w():
        turtle.forward(10)
        liste.append('w')

    def key_a():
        turtle.left(45)
        liste.append('a')

    def key_s():
        turtle.backward(10)
        liste.append('s')

    def key_d():
        turtle.right(45)
        liste.append('d')

    def key_f():
        turtle.up()
        liste.append('f')

    def key_g():
        turtle.down()
        liste.append('g')

    turtle.listen()
    turtle.onkey(key_w, 'w')
    turtle.onkey(key_a, 'a')
    turtle.onkey(key_s, 's')
    turtle.onkey(key_d, 'd')
    turtle.onkey(key_f, 'f')
    turtle.onkey(key_g, 'g')
    turtle.onkey(turtle.bye, 'Return')
    turtle.mainloop()
    return liste


def liste_zeichnen(dict_datei, char):
    turtle.down()
    for element in dict_datei[char]:
        if element == 'w':
            turtle.forward(10)
        if element == 'a':
            turtle.left(45)
        if element == 's':
            turtle.backward(10)
        if element == 'd':
            turtle.right(45)
        if element == 'f':
            turtle.up()
        if element == 'g':
            turtle.down()
    turtle.up()


def read_charakter():
    charakter = input("Geben Sie eine Charakter ein, welche Sie zeichnen wollen: ")
    return charakter


def liste_ins_dictionar():
    f = open('dict_datei.txt', 'r')
    inhalt = f.read()
    dict_datei = json.loads(inhalt)
    return dict_datei


def dictionar_in_liste(dict_datei):
    f = open('dict_datei.txt', 'w')
    f.write(json.dumps(dict_datei))
    f.close()
    return f


def durchfuhren(string, dictionar):
    turtle.Screen().setup(1500, 500)
    turtle.up()
    turtle.setpos(-700, 0)
    dict_datei = liste_ins_dictionar()
    for char in string:
        if char in dictionar.keys():
            dictionar[char]()
        elif char in dict_datei.keys():
            liste_zeichnen(dict_datei, char)
    turtle.mainloop()


def uberprufen(charakter):
    dict_datei = liste_ins_dictionar()
    liste = []
    if charakter in dict_datei.keys():
        print('Es gibt schon')
    else:
        turtle.Pen()
        liste = zeichnen_fur_dict([])
        dict_datei[charakter] = liste
        f = dictionar_in_liste(dict_datei)
