# scatterplot of x-platelet count  vs y-death event
from time import sleep
import matplotlib.pyplot as plt
from pathlib import Path
import pandas as pd


df = pd.read_csv(str(Path(__file__).parent.absolute()/"heart_failure.csv"))
print(df.columns)
df.plot.scatter(x="DEATH_EVENT",y="platelets" )
plt.show()