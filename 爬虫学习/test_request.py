from urllib import request,parse
from http import cookiejar
import requests
import os
#urlopen
# re = request.urlopen("http://www.baidu.com")
# print(re.read())

#urlencode
#re = request.urlopen("http://www.baidu.com/s?wd=新型冠状病毒")
# q = {"wd":"新型冠状病毒"}
# url = "http://www.baidu.com/s?"
#
# n_q = parse.urlencode(q)
# print(n_q)
# url = url +n_q
# re = request.urlopen(url)
# print(re.read())

#unquote
# q = {"wd":"新型冠状病毒"}
# en_q = parse.urlencode(q)
# print(en_q)
# de_q = parse.unquote(en_q)
# print(de_q)

#urlparse

# url = parse.urlparse('https://i.cnblogs.com/EditPosts.aspx?opt=1')
# print(url)

#request.Request
#
url = "https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false"
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
    "Referer":"https://www.lagou.com/jobs/list_python"
}
data = {
"first": "true",
"pn": str(1),
"kd": "python"
}
rep = request.Request(url,headers=headers,data= parse.urlencode(data).encode("utf-8"),method="PSOT")
re = request.urlopen(url)
st = re.read().decode("utf-8")
f = open("index.html","w")
count = f.write(st)

f.close()
print(st)
print(count)
