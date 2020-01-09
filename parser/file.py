import lxml.html as html
import requests


main_domain = "https://habr.com/ru/"

req = requests.get(main_domain)
page = html.fromstring(req.content)

article_links = page.xpath("//li/article[contains(@class, 'post_preview')]/h2/a")
# print(article_links[0].xpath(".//@href"))

for x in article_links:
    print(x.xpath(".//@href"), x.text)

article_links = page.xpath("//li/article[contains(@class, 'post_preview')]/div/div/img/@src | //li/article[contains(@class, 'post_preview')]/div/div/div/img/@src")

for x in article_links:
    print(x)