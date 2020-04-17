import requests
from lxml import etree

#html = etree.parse("index.html",parser=etree.HTMLParser())
# print(etree.tostring(html,encoding="utf-8").decode("utf-8"))
url = "https://movie.douban.com/cinema/nowplaying/anqing/"
headers= {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"
}

html = requests.get(url,headers= headers)
# print(html.text)

html = etree.HTML(html.text)
p = html.xpath("//ul[@class='lists']")[0]
ul = p.xpath("./li")

for v in ul:
    title = v.xpath("@data-title")[0]
    print(title)