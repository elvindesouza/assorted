from time import sleep
from Pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv(str(Path(__file__).parent.absolute() / "heart_failure.csv"))


print(df.columns)
sleep(0.1)
# df['serum_creatinine'].value_counts().plot(kind="bar")
df.groupby('serum_creatinine').size().plot(kind='bar')


# a=pd.DataFrame(df.to_numpy()  )
# a.plot.bar(stacked=True)
print(df[1:].describe())


plt.show()
