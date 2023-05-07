# 1.
# a. Geben sei eine Textdatei mit dem Namen "text.txt" an, die in jeder Zeile den Namen des Schülers, das Fach und
# die jeweilige Note enthält, getrennt durch zwei Leerzeichen ("  "), schreiben Sie eine Funktion namens "ub1", die:
# 	- aus der angegebenen CSV-Datei "text.txt" liest
# 	- nur die Zeilen behält, die die Note größer als 8 haben (0.5p)
# 	- die Summe der Noten, der behaltenen Zeilen, berechnet und das Ergebnis zurückgibt (0.5p)
# Es sind keine for- oder while-Schleifen erlaubt. Es wird erwartet, dass die Lösung map, filter oder reduce und
# andere mathematische Operationen, falls erforderlich, benützt sind. (2p)
#
# b. Schreiben Sie für die Funktion "ub1" zwei Testfälle. (1p)
# Einer, der das erwartete Ergebnis der Funktion bestätigt und ein anderer, der absichtlich fehlschlägt.
#

import functools

def ub1():
    with open('text.txt','r') as f:
        inhalt=f.read()
    inhalt=inhalt.split('\n')
    inhalt=list(map(lambda elem:elem.split('  '),inhalt))
    inhalt=list(filter(lambda elem:int(elem[3])>8,inhalt))
    noten=list(map(lambda elem:int(elem[3]),inhalt))
    summe=functools.reduce(lambda a,b:a+b,noten)
    return summe

print(ub1())

def test_ub1():
    expected=58
    result=ub1()
    try:
        assert result == expected
    except AssertionError:
        print('Test 1 failed!')
    else:
        print('Test 1 succeded!')

    expected = 68
    result = ub1()
    try:
        assert result == expected
    except AssertionError:
        print('Test 2 failed!')
    else:
        print('Test 2 succeded!')

test_ub1()