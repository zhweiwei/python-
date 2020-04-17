# def fun1():
#     return 1, 2
#
# def fun2():
#     return 1
#
# print(fun1())
# print(fun2())
# print(type(fun1()))
#
# print(type(fun2()))

#
# def fun(arg1,arg2 = 100):
#     print(arg1+":"+ str(arg2))
#
# fun("value")
# fun("value",300)
# fun(arg2 = 200,arg1 = "value")

# def fun(arg1, *arg2):
#     print(type(arg2))
#     print(arg1)
#     print(arg2)
#
# fun(12,*(12,32,43,32))

# def fun(arg1, **arg2):
#     print(type(arg2))
#     print(arg1)
#     print(arg2)
#
# fun(12,**{"name" :"zhang","value ": "sfgi"})

# def fun(arg1,*,arg2):
#
#     print(arg1)
#     print(arg2)
#
# fun(1, arg2 = 2)

def fun(arg1, arg2, cmp = None):
    if cmp is None:
        if arg1 > arg2:
            return 1
        elif arg1 == arg2:
            return 0
        else:
            return -1
    else:
        return cmp(arg1,arg2)

def cmp(arg1, arg2):
    return "this is cmp"

print(fun(1,2))
print(fun(1,2,cmp))