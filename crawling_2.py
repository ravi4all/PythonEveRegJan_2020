import urllib.request as url
import bs4

for i in range(1,4):
    path = f"https://www.flipkart.com/search?q=tv&page={i}"

    # 1. Hit request and we will get a response
    res = url.urlopen(path)

    # 2. Pass the response to beautiful Soup
    page = bs4.BeautifulSoup(res,'lxml')

    # 3. Find the tag with class or id from where you want to fetch data
    div = page.findAll('div',class_='_3wU53n')
    price = page.findAll('div',class_='_1vC4OE _2rQ-NK')

    for j in range(len(div)):
        print(div[j].text)
        print(price[j].text)
        print("="*20)

    print(f"*********Page - {i}**********")
