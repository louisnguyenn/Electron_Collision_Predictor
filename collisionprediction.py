import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv("dielectron.csv")

# exploring the data
invariant_mass = df["M"].values
sns.displot(invariant_mass)

electron1 = df["E1"].values
electron2 = df["E2"].values

sns.lineplot(electron1, 
