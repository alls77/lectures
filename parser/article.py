import lxml.html as html
import requests

url = "https://habr.com/ru/post/483218/"

req = requests.get(url)
page = html.fromstring(req.content)

title = page.xpath("//article[contains(@class, 'post_full')]/div/h1/span/text()")
time = page.xpath("//article/div/header/span/text()")
text = page.xpath("")


print(title, author)