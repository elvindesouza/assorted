from time import sleep
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("/home/elvin/Downloads/heart_failure.csv")
print(df.columns)
sleep(1)
# df['serum_creatinine'].value_counts().plot(kind="bar")
df.groupby('platelets').size().plot(kind='bar')
# a=pd.DataFrame(df.to_numpy()  )
# a.plot.bar(stacked=True)
plt.show()
# print(df[1:].describe())
