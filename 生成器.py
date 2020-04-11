# t = [i for i in range(5)] #推导式
# print(type(t))
# print(t)
#
# s = (i for i in range(5)) #生成器
# print(type(s))
# for value in s:
#     print(value)

def fun(arg):
    i = 0
    while i < arg:
        yield i
        i += 1
    print("OK")

for value in fun(6):
    print(value)
