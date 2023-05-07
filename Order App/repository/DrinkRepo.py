import json
from repository.DataRepo import DataRepo
from modelle.Getrank import Getrank


class DrinkRepo(DataRepo):
    def convertToString(self, data):
        dataTuples = list(map(lambda x: (x.id, x.portionsgrosse, x.preis, x.alkoholgehalt), data))
        return json.dumps(
            list(map(lambda x: {'ID': x[0], 'Portionsgrosse': x[1], 'Preis': x[2], 'Alkoholgehalt': x[3]}, dataTuples)),
            indent=2)

    def convertFromString(self, data):
        dataTuples = list(
            map(lambda x: (x["ID"], x["Portionsgrosse"], x['Preis'], x["Alkoholgehalt"]), json.loads(data)))
        return list(map(lambda x: Getrank(x[0], x[1], x[2], x[3]), dataTuples))
