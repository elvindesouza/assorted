# distribution of x-platelet count  vs y-death event
from time import sleep
import matplotlib.pyplot as plt
from pathlib import Path
import pandas as pd


df = pd.read_csv(str(Path(__file__).parent.absolute()/"heart_failure.csv"))
print(df.columns)
# filter platelets w/deathevent=1
df
# filter platelets w/deathevent=0

# df.plot.bar(x="platelets",y="DEATH_EVENT" )
plt.show()