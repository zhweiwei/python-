from urllib import request

url = "http://httpbin.org/ip"
re =request.urlopen(url)
print(re.read().decode("utf-8"))

handler = request.ProxyHandler({"http":"121.237.148.192:3000"})
opener = request.build_opener(handler)
req = request.Request(url)
se = opener.open(url)
print(se.read().decode("utf-8"))