import json
from repository.DataRepo import DataRepo
from modelle.GekochterGericht import GekochterGericht


class CookedDishRepo(DataRepo):
    def convertToString(self, data):
        dataTuples = list(map(lambda x: (x.id, x.portionsgrosse, x.preis, x.zubereitungszeit), data))
        return json.dumps(list(
            map(lambda x: {'ID': x[0], 'Portionsgrosse': x[1], 'Preis': x[2], 'Zubereitungszeit': x[3]}, dataTuples)),
            indent=2)

    def convertFromString(self, data):
        dataTuples = list(
            map(lambda x: (x['ID'], x['Portionsgrosse'], x['Preis'], x['Zubereitungszeit']), json.loads(data)))
        return list(map(lambda x: GekochterGericht(x[0], x[1], x[2], x[3]), dataTuples))
