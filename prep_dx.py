import csv
import json
from pprint import pprint

data = {}
with open("data/DIAGNOSES_ICD.csv", "r") as fp:
    reader = csv.reader(fp)
    header = next(reader)
    for row in reader:
        d = {k:v for k, v in zip(header, row)}
        if d["HADM_ID"] not in data:
            data[d["HADM_ID"]] = []
        data[d["HADM_ID"]].append(d["ICD9_CODE"])

with open("data/hadm2dx.json", "w") as fp:
    json.dump(data, fp, indent=2)

