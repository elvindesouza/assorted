from time import sleep
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("/home/elvin/Downloads/heart_failure.csv")

print(df[1:].describe())

print(df.columns)