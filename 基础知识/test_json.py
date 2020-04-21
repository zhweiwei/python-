import json

ob = [
    {"name":"小名",
     "age":23
     },
    {"name":"消防",
     "age":23
     }
]

# json_str = json.dumps(ob,ensure_ascii=False)
# print(type(json_str))
# print(json_str)

# with open("test.json","w",encoding="utf-8") as f:
#     count = json.dump(ob,f,ensure_ascii=False)
#     print(count)

# json_str = '[{"name": "小名", "age": 23}, {"name": "消防", "age": 23}]'
# objson = json.loads(json_str)
# print(type(objson))
# print(objson)

with open("test.json","r",encoding="utf-8") as f:
    objson = json.load(f)
    print(type(objson))
    print(objson)