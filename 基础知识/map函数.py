# def fun(x):
#     return 2 * x
#
# t = [1,2,3,4,5]
# re = map(fun,t)
# print(t)
# re = list(re)
# print(re)

t = [1,2,3,4,5]
re = map(lambda x:2 *x,t)
print(t)
re = list(re)
print(re)
