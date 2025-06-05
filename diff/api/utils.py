import json

def writeJsonFile (fileName, data):
  with open(fileName, "w") as file:
    json.dump(data, file, indent=2) 

def readJsonFile(fileName):
  data = 0
  with open(fileName, "r") as file:
    data = json.load(file)
  return data
  