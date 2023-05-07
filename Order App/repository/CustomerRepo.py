import json
from repository.DataRepo import DataRepo
from modelle.Kunde import Kunde


class CustomerRepo(DataRepo):

    def convertToString(self, data):
        dataTuples = list(map(lambda x: (x.id, x.name, x.adresse), data))
        return json.dumps(list(map(lambda x: {'ID': x[0], 'Name': x[1], 'Adresse': x[2]}, dataTuples)), indent=2)

    def convertFromString(self, data):
        dataTuples = list(map(lambda x: (x['ID'], x['Name'], x['Adresse']), json.loads(data)))
        return list(map(lambda x: Kunde(x[0], x[1], x[2]), dataTuples))
