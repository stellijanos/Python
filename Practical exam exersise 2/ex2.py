# 2.
# a. Schreiben Sie die Definition für eine Klasse namens "Shop".
# Die Klasse sollte in der Lage sein, das Folgende zu tun:
# 	 - bei der Initialisierung wird die Instanzvariable "products" auf einen gegebenen Parameter gesetzt.
# 	   Der Typ des Parameters ist eine Liste von strings. (0.5p)
# 	 - eine Methode namens "buy" haben, die:
# 	 	- einen einzelnen ganzzahligen Parameter namens "price" bekommt
# 	 	- für alle Element aus der Liste "products" prüft, dass die doppelte Länge des Elements nicht größer als "price" ist (0.5pp)
# 	 	- gibt eine neue Liste mit strings zurück, die dem folgenden Format behalten: "<element> - <price>" (0.5p)
# 	 	- eine benutzerdefinierte Ausnahme namens "BadName" wirft, wenn die Prüfung der Lange nicht fördert(0.5p)
#

class Shop:
    def __init__(self,products:list[str]):
        self.products=products

    def buy(self,price:int):


# b. Schreiben Sie die Definition für eine Klasse namens "BetterShop", die von "Shop" erbt.
#  Die Klasse sollte folgendes können:
# 	- bei der Initialisierung setzt sie neben den Variablen von "Shop" auch eine Instanzvariable namens
#  	  "total" auf 0 (0.25p)
# 	- Überschreiben der Methode "buy", um Folgendes zu tun:
# 		- Wiederverwendung der Methode "buy" aus der Basisklasse (0.25)
# 		- Im Falle eines erfolgreichen Aufrufs wird das Ergebnis zurückgegeben und die Instanzvariable "total" mit dem
# 	      Wert von "price" erhöht (0.25p)
# 		- im Falle einen fehlgeschlagenen Aufruf wird die Instanzvariable "total" auf -1 gesetzt (0.25p)
# 	- Das Ergebnis der Subtraktion zwischen zwei Instanzen des Typs "BetterShop" (shop1 - shop2) ist eine Liste
#     von strings die sich in der "products" der beiden Instanzen befinden.
#     (1p)
#