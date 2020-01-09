from bs4 import BeautifulSoup
import requests

url = "https://habr.com/ru/"

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

article_links = soup.select('li article.post_preview h2 a')

for x in article_links:
    print(x['href'])