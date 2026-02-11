import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv('bestsellinbooks2025.csv')

#print(df.head())

top_genre = (df.Genre.value_counts())

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