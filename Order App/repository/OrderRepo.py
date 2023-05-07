import json
from repository.DataRepo import DataRepo
from modelle.Bestellung import Bestellung


class OrderRepo(DataRepo):
    def convertToString(self, data):
        dataTuples = list(map(lambda x: (x.id, x.kundenId, x.listeIdGerichte, x.listeIdGetranke, x.gesamtkosten), data))
        return json.dumps(list(
            map(lambda x: {'ID': x[0], 'Kunden ID': x[1], 'Name Gericht': x[2], 'Name Getrank': x[3],
                           'Gesamtkosten': x[4]}, dataTuples)), indent=2)

    def convertFromString(self, data):
        dataTuples = list(
            map(lambda x: (x['ID'], x['Kunden ID'], x['Name Gericht'], x['Name Getrank'], x['Gesamtkosten']),
                json.loads(data)))
        return list(map(lambda x: Bestellung(x[0], x[1], x[2], x[3], [x[4]]), dataTuples))
