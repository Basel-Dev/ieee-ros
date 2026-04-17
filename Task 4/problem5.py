import os
import json
from pathlib import Path

parentDir = Path(__file__).resolve().parent
configFilePath = parentDir / "data/config.json"

defaultConfigSettings = {"setting1": "abc"}

if os.path.exists(configFilePath):
    print("System Ready")
else:
    with open(configFilePath, "w") as file:
        json.dump(defaultConfigSettings, file)