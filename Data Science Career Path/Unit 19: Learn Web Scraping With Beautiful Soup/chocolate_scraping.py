import codecademylib3_seaborn
from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

webpage = requests.get('https://s3.amazonaws.com/codecademy-content/courses/beautifulsoup/cacao/index.html')

soup = BeautifulSoup(webpage.content, 'html.parser')

ratings_tds = soup.find_all(attrs={"class": "Rating"})
ratings = []

for i in range(1,len(ratings_tds)):
  ratings.append(float(ratings_tds[i].get_text()))
  
plt.hist(ratings)
plt.show()

companies_tds = soup.select(".Company")
companies = []

for i in range(1, len(companies_tds)):
  companies.append(companies_tds[i].get_text())
  
df = pd.DataFrame.from_dict({"Company": companies, "Rating": ratings })

mean_ratings = df.groupby('Company').Rating.mean()
top_ten = mean_ratings.nlargest(10)
print(top_ten)

percentage_tds = soup.select(".CocoaPercent")
percentages = []

for percentage in percentage_tds[1:]:
  percentages.append(int(float(percentage.get_text().strip('%'))))
  
df["CocoaPercentage"] = percentages

plt.clf()
plt.scatter(df.CocoaPercentage, df.Rating)
z = np.polyfit(df.CocoaPercentage, df.Rating, 1)
line_function = np.poly1d(z)
plt.plot(df.CocoaPercentage, line_function(df.CocoaPercentage), "r--")
plt.show()