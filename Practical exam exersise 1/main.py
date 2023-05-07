# Benotung:
# 1.a 3 Punkte
# 1.b 1 Punkt

# 2.a 2 Punkte
# 2.b 2 Punkte

# 3. 1 Punkt
# Insgesamt: 9 Punkte

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
# 2.
# a. Schreiben Sie die Definition für eine Klasse namens "DebitCard".
# Die Klasse sollte in der Lage sein, das Folgende zu tun:
# 	 - bei der Initialisierung die Instanzvariable "money" auf 0 und die Instanzvariable "name" auf einen
# 	   gegebenen Parameter setzen (0.5p)
# 	 - eine Methode namens "pay" haben, die:
# 	 	- einen einzelnen ganzzahligen Parameter bekommt
# 	 	- prüft, ob der Parameter größer oder gleich der Variablen "money" ist (0.5pp)
# 	 	- die Differenz zwischen dem "money" und dem gegebenen Parameter zurückgibt und als neue Wert für "money" speichert (0.5p)
# 	 	- eine benutzerdefinierte Ausnahme namens "NoBalance" wirft, wenn der Parameter größer als "money" ist (0.5p)
#
# b. Schreiben Sie die Definition für eine Klasse namens "CreditCard", die von "DebitCard" erbt.
#  Die Klasse sollte folgendes können:
# 	- bei der Initialisierung setzt sie neben den Variablen von "DebitCard" auch eine Instanzvariable namens
#  	  "debt" auf 0 (0.25p)
# 	- Überschreiben der Methode "pay", um Folgendes zu tun:
# 		- Wiederverwendung der Methode "pay" aus der Basisklasse (0.25)
# 		- im Falle einer erfolgreichen Abhebung wird das Ergebnis zurückgegeben (0.25p)
# 		- im Falle einer fehlgeschlagenen Abhebung wird ganzzahligen Parameter von der "pay" Methode zum "debt" addiert (0.25p)
# 	- Die Multiplikation zwischen ein "CreditCard" Instanz und eine Zahl (credit_card * 3) hat als Ergebnis
#     eine Liste von "CreditCard" instanzen die der gleiche Zustand der originalen Instanz haben. Die länge der Liste
#     ist gleich mit der Zahl aus der Multiplikation (1p)
#
# 3. Schreibe die folgende Funktion so um, dass sie rekursiv ist: (1p)
def my_func(lst, x):
    low = 0
    high = len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == x:
            return mid
        elif lst[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1
