from time import sleep
from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv(str(Path(__file__).parent.absolute() / "heart_failure.csv"))
df["platelets"].plot(kind="hist")


ratio = df["sex"].value_counts()
print(ratio)

plt.show()
