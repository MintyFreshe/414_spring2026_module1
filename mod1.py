import seaborn as sns
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np



df2 = pd.read_csv('price_of_healthy_diet_clean.csv')

df2.head()

us_rows = df2[df2["country"].isin(["United States of America", "Mexico", "Canada"])]

ax = sns.lineplot(
    data=us_rows,
    x="year",
    y="annual_cost_healthy_diet_usd",
    hue="country",
    marker="o"
)


plt.title("Annual Cost of Healthy Diet in North America")
plt.xlabel("Year")
plt.ylabel("USD adjusted for purchasing power")
plt.show()