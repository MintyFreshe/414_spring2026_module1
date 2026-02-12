import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

#df = pd.read_csv('bestsellinbooks2025.csv')

df2 = pd.read_csv('price_of_healthy_diet_clean.csv')


us_rows = df2[df2["country"] == "United States of America"]

#print(us_rows.iloc[6])

#print(us_rows.annual_cost_healthy_diet_usd)

#us_rows.annual_cost_healthy_diet_usd.plot(kind='hist', bins=10, edgecolor='black')

#plt.show()

x = us_rows.year
y = us_rows.annual_cost_healthy_diet_usd

plt.plot(x, y)
plt.xlabel("Year")
plt.ylabel("Anual Cost (USD)")
plt.title("Annual Cost of Healthy Diet in the USA")
plt.show()





#print(df.head())

#top_genre = (df.Genre.value_counts())

#print(top_genre)

#print(top_genre.iloc[0])  # Print the count of the most common genre

#print(top_genre.key[1])  # Print the most common genre


# # Bar chart with day against tip
# plt.bar(data['day'], data['tip'])

# plt.title("Bar Chart")

# # Setting the X and Y labels
# plt.xlabel('Day')
# plt.ylabel('Tip')

# # Adding the legends
# plt.show()