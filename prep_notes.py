import re
import csv
from pprint import pprint
from collections import Counter
from tqdm import tqdm

section_pattern = r"(?:\s{2,}|\r|\n)[a-zA-Z]+(?: [a-zA-Z]+)*\s?:\s?"
anonym_pattern = r"\[\*\*[\w\s()]+\*\*\]"

sections = ["history of present illness",
            "allergies",
            "past medical history",
            "discharge diagnosis",
            "chief complaint",
            "discharge condition",
            "discharge diagnoses",
            "condition on discharge",
            "final diagnosis",
            "condition at discharge",
            "secondary diagnosis",
            "family history"]


tot = 0
cnt = Counter()




with open("data/NOTEEVENTS.csv", "r") as fp:

    reader = csv.reader(fp)
    header = next(reader)
    for row in tqdm(reader):
        d = {k:v for k, v in zip(header, row)}
        if d["CATEGORY"] != "Discharge summary":
            continue
        tot += 1
        for atoken in re.findall(section_pattern, d["TEXT"]):
            cnt[atoken.lower().strip()] += 1

        #for x in re.split(section_pattern, d["TEXT"]):
        #    print(x)
        #break

        for atoken in re.findall(anonym_pattern, d["TEXT"]):
            t = "".join([x for x in atoken if x.isalpha()])
            cnt[t] += 1

pprint(cnt.most_common(300))
print(tot)



