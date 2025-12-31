import pandas as pd
import numpy as np 
import math
import random

import csv

#file_path = 'MOCK_DATA.csv'

#with open(file_path, mode='r', newline='', encoding='utf-8') as csv_file:
   # csv_reader = csv.DictReader(csv_file)
   # for row in csv_reader:
   #     # Access data by column name, e.g., row['column_name']
    #    print(f'{row["first_name"]} has the email:{row["email"]}')

#df = pd.DataFrame(data = {
  #  "StudentID": np.arange(1001, 1011),
  #  "ExamScore": np.random.randint(60, 100, 10),
  #  "StudyHours": np.round(np.random.uniform(1, 8, 10), 1),
  #  "Major": np.random.choice(["EE", "CompE", "CS", "ME"], 10),
#    "Passed": None,
  #  "Credit": np.random.randint(0,5,10)
#})

df = pd.read_csv('MOCK_DATA.csv')
#df["Passed"] = df["ExamScore"] >= 70

men = df[df['gender'] == 'Male']
gmailmen = men[men["email"].astype(str).str.contains("@discovery", case=False, regex=False)]
print(gmailmen.head(10))

