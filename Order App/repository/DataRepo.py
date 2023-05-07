import json

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
