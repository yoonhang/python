import os
import sys
import re
import json
from pathlib import Path

path = "c:\\temp"
flist = os.listdir(path)

print(flist, sep='\\r\\n'); print();


with open("C:\\Users\\com71\\Downloads\\sample.json", encoding="UTF-8") as f:
    json_data = json.load(f)
print(json_data)


print(json.dumps(json_data, indent=1))


#################
option = sys.argv[1]
memo = sys.argv[2]

print(option)
print(memo)



