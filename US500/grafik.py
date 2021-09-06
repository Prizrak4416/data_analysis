import matplotlib.pyplot as plt
import pandas as pd
from datetime import date

path_csv_us500 = "../csv_date/ES=F.csv"
df = pd.read_csv(path_csv_us500, parse_dates=True, index_col=0)
df["average_value"] = (df["High"] + df["Low"]) / 2
Xaxis = df.index
Yaxis = df["average_value"].values

plt.figure(figsize=(14, 8))
plt.plot(Xaxis, Yaxis, 'black')
plt.grid()

for i in range(2020, 2021):
    plt.axvline(date(i, 9, 1), c='red')
    plt.axvspan(date(i, 9, 1), date(i, 9, 30), alpha=0.3)

plt.show()