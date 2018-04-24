
from sweeping.models import *
import pandas as pd
import numpy as np

fl = "/Users/jp/Documents/Make/Projects/bsp/Berkeley Street Sweeping Data.csv"
dS = pd.read_csv(fl)






for index,row in dS.iterrows():	
	sweep = Sweep.objects.create(
		rte = row["RTE"],
		street_name = row["Street Name"],
		from_address = row["From Address"],
		to_address = row["To Address"],
		day = Weekday.objects.get(num=int(str(row['RTE'])[0])),
		of_month = int(str(row['RTE'])[1]),
		time = row["Time"],
		side = row["Side"],
		from_street = row["From Street"],
		to_street = row["To Street"],
		optout = row["Optout"] if not pd.isnull(row["Optout"]) else 0
	)
	sweep.save()

row =dS.loc[3]
sweep = Sweep.objects.create(
rte = row["RTE"],
street_name = row["Street Name"],
from_address = row["From Address"],
to_address = row["To Address"],
day = Weekday.objects.get(num=int(str(row['RTE'])[0])),
of_month = int(str(row['RTE'])[1]),
time = row["Time"],
side = row["Side"],
from_street = row["From Street"],
to_street = row["To Street"],
optout = row["Optout"] if not pd.isnull(row["Optout"]) else 0
)