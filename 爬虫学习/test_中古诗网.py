import requests
import re

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36"
}

url = "https://www.gushiwen.org/default_1.aspx"

content = requests.get(url,headers= headers)
titles = re.findall('<div\sclass="cont".*?<b>(.*?)</b>',content.text,re.DOTALL)#re.DOTALL 默认情况下,.表示所有除了换行的字符，加上re.DOTALL参数后，就是真正的所有字符了，包括换行符（\n）
dynastyds = re.findall('<p\sclass="source".*?<a.*?>(.*?)</a>',content.text,re.DOTALL)
authoers = re.findall('<p\sclass="source.*?</a>.*?<a.*?>(.*?)</a>',content.text,re.DOTALL)
print(len(authoers))
print("="*20)
contents = re.findall('<div\sclass="contson".*?>(.*?)</div>',content.text,re.DOTALL)
print(contents)
for index,value in enumerate(contents):
    contents[index] = re.sub(r"<br />","",value).strip()
    contents[index] = re.sub(r"<.*?p>","",contents[index])
print("="*20)
print(contents)
print("="*20)
print(len(contents))

for t,d,a,c in zip(titles,dynastyds,authoers,contents):
    print(t)
    print("{}:{}".format(d,a))
    print(c)
    print("="*30)