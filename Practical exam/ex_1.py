
# 1.
# Geben Sie eine Textdatei mit dem Namen 'text.txt' an, die in jeder Zeile den Vor- und Nachnamen des Schülers,
# das Fach und die jeweilige Note enthält. Die Felder sollen durch drei Strichpunkt (';;;') voneinander getrennt sein.
# Schreiben Sie eine Funktion namens 'ub1', die folgendes tut:
#  - liest aus der angegebenen Datei 'text.txt'
#  - behält nur die Zeilen, bei denen der Nachname eine Länge von 3 hat und die Note eine gerade Zahl ist (0,5 Punkte)
#  - gibt einen String aller Fächer aus den behaltenen Zeilen zurück. Die Fächer sollen in Kleinbuchstaben und durch
#    Kommas getrennt sein. (0,5 Punkte)
# Die Verwendung von for- oder while-Schleifen, list comprehension ist nicht erlaubt. Es wird erwartet,
# dass die Lösung map, filter, reduce und andere mathematische Operationen, falls erforderlich, verwendet. (2 Punkte)
#
# b. Schreiben Sie für die Funktion "ub1" zwei Testfälle. (1p)
# Einer, der das erwartete Ergebnis der Funktion bestätigt und ein anderer, der absichtlich fehlschlägt.
#

def ub1():
    with open('text.txt','r') as f:
        inhalt=f.read().split('\n')
    inhalt=list(map(lambda elem:elem.split(';;;'),inhalt))
    inhalt=list(filter(lambda elem:len(elem[1])==3 and int(elem[3])%2==0,inhalt))
    fache=list(map(lambda elem:elem[2],inhalt))
    fache=list(map(lambda elem:elem.lower(),fache))
    return ','.join(fache)

print(ub1())

def test_ub1():
    expected='advanced programming,programming fundamentals'
    result=ub1()
    try:
        assert expected==result
    except AssertionError:
        print('Test 1 failed!')
    else:
        print('Test 1 succeded!')

    expected = 'programming fundamentals,advanced programming'
    result = ub1()
    try:
        assert expected == result
    except AssertionError:
        print('Test 2 failed!')
    else:
        print('Test 2 succeded!')

test_ub1()