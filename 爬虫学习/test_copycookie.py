from urllib import request

url = "http://www.renren.com/880151247/profile"


headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
}
con = request.Request(url,headers=headers)
re = request.urlopen(con)
with open("index.html", "w", encoding="utf-8") as f:
    count = f.write(re.read().decode("utf-8"))
    print(count)


# url = "http://www.renren.com/880151247/profile"
#
#
# headers = {
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
#     "Cookie": "anonymid=k8z4m6vqmanbx1; depovince=ZGQT; _r01_=1; ick_login=54ab843c-0148-452e-876f-1000750fee60; taihe_bi_sdk_uid=be815781c6ed0e878618286dd0cb9c95; taihe_bi_sdk_session=09c5723e0fb4ab2b49ad72ac07238759; t=1ceade902ec4772900546b6e1e188c3f0; societyguester=1ceade902ec4772900546b6e1e188c3f0; id=974224400; xnsid=8a002435; jebecookies=45ac8704-a0f6-4645-8f1a-797edcd5d3e0|||||; ver=7.0; loginfrom=null; jebe_key=68318478-abaa-4248-b487-11c0b8256130%7Cbb1f5efe2ae67ec3b4376d19dfd23104%7C1586822635944%7C1%7C1586822620472; wp_fold=0"
# }
# con = request.Request(url,headers=headers)
# re = request.urlopen(con)
# with open("index.html", "w", encoding="utf-8") as f:
#     count = f.write(re.read().decode("utf-8"))
#     print(count)
