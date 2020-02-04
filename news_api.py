import urllib.request as url
import json

res = url.urlopen("https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=695e07af402f4b119f0703e9b19f4683")
data = json.load(res)
articles = data['articles']
for i in range(len(articles)):
    article = articles[i]
    title = article['title']
    print(title)