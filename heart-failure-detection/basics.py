from time import sleep
from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd

columns = [
    "age",
    "anaemia",
    "DEATH_EVENT",
    "diabetes",
    "creatinine_phosphokinase",
    "ejection_fraction",
    "high_blood_pressure",
    "platelets",
    "serum_sodium",
    "sex",
    "smoking",
    "time",
]

df = pd.read_csv(
    str(Path(__file__).parent.absolute() / "heart_failure.csv"), usecols=columns
)
description = df.describe()

output_list = [
    df,
    description,
    df.head,
    df.tail,
    df.shape,
    df.index,
    df.columns,
    df.info,
    df.values,
    df.size,
    df.ndim,
    df.dtypes,
    df.axes,
    df.empty,
]

for item in output_list:
    print(item)
# df.plot(kind='bar', x="anaemia", y="DEATH_EVENT")
# make async KeyboardInt
# cols = df.columns.values.tolist()
col = 3
df[columns[col]].value_counts().plot(
    kind="pie", title=f"Records in dataset in which the person had {columns[col]}"
)

plt.show()
