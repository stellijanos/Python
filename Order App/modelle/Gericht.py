from modelle.Identifizierbar import Identifizierbar


class Gericht(Identifizierbar):
    def __init__(self, id, portiongrosse, preis):
        super().__init__(id)
        self.portionsgrosse = portiongrosse
        self.preis = preis
