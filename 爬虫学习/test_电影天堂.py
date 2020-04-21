import  requests
from lxml import etree


BASE_URL="https://www.dytt8.net"
url = "https://www.dytt8.net/html/gndy/dyzz/list_23_1.html"
headers1 = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"
}

html = requests.get(url,headers= headers1)
html = etree.HTML(html.content.decode("gbk"))
# print(etree.tostring(html,encoding="gbk").decode("gbk"))
ul = html.xpath("//div[@class='co_content8']//ul//a/@href")
ul = map(lambda x:BASE_URL+x,ul)
ul = list(ul)

url2  = ul[0]
result = { }
html = requests.get(url2,headers = headers1)
content = etree.HTML(html.content.decode("gbk"))
title = content.xpath("//div[@class='title_all']//font[@color='#07519a']/text()")[0].strip()
result["title"] = title
other_content = content.xpath("//div[@id='Zoom']//p")[0]
img = other_content.xpath(".//img/@src")[0]
result['img'] = img

text = other_content.xpath(".//text()")
for val in text:
    print(val)