from modelle.Gericht import Gericht


class GekochterGericht(Gericht):
    def __init__(self, id, portionsgrosse, preis, zubereitungszeit):
        super().__init__(id, portionsgrosse, preis)
        self.zubereitungszeit = zubereitungszeit

    def __eq__(self, other):
        return self.id == other.id and self.portionsgrosse == other.portionsgrosse and self.preis == other.preis and self.zubereitungszeit == other.zubereitungszeit