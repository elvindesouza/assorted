from time import sleep
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv(str(Path(__file__).parent.absolute() / "heart_failure.csv"))
# print(df.columns)

a=pd.DataFrame(df.to_numpy()  )
a.plot.hist(stacked=True)
plt.show()
# print(df[1:].describe())
