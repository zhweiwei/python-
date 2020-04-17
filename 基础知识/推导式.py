# l = [i for i in range(10)]
# print(l)
#
# def square(i):
#     return i * i
#
# p = [square(i) for i in range(10)]
# print(p)

# d = {"vs": 2, "sfb": 42}
# new_d = {value: key for key, value in d.items()}
#
# print(d)
# print(new_d)

# s = {"sdvsvs","svsv","df"}
# s_len = {key:len(key) for key in s}
# print(s_len)

names = ['Bob', 'JOHN', 'alice', 'bob', 'ALICE', 'James', 'Bob', 'JAMES', 'jAMeS']
names_standard = {name.lower() for name in names}
print(names)
print(names_standard)
