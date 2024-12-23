import requests
from bs4 import BeautifulSoup
import csv

title = []
response = requests.get("https://www.rbc.ru/")
soup = BeautifulSoup(response.text, 'html.parser')

news_items = soup.find_all('div', class_='main__feed')

for item in news_items:
    titles = item.find_all('span', class_='main__feed__title')
    for x in titles:
        title.append(x.text)

with open('news.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Title'])
    for item in title:
        writer.writerow([item])
