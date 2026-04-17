from pathlib import Path

parentDir = Path(__file__).resolve().parent
logFilePath = parentDir / "data/log.txt"

def writeLog(message):
    with open(logFilePath, "a") as file:
        file.write(message + "\n")
        print("Logged message")

def readLogs():
    with open(logFilePath, "r") as file:
        data = file.read()
        print("Printing logs")
        for log in data.split("\n"):
            print(log)

writeLog("Log 1")
writeLog("Log 2")
writeLog("Log 3")

readLogs()