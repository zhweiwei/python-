import requests

# req = requests.get('https://httpbin.org/get')
# # print(req.text)

# headers = {
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
#
# }
#
# data = {
# "wd":"新型冠状病毒"
# }
# url = "http://www.baidu.com/s"
# re = requests.get(url,params=data,headers= headers)
# print(re.url)
# with open("index.html","w",encoding="utf-8") as f:
#     count = f.write(re.content.decode("utf-8"))
#     print(count)

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
    "Cookie": "BIDUPSID=41BB40B30F5505BBAFB383EC2890356C; PSTM=1582981521; BAIDUID=41BB40B30F5505BB1B849015D5D91E79:FG=1; BD_UPN=12314753; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDUSS=hpSllZUVQ5U1JnZkVzdVBJMVp1MmZhUGd0OG9KVTYwTnJvY1dpTVlpeVpyN0plRVFBQUFBJCQAAAAAAAAAAAEAAACXS39dw7u07V-088nxvN21vQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJkii16ZIoteeE; H_PS_PSSID=1464_31124_21090_31187_30903_31271_31228_30823_31085_26350_31164_22159; sugstore=1; H_PS_645EC=6b05Ik9MKkAEZv4IFslxBo9KEklxQ1OO4z81AbF42RTzgtIiyvevJEQieyM; BDSVRTM=0; WWW_ST=1586850915148"
}

data = {
"wd":"新型冠状病毒"
}
url = "http://www.baidu.com/s"
re = requests.get(url,params=data,headers= headers)
print(re.url)
with open("index.html","w",encoding="utf-8") as f:
    count = f.write(re.content.decode("utf-8"))
    print(count)