import requests

#
# data = {"key1":"value1","key2":"value2"}
# url = "http://httpbin.org/post"
# re = requests.post(url,data=data)
# print(re.text)
#
# url = "https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput="
# data_url ="https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false"
#
# headers1 = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"
# }
#
# headers2 = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
#     "Referer":url
# }
#
# data = {
#     "first": "true",
#     "pn": "1",
#     "kd": "python"
# }
# re = requests.Session()
# #获取cookies
# r = re.get(url,headers = headers1)
# print(r.text)
# #通过上面获取的cookie继续发送消息
# r = re.post(data_url,headers = headers2,data = data)
# with open("index.html","w",encoding="utf-8") as f:
#    count =  f.write(r.content.decode("utf-8"))
#    print(count)

url = 'http://www.httpbin.org/ip'

print(requests.get(url).text)

proxies = {
    'http': 'http://117.88.176.135:3000'
}

r = requests.get(url,proxies =proxies)
print(r.text)