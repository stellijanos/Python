
import json
from modelle.modelle import *

import abc
class DataRepo(abc.ABC):
    def __init__(self, file):
        self.file = file

    def save(self, data):
        dataString = self.convertToString(data)
        self.writeToFile(dataString)

    def load(self):
        fileContents = self.readFile()
        data = self.convertFromString(fileContents)
        return data

    def readFile(self):
        with open(self.file, 'r') as f:
            return f.read()

    def writeToFile(self, data):
        with open(self.file, 'w') as f:
            f.write(data)

    @abc.abstractmethod
    def convertToString(self, data):
        return json.dumps(data)

    @abc.abstractmethod
    def convertFromString(self, data):
        return json.loads(data)


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


class CustomerRepo(DataRepo):

    def convertToString(self, data):
        dataTuples = list(map(lambda x: (x.id, x.name, x.adresse), data))
        return json.dumps(list(map(lambda x: {'ID': x[0], 'Name': x[1], 'Adresse': x[2]}, dataTuples)), indent=2)

    def convertFromString(self, data):
        dataTuples = list(map(lambda x: (x['ID'], x['Name'], x['Adresse']), json.loads(data)))
        return list(map(lambda x: Kunde(x[0], x[1], x[2]), dataTuples))


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
