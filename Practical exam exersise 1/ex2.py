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

class DebitCard:
    def __init__(self,name):
        self.money=0
        self.name=name

    def pay(self,zahl:int):
        if zahl<=self.money:
            self.money-=zahl
            return self.money
        else:
            raise NoBalance('Nicht genug Geld!')

class NoBalance(Exception): pass


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

class CreditCard(DebitCard):
    def __init__(self,name):
        super().__init__(name)
        self.debt=0

    def pay(self,zahl):
        try:
            result=super().pay(zahl)
            return result
        except NoBalance:
            self.debt+=zahl

    def __mul__(self,other):
        return [CreditCard(self.name) for _ in range(other)]

credit_card = CreditCard("John Doe")
cards = credit_card * 4

print(len(cards)) # Output: 3
