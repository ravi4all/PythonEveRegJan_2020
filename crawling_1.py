import urllib.request as url
import bs4

path = "https://www.flipkart.com/search?q=tv"

# 1. Hit request and we will get a response
res = url.urlopen(path)

# 2. Pass the response to beautiful Soup
page = bs4.BeautifulSoup(res,'lxml')

# 3. Find the tag with class or id from where you want to fetch data
div = page.find('div',class_='_3wU53n')
print(div.text)

price = page.find('div',class_='_1vC4OE _2rQ-NK')
print(price.text)
