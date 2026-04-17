import json
from pathlib import Path

parentDir = Path(__file__).resolve().parent
inventoryFilePath = parentDir / "data/inventory.json" 

def save_inventory(path, data):
    with open(path, "w") as file:
        json.dump(data, file)

def load_inventory(path):
    try:
        with open(path, "r") as file:
            content = file.read()
            return json.loads(content)
    except FileNotFoundError:
        print(f"File ({inventoryFilePath}) was not found.")
        return {}


print(load_inventory(inventoryFilePath))