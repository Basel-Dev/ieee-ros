import platform
import datetime
from pathlib import Path

parentDir = Path(__file__).resolve().parent
systemLogFilePath = parentDir / "data/sys_log.txt"

def logSystemInfo():
    logData = f"Platform: {platform.system()}\nTimestamp: {datetime.datetime.now().timestamp()}"
    with open(systemLogFilePath, "w") as file:
        file.write(logData)

def main():
    logSystemInfo()

if __name__ == "__main__":
    main()