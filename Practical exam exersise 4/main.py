# Benotung:
# 1.a 3 Punkte
# 1.b 1 Punkt

# 2.a 2 Punkte
# 2.b 2 Punkte

# 3. 1 Punkt
# Insgesamt: 9 Punkte

# 1.
# a. Geben sei eine Textdatei mit dem Namen "something.txt" an, die in jeder Zeile den Vor- und Nachnamen
# des Schülers, das Fach und die jeweilige Note enthält, getrennt durch ein Tab-Zeichen ("\t"),
# schreiben Sie eine Funktion namens "ub1", die:
#   - einen Parameter namens "even" erhält
# 	- aus der angegebenen CSV-Datei "something.txt" liest
# 	- wenn "even" der Wert "True" (bool) hat, behalten nur die Zeilen, deren Index eine gerade Zahl ist (0.25p)
# 	- wenn "even" der Wert "False" (bool) hat, behalten nur die Zeilen, deren Index eine ungerade Zahl ist (0.25p)
# 	- Das Ergebnis der Funktion ist eine Zeichenkette, die aus den Vornamen der behaltenen Zeilen, zusammengefügt mit dem "." Zeichen, aufgebaut ist. (0.5p)
# Es sind keine for- oder while-Schleifen erlaubt. Es wird erwartet, dass die Lösung map, filter oder reduce und
# andere mathematische Operationen, falls erforderlich, benützt sind. (2p)
#
# b. Schreiben Sie für die Funktion "ub1" zwei Testfälle. (1p)
# Einer, der das erwartete Ergebnis der Funktion bestätigt und ein anderer, der absichtlich fehlschlägt.
#
# 2.
# a. Schreiben Sie die Definition für eine Klasse namens "CaesarEncryptedText".
# Die Klasse sollte in der Lage sein, das Folgende zu tun:
# 	 - bei der Initialisierung wird die Instanzvariable "numbers" auf einen gegebenen Parameter gesetzt.
# 	   Der Typ des Parameters ist eine Liste von Zahlen. (0.5p)
# 	 - eine Methode namens "decrypt" haben, die:
# 	 	- einen einzelnen ganzzahligen Parameter namens "decryption_key" bekommt
# 	 	- für alle Zahlen aus der Liste "numbers" prüft, dass das Ergebnis der Subtraktion "zahl - decryption_key" sich im Interval von 65 bis 90 befindet. (0.5pp)
# 	 	- gibt die Liste der Ergebnisse zurück (0.5p)
# 	 	- eine benutzerdefinierte Ausnahme namens "BadValue" wirft, wenn einer der Ergebnisse nicht im Interval befindet (0.5p)
#
# b. Schreiben Sie die Definition für eine Klasse namens "ActualCaesarEncryptedText", die von "CaesarEncryptedText" erbt.
#  Die Klasse sollte folgendes können:
# 	- bei der Initialisierung setzt sie neben den Variablen von "CaesarEncryptedText" auch eine Instanzvariable namens
#  	  "message" auf None Wert (0.25p)
# 	- Überschreiben der Methode "decrypt", um Folgendes zu tun:
# 		- Wiederverwendung der Methode "decrypt" aus der Basisklasse (0.25)
# 		- Im Falle eines erfolgreichen Aufrufs wird das Ergebnis zurückgegeben und im Instanzvariable "message" gespeichert (0.25p)
# 		- im Falle einen fehlgeschlagenen Aufruf wird die Instanzvariable "message" auf None gesetzt (0.25p)
# 	- Das Ergebnis der Division zwischen zwei Instanzen des Typs "ActualCaesarEncryptedText" (instanz1 / instanz2) ist
#  	  eine Zeichenkette, die aus den entschlüsselten Elementen aus dem "message" der ersten Instanz aufgebaut ist.
#     *In diesem Fall bedeutet "entschlüsselt" das Wandeln der Zahl in das entsprechende ASCII-Zeichen.
#     (1p)
#
# 3. Schreibe die folgende Funktion so um, dass sie rekursiv ist: (1p)
def my_func(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

#cautare binara