import json
from utils import readJsonFile

def validateData ():
  results_file = "results.json"
  loaded_data = []

  try:
    loaded_data = readJsonFile(results_file)

  except FileNotFoundError:
      print(f"Fehler: Datei '{results_file}' nicht gefunden.")
      print("Bitte führe zuerst 'generate_data.py' aus, um die Daten zu erstellen.")
      exit()

  for i, dataArray in enumerate(loaded_data):
      if not isinstance(dataArray, (list, tuple)) or len(dataArray) != 3:
          raise ValueError(f"Fehler im Datensatz {i}: Datenformat ist nicht korrekt. Erwartet Liste oder Tuple mit 3 Elementen, aber {type(dataArray).__name__} mit Länge {len(dataArray) if isinstance(dataArray, (list, tuple)) else 'unbekannt'} gefunden.")

      age = dataArray[0]
      wealth = dataArray[1]
      phone = dataArray[2]

  print("Datenformat ist korrekt.")