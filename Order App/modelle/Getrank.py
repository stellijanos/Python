from modelle.Gericht import Gericht


class Getrank(Gericht):
    def __init__(self, id, portionsgrosse, preis, alkoholgehalt):
        super().__init__(id, portionsgrosse, preis)
        self.alkoholgehalt = alkoholgehalt

    def __eq__(self, other):
        return self.id == other.id and self.portionsgrosse == other.portionsgrosse and self.preis == other.preis and self.alkoholgehalt == other.alkoholgehalt
