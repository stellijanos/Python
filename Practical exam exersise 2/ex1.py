# 1.
# a. Geben sei eine Textdatei mit dem Namen "zahlen.txt" an, auf eine mehreren Zeilen, Zahlen die durch
# die Zeichenkette "UBB" getrennt sind.
# schreiben Sie eine Funktion namens "ub1", die:
#   - einen Parameter namens "even_row" erhält
# 	- aus der angegebenen CSV-Datei "zahlen.txt" liest
# 	- wenn "even_row" der Wert "True" (bool) hat, behalten nur die Zeilen, wo alle Zahlen gerade Zahlen sind (0.25p)
# 	- wenn "even_row" der Wert "False" (bool) hat, behalten nur die Zeilen, wo alle Zahlen ungerade Zahlen sind (0.25p)
# 	- Das Ergebnis der Funktion ist die Summe der Zahlen der behaltenen Zeilen (0.5p)
# Es sind keine for- oder while-Schleifen erlaubt. Es wird erwartet, dass die Lösung map, filter oder reduce und
# andere mathematische Operationen, falls erforderlich, benützt sind. (2p)
#
# b. Schreiben Sie für die Funktion "ub1" zwei Testfälle. (1p)
# Einer, der das erwartete Ergebnis der Funktion bestätigt und ein anderer, der absichtlich fehlschlägt.
#


import functools

def multe(elem):
    return list(map(lambda x:int(x),elem.split('UBB')))


def verific_par(elem):
    adevarat=list(map(lambda x:x%2==0,elem))
    if False in adevarat:
        return False
    return True

def verific_impar(elem):
    adevarat=list(map(lambda x:x%2==0,elem))
    if True in adevarat:
        return False
    return True

def ub1(even_row):
    with open('zahlen.txt') as f:
        inhalt=f.read().split('\n')
    inhalt=list(map(lambda elem:multe(elem),inhalt))
    if even_row==True:
        rezult=list(filter(lambda elem:verific_par(elem)==True,inhalt))
    else:
        rezult=list(filter(lambda elem:verific_impar(elem)==True,inhalt))
    if len(rezult)==0:
        return 0
    rezult=list(functools.reduce(lambda a,b:a+b,rezult))
    rezult=functools.reduce(lambda a,b:a+b,rezult)
    return rezult

print(ub1(True))

def test_ub1():
    expected=98
    rezult=ub1(False)

    try:
        assert expected==rezult
    except AssertionError:
        print('Test 1 failed!')
    else:
        print('Test 1 succeded')

    expected = 90
    rezult = ub1(False)

    try:
        assert expected == rezult
    except AssertionError:
        print('Test 1 failed!')
    else:
        print('Test 1 succeded')

test_ub1()