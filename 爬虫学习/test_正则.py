import re

# text = "hello"
# ret = re.search("e",text)
# print(ret.group())
# text = "apple price is $99,orange price is $10"
# ret = re.search(r".*(\$\d+).*(\$\d+)",text)
# print(ret.group())
# print(ret.group(0))
# print(ret.group(1))
# print(ret.group(2))
# print(ret.groups())
# print(type(ret.groups()))

# text = "apple price is $99,orange price is $10"
# ret = re.findall("\d.",text)
# print(ret)

# text = 'apple price $99 orange price $88'
# ret = re.sub('\d+','100',text)
# print(ret)

# text = "hello world ni hao"
# ret = re.split('\W',text)
# print(ret)

text = "the number is 20.50"
r = re.compile(r"""
                \d+ # 小数点前面的数字
                \.? # 小数点
                \d* # 小数点后面的数字
                """,re.VERBOSE)
ret = re.search(r,text)
print(ret.group())