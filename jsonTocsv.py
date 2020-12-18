import json
#import csv
import pandas as pd
with open('all_2020_07-08.json', encoding='utf-8') as input:
    df = pd.read_json(input)
df.to_csv("all_2020_07-08.csv", encoding="cp949", index=False)