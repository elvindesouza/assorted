from time import sleep
from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv(str(Path(__file__).parent.absolute() / "heart_failure.csv"))
df["platelets"].plot(kind="hist")
print(df.columns)

mean = df["platelets"].mean()
median = df["platelets"].median()
mode = df["platelets"].mode()
print(mean, median, mode)

ratio = df["sex"].value_counts()
print(ratio)

print(df["creatinine_phosphokinase"].describe())

plt.show()
