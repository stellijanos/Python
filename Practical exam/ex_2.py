# 2.
# a. Schreiben Sie die Definition für eine Klasse namens "Student". Die Klasse sollte in der Lage sein,
# Folgendes zu tun:
# - Bei der Initialisierung wird die Instanzvariable "grades" auf einen gegebenen Parameter gesetzt.
# - Der Typ des Parameters ist eine Liste von Zahlen. (0,5 Punkte)
# - Eine Methode namens "take_exam" haben, die:
#   - Einen einzelnen String-Parameter namens "exam" bekommt
#   - Für alle Elemente aus der Liste "grades" prüft, ob alle größer oder gleich 5 sind (0,5 Punkte)
#   - Eine neue Liste zurückgibt, die nur ein Element enthält, und zwar ein Tuple, gebildet aus dem Parameter "exam"
#     und dem ersten Element der Liste "grades" (0,5 Punkte)
#   - Eine benutzerdefinierte Ausnahme namens "FailedExam" wirft, wenn kein Element größer oder gleich 5 ist(0,5 Punkte)

class Student:
    def __init__(self, grades):
        self.grades = grades

    def take_exam(self, exam):
        l = []
        for grade in self.grades:
            if grade >= 5:
                l.append(grade)
        if len(l) == 0:
            raise FailedExam('Alle haben failed')
        else:
            return [(exam, self.grades[0])]


class FailedExam(Exception):
    pass


# b. Schreiben Sie die Definition für eine Klasse namens "ComputerScienceStudent", die von "Student" erbt.
# Die Klasse sollte Folgendes können:
# - Bei der Initialisierung setzt sie neben den Variablen von "Book" auch eine Instanzvariable namens "laptop" auf ein
#   leeres Wörterbuch (dict). (0,25 Punkte)
# - Überschreiben der Methode "take_exam", um Folgendes zu tun:
#   - Wiederverwendung der Methode "take_exam" aus der Basisklasse (0,25 Punkte)
#   - Im Falle eines erfolgreichen Aufrufs wird das Ergebnis in der Instanzvariable "laptop" gespeichert, wobei der
#     Schlüssel und der Wert das erste beziehungsweise zweite Element des Tupels sind (0,25 Punkte)
#   - Im Falle eines fehlgeschlagenen Aufrufs wird in der Instanzvariable "laptop" ein Eintrag hinzugefügt, wobei der
#     Schlüssel der Parameter "exam" ist und der Wert 0 ist (0,25 Punkte)
# - Das Ergebnis der Addition zwischen zwei Instanzen des Typs "ComputerScienceStudent" (stud1 + stud2) ist ein
#   Wörterbuch, das alle Einträge der beiden "laptop"-Instanzvariablen enthält.
#   Die Priorität der Einträge ist nicht wichtig. (1 Punkt)
#


class ComputerScienceStudent(Student):
    def __init__(self, grades):
        super().__init__(grades)
        self.laptop = {}

    def take_exam(self, exam):
        try:
            result = super().take_exam(exam)
        except FailedExam:
            self.laptop = {exam: 0}
            return self.laptop
        else:
            self.laptop = {result[0][0]: result[0][1]}
            return self.laptop

    def __add__(self, other):
        self.laptop.update(other.laptop)
        return self.laptop
