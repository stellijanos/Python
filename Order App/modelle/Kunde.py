from modelle.Identifizierbar import Identifizierbar


class Kunde(Identifizierbar):
    def __init__(self, kunden_id, name, adresse):
        super().__init__(kunden_id)
        self.name = name
        self.adresse = adresse

    def __eq__(self, other):
        return self.id == other.id and self.name == other.name and self.adresse == other.adresse
