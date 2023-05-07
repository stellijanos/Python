import functools
from datetime import datetime


class Identifizierbar():
    def __init__(self, id):
        # self.id = hash(self)
        self.id = id


class Gericht(Identifizierbar):
    def __init__(self, id, portiongrosse, preis):
        super().__init__(id)
        self.portionsgrosse = portiongrosse
        self.preis = preis


class GekochterGericht(Gericht):
    def __init__(self, id, portionsgrosse, preis, zubereitungszeit):
        super().__init__(id, portionsgrosse, preis)
        self.zubereitungszeit = zubereitungszeit


class Getrank(Gericht):
    def __init__(self, id, portionsgrosse, preis, alkoholgehalt):
        super().__init__(id, portionsgrosse, preis)
        self.alkoholgehalt = alkoholgehalt


class Kunde(Identifizierbar):
    def __init__(self, kunden_id, name, adresse):
        super().__init__(kunden_id)
        self.name = name
        self.adresse = adresse


class Bestellung(Identifizierbar):
    def __init__(self, id, kundenId, listeIdGerichte, listeIdGetranke, gesamtkosten):
        super().__init__(id)
        self.kundenId = kundenId
        self.listeIdGerichte = listeIdGerichte
        self.listeIdGetranke = listeIdGetranke
        self.gesamtkosten = self.berechnungKosten(gesamtkosten)

    def berechnungKosten(self, gerichtePreisListe):
        gesamtkosten = functools.reduce(lambda x, y: x + y, gerichtePreisListe)
        return gesamtkosten

    def __erzeugeRechnung(self):
        gerichte_str = map(str, self.listeIdGerichte)
        getranke_str = map(str, self.listeIdGetranke)
        now = datetime.now()
        rechnung = "----------------------------\nRECHNUNG\n\nGerichte: {}\nGetranke: {}\nGesamtkosten: {} Euro\n{}\n----------------------------".format(
            ", ".join(gerichte_str),
            ", ".join(getranke_str), self.gesamtkosten, now.strftime("Datum: %Y.%m.%d\nZeit: %H:%M:%S"))
        return rechnung

    def anzeigeRechnung(self):
        rechnung = self.__erzeugeRechnung()
        print(rechnung)
