from collections.abc import Iterable
from collections.abc import Iterator

print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance('abc', Iterator))


def fun(arg):
    for i in range(arg):
        yield i
g = fun(6)
print(type(g))

print(isinstance(g, Iterable))
print(isinstance(g, Iterator))
