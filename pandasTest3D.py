import pandas as pd

import matplotlib.pyplot as plt

import numpy as np

from mpl_toolkits.mplot3d import Axes3D

print(pd.__version__)



df = pd.read_csv("ML_apple_quality.csv")
colors = np.where(df["Quality"]=="good",'g','r')
print(df.head())
df['Acidity'] = pd.to_numeric(df['Acidity'], errors='coerce')
x = "Juiciness"
y = "Crunchiness"
z = "Sweetness"

fig = plt.figure()
threedee = fig.add_subplot(111, projection='3d')
#threedee.scatter(df["Size"], df["Weight"], df["Sweetness"], c=colors)
threedee.scatter(df[x], df[y], df[z], c=colors)
threedee.set_xlabel(x)
threedee.set_ylabel(y)
threedee.set_zlabel(z)
plt.show()













