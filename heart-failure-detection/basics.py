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
print(df)

description = df.describe()
print(description)

# df.plot(kind='bar', x="anaemia", y="DEATH_EVENT")
# make async KeyboardInt
cols = df.columns.values.tolist()
for col in cols:
    df[col].value_counts().plot(
        kind="pie", title=f"Records in dataset in which the person had {col}"
    )

plt.show()
