#!/bin/bash

LOG_FILE='server.log'

echo "Checking the file: $LOG_FILE"

echo "End of Report" > audit.txt
# echo "Date: 2026" > audit.txt (This would overwrite the previous echo)
echo "Date: 2026" >> audit.txt # This will append
