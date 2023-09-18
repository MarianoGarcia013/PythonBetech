import json # Libreria de json
from pathlib import Path

# escribir json
productos = [ 
    {"id": 1, "name": "Pablo"},
    {"id": 2, "name": "Pedro"},
    {"id": 3, "name": "Juan"},
]
dats = "hola mundo"

data = json.dumps(dats)
print(data)
