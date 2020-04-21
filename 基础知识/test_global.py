def fun1():
    print(a)

def fun2():
    global a
    a =3
    print(a)

def fun3():
    global a
    a = a +1
    print(a)
a = 1


fun1()
print("fun1 之后a = {}".format(a))
fun2()
print("fun2 之后a = {}".format(a))
fun3()
print("fun3 之后a = {}".format(a))
