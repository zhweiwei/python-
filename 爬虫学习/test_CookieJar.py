from http import cookiejar
from urllib import request, parse

url = "https://www.lagou.com/jobs/list_python/p-city_0?&cl=false&fromSearch=true&labelWords=&suginput="
data_url = "https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
    "Referer": url
}
data = {
    "first": "true",
    "pn": str(1),
    "kd": "python"
}

# 创建cookiejar实例对象
cookie_jar = cookiejar.CookieJar()

# 根据创建的cookie生成cookie的管理器
handler = request.HTTPCookieProcessor(cookie_jar)

# 创建http请求管理器
http_handle = request.HTTPHandler()

# 创建https管理器
https_handle = request.HTTPSHandler()

# 有了opener，就可以替代urlopen来获取请求了
opener = request.build_opener(handler, http_handle, https_handle)

req = request.Request(url, headers=headers)

# 正常是用request.urlopen(),这里用opener.open()发起请求,获取cookies
opener.open(req)

rep = request.Request(data_url, headers=headers, data=parse.urlencode(data).encode("utf-8"))

res = opener.open(rep)
st = res.read().decode("utf-8")
f = open("index.html", "w")
count = f.write(st)

f.close()
print(st)
print(count)
