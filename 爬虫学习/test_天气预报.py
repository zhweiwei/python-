import requests
from bs4 import BeautifulSoup


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"
}

count = 0


def parse_site(url):
  #  url = "http://www.weather.com.cn/textFC/hb.shtml"
    html = requests.get(url, headers=headers)
    tb = BeautifulSoup(html.content.decode("utf-8"), "html5lib")
    con = tb.find_all("div", attrs={"class": "conMidtab"})[0]
    tables = con.find_all("table")
    for v in tables:  # 查找每个table
        # print(v)
        # print("="*20)
        # continue
        trs = v.find_all("tr")[2:]  # 去除前面两个tr
        #   print(trs)
        for r in trs:

            tds = r.find_all("td")
            city_s = tds[-8]
            city = list(city_s.stripped_strings)[0]
            temp_s = tds[-2]
            temp = list(temp_s.stripped_strings)[0]
            print("city:{},temp:{}".format(city, temp))
            global count
            count = count + 1


if __name__ == '__main__':
    sites = [
        "http://www.weather.com.cn/textFC/hb.shtml",
        "http://www.weather.com.cn/textFC/db.shtml",
        "http://www.weather.com.cn/textFC/hd.shtml",
        "http://www.weather.com.cn/textFC/hz.shtml",
        "http://www.weather.com.cn/textFC/hn.shtml",
        "http://www.weather.com.cn/textFC/xb.shtml",
        "http://www.weather.com.cn/textFC/xn.shtml",
        "http://www.weather.com.cn/textFC/gat.shtml"
    ]

    for url in sites:
        parse_site(url)
    print(count)
