from time import sleep
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("/home/elvin/Downloads/heart_failure.csv")
# print(df.columns)

a=pd.DataFrame(df.to_numpy()  )
a.plot.bar(stacked=True)
plt.show()
# print(df[1:].describe())
