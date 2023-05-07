import functools
from datetime import datetime
from modelle.Identifizierbar import Identifizierbar


class Bestellung(Identifizierbar):
    def __init__(self, id, kundenId, listeIdGerichte, listeIdGetranke, gesamtkosten):
        super().__init__(id)
        self.kundenId = kundenId
        self.listeIdGerichte = listeIdGerichte
        self.listeIdGetranke = listeIdGetranke
        self.gesamtkosten = self.berechnungKosten(gesamtkosten)

    def __eq__(self, other):
        return self.id == other.id and self.kundenId == other.kundenId and self.listeIdGerichte == other.listeIdGerichte and self.listeIdGetranke == other.listeIdGetranke and self.gesamtkosten == other.gesamtkosten

    def berechnungKosten(self, gerichtePreisListe):
        gesamtkosten = functools.reduce(lambda x, y: x + y, gerichtePreisListe)
        return gesamtkosten

    def __erzeugeRechnung(self):
        gerichte_str = map(str, self.listeIdGerichte)
        getranke_str = map(str, self.listeIdGetranke)
        rechnung = "----------------------------\nRECHNUNG\n\nGerichte: {}\nGetranke: {}\nGesamtkosten: {} Euro\n----------------------------".format(
            ", ".join(gerichte_str), ", ".join(getranke_str), self.gesamtkosten)
        return rechnung

    def anzeigeRechnung(self):
        rechnung = self.__erzeugeRechnung()
        print('{}\n{}\n----------------------------'.format(rechnung,
                                                            datetime.now().strftime("Datum: %Y.%m.%d\nZeit: %H:%M:%S")))
    #Hilffunktion um die Teste machen zu konnen
    def returnRechnung(self):
        rechnung = self.__erzeugeRechnung()
        return rechnung
