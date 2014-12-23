from Model.Share import Share

__author__ = 'thiagocastroferreira'

import os
import datetime

def run():
    dirs = os.listdir("/Users/thiagocastroferreira/Documents/workspace/BovespaNLG/Data/PETR4")
    shares = {}

    del dirs[list(dirs).index(".DS_Store")]

    for dir in dirs:
        file = open("/Users/thiagocastroferreira/Documents/workspace/BovespaNLG/Data/PETR4/"+dir, "r")
        doc = file.readlines()

        for line in doc:
            values = str(line).split("\t")
            id = values[0]
            price = float(values[2])
            variation = float(values[3])
            volume = int(values[4])

            date = str(values[1]).split("/")
            time = str(values[5]).split(":")

            if len(date) == 3 and len(time) == 3:
                key = str(datetime.date(int(date[2]), int(date[1]), int(date[0])))
                if key not in shares.keys():
                    shares[key] = []
                datetimeVar = datetime.datetime(int(date[2]), int(date[1]), int(date[0]), int(time[0]), int(time[1]), int(time[2]))
                share = Share(id, id, price, variation, volume, datetimeVar)
                shares[key].append(share)
    return shares

# shares = run()
# shares = sorted(shares, key=lambda p: p.date)
# keys = sorted(shares.keys())
# for key in keys:
#     print(key)