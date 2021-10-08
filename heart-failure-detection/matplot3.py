from time import sleep
from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv(str(Path(__file__).parent.absolute() / "heart_failure.csv"))

print(df[1:].describe())

print(df.columns)
